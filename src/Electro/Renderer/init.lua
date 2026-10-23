local Renderer = {}

function Renderer.Init()
    Renderer.Canvas = love.graphics.newCanvas(480, 360)
end

function Renderer.Render()
    love.graphics.setCanvas(Renderer.Canvas)
    love.graphics.clear(1,1,1)

    for _, Target in pairs(Electro.Project.Targets) do
        if Target.Visible then
            local CurrentImage = Target:GetCostume().Image
            local RotationCenter = Target:GetCostume().RotationCenter

            local Position = Electro.Util.FromScratch(Target.Position)

            love.graphics.push()
            love.graphics.translate(Position.X, Position.Y)
            love.graphics.translate(-RotationCenter.X, -RotationCenter.Y)

            love.graphics.draw(CurrentImage, 0,0)
            love.graphics.pop()
        end
    end

    love.graphics.setCanvas()

    love.graphics.draw(Renderer.Canvas, 0,0)
end

return Renderer