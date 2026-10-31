local Enum = Electro.Enum
local Sensing = {}

Sensing.KeyLookup = {
    w = "w",
    a = "a",
    s = "s",
    d = "d",
    b = "b",
    z = "z",
    n = "n",
    space = "space",
    enter = "return",
    any = "any",
    ["down arrow"] = "down",
    ["up arrow"] = "up",
    ["right arrow"] = "right",
    ["left arrow"] = "left",
}

Sensing.AnyKey = false

local Mouse = Vector2.zero

function Sensing.KeyPressed(Args, _)
    if Args.KEY_OPTION == "any" then
        return Sensing.AnyKey
    end

    return love.keyboard.isDown(Args.KEY_OPTION)
end

function Sensing.KeyOptions(Args, _)
    local Lookup = Sensing.KeyLookup[Args.KEY_OPTION.Name]
    assert(Lookup, "No key "..Args.KEY_OPTION.Name)

    return Lookup
end

function Sensing.Timer(_, _)
    return love.timer.getTime() - Electro.StartTime
end

function Sensing.ResetTimer(_, _)
    Electro.StartTime = love.timer.getTime()
end

function Sensing.MouseDown(_, _)
    return love.mouse.isDown(1)
end

function Sensing.TouchingObjectMenu(Args, API)
    local Type = Args.TOUCHINGOBJECTMENU

    if Type.Name == "_mouse_" then
        return Electro.MouseRect
    elseif Type.Name == "_edge_" then
        return Electro.Util.Rect(Vector2.zero, Electro.CanvasSize)
    else
        return Electro.Project.SpriteFromName(Type.Name).Rect
    end
end

function Sensing.OfObjectMenu(Args, API)
    return Electro.Project.SpriteFromName(Args.OBJECT.Name)
end

function Sensing.Of(Args, API)
    local Property = Args.PROPERTY.Name
    local Object = Args.OBJECT

    if Property == "x position" then
        return Object.Position.X
    end
end

-- TODO: Implement
function Sensing.TouchingObject(Args, API)
    local SpriteRect = API.Sprite.Rect

    return Electro.Util.CheckAABB(Args.TOUCHINGOBJECTMENU, SpriteRect)
end

function Sensing.DistanceTo(Args, API)
    print(Args)
end

function Sensing.DistanceToMenu(Args, API)
    print(Args)
end

function Sensing.LetterOf(Args, API)
    print(Args)
end

function Sensing.MouseX()
    return Mouse.X
end

function Sensing.MouseY()
    return Mouse.Y
end

function Sensing.Loudness()
    return 0
end

function Sensing.OnUpdate()
    Mouse = Electro.Util.ToScratch(Vector2.new(Electro.MouseRect.X1, Electro.MouseRect.Y1))
end

Sensing.Definitions = {
    ["keypressed"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sensing.KeyPressed
    },
    ["keyoptions"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sensing.KeyOptions
    },
    ["timer"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sensing.Timer
    },
    ["mousedown"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sensing.MouseDown
    },
    ["touchingobject"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sensing.TouchingObject
    },
    ["touchingobjectmenu"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sensing.TouchingObjectMenu
    },
    ["of"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sensing.Of
    },
    ["of_object_menu"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sensing.OfObjectMenu
    },
    ["distanceto"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sensing.DistanceTo
    },
    ["distancetomenu"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sensing.DistanceToMenu
    },
    ["letter_of"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sensing.LetterOf
    },
    ["mousex"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sensing.MouseX
    },
    ["mousey"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sensing.MouseY
    },
    ["resettimer"] = {
        Type = Enum.BLOCK_STACK,
        Function = Sensing.ResetTimer
    },
    ["loudness"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sensing.Loudness
    },
    ["askandwait"] = {
        Type = Enum.BLOCK_STACK
    },
    ["answer"] = {
        Type = Enum.BLOCK_INPUT
    }
}

Sensing.Events = {
    Update = Sensing.OnUpdate
}

return Sensing