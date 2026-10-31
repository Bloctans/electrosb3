local Renderer = {}

Renderer.RenderTargets = {}

local SpriteShader = love.graphics.newShader("Electro/Renderer/EffectShader.glsl")

function Renderer.Init()
    Renderer.Canvas = love.graphics.newCanvas(Electro.CanvasSize.X, Electro.CanvasSize.Y)
    Renderer.PenCanvas = love.graphics.newCanvas(Electro.CanvasSize.X, Electro.CanvasSize.Y)
end

function Renderer.AddTarget(Target)
    table.insert(Renderer.RenderTargets, Target)
end

function Renderer.RemoveTarget(Target)
    table.removeValue(Renderer.RenderTargets, Target)
end

function Renderer.DrawDebug(Target)
    love.graphics.push("all")
    love.graphics.origin()

    local Rect = Target.Rect
    love.graphics.rectangle("line", Rect.X1, Rect.Y1, Rect.X2 - Rect.X1, Rect.Y2 - Rect.Y1)

    love.graphics.pop()
    love.graphics.print("Layer "..Target.Layer, 0,0)
    love.graphics.print("CostumeID "..Target.CurrentCostume, 0,20)
end

function Renderer.DebugLayer()
    local a = {}
    for i, _ in pairs(Renderer.RenderTargets) do table.insert(a,i) end

    print(a)
end

function Renderer.MoveToLayer(Target, Layer)
    assert(Target, "no target")

    Layer = math.max(Layer, 1)

    -- Remove the target from the renderer
    local TargetIndex = table.find(Renderer.RenderTargets, Target)
    table.remove(Renderer.RenderTargets, TargetIndex)

    local Length = #Renderer.RenderTargets
    local NewTargets = {}

    for i = 1,Layer-1 do
        table.insert(NewTargets, Renderer.RenderTargets[i])
    end

    table.insert(NewTargets, Target)

    -- Shift all after the layer to target up
    for i = Layer, Length do
        table.insert(NewTargets, Renderer.RenderTargets[i])
    end

    Renderer.RenderTargets = NewTargets

    -- Add back to targets
    Renderer.SyncLayers()
end

function Renderer.SyncLayers()
    for Layer, Target in pairs(Renderer.RenderTargets) do
        Target.Layer = Layer
    end
end

function Renderer.GetTopLayer()
    return table.length(Renderer.RenderTargets)+1
end

function Renderer.Render()
    Electro.Profiler.Start("Electro - Render")

    love.graphics.push("all")
    love.graphics.setCanvas(Renderer.Canvas)
    love.graphics.clear(1,1,1)

    for Layer, Target in pairs(Renderer.RenderTargets) do
        Electro.Profiler.Start("Render Target")

        if Layer == 2 then -- Draw pen layer before layer 2
            love.graphics.draw(Renderer.PenCanvas)
        end

        if Target.Visible then
            local Costume = Target:GetCostume()
            local RotationCenter = Costume and Costume.RotationCenter or Vector2.zero
            local CurrentImage = Costume and Costume.Image

            local Position = Electro.Util.FromScratch(Target.Position)

            love.graphics.push("all")
            love.graphics.translate(Position.X, Position.Y)
            love.graphics.scale(Target.Size/100 * Costume.Scale)
            love.graphics.rotate(math.rad(Target.Direction - 90))
            love.graphics.translate(-RotationCenter.X, -RotationCenter.Y)

            local Effects = Target.Effects

            SpriteShader:send("brightness", Effects.BRIGHTNESS/100)
            love.graphics.setShader(SpriteShader)
            love.graphics.setColor(1,1,1, 1- (Effects.GHOST/100))

            if (not CurrentImage) then
                love.graphics.setColor(0,0,0)
                love.graphics.print("Invalid costume",0,0)
            else
                love.graphics.draw(CurrentImage, 0,0)
            end

            --Renderer.DrawDebug(Target)

            love.graphics.setShader()
            love.graphics.pop()
        end

        Electro.Profiler.End()
    end

    love.graphics.pop()
    Electro.Profiler.End()
    
    return Renderer.Canvas
end

return Renderer