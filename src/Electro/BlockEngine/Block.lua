return function()
    local Block = {
        ID = nil,
        Next = nil,
        Parent = nil,
        Opcode = nil,
        Sprite = nil,
        Definition = nil,
        RawArgs = {},
        API = Electro.BlockEngine.BlockAPI() ---@class ElectroBlockAPI
    }

    -- This IS recursive but oh well
    function Block.ParseInputs(Inputs, Script)
        local ParsedInputs = {}

        for Name, Data in pairs(Inputs) do
            local Type = Data[1]
            local Value = Data[2]

            if type(Value) == "table" then
                Type = Value[1]
                Value = Value[2]
            end

            if Type <= 3 then -- Blocks/Substacks
                local Block = Electro.BlockEngine.GetBlock(Value)

                if Block.Definition.Type == Electro.Enum.BLOCK_INPUT then -- Execute this block
                    local Return = Block.Execute(Script)
                    assert(type(Return) ~= "nil", Block.Opcode.." returned nil")

                    ParsedInputs[Name] = Return
                else
                    ParsedInputs[Name] = Value
                end
            elseif Type == 10 then -- String
                ParsedInputs[Name] = Value
            elseif Type == 11 then -- Broadcast (TODO)
                ParsedInputs[Name] = nil
            elseif Type >= 4 and Type <= 9 then
                ParsedInputs[Name] = tonumber(Value)
            else
                error("Invalid Type "..Type.." ("..Value..")")
            end
        end

        return ParsedInputs
    end

    function Block.ParseArgs(Args, Script)
        local Inputs = Block.ParseInputs(Args.Inputs, Script)

        for Name, Value in pairs(Args.Fields) do
            Inputs[Name] = {
                Name = Value[1],
                ID = Value[2]
            }
        end

        return Inputs
    end

    --[[
        1. Go through and collect result of all inputs
        2. Run block

        (ONLY HATS CAN HAVE NO FUNCTION IN THEIR DEF!!)
    ]]
    function Block.Execute(Script)
        Block.API:Configure(Script, Script.Sprite, Block)
        Block.API.Loops = Block.API.Loops + 1

        local Definition = Block.Definition
        assert(Definition and Definition.Function, Block.Opcode.." has no function definition")
        
        local Args = Block.ParseArgs(Block.RawArgs, Script)

        return Definition.Function(Args, Block.API)
    end

    return Block
end