-- Load our packages here for now
Resvg = require("Packages.svg")
JSON = require("Packages.json")
Vector2 = require("Packages.Vector2")
Delton = require("Packages.delton")

require("table.clear")

Electro = {
    VERSION = "0.1",
    Rate = 1/30,
    StartTime = 0,
    CanvasSize = Vector2.new(512,448)--480, 360),
}

function Electro.PrintSplash()
    print("\n\nElectroSB3 "..Electro.VERSION.."\nA LOVE reimplementation of the Scratch VM, Read the README for more info.\nOriginally Created by Touchcreator, Taken over by Bloctans.\n")

    local Known = Electro.BlockEngine.Extensions.KnownBlocks()
    print(Known.Implemented.." blocks implemented and "..Known.Known.." blocks known out of "..Known.Total.." total blocks")
end

function Electro.StartProject()
    Electro.BlockEngine.StartHats("event_whenflagclicked")
    Electro.StartTime = love.timer.getTime()
end

function Electro.Init()
    Electro.Util = require("Electro.Util")
    Electro.Profiler = require("Electro.Profiler")
    Electro.Enum = require("Electro.Enum")

    Electro.MouseRect = Electro.Util.Rect(Vector2.zero, Vector2.zero)

    Electro.Data = require("Electro.Data")
    Electro.Project = require("Electro.Project")
    Electro.BlockEngine = require("Electro.BlockEngine")
    Electro.Renderer = require("Electro.Renderer")

    Electro.Render = Electro.Renderer.Render

    Electro.Profiler.Init()
    Electro.Renderer.Init()
    Electro.BlockEngine.Init()

    Electro.PrintSplash()
end

function Electro.Update(_, Config)
    Electro.Profiler.Start("Electro - Update")

    Electro.MouseRect = Config.MouseRect or Electro.Util.Rect(Vector2.zero, Vector2.zero)

    Electro.BlockEngine.SetExtensionVariable("sensing", "AnyKey", Config.AnyPressed)

    Electro.BlockEngine.Update()

    Electro.Profiler.End()
    Electro.Profiler.Render()
end

return Electro