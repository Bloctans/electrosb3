local Enum = Electro.Enum
local Stepper = Electro.BlockEngine.Stepper

return function(Hat, Sprite)
    ---@class ElectroScript
    local Script = {}

    Script.Sprite = Sprite
    Script.Hat = Hat
    Script.StartBlock = Stepper.GetBlock(Hat.Next)

    local DidControlFlow = false
    local CurrentBlock = Script.StartBlock
    local Stack = {}

    Script.State = Enum.STATUS_RUNNING
    Script.UUID = CreateUUID()

    -- Push the current state to the stack
    function Script.PushStack(IsLoop)
        table.insert(Stack, {
            BlockID = CurrentBlock.ID,
            IsLoop = IsLoop
        })
    end

    function Script.PopStack()
        return table.remove(Stack)
    end

    function Script.SetYielded()
        Script.State = Enum.STATUS_YIELDED
    end

    -- Push our current block to the stack, then goto the new one
    function Script.BranchToBlock(BlockID, IsLoop)
        Script.PushStack(IsLoop)
        Script.Goto(BlockID)
    end

    function Script.Goto(BlockID, DontFlow)
        CurrentBlock = Stepper.GetBlock(BlockID)

        if DontFlow then return end -- There is the possibility we may use this function but NOT want to indicate control flow
        DidControlFlow = true -- Assuming we want, Indicate that we did control flow so that the stepper doesnt skip the new block
    end

    function Script.GetNextBlock(Block) return (Block or CurrentBlock).Next end
    function Script.PeekStack() return Stack[#Stack] end

    -- Find the next block to run, accounting for control flow
    function Script.StepNextBlock()
        while true do
            local LastStack = Script.PopStack()

            if (not LastStack) then -- No more stack, so we're done with this script
                Script.State = Enum.STATUS_DONE
                return true
            end

            if LastStack.IsLoop then -- Re-run previous
                Script.Goto(LastStack.BlockID)
                return true -- Unless we're in warp mode, yield 
            end

            -- Check if theres a block after the last one in the stack
            local NextBlock = Script.GetNextBlock(LastStack.BlockID)

            if NextBlock then -- We found a new block, step to it
                Script.Goto(NextBlock)
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
        CurrentBlock.Execute(Script)

        -- Re-wake yielded script
        if Script.State == Enum.STATUS_YIELDED then
            Script.State = Enum.STATUS_RUNNING
            return true -- Re-Run current block next tick
        end

        -- If we already went to a block, we dont wanna continue after here
        if DidControlFlow then
            DidControlFlow = false
            return
        end

        local NextBlock = Script.GetNextBlock()

        if NextBlock then
            Script.Goto(NextBlock, true)
        else -- Cannot simply go to next block, look on the stack!
            return Script.StepNextBlock()
        end
    end

    -- Step block until yield or no longer running
    function Script.Step()
        while true do
            local DidBreak = Script.StepBlock()
            if DidBreak then return end
        end
    end

    return Script
end