local Enum = Electro.Enum
local Argument = {}

function Argument.ReporterLiteral(Args, API)
    local ProcedureStack = API:GetProcedureStack()
    local Params = ProcedureStack and ProcedureStack.Params or {}

    return Params[Args.VALUE.Name] or 0
end

function Argument.ReporterBoolean(Args, API)
    print(Args)
end

Argument.Definitions = {
    ["reporter_string_number"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Argument.ReporterLiteral
    },
    ["reporter_boolean"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Argument.ReporterBoolean
    }
}

return Argument