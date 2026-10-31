local Enum = Electro.Enum
local Looks = {}

function Looks.CostumeMenu(Args, API)
    return Args.COSTUME.Name
end

function Looks.SwitchCostumeTo(Args, API)
    local CostumeID = API.Sprite:CostumeIDFromName(Args.COSTUME)
    if not CostumeID then CostumeID = API:Float(Args.COSTUME) end

    API.Sprite:SetCostume(CostumeID)
end

function Looks._SetSize(API, Size)
    API.Sprite.Size = Size
    API:RequestRedraw()
end

function Looks.SetSizeTo(Args, API)
    Looks._SetSize(API, API:Float(Args.SIZE))
end

function Looks.ChangeSizeBy(Args, API)
    Looks._SetSize(API, API.Sprite.Size + API:Float(Args.CHANGE))
end

function Looks.CostumeNumberName(Args, API)
    local Mode = Args.NUMBER_NAME.Name
    
    if Mode == "number" then
        return API.Sprite.CurrentCostume
    else
        return API.Sprite:GetCostume().Name
    end
end

function Looks.Show(_, API)
    API.Sprite.Visible = true
end

function Looks.Hide(_, API)
    API.Sprite.Visible = false
end

function Looks.Size(_, API)
    return API.Sprite.Size
end

function Looks.SetEffectTo(Args, API)
    API.Sprite.Effects[Args.EFFECT.Name] = Args.VALUE
end

function Looks.ChangeEffectBy(Args, API)
    API.Sprite.Effects[Args.EFFECT.Name] = API.Sprite.Effects[Args.EFFECT.Name] + Args.CHANGE
end

function Looks.NextCostume(_, API)
    API.Sprite:SetCostume(API.Sprite.CurrentCostume + 1)
end

function Looks.GotoFrontBack(Args, API)
    local Mode = Args.FRONT_BACK.Name

    if Mode == "back" then
        Electro.Renderer.MoveToLayer(API.Sprite, Electro.Project.GetStage().Layer+1)
    else
        Electro.Renderer.MoveToLayer(API.Sprite, Electro.Renderer.GetTopLayer())
    end
end

function Looks.SwitchBackdropTo(Args, API)
    local Stage = Electro.Project.GetStage()
    Stage:SetCostume(Args.BACKDROP)
end

function Looks.Backdrops(Args, API)
    return Electro.Project.GetStage():CostumeIDFromName(Args.BACKDROP.Name)
end

function Looks.GoLayer(Args, API)
    local Mode = Args.FORWARD_BACKWARD.Name

    if Mode == "backward" then
        Electro.Renderer.MoveToLayer(API.Sprite, API.Sprite.Layer-Args.NUM)
    else
        Electro.Renderer.MoveToLayer(API.Sprite, API.Sprite.Layer+Args.NUM)
    end
end

function Looks.ClearEffects(Args, API)
    local Effects = API.Sprite.Effects

    Effects.GHOST = 0
    Effects.BRIGHTNESS = 0
end

function Looks.Say(Args, API)
    print(Args)
end

Looks.Definitions = {
    ["nextcostume"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.NextCostume
    },
    ["switchcostumeto"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.SwitchCostumeTo
    },
    ["costumenumbername"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Looks.CostumeNumberName
    },
    ["costume"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Looks.CostumeMenu
    },
    ["changeeffectby"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.ChangeEffectBy
    },
    ["switchbackdropto"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.SwitchBackdropTo
    },
    ["seteffectto"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.SetEffectTo
    },
    ["hide"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.Hide
    },
    ["cleargraphiceffects"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.ClearEffects
    },
    ["setsizeto"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.SetSizeTo
    },
    ["changesizeby"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.ChangeSizeBy
    },
    ["size"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Looks.Size
    },
    ["show"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.Show
    },
    ["gotofrontback"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.GotoFrontBack
    },
    ["backdrops"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Looks.Backdrops
    },
    ["say"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.Say
    },
    ["goforwardbackwardlayers"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.GoLayer
    }
}

return Looks