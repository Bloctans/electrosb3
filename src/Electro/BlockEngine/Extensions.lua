-- General supporter functions for handling extensions and their management
local Extension = {}
Extension.BlockSets = {}

Extension.Events = {
    Update = {},
    MouseClick = {}
}

function Extension.CallEvents(Name)
    for _, Function in pairs(Extension.Events[Name]) do
        Function()
    end
end

function Extension.Register(...)
    local Extensions = {...}

    for _, Name in pairs(Extensions) do
        local Module = require("Electro.Blocks."..Name)

        Extension.BlockSets[Name] = Module.Definitions

        if Module.Events then
            for Event, Function in pairs(Module.Events) do
                table.insert(Extension.Events[Event], Function)
            end
        end
    end
end

function Extension.GetDefinition(Opcode)
    local Split = string.split(Opcode, "_")

    local BlockSet = Extension.BlockSets[Split[1]]
    assert(BlockSet, "Opcode "..Opcode.." doesnt exist!")

    local BlockDef = BlockSet[table.concat(Split, "_", 2, #Split)]
    assert(BlockDef, "Opcode "..Opcode.." doesnt exist!")

    return BlockDef
end

-- dumbass way to do this? idk
function Extension.SetVariable(Set, Key, Value)
    require("Electro.Blocks."..Set)[Key] = Value
end

return Extension