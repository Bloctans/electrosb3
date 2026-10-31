package.cpath = package.cpath..";./CLibraries/?.so"

require("Packages.LuauPolyfill")
require("Electro")

local MouseRect
local Anypressed = false

function love.load()
    local FileDialog = require("Packages.filedialog")
    local ProjectPath = "/home/bloctans/github/electrosb3/project_tests/Super Mario Bros. Scratched v0.8.sb3" --FileDialog.OpenFileDialog("Open Project")\
    --local ProjectPath = "/home/bloctans/github/electrosb3/project_tests/Advanced - Scratch the show.pmp"
    --local ProjectPath = "/home/bloctans/github/electrosb3/project_tests/Advanced - POWERTILED.sb3"
    --local ProjectPath = "/home/bloctans/github/electrosb3/project_tests/Advanced - Wave simulator - Edit.pmp" --FileDialog.OpenFileDialog("Open Project")

    if (not ProjectPath) then 
        print("No project passed, qutting...")
        love.event.quit()
        return
    end

    Electro.Init()

    Electro.Project.Load(ProjectPath)
    Electro.StartProject()
end

function love.draw()
    local WindowDimensions = Vector2.new(love.graphics.getWidth(), love.graphics.getHeight())
    local CanvasDimensions = Electro.CanvasSize

    local ScaleRatio = WindowDimensions/CanvasDimensions
    local Aspect = ScaleRatio.Y / ScaleRatio.X

    if Aspect > 1 then
        ScaleRatio = Vector2.one * ScaleRatio.X
    else
        ScaleRatio = Vector2.one * ScaleRatio.Y
    end

    local X,Y = love.mouse.getPosition()
    MouseRect = Electro.Util.Rect(Vector2.new(X / ScaleRatio.X, Y / ScaleRatio.Y), Vector2.one * 20)

    local ElectroCanvas = Electro.Render()

    love.graphics.scale(ScaleRatio.X, ScaleRatio.Y)
    love.graphics.draw(ElectroCanvas,0,0)

    if love.keyboard.isDown(".") then
        Electro.Profiler.Present()
    end
end

function love.keypressed()
    Anypressed = true
end

function love.keyreleased()
    Anypressed = false
end

function love.update(dt)
    Electro.Update(dt, {
        MouseRect = MouseRect,
        AnyPressed = Anypressed
    })
end