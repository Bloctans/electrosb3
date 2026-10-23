Electro = {
    VERSION = "0.1",
    Rate = 1/30
}

-- Load our packages here for now
Resvg = require("Packages.svg")
JSON = require("Packages.json")
Vector2 = require("Packages.Vector2")

function Electro.PrintSplash()
    print("\n\nElectroSB3 "..Electro.VERSION.."\nA LOVE reimplementation of the Scratch VM, Read the README for more info.\nOriginally Created by Touchcreator, Taken over by Bloctans.\n")
end

function Electro.Init()
    Electro.Util = require("Electro.Util")
    Electro.Enum = require("Electro.Enum")

    Electro.Project = require("Electro.Project")
    Electro.BlockEngine = require("Electro.BlockEngine")
    Electro.Renderer = require("Electro.Renderer")

    Electro.Renderer.Init()
    Electro.BlockEngine.Init()

    Electro.PrintSplash()
end

function Electro.Render()
    Electro.Renderer.Render()
end

function Electro.Update(Delta)
    Electro.BlockEngine.Update()
end

return Electro