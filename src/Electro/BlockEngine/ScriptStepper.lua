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

    ScriptStepper.Scripts[Script.UUID] = Script
end

function ScriptStepper.StartHats(Opcode)
    for _, Block in pairs(ScriptStepper.Blocks) do
        if Block.Opcode == Opcode then
            ScriptStepper.CreateScript(Block, Block.Sprite)
        end
    end
end

function ScriptStepper.Update(dt)
    local Start = love.timer.getTime()

    while (not ScriptStepper.RedrawRequested) and (love.timer.getTime() - Start) < (Electro.Rate * 0.75) do
        local ToKill = {}

        ---@param Script ElectroScript
        for _, Script in pairs(ScriptStepper.Scripts) do
            Script.Step()

            if Script.State == Enum.STATUS_DONE then
                table.insert(ToKill, Script)
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