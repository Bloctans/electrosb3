local Enum = Electro.Enum
local Sounds = {}

Sounds.Playing = {}

function Sounds.Play(Args, API)
    local Sound = Args.SOUND_MENU

    if Sound then
        Sound.Play()
    end
end

function Sounds.SoundMenu(Args, API)
    return API.Sprite:SoundFromName(Args.SOUND_MENU.Name)
end

function Sounds.PlayUntilDone(Args, API)
    local Sound = Args.SOUND_MENU

    if Sound.GetPlaying() then
        API:Yield()
    elseif (not Sound.PlayingYield) then
        Sound.PlayingYield = true
        Sound.Play()

        Sounds.Playing[Sound.ID] = Sound

        API:Yield()
    else
        Sounds.Playing[Sound.ID] = nil
        Sound.PlayingYield = false
    end
end

function Sounds.StopAllSounds()
    for _, Sound in pairs(Sounds.Playing) do
        Sound:Stop()
    end
end

Sounds.Definitions = {
    ["sounds_menu"] = {
        Type = Enum.BLOCK_INPUT,
        ReturnOptional = true,
        Function = Sounds.SoundMenu
    },
    ["playuntildone"] = {
        Type = Enum.BLOCK_STACK,
        Function = Sounds.PlayUntilDone
    },
    ["play"] = {
        Type = Enum.BLOCK_STACK,
        Function = Sounds.Play
    },
    ["setvolumeto"] = {
        Type = Enum.BLOCK_STACK
    },
    ["cleareffects"] = {
        Type = Enum.BLOCK_STACK
    },
    ["stopallsounds"] = {
        Type = Enum.BLOCK_STACK,
        Function = Sounds.StopAllSounds
    }
}

return Sounds