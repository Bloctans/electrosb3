-- General supporter functions for handling extensions and their management
local Extension = {}
Extension.BlockSets = {}

function Extension.Register(...)
    local Extensions = {...}

    for _, Name in pairs(Extensions) do
        local Module = require("Electro.Blocks."..Name)

        Extension.BlockSets[string.lower(Name)] = Module.Definitions
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

return Extension