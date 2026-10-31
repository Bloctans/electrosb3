local Enum = Electro.Enum
local procedures = {}

function procedures.Definition(Args, API)
    return Args.custom_block
end

function procedures.Prototype(Args, API)
    return API:GetMutation()
end

function procedures.Call(Args, API)
    local Mutation = API:GetMutation()

    API:EachHat("procedures_definition", function(Block)
        local Prototype = Block.Execute(API.Script)

        if (Prototype.Name == Mutation.Name) and (Block.Sprite == API.Sprite:GetRootSprite()) then
            print("Found proc for "..Mutation.Name)

            local PrototypeArgs = Prototype.Arguments

            local Stack = API:BranchTo(Block.ID, false)
            Stack.IsProcedure = true

            for Index, Value in pairs(Args) do
                Stack.Params[PrototypeArgs[Index]] = Value
            end
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