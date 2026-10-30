local Enum = Electro.Enum
local Sensing = {}

Sensing.KeyLookup = {
    w = "w",
    a = "a",
    s = "s",
    d = "d",
    space = "space"
}

function Sensing.KeyPressed(Args, _)
    return love.keyboard.isDown(Args.KEY_OPTION)
end

function Sensing.KeyOptions(Args, _)
    return Sensing.KeyLookup[Args.KEY_OPTION.Name]
end

function Sensing.Timer(_, _)
    return love.timer.getTime() - Electro.StartTime
end

function Sensing.MouseDown(_, _)
    return love.mouse.isDown(1)
end

function Sensing.TouchingObjectMenu(Args, API)
    local Type = Args.TOUCHINGOBJECTMENU

    if Type.Name == "_mouse_" then
        return Electro.MouseRect
    elseif Type.Name == "_edge_" then
        return Electro.Util.Rect(Vector2.zero, Electro.CanvasSize, true)
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
}

return Sensing