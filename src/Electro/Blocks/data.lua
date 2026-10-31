local Enum = Electro.Enum
local Data = {}

function Data.SetVariableTo(Args, API)
    API:SetVariable(Args.VARIABLE.ID, Args.VALUE)
end

function Data.ChangeVariableBy(Args, API)
    local Value = API:GetVariable(Args.VARIABLE.ID)

    API:SetVariable(Args.VARIABLE.ID, Value + Args.VALUE)
end

function Data.DeleteAllOfList(Args, API)
    local List = API:GetList(Args.LIST.ID)
    table.clear(List)
end

function Data.ItemOfList(Args, API)
    return API:GetList(Args.LIST.ID)[API:Float(Args.INDEX)]
end

function Data.AddToList(Args, API)
    local List = API:GetList(Args.LIST.ID)

    table.insert(List, Args.ITEM)
end

function Data.LengthOfList(Args, API)
    return #API:GetList(Args.LIST.ID)
end

function Data.ItemNumberOfList(Args, API)
    print(Args)
end

function Data.ReplaceItemOfList(Args, API)
    local List = API:GetList(Args.LIST.ID)

    List[Args.INDEX] = Args.ITEM
end

function Data.DeleteOfList(Args, API)
    print(Args)
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
    },
    ["deletealloflist"] = {
        Type = Enum.BLOCK_STACK,
        Function = Data.DeleteAllOfList
    },
    ["itemoflist"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Data.ItemOfList
    },
    ["addtolist"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Data.AddToList
    },
    ["lengthoflist"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Data.LengthOfList
    },
    ["itemnumoflist"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Data.ItemNumberOfList
    },
    ["replaceitemoflist"] = {
        Type = Enum.BLOCK_STACK,
        Function = Data.ReplaceItemOfList
    },
    ["deleteoflist"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Data.DeleteOfList
    },
}

return Data