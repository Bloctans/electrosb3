local Data = {}
local DataEntries = {}, {}

-- Setup stage data container
function Data.SetupData(SpriteID)
    DataEntries[SpriteID] = {
        Variable = {},
        List = {}
    }

    return DataEntries[SpriteID]
end

function Data.GetData(SpriteID, Type)
    return DataEntries[SpriteID][Type], DataEntries[Electro.Project.StageID][Type]
end

function Data.Clear(SpriteID)
    DataEntries[SpriteID] = nil
end

function Data.Clone(SubjectID, TargetID)
    local TargetEntry = Data.SetupData(TargetID)
    local SubjectEntry = table.deepcopy(DataEntries[SubjectID])

    TargetEntry.Variable = SubjectEntry.Variable
    TargetEntry.List = SubjectEntry.List
end

function Data.GetVariable(SpriteID, ID)
    local Variables, StageVariables = Data.GetData(SpriteID, "Variable")

    if StageVariables[ID] then
        return StageVariables[ID]
    else
        if (not Variables[ID]) then Variables[ID] = 0 end -- If it doesnt exist, create it

        return Variables[ID] -- return the sprite variablew
    end
end

function Data.SetVariable(SpriteID, ID, Value)
    local Variables, StageVariables = Data.GetData(SpriteID, "Variable")

    if StageVariables and StageVariables[ID] then
        StageVariables[ID] = Value
    else
        Variables[ID] = Value
    end
end

function Data.GetList(SpriteID, ID)
    local List, StageList = Data.GetData(SpriteID, "List")

    if StageList[ID] then
        return StageList[ID]
    else
        if (not List[ID]) then List[ID] = {} end -- If it doesnt exist, create it

        return List[ID]
    end
end

return Data