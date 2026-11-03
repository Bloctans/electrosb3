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
    x = "x",
    v = "v",
    q = "q",
    e = "e",
    r = "r",
    ["0"] = "0",
    ["1"] = "1",
    ["2"] = "2",
    ["3"] = "3",
    ["4"] = "4",
    ["5"] = "5",
    ["6"] = "6",
    ["7"] = "7",
    ["8"] = "8",
    ["9"] = "9",
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

    local Lookup = Sensing.KeyLookup[Args.KEY_OPTION]
    assert(Lookup, Args.KEY_OPTION.." not in lookup")

    return love.keyboard.isDown(Lookup)
end

function Sensing.KeyOptions(Args, _)
    return Args.KEY_OPTION.Name
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
        return {Electro.MouseRect}
    elseif Type.Name == "_edge_" then
        return {Electro.Util.Rect(Vector2.zero, Electro.CanvasSize, true)}
    else
        return Electro.Project.SpriteFromName(Type.Name):GetCloneRects()
    end
end

function Sensing.OfObjectMenu(Args, API)
    return Electro.Project.SpriteFromName(Args.OBJECT.Name)
end

function Sensing.Of(Args, API)
    local Property = Args.PROPERTY.Name
    local Object = Args.OBJECT

    local AsVariable = Electro.Data.GetLookup(Object.ID, Property)

    if Property == "x position" then
        return Object.Position.X
    elseif Property == "y position" then
        return Object.Position.Y
    elseif Property == "direction" then
        return Object.Direction
    elseif Property == "costume name" then
        return Object:GetCostume().Name
    elseif AsVariable then
        return Electro.Data.GetVariable(Object.ID, AsVariable)
    else
        error("Invalid property "..Property)
    end
end

-- TODO: Implement
function Sensing.TouchingObject(Args, API)
    API.Sprite:Redraw()

    local SpriteRect = API.Sprite.Rect
    local Rects = Args.TOUCHINGOBJECTMENU

    local Touching = false

    for _, Rect in pairs(Rects) do
        if Electro.Util.CheckAABB(SpriteRect, Rect) then
            Touching = true
        end
    end

    return Touching
end

function Sensing.DistanceTo(Args, API)
    local SubjectSprite = Electro.Project.SpriteFromName(Args.DISTANCETOMENU)

    return (API.Sprite.Position - SubjectSprite.Position):Magnitude()
end

function Sensing.DistanceToMenu(Args, API)
    return Args.DISTANCETOMENU.Name
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

function Sensing.Username()
    return "ElectroUser"
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
    },
    ["username"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sensing.Username
    }
}

Sensing.Events = {
    Update = Sensing.OnUpdate
}

return Sensing