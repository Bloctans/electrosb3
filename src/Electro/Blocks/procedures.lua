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
    local SpriteInfo = API:GetSpriteInfo()

    -- Create prototype cache
    if (not SpriteInfo.PrototypeCache) then SpriteInfo.PrototypeCache = {} end
    local PrototypeCache = SpriteInfo.PrototypeCache

    -- Check if the mutation and block are already cached
    local Prototype = PrototypeCache[Mutation.Name]

    -- If its not, find it in the block list
    if (not Prototype) then
        API:EachHat("procedures_definition", function(Block)
            local Prototype = Block.Execute(API.Script)

            if (Prototype.Name == Mutation.Name) and (Block.Sprite == API.Sprite:GetRootSprite()) then
                if Block.Next then
                    PrototypeCache[Mutation.Name] = {
                        Block = Block,
                        Mutation = Prototype
                    }
                else
                    warn("Found empty procedure during caching, these will cause performance issues if they're the only procedure with that name")
                end
            end
        end)

        Prototype = PrototypeCache[Mutation.Name]
    end

    if Prototype then
        -- Run the prototype
        local PrototypeArgs = Prototype.Mutation.Arguments

        local Stack = API:BranchTo(Prototype.Block.ID, false, Mutation.Warp)
        Stack.IsProcedure = true
        
        for Index, Value in pairs(Args) do
            Stack.Params[PrototypeArgs[Index]] = Value
        end
    end
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