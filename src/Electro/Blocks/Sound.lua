local Enum = Electro.Enum
local Sound = {}

function Sound.Play(Args, API)
    API.Sprite.PlaySound(Args.SOUND_MENU)
end

function Sound.SoundMenu(Args, API)
    return API.Sprite.SoundIDFromName(Args.SOUND_MENU)
end

Sound.Definitions = {
    ["sounds_menu"] = {
        Type = Enum.BLOCK_INPUT,
        Function = Sound.SoundMenu
    },
    ["play"] = {
        Type = Enum.BLOCK_STACK,
        Function = Sound.Play
    }
}

return Sound