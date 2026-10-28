-- Simulates the Scratch-VM Sequencer
local ScriptStepper = {}

local Enum, BlockEngine = Electro.Enum, Electro.BlockEngine

ScriptStepper.RedrawRequested = false

ScriptStepper.Scripts = {}
ScriptStepper.Blocks = {}

function ScriptStepper.RequestRedraw()
    ScriptStepper.RedrawRequested = true
end

function ScriptStepper.AddBlock(ID, Block)
    ScriptStepper.Blocks[ID] = Block
end

function ScriptStepper.GetBlock(ID)
    return ScriptStepper.Blocks[ID]
end

-- Create a new script object using a target sprite and hat
function ScriptStepper.CreateScript(Hat, Sprite)
    local Script = BlockEngine.Script(Hat, Sprite)
    --print("Create new "..Hat.Opcode, Script.UUID)

    ScriptStepper.Scripts[Script.UUID] = Script
end

function ScriptStepper.EachScript(Callback)
    for _, Script in pairs(ScriptStepper.Scripts) do
        Callback(Script)
    end
end

function ScriptStepper.EachHat(Opcode, Callback, ...)
    for _, Block in pairs(ScriptStepper.Blocks) do
        if Block.Opcode == Opcode then
            Callback(Block, ...)
        end
    end
end

--[[
    Start a single hat block.

    Currently only handles creation per clone, and not restarting threads

    for restarting threads:
        although this is probably a really bad idea, 
]]
function ScriptStepper.StartHat(Hat)
    local BlockSprite = Hat.Sprite

    ScriptStepper.CreateScript(Hat, Hat.Sprite)
end

function ScriptStepper.StartHats(Opcode, Fields)
    ScriptStepper.EachHat(Opcode, function(Block, Fields)
        local PassFields = true

        if Fields then
            for Name, Field in pairs(Block.ParseFields()) do
                if Fields[Name] ~= Field.Name then
                    PassFields = false
                end
            end
        end

        if PassFields then
            ScriptStepper.StartHat(Block)
        end
    end, Fields)
end

function ScriptStepper.Update(dt)
    local Start = love.timer.getTime()

    while (not ScriptStepper.RedrawRequested) and ((love.timer.getTime() - Start) < (Electro.Rate * 0.75)) do
        local ToKill = {}

        ---@param Script ElectroScript
        for _, Script in pairs(ScriptStepper.Scripts) do
            if Script.State == Enum.STATUS_DONE then
                ToKill[Script.UUID] = Script
            else
                Script.Step()
            end
        end

        for _, Script in pairs(ToKill) do
            -- TODO: More

            ScriptStepper.Scripts[Script.UUID] = nil
        end
    end

    ScriptStepper.RedrawRequested = false
end

return ScriptStepper