local Renderer = {}

Renderer.RenderTargets = {}

local SpriteShader = love.graphics.newShader("Electro/Renderer/EffectShader.glsl")

function Renderer.Init()
    Renderer.Canvas = love.graphics.newCanvas(Electro.CanvasSize.X, Electro.CanvasSize.Y)
end

function Renderer.AddTarget(Target)
    table.insert(Renderer.RenderTargets, Target)
end

function Renderer.RemoveTarget(Target)
    table.removeValue(Renderer.RenderTargets, Target)
end

function Renderer.DrawDebugRect(Target)
    local Rect = Target.Rect
    love.graphics.rectangle("line", Rect.X1, Rect.Y1, Rect.X2 - Rect.X1, Rect.Y2 - Rect.Y1)
end

function Renderer.Render(MouseRect)
    Electro.MouseRect = MouseRect

    love.graphics.setCanvas(Renderer.Canvas)
    love.graphics.clear(1,1,1)

    for _, Target in pairs(Renderer.RenderTargets) do
        if Target.Visible then
            local Costume = Target:GetCostume()
            local RotationCenter = Costume and Costume.RotationCenter or Vector2.zero
            local CurrentImage = Costume and Costume.Image

            local Position = Electro.Util.FromScratch(Target.Position)

            Renderer.DrawDebugRect(Target)

            love.graphics.push("all")
            love.graphics.translate(Position.X, Position.Y)
            love.graphics.scale(Target.Size/100)
            love.graphics.rotate(math.rad(Target.Direction - 90))
            love.graphics.translate(-RotationCenter.X, -RotationCenter.Y)

            SpriteShader:send("brightness", Target.Effects.BRIGHTNESS/100)
            love.graphics.setShader(SpriteShader)

            if (not CurrentImage) then
                love.graphics.setColor(0,0,0)
                love.graphics.print("Cannot draw costume",0,0)
            else
                love.graphics.draw(CurrentImage, 0,0)
            end

            love.graphics.setShader()
            love.graphics.pop()
        end
    end

    love.graphics.setCanvas()
    return Renderer.Canvas
end

return Renderer