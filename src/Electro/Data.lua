local Data = {}
local Variable = {}

-- Setup stage data container
function Data.SetupData(SpriteID)
    Variable[SpriteID] = {}
    return Variable[SpriteID]
end

function Data.GetVariables(SpriteID)
    return Variable[SpriteID], Variable[Electro.Project.StageID]
end

function Data.Clear(SpriteID)
    Variable[SpriteID] = nil
end

function Data.Clone(SubjectID, TargetID)
    local TargetVariables = Data.SetupData(TargetID)

    for ID, Value in pairs(Variable[SubjectID]) do
        TargetVariables[ID] = Value
    end
end

function Data.GetVariable(SpriteID, ID)
    local Variables, StageVariables = Data.GetVariables(SpriteID)

    if StageVariables[ID] then
        return StageVariables[ID]
    else
        if (not Variables[ID]) then Variables[ID] = 0 end -- If it doesnt exist, create it

        return Variables[ID] -- return the sprite variablew
    end
end

function Data.SetVariable(SpriteID, ID, Value)
    local Variables, StageVariables = Data.GetVariables(SpriteID)

    if StageVariables and StageVariables[ID] then
        StageVariables[ID] = Value
    else
        Variables[ID] = Value
    end
end

return Data