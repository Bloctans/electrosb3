local Enum = Electro.Enum
local Event = {}

function Event.Broadcast(Args, API)
    API:StartHats("event_whenbroadcastreceived", {
        BROADCAST_OPTION = Args.BROADCAST_INPUT
    })
end

Event.Definitions = {
    ["whenflagclicked"] = {
        Type = Enum.BLOCK_HAT
    },
    ["broadcast"] = {
        Type = Enum.BLOCK_STACK,
        Function = Event.Broadcast
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