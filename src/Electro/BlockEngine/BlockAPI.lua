-- Seperate api helper for blocks
-- Metatable based as apis only change their script, sprite and block depending on their config

---@class ElectroBlockAPI
local Methods = {}

function Methods:Configure(Script, Sprite, Block)
    self.Script = Script
    self.Sprite = Sprite
    self.Block = Block
end

function Methods:BranchTo(Block, IsLoop)
    self.Script.BranchToBlock(Block, IsLoop)
end

function Methods:Yield()
    self.Script.SetYielded()
end

function Methods:RequestRedraw()
    Electro.BlockEngine.Stepper:RequestRedraw()
end

function Methods:Compare(A,B)
    return Electro.Util.Compare(A,B)
end

function Methods:StartTimer(Duration)
    self.Timer = os.clock()
    self.TimerDuration = Duration
    self.TimerStarted = true
end

function Methods:ResetLoops()
    self.Loops = 0
end

function Methods:TimerEnded()
    local DidEnd = (os.clock() - self.Timer) > self.TimerDuration

    -- Auto-end timer
    if DidEnd and self.TimerStarted then
        self.TimerStarted = false
    end

    return DidEnd
end

return function()
    return setmetatable({
        Timer = 0,
        Loops = 0,
        TimerStarted = 0,
        TimerDuration = 0
    }, {
        __index = Methods
    })
end