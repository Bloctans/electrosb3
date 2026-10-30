---@class ElectroProject
local Project = {}

Project.Deserializer = require("Electro.Project.Deserializer")
Project.Sprite = require("Electro.Project.Sprite")
Project.Costume = require("Electro.Project.Costume")
Project.Sound = require("Electro.Project.Sound")

Project.Targets = {}
Project.StageID = nil

local MountName = "ElectroProject"

function Project.Load(ProjectPath)
    local DidMount = love.filesystem.mountFullPath(ProjectPath, MountName)
    if (not DidMount) then error("Could not mount project at path: "..ProjectPath) end

    Project.Deserializer.Deserialize(MountName)

    for _, Target in pairs(Project.Targets) do
        if Target.IsStage then
            Project.StageID = Target.ID
        end
    end

    -- Sort and sync rendering layers
    table.sort(Electro.Renderer.RenderTargets, function (a, b)
        return a.Layer < b.Layer
    end)

    Electro.Renderer.SyncLayers()
end

function Project.SpriteFromName(Name)
    for _, Target in pairs(Project.Targets) do
        if Target.Name == Name then
            return Target
        end
    end
end

function Project.GetStage()
    return Project.Targets[Project.StageID]
end

return Project