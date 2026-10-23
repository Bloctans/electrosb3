local Enum = Electro.Enum
local Operator = {}

function Operator.Equals(Args, API)
    return API:Compare(Args.OPERAND1, Args.OPERAND2) == 0
end

function Operator.Subtract(Args, API)
    print(Args)
end

Operator.Definitions = {
    ["equals"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.Equals
    },
    ["subtract"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Operator.Subtract
    }
}

return Operator