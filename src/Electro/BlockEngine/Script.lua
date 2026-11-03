local Enum = Electro.Enum
local Stepper = Electro.BlockEngine.Stepper

return function(Hat, Sprite)
    ---@class ElectroScript
    local Script = {}

    function Script.GetBlock(BlockID)
        local Root = Script.Sprite:GetRootSprite()

        return Stepper.GetBlock(Root.ID, BlockID)
    end

    Script.Sprite = Sprite
    Script.Hat = Hat
    Script.StartBlock = Script.GetBlock(Hat.Next)

    Script.CreationTraceback = debug.traceback()

    Script.Info = {}

    local DidControlFlow = false
    local CurrentBlock = Script.StartBlock
    local Stack = {}

    Script.State = Enum.STATUS_RUNNING
    Script.UUID = CreateUUID()

    -- Push the current state to the stack
    function Script.PushStack(Loop, Warp)
        local StackFrame = {
            BlockID = CurrentBlock.ID,
            IsLoop = Loop,
            WarpMode = Warp,
            Params = {},
            IsProcedure = false
        }

        table.insert(Stack, StackFrame)
        return StackFrame
    end

    -- Find latest hot procedure stacks in your area why am i like this
    function Script.FindProcedureStack()
        for i = #Stack, 1, -1 do
            local Frame = Stack[i]

            if Frame.IsProcedure then return Frame end
        end
    end

    function Script.StopThisScript()
        while true do
            local LastStack = Script.PeekStack() -- TODO: Custom block support

            if not LastStack then break end

            if not LastStack.IsProcedure then
                Script.PopStack()
            else
                break
            end
        end
    end

    function Script.Kill()
        Script.State = Enum.STATUS_DONE
    end

    function Script.PopStack()
        return table.remove(Stack)
    end

    function Script.IsWarpMode()
        local ProcStack = Script.FindProcedureStack()

        return ProcStack and ProcStack.WarpMode or false
    end

    function Script.SetYielded()
        Script.State = Enum.STATUS_YIELDED
    end

    function Script.SetYieldTick()
        Script.State = Enum.STATUS_YIELDTICK
    end

    -- Push our current block to the stack, then goto the new one
    function Script.BranchToBlock(BlockID, IsLoop, Warp)
        local Stack = Script.PushStack(IsLoop, Warp)
        Script.Goto(BlockID)

        return Stack
    end

    --[[
        BlockID: the block id to go to
        DontFlow: 
            if true, the control flow flag will not be set

            if we dont indicate control flow for a block, then branching (for eg. a c block)
            will skip the first block in the new stack

            however if we indiciate control flow during the routine that handles stepping to the next block, we risk
            yielding and thus running the first block twice
    ]]
    function Script.Goto(BlockID, DontFlow)
        CurrentBlock = Script.GetBlock(BlockID)

        if CurrentBlock then
            if DontFlow then return end -- There is the possibility we may use this function but NOT want to indicate control flow
            DidControlFlow = true -- Assuming we want, Indicate that we did control flow so that the stepper doesnt skip the new block
        end
    end

    function Script.GetNextBlock(Block) return (Block or CurrentBlock).Next end
    function Script.PeekStack() return Stack[#Stack] end

    -- Find the next block to run, accounting for control flow
    function Script.StepNextBlock()
        while true do
            local LastStack = Script.PopStack()

            if (not LastStack) then -- No more stack, so we're done with this script
                Script.Kill()
                return true
            end

            if LastStack.IsLoop then -- Re-run previous
                Script.Goto(LastStack.BlockID, true)

                if Script.IsWarpMode() then
                    return
                end

                return true -- Unless we're in warp mode, yield 
            end

            -- Check if theres a block after the last one in the stack
            local NextBlock = Script.GetNextBlock(Script.GetBlock(LastStack.BlockID))

            if NextBlock then -- We found a new block, step to it
                Script.Goto(NextBlock, true)
                return
            end

            -- If we dont find a new block, do all of this over again
        end
    end
    
    --[[
        VM Stepper (sequencer.stepThread):
            Thread is running or yielded

            stackframe(s): the identifier for what ran in the past, commonly known as what is the stack
            stack: a group of stack blocks

            First off, Run through every block in a stack to the next until we yield or reach the end of the stack
            However, only go to next block if we havent done control flow

            if we yield, return this step
            if we reach the end of our current stack (no next block)
            we then look at the stackframes
            
            if the previous stackframe identifies as a loop, jump to the said block and re-run it
            otherwise, we jump to the stackframe and find the next block in its stack
    ]]
    function Script.StepBlock()
        if CurrentBlock then -- Simulate vm behavior by treating a null block as a block that isnt ran.
            CurrentBlock.Execute(Script)
        end

        -- Re-wake yielded script
        if Script.State == Enum.STATUS_YIELDED then
            Script.State = Enum.STATUS_RUNNING

            if Script.IsWarpMode() then
                return
            end

            return true -- Re-Run current block next tick
        end

        -- If we already went to a block, we dont wanna continue after here
        if DidControlFlow then
            DidControlFlow = false
            return
        end

        local NextBlock = CurrentBlock and Script.GetNextBlock()

        if NextBlock then
            Script.Goto(NextBlock, true)
        else -- Cannot simply go to next block, look on the stack!
            return Script.StepNextBlock()
        end
    end

    -- Step block until yield or no longer running
    function Script.Step()
        assert(Script.State ~= Enum.STATUS_DONE, "Stepped a killed script!") -- Fucked up shit happens if we dont have this hard check

        while true do
            local DidBreak = Script.StepBlock()

            if Script.State == Enum.STATUS_YIELDTICK then
                Script.State = Enum.STATUS_RUNNING
                return
            end

            -- If we want to break then we retrun from this loop, ALSO hard-coded kill check that prevents this from stepping any further
            if DidBreak or (Script.State == Enum.STATUS_DONE) then return end
        end
    end

    return Script
end