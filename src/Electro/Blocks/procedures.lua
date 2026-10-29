local Enum = Electro.Enum
local procedures = {}

function procedures.Definition(Args, API)
    return Args.custom_block
end

function procedures.Call(Args, API)
    print(Args)
end

procedures.Definitions = {
    ["definition"] = { -- Base block, assuming for scratch renderer, ignore.
        Type = Enum.BLOCK_HAT,
        Function = procedures.Definition
    },
    ["prototype"] = { -- Actual definition part we care about.
        Type = Enum.BLOCK_INPUT
    },
    ["call"] = {
        Type = Enum.BLOCK_STACK,
        Function = procedures.Call
    }
}

return procedures