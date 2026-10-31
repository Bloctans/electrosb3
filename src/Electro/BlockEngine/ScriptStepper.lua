-- Simulates the Scratch-VM Sequencer
local ScriptStepper = {}

local Enum, BlockEngine = Electro.Enum, Electro.BlockEngine

ScriptStepper.RedrawRequested = false

ScriptStepper.Scripts = {}
ScriptStepper.HatLookup = {} -- lookup of running scripts to current hats
ScriptStepper.Blocks = {}
ScriptStepper.BlocksByTarget = {}

function ScriptStepper.RequestRedraw()
    ScriptStepper.RedrawRequested = true
end

function ScriptStepper.AddBlock(ID, Block, TargetID)
    if (not ScriptStepper.BlocksByTarget[TargetID]) then
        ScriptStepper.BlocksByTarget[TargetID] = {}
    end

    ScriptStepper.BlocksByTarget[TargetID][ID] = Block
    ScriptStepper.Blocks[ID] = Block
end

function ScriptStepper.GetBlock(ID)
    return ScriptStepper.Blocks[ID]
end

-- Create a new script object using a target sprite and hat
function ScriptStepper.CreateScript(Hat, Sprite)
    if (not Hat.Next) then -- skip empty hats
        return
    end

    local Script = BlockEngine.Script(Hat, Sprite)
    --print("Create new "..Hat.Opcode, Script.UUID)

    table.insert(ScriptStepper.Scripts, Script)

    if (not ScriptStepper.HatLookup[Hat.ID]) then
        ScriptStepper.HatLookup[Hat.ID] = {}
    end

    table.insert(ScriptStepper.HatLookup[Hat.ID], Script)
end

function ScriptStepper.EachScript(Callback)
    for _, Script in pairs(ScriptStepper.Scripts) do
        Callback(Script)
    end
end

function ScriptStepper.EachHat(Opcode, Callback, ...)
    --[[
        This is an insanely dumb implementation detail you need to follow that otherwise breaks projects
        if you need to know why, https://github.com/scratchfoundation/scratch-vm/blob/developer/src/engine/runtime.js#L1962
    ]]
    for i = #ScriptStepper.BlocksByTarget, 1, -1 do
        for _, Block in pairs(ScriptStepper.BlocksByTarget[i]) do
            if Block.Opcode == Opcode then
                Callback(Block, ...)
            end
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
    local Definition = Hat.Definition

    if Definition.RestartScripts and ScriptStepper.HatLookup[Hat.ID] then
        for _, Script in pairs(ScriptStepper.HatLookup[Hat.ID]) do
            Script.Kill()
        end
    end

    for _, Clone in pairs(BlockSprite.Clones) do
        ScriptStepper.CreateScript(Hat, Clone)
    end

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

    Electro.Profiler.Start("Step Scripts")

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
            local Index = table.find(ScriptStepper.Scripts, Script)
            local LookupEntry = ScriptStepper.HatLookup[Script.Hat.ID]

            local HatIndex = table.find(LookupEntry, Script)
            assert(HatIndex, "?????")

            table.remove(LookupEntry, HatIndex)
            table.remove(ScriptStepper.Scripts, Index)
        end
    end

    Electro.Profiler.End()

    ScriptStepper.RedrawRequested = false
end

return ScriptStepper