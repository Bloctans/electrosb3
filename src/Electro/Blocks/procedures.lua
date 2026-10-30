local Enum = Electro.Enum
local procedures = {}

function procedures.Definition(Args, API)
    return Args.custom_block
end

function procedures.Prototype(Args, API)
    return {
        Name = API:GetMutation().Name
    }
end

function procedures.Call(Args, API)
    local Mutation = API:GetMutation()

    API:EachHat("procedures_definition", function(Block)
        local Prototype = Block.Execute(API.Script)

        if Prototype.Name == Mutation.Name then
            API:BranchTo(Block.ID, false)
        end
    end)
end

procedures.Definitions = {
    ["definition"] = { -- Base block, assuming for scratch renderer, ignore.
        Type = Enum.BLOCK_HAT,
        Function = procedures.Definition
    },
    ["prototype"] = { -- Actual definition part we care about.
        Type = Enum.BLOCK_INPUT,
        Function = procedures.Prototype
    },
    ["call"] = {
        Type = Enum.BLOCK_STACK,
        Function = procedures.Call
    }
}

return procedures