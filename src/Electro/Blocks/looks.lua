local Enum = Electro.Enum
local Looks = {}

function Looks.CostumeMenu(Args, API)
    return API.Sprite:CostumeIDFromName(Args.COSTUME.Name)
end

function Looks.SwitchCostumeTo(Args, API)
    local CostumeID = Args.COSTUME
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
    end
end

function Looks.Empty()
   
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

function Looks.NextCostume(_, API)
    API.Sprite:SetCostume(API.Sprite.CurrentCostume + 1)
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
        Type = Enum.BLOCK_STACK
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
        Type = Enum.BLOCK_STACK
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
        Type = Enum.BLOCK_STACK
    }
}

return Looks