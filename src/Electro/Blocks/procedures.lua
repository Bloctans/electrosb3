local Enum = Electro.Enum
local procedures = {}

procedures.Definitions = {
    ["definition"] = { -- Base block, assuming for scratch renderer, ignore.
        Type = Enum.BLOCK_HAT
    },
    ["prototype"] = { -- Actual definition part we care about.
        Type = Enum.BLOCK_INPUT
    },
    ["call"] = {
        Type = Enum.BLOCK_STACK
    }
}

return procedures