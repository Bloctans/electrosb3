local Enum = Electro.Enum
local BlockEngine = Electro.BlockEngine
local Control = {}

function Control.Repeat(Args, API)
    if API.Loops <= Args.TIMES then
        API:BranchTo(Args.SUBSTACK, true)
    else
        API:ResetLoops()
    end
end

function Control.RepeatUntil(Args, API)
    if not Args.CONDITION then
        API:BranchTo(Args.SUBSTACK, true)
    end
end

function Control.Wait(Args, API)
    if not API.TimerStarted then
        API:StartTimer(Args.DURATION)
        API:Yield()
        --API:RequestRedraw()
    elseif not API:TimerEnded() then
        API:Yield()
        API:RequestRedraw() -- For some reason this works???
    end
end

function Control.WaitUntil(Args, API)
    if not Args.CONDITION then
        API:Yield()
        API:RequestRedraw()
    end
end

function Control.Forever(Args, API)
    API:BranchTo(Args.SUBSTACK, true)
end

function Control.If(Args, API)
    if Args.CONDITION then
        API:BranchTo(Args.SUBSTACK, false)
    end
end

function Control.IfElse(Args, API)
    if Args.CONDITION then
        API:BranchTo(Args.SUBSTACK, false)
    else
        API:BranchTo(Args.SUBSTACK2, false)
    end
end

function Control.EachCloneHat(Hat, NewClone)
    if Hat.Sprite == NewClone.Parent then
        BlockEngine.Stepper.CreateScript(Hat, NewClone)
    end
end

---@param API ElectroBlockAPI
function Control.CreateClone(Args, API)
    local NewClone = Args.CLONE_OPTION:CreateClone()
    API:EachHat("control_start_as_clone", Control.EachCloneHat, NewClone)
end

function Control.CreateCloneMenu(Args, API)
    local CloneOption = Args.CLONE_OPTION.Name

    if CloneOption == "_myself_" then
        return API.Sprite
    else
        error("Invalid option "..CloneOption)
    end
end

function Control.DeleteClone(Args, API)
    API.Sprite:Delete()
end

Control.Definitions = {
    ["repeat"] = {
        Type = Enum.BLOCK_STACK,
        Function = Control.Repeat
    },
    ["repeat_until"] = {
        Type = Enum.BLOCK_C,
        Function = Control.RepeatUntil
    },
    ["wait"] = {
        Type = Enum.BLOCK_STACK,
        Function = Control.Wait
    },
    ["forever"] = {
        Type = Enum.BLOCK_C,
        Function = Control.Forever
    },
    ["if"] = {
        Type = Enum.BLOCK_C,
        Function = Control.If
    },
    ["if_else"] = {
        Type = Enum.BLOCK_C,
        Function = Control.IfElse
    },
    ["wait_until"] = {
        Type = Enum.BLOCK_STACK,
        Function = Control.WaitUntil
    },
    ["stop"] = {
        Type = Enum.BLOCK_STACK,
    },
    ["delete_this_clone"] = {
        Type = Enum.BLOCK_STACK,
        Function = Control.DeleteClone
    },
    ["create_clone_of_menu"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Control.CreateCloneMenu
    },
    ["create_clone_of"] = {
        Type = Enum.BLOCK_STACK,
        Function = Control.CreateClone
    },
    ["start_as_clone"] = {
        Type = Enum.BLOCK_HAT
    }
}

return Control