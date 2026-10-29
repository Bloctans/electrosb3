---@class ElectroSprite
local Methods = {}

function Methods:GetCostume()
    return self.Costumes[self.CurrentCostume]
end

function Methods:SetCostume(ID)
    self.CurrentCostume = Electro.Util.TableMod(ID, self.Costumes)
    Electro.BlockEngine.RequestRedraw()
end

-- Can only delete as clone
function Methods:Delete()
    local BlockEngine = Electro.BlockEngine

    if self.Parent then
        Electro.Renderer.RemoveTarget(self) -- Remove from renderer
        table.removeValue(self.Parent.Clones, self) -- Unregister as clone
        Electro.Data.Clear(self.ID)

        -- Kill all threads/scripts
        BlockEngine.Stepper.EachScript(function(Script)
            if Script.Sprite == self then
                Script.Kill()
            end
        end)
    end
end

function Methods:CreateClone()
    local CloneSprite = Electro.Project.Sprite()

    -- Copy variables (God...)
    CloneSprite.ID = CreateUUID()
    CloneSprite.Parent = self:GetRootSprite()
    CloneSprite.Position = self.Position:Copy()
    CloneSprite.Size = self.Size
    CloneSprite.CurrentCostume = self.CurrentCostume
    CloneSprite.Costumes = self.Costumes
    CloneSprite.Sounds = self.Sounds
    CloneSprite.Direction = self.Direction
    CloneSprite.Visible = self.Visible
    CloneSprite.Layer = self.Layer-1

    -- Register to what is needed, starting of hats is handled in block
    table.insert(self.Clones, CloneSprite)
    Electro.Data.Clone(self.ID, CloneSprite.ID)

    return CloneSprite
end

function Methods:GetStage()
    return Electro.Project.GetStage()
end

function Methods:GetRootSprite()
    return self.Parent or self
end

function Methods:CostumeIDFromName(Name)
    for ID, Costume in pairs(self.Costumes) do
        if Costume.Name == Name then
            return ID
        end
    end

    return 1
end

function Methods:Redraw()
    local Dimension = Vector2.zero
    local Pivot = Vector2.zero

    local Costume = self:GetCostume()
    
    if Costume then
        Dimension = Costume.Size * (self.Size/100)
        Pivot = Costume.RotationCenter
    end

    self.Rect = Electro.Util.Rect(Electro.Util.FromScratch(self.Position) - Pivot, Dimension)
end

function Methods:SoundFromName(Name)
    for ID, Sound in pairs(self.Sounds) do
        if Sound.Name == Name then
            return Sound
        end
    end
end

return function()
    local Sprite = setmetatable({
        -- Data
        IsStage = false,
        ID = nil,
        Costumes = {},
        Sounds = {},

        Effects = {
            BRIGHTNESS = 0,
            GHOST = 0
        },

        Rect = Electro.Util.Rect(Vector2.zero, Vector2.zero),

        -- Sprite state
        Position = Vector2.zero, ---@class Vector2
        Size = 100,
        Direction = 0,
        Visible = true,
        CurrentCostume = 0,
        Layer = 0,

        -- Clones
        Clones = {},
        Parent = nil,
    }, {
        __index = Methods
    })

    Electro.Renderer.AddTarget(Sprite)
    return Sprite
end