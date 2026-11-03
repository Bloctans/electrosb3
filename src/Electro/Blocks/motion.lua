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

function Motion.TurnLeft(Args, API)
    Motion._SetDirection(API, API.Sprite.Direction - API:Float(Args.DEGREES))
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

function Motion.Direction(_, API)
    return API.Sprite.Direction
end

function Motion._SetDirection(API, Direction)
    API.Sprite.Direction = Direction
    API:RequestRedraw()
end

function Motion._Change(API, Pos)
    if Pos.X ~= Pos.X or Pos.Y ~= Pos.Y then
        return
    end

    Motion._Set(API, API.Sprite.Position + Pos)
end

function Motion._Set(API, Pos)
    API.Sprite.Position = Pos
    API:RequestRedraw()
end

function Motion.Goto(Args, API)
    local Sprite = Electro.Project.SpriteFromName(Args.TO)

    API.Sprite.Position = Sprite.Position:Copy()
    API:RequestRedraw()
end

function Motion.GotoMenu(Args, API)
    return Args.TO.Name
end

function Motion.PointTowards(Args, API)
    
end


function Motion.PointTowardsMenu(Args, API)
    
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
    ["direction"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Motion.Direction
    },
    ["movesteps"] = {
        Type = Enum.BLOCK_STACK,
        Function = Motion.MoveSteps
    },
    ["pointindirection"] = {
        Type = Enum.BLOCK_STACK,
        Function = Motion.SetDirection
    },
    ["setrotationstyle"] = {
        Type = Enum.BLOCK_STACK
    },
    ["turnleft"] = {
        Type = Enum.BLOCK_STACK,
        Function = Motion.TurnLeft
    },
    ["goto"] = {
        Type = Enum.BLOCK_STACK,
        Function = Motion.Goto
    },
    ["goto_menu"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Motion.GotoMenu
    },
    ["pointtowards"] = {
        Type = Enum.BLOCK_STACK,
        Function = Motion.PointTowards
    },
    ["pointtowards_menu"] = {
        Type = Enum.BLOCK_STACK,
        Function = Motion.PointTowardsMenu
    }
}

return Motion