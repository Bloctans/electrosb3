-- Seperate api helper for blocks
-- Metatable based as apis only change their script, sprite and block depending on their config

---@class ElectroBlockAPI
local Methods = {}
local BlockEngine = Electro.BlockEngine

function Methods:Configure(Script, Sprite, Block)
    if (not Script.Info[Block.ID]) then
        Script.Info[Block.ID] = {
            Loops = 0
        }
    end

    self.Script = Script
    self.Sprite = Sprite
    self.Block = Block
end

function Methods:BranchTo(Block, IsLoop)
    return self.Script.BranchToBlock(Block, IsLoop)
end

function Methods:GetProcedureStack()
    return self.Script.FindProcedureStack()
end

function Methods:StartHats(Opcode, Fields)
    BlockEngine.Stepper.StartHats(Opcode, Fields)
end

function Methods:StartHat(Hat, Fields)
    BlockEngine.Stepper.StartHat(Hat, Fields)
end

function Methods:EachHat(Opcode, Callback, ...)
    BlockEngine.Stepper.EachHat(Opcode, Callback, ...)
end

function Methods:Boolean(Value) return Electro.Util.ToBoolean(Value) end
function Methods:Float(Value) return tonumber(Value) or 0 end

function Methods:SetVariable(ID, Value)
    return Electro.Data.SetVariable(self.Sprite.ID, ID, Value)
end

function Methods:GetList(ID)
    return Electro.Data.GetList(self.Sprite.ID, ID)
end

function Methods:Yield()
    self.Script.SetYielded()
end

function Methods:GetMutation()
    return self.Block.Mutation
end

function Methods:GetVariable(ID)
    return Electro.Data.GetVariable(self.Sprite.ID, ID)
end

function Methods:RequestRedraw()
    BlockEngine.Stepper:RequestRedraw()
    self.Sprite:Redraw()
end

function Methods:Compare(A,B)
    return Electro.Util.Compare(A,B)
end

function Methods:StartTimer(Duration)
    self.Timer = love.timer.getTime()
    self.TimerDuration = Duration
    self.TimerStarted = true
end

function Methods:GetScriptInfo()
    return self.Script.Info[self.Block.ID]
end

function Methods:TimerEnded()
    local DidEnd = (love.timer.getTime() - self.Timer) > self.TimerDuration

    -- Auto-end timer
    if DidEnd and self.TimerStarted then
        self.TimerStarted = false
    end

    return DidEnd
end

return function()
    return setmetatable({ -- TODO: in the case of clones, these may be utilized improperly during control flow swapping
        Timer = 0,
        TimerStarted = false,
        TimerDuration = 0
    }, {
        __index = Methods
    })
end