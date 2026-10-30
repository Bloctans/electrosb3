local Enum = Electro.Enum
local Motion = {}

function Motion.ChangeYBy(Args, API)
    Motion._Change(API, Vector2.yAxis * API:Float(Args.DY))
end

function Motion.MoveSteps(Args, API)
    local Steps = Args.STEPS
    local DirRad = math.rad(API.Sprite.Direction)

    Motion._Change(API, Vector2.new(math.sin(DirRad) * Steps, math.cos(DirRad) * Steps))
end

function Motion.SetX(Args, API)
    Motion._Set(API, Vector2.new(Args.X, Motion.YPosition(nil, API)))
end

function Motion.SetY(Args, API)
    Motion._Set(API, Vector2.new(Motion.XPosition(nil, API), Args.Y))
end

function Motion.TurnRight(Args, API)
    Motion._SetDirection(API, API.Sprite.Direction + API:Float(Args.DEGREES))
end

function Motion.ChangeXBy(Args, API)
    Motion._Change(API, Vector2.xAxis * API:Float(Args.DX))
end

function Motion.SetDirection(Args, API)
    Motion._SetDirection(API, API:Float(Args.DIRECTION))
end

function Motion.GotoXY(Args, API)
    Motion._Set(API, Vector2.new(API:Float(Args.X), API:Float(Args.Y)))
end

function Motion.XPosition(_, API)
    return API.Sprite.Position.X
end

function Motion.YPosition(_, API)
    return API.Sprite.Position.Y
end

function Motion._SetDirection(API, Direction)
    API.Sprite.Direction = Direction
    API:RequestRedraw()
end

function Motion._Change(API, Pos)
    Motion._Set(API, API.Sprite.Position + Pos)
end

function Motion._Set(API, Pos)
    API.Sprite.Position = Pos
    API:RequestRedraw()
end

Motion.Definitions = {
    ["changeyby"] = {
        Type = Enum.BLOCK_STACK,
        Function = Motion.ChangeYBy
    },
    ["changexby"] = {
        Type = Enum.BLOCK_STACK,
        Function = Motion.ChangeXBy
    },
    ["turnright"] = {
        Type = Enum.BLOCK_STACK,
        Function = Motion.TurnRight
    },
    ["setx"] = {
        Type = Enum.BLOCK_STACK,
        Function = Motion.SetX
    },
    ["sety"] = {
        Type = Enum.BLOCK_STACK,
        Function = Motion.SetY
    },
    ["gotoxy"] = {
        Type = Enum.BLOCK_STACK,
        Function = Motion.GotoXY
    },
    ["xposition"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Motion.XPosition
    },
    ["yposition"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Motion.YPosition
    },
    ["movesteps"] = {
        Type = Enum.BLOCK_STACK,
        Function = Motion.MoveSteps
    },
    ["pointindirection"] = {
        Type = Enum.BLOCK_STACK,
        Function = Motion.SetDirection
    }
}

return Motion