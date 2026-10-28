local Enum = Electro.Enum
local Template = {}

Template.Definitions = {
    ["sounds_menu"] = {
        Type = Enum.BLOCK_INPUT,
        ReturnOptional = true,
        Function = Template.SoundMenu
    },
}

return Template