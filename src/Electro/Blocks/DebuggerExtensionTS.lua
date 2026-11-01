-- Since the addons debugger uses procedures, 
-- this is an implementation of the log block from Shovel Debugger by TheShovel (https://github.com/TheShovel/)
local Enum = Electro.Enum
local Debugger = {}

function Debugger.Log(Args, API)
    if Electro.Flags.EnableDebugger then
        print(Args.TEXT)
    end
end

Debugger.Definitions = {
    ["log"] = {
        Type = Enum.BLOCK_STACK,
        Function = Debugger.Log
    },
}

return Debugger