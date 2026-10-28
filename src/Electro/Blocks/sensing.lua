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
    end
end

function Sensing.OfObjectMenu(Args, API)
    
end

function Sensing.Of(Args, API)
    print(Args)
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