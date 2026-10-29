local BlockEngine = {}

BlockEngine.LastUpdate = 0

function BlockEngine.DefineShortcuts()
    BlockEngine.StartHats = BlockEngine.Stepper.StartHats
    BlockEngine.GetBlock = BlockEngine.Stepper.GetBlock
    BlockEngine.RequestRedraw = BlockEngine.Stepper.RequestRedraw
end

function BlockEngine.Init()
    BlockEngine.Stepper = require("Electro.BlockEngine.ScriptStepper")
    BlockEngine.Script = require("Electro.BlockEngine.Script")

    BlockEngine.BlockAPI = require("Electro.BlockEngine.BlockAPI")
    BlockEngine.Block = require("Electro.BlockEngine.Block")

    BlockEngine.Extensions = require("Electro.BlockEngine.Extensions")
    BlockEngine.Extensions.Register("control", "event", "sound", "looks", "operator", "sensing", "data", "motion", "DebuggerExtensionTS", "procedures")

    BlockEngine.DefineShortcuts()
end

function BlockEngine.Update()
    local TimeSince = love.timer.getTime() - BlockEngine.LastUpdate

    if TimeSince > Electro.Rate then
        BlockEngine.LastUpdate = love.timer.getTime()
        BlockEngine.Stepper.Update()
    end
end

return BlockEngine