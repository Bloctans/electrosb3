package.cpath = package.cpath..";./CLibraries/?.so"

require("Packages.LuauPolyfill")
require("Electro")

function love.load()
    local FileDialog = require("Packages.filedialog")
    local ProjectPath = "/home/bloctans/github/electrosb3/project_tests/Advanced - Wave simulator - Edit.pmp" --FileDialog.OpenFileDialog("Open Project")

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
    local MouseRect = Electro.Util.Rect(Vector2.new(X / ScaleRatio.X, Y / ScaleRatio.Y), Vector2.one * 20)

    local ElectroCanvas = Electro.Render(MouseRect)

    love.graphics.scale(ScaleRatio.X, ScaleRatio.Y)
    love.graphics.draw(ElectroCanvas,0,0)
end

function love.update(dt)
    Electro.Update(dt)
end