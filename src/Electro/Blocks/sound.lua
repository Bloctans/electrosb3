local Enum = Electro.Enum
local Sounds = {}

Sounds.Playing = {}

local Volume = 100

function Sounds.Play(Args, API)
    local Sound = API.Sprite:SoundFromName(Args.SOUND_MENU)
    if (not Sound) then return end

    if Sound then
        Sound.Play()
    end
end

function Sounds.SoundMenu(Args, API)
    return Args.SOUND_MENU.Name
end

function Sounds.PlayUntilDone(Args, API)
    local Sound = API.Sprite:SoundFromName(Args.SOUND_MENU)
    if (not Sound) then return end

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

function Sounds.ChangeVolumeBy(Args, API)
    print(Args)
end

function Sounds.Volume()
    return Volume
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
    ["changevolumeby"] = {
        Type = Enum.BLOCK_STACK,
        Function = Sounds.ChangeVolumeBy
    },
    ["volume"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sounds.Volume
    },
    ["seteffectto"] = {
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