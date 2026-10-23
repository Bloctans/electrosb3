package.cpath = package.cpath..";./CLibraries/?.so"

require("Packages.LuauPolyfill")
require("Electro")

function love.load()
    local FileDialog = require("Packages.filedialog")
    local ProjectPath = "/home/bloctans/github/electrosb3/project_tests/amv/The Air Up Here 6.sb3" --FileDialog.OpenFileDialog("Open Project")

    if (not ProjectPath) then 
        print("No project passed, qutting...")
        love.event.quit()
        return
    end

    Electro.Init()
    Electro.Project.Load(ProjectPath)
    Electro.BlockEngine.StartHats("event_whenflagclicked")
end

function love.draw()
    Electro.Render()
end

function love.update(dt)
    Electro.Update(dt)
end