return function()
    local Sprite = {
        Position = Vector2.zero,
        Size = 100,
        IsStage = false,
        Costumes = {},
        Sounds = {},
        Visible = true,
        CurrentCostume = 0
    }

    function Sprite.GetCostume()
        return Sprite.Costumes[Sprite.CurrentCostume]
    end

    function Sprite.PlaySound(ID)
        Sprite.Sounds[ID].Play()
    end

    function Sprite.CostumeIDFromName(Name)
        for ID, Costume in pairs(Sprite.Costumes) do
            if Costume.Name == Name then
                return ID
            end
        end

        return 1
    end

    function Sprite.SoundIDFromName(Name)
        for ID, Sound in pairs(Sprite.Sounds) do
            if Sound.Name == Name then
                return ID
            end
        end

        return 1
    end

    return Sprite
end