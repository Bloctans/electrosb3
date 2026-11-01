local Enum = Electro.Enum
local Renderer = Electro.Renderer
local PenCanvas = Renderer.PenCanvas

local Pen = {}

function Pen.Clear(Args, API) -- Hopefully love is fine with draw operations during updates...
    --[[love.graphics.setCanvas(PenCanvas)
    love.graphics.clear(0,0,0,0)
    love.graphics.setCanvas()]]
end

function Pen.Stamp(Args, API)
    love.graphics.setCanvas(PenCanvas)
    love.graphics.origin()
    Renderer.RenderTarget(API.Sprite)
    love.graphics.setCanvas()
end

Pen.Definitions = {
    ["clear"] = {
        Type = Enum.BLOCK_STACK,
        Function = Pen.Clear
    },
    ["stamp"] = {
        Type = Enum.BLOCK_STACK,
        Function = Pen.Stamp
    },
    ["setPenColorToColor"] = {
        Type = Enum.BLOCK_STACK
    },
    ["setPenColorParamTo"] = {
        Type = Enum.BLOCK_STACK
    },
    ["setPenSizeTo"] = {
        Type = Enum.BLOCK_STACK
    },
    ["penDown"] = {
        Type = Enum.BLOCK_STACK
    },
    ["penUp"] = {
        Type = Enum.BLOCK_STACK
    },
    ["menu_colorParam"] = {
        Type = Enum.BLOCK_INPUT,
        ReturnOptional = true
    }
}

return Pen