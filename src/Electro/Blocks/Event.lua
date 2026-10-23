local Enum = Electro.Enum
local Event = {}

function Event.Empty(Args, API)
    
end

Event.Definitions = {
    ["whenflagclicked"] = {
        Type = Enum.BLOCK_HAT
    },
    ["broadcast"] = {
        Type = Enum.BLOCK_STACK,
        Function = Event.Empty
    },
    ["whenbroadcastreceived"] = {
        Type = Enum.BLOCK_HAT
    }
}

return Event