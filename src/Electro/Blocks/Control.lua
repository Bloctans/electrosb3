local Enum = Electro.Enum
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
    elseif not API:TimerEnded() then
        API:Yield()
    end
end

function Control.Empty()
    
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
    ["delete_this_clone"] = {
        Type = Enum.BLOCK_STACK,
        Function = Control.Empty
    },
    ["create_clone_of_menu"] = {
        Type = Enum.BLOCK_STACK,
        Function = Control.Empty
    },
    ["create_clone_of"] = {
        Type = Enum.BLOCK_STACK,
        Function = Control.Empty
    },
    ["start_as_clone"] = {
        Type = Enum.BLOCK_HAT,
        Function = Control.Empty
    }
}

return Control