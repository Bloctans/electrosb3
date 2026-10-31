-- General supporter functions for handling extensions and their management
local Extension = {}
Extension.BlockSets = {}

Extension.Events = {
    Update = {}
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

function Extension.KnownBlocks()
    local Known = 0
    local Implemented = 0

    for _, Set in pairs(Extension.BlockSets) do
        Known = Known + table.length(Set)

        for _, Block in pairs(Set) do
            if Block.Function then
                Implemented = Implemented + 1
            end
        end
    end

    return {
        Known = Known,
        Implemented = Implemented,
        Total = 126
    }
end

return Extension