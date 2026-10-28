local Enum = Electro.Enum
local Data = {}

function Data.SetVariableTo(Args, API)
    API:SetVariable(Args.VARIABLE.ID, Args.VALUE)
end

function Data.ChangeVariableBy(Args, API)
    local Value = API:GetVariable(Args.VARIABLE.ID)

    API:SetVariable(Args.VARIABLE.ID, Value + Args.VALUE)
end

Data.Definitions = {
    ["setvariableto"] = {
        Type = Enum.BLOCK_STACK,
        Function = Data.SetVariableTo
    },
    ["changevariableby"] = {
        Type = Enum.BLOCK_STACK,
        Function = Data.ChangeVariableBy
    },
    ["showvariable"] = {
        Type = Enum.BLOCK_STACK
    },
    ["hidevariable"] = {
        Type = Enum.BLOCK_STACK
    }
}

return Data