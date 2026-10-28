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

    function Block.ParseInput(Data, Script)
        local Type = Data[1]
        local Value = Data[2]

        if type(Value) == "table" then
            Data = Value

            Type = Data[1]
            Value = Data[2]
        end

        if Type <= 3 then -- Blocks/Substacks
            local Block = Electro.BlockEngine.GetBlock(Value)

            if Block and (Block.Definition.Type == Electro.Enum.BLOCK_INPUT) then -- Execute this block
                local Return = Block.Execute(Script)

                if not Block.Definition.ReturnOptional then
                    assert(type(Return) ~= "nil", Block.Opcode.." returned nil")
                end

                return Return
            else
                return Value
            end
        elseif Type == 10 then -- String
            return Value
        elseif Type == 11 then -- Broadcast
            return Value
        elseif Type == 12 then -- Variable
            return Block.API:GetVariable(Data[3])
        elseif Type >= 4 and Type <= 9 then
            return tonumber(Value)
        else
            error("Invalid Type "..Type.." ("..Value..")")
        end
    end

    -- This IS recursive but oh well
    function Block.ParseInputs(Script)
        local ParsedInputs = {}

        for Name, Data in pairs(Block.RawArgs.Inputs) do
            ParsedInputs[Name] = Block.ParseInput(Data, Script)
        end

        return ParsedInputs
    end

    function Block.ParseFields(Inputs)
        local Inputs = Inputs or {}

        for Name, Value in pairs(Block.RawArgs.Fields) do
            Inputs[Name] = {
                Name = Value[1],
                ID = Value[2]
            }
        end

        return Inputs
    end

    function Block.ParseArgs(Script)
        local Inputs = Block.ParseInputs(Script)
        Block.ParseFields(Inputs)

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
        assert(Definition, Block.Opcode.." has no definition!")
        
        local Args = Block.ParseArgs(Script)

        if (not Definition.Function) then
            print(Block.Opcode.." has no function definition, skipping")
            return
        end

        return Definition.Function(Args, Block.API)
    end

    return Block
end