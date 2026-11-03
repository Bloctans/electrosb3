local Enum = Electro.Enum
local Event = {}

function Event.Broadcast(Args, API)
    API:StartHats("event_whenbroadcastreceived", {
        BROADCAST_OPTION = Args.BROADCAST_INPUT
    })
end

function Event.BroadcastAndWait(Args, API)
    local Info = API:GetScriptInfo()

    if (not Info.StartBroadcast) then
        Info.StartBroadcast = true

        Info.Scripts = API:StartHats("event_whenbroadcastreceived", {
            BROADCAST_OPTION = Args.BROADCAST_INPUT
        })
    end

    local ShouldYield = false

    for _, v in pairs(Info.Scripts) do
        if v.Status ~= Enum.STATUS_DONE then
            ShouldYield = true
        end
    end

    if ShouldYield then
        API:YieldTick()
    end
end

Event.Definitions = {
    ["whenflagclicked"] = {
        Type = Enum.BLOCK_HAT
    },
    ["broadcast"] = {
        Type = Enum.BLOCK_STACK,
        Function = Event.Broadcast
    },
    ["broadcastandwait"] = {
        Type = Enum.BLOCK_STACK,
        Function = Event.BroadcastAndWait
    },
    ["whenbroadcastreceived"] = {
        Type = Enum.BLOCK_HAT,
        RestartScripts = true,
    },
    ["whenkeypressed"] = {
        Type = Enum.BLOCK_HAT,
    },
    ["whengreaterthan"] = { -- This is stupid, KNOWN, not implemented..
        Type = Enum.BLOCK_HAT
    },
    ["whenthisspriteclicked"] = { -- This is stupid, KNOWN, not implemented..
        Type = Enum.BLOCK_HAT
    }
}

return Event