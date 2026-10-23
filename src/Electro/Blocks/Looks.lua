local Enum = Electro.Enum
local Looks = {}

function Looks.CostumeMenu(Args, API)
    return API.Sprite.CostumeIDFromName(Args.COSTUME.Name)
end

function Looks.SwitchCostumeTo(Args, API)
    local CostumeID = Args.COSTUME
    API.Sprite.CurrentCostume = CostumeID
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

function Looks.NextCostume(_, API)
    API.Sprite.CurrentCostume = API.Sprite.CurrentCostume + 1
    API:RequestRedraw()
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
        Type = Enum.BLOCK_STACK
    },
    ["hide"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.Hide
    },
    ["cleargraphiceffects"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.Empty
    },
    ["show"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.Show
    },
    ["gotofrontback"] = {
        Type = Enum.BLOCK_STACK,
        Function = Looks.Empty
    }
}

return Looks