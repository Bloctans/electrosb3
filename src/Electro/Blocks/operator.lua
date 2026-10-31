local Enum = Electro.Enum
local Operator = {}

local MathOps = {
    floor = math.floor,
    sin = math.sin,
    cos = math.cos
}

local Trig = {sin = true, cos = true, tan = true} -- These require degrees to radians

function Operator.Equals(Args, API)
    return API:Compare(Args.OPERAND1, Args.OPERAND2) == 0
end

function Operator.GreaterThan(Args, API)
    return API:Compare(Args.OPERAND1, Args.OPERAND2) > 0
end

function Operator.LessThan(Args, API)
    return API:Compare(Args.OPERAND1, Args.OPERAND2) < 0
end

function Operator.Join(Args, API)
    return Args.STRING1..Args.STRING2
end

function Operator.LetterOf(Args, API)
    print(Args) 
end

function Operator.Length(Args, API)
    print(Args)
end

function Operator.Round(Args, API)
    print(Args)
end

function Operator.Multiply(Args, API)
    return API:Float(Args.NUM1) * API:Float(Args.NUM2)
end

function Operator.Not(Args, API)
    return not API:Boolean(Args.OPERAND)
end

function Operator.And(Args, API)
    return API:Boolean(Args.OPERAND1) and API:Boolean(Args.OPERAND2)
end

function Operator.Or(Args, API)
    return API:Boolean(Args.OPERAND1) or API:Boolean(Args.OPERAND2)
end

function Operator.Divide(Args, API)
    return API:Float(Args.NUM1) / API:Float(Args.NUM2)
end

function Operator.Add(Args, API)
    return API:Float(Args.NUM1) + API:Float(Args.NUM2)
end

function Operator.Subtract(Args, API)
    return API:Float(Args.NUM1) - API:Float(Args.NUM2)
end

function Operator.MathOperation(Args, API)
    local OpString = Args.OPERATOR.Name
    local Operation = MathOps[OpString]
    if (not Operation) then error("No operator "..Args.OPERATOR.Name) end

    local Value = API:Float(Args.NUM)

    if Trig[OpString] then
        Value = math.rad(Value)
    end

    return Operation(Value)
end

function Operator.Modulo(Args, API)
    return API:Float(Args.NUM1) % API:Float(Args.NUM2)
end

function Operator.Random(Args, API)
    return math.random(API:Float(Args.FROM), API:Float(Args.TO))
end

Operator.Definitions = {
    ["equals"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.Equals
    },
    ["subtract"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.Subtract
    },
    ["multiply"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.Multiply
    },
    ["divide"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.Divide
    },
    ["add"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.Add
    },
    ["join"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.Join
    },
    ["not"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.Not
    },
    ["gt"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.GreaterThan
    },
    ["lt"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.LessThan
    },
    ["mathop"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.MathOperation
    },
    ["mod"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.Modulo
    },
    ["and"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.And
    },
    ["or"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.Or
    },
    ["random"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.Random
    },
    ["letter_of"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.LetterOf
    },
    ["length"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.Length
    },
    ["round"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.Round
    }
}

return Operator