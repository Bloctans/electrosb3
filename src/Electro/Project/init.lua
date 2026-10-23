---@class ElectroProject
local Project = {}

Project.Deserializer = require("Electro.Project.Deserializer")
Project.Sprite = require("Electro.Project.Sprite")
Project.Costume = require("Electro.Project.Costume")
Project.Sound = require("Electro.Project.Sound")

Project.Targets = {}

local MountName = "ElectroProject"

function Project.Load(ProjectPath)
    local DidMount = love.filesystem.mountFullPath(ProjectPath, MountName)
    if (not DidMount) then error("Could not mount project at path: "..ProjectPath) end

    Project.Deserializer.Deserialize(MountName)
end

return Project