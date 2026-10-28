local Deserializer = {}
local MountName

function Deserializer.Read(Path)
    local Data = love.filesystem.read(MountName..Path)
    assert(Data, "Failed to read "..Path)

    return Data
end

function Deserializer.DeserializeBlocks(Blocks, Sprite)
    local BlockEngine = Electro.BlockEngine
    local Stepper = BlockEngine.Stepper

    for ID, Block in pairs(Blocks) do
        local DeserializedBlock = BlockEngine.Block()
        DeserializedBlock.ID = ID
        DeserializedBlock.Next = Block.next
        DeserializedBlock.Parent = Block.parent
        DeserializedBlock.Opcode = Block.opcode
        DeserializedBlock.Sprite = Sprite
        DeserializedBlock.Definition = BlockEngine.Extensions.GetDefinition(Block.opcode)

        DeserializedBlock.RawArgs = {
            Inputs = Block.inputs,
            Fields = Block.fields
        }

        Stepper.AddBlock(ID, DeserializedBlock)
    end
end

function Deserializer.DeserializeTarget(TargetID, TargetJSON)
    local Target = Electro.Project.Sprite()

    Target.Position = Vector2.new(TargetJSON.x or 0, TargetJSON.y or 0)
    Target.IsStage = TargetJSON.isStage
    Target.Name = TargetJSON.name
    Target.CurrentCostume = TargetJSON.currentCostume + 1
    Target.Visible = Target.IsStage and true or TargetJSON.visible
    Target.Direction = TargetJSON.direction or 90
    Target.Size = TargetJSON.size or 100
    Target.ID = TargetID

    for ID, Costume in pairs(TargetJSON.costumes) do
        assert(Costume.md5ext, "Costume w/o md5ext not supported yet")
        
        local Image, Size = Resvg.CreateImage(Deserializer.Read(Costume.md5ext))

        local TargetCostume = Electro.Project.Costume()
        TargetCostume.Image = Image
        TargetCostume.Size = Size
        TargetCostume.RotationCenter = Vector2.new(Costume.rotationCenterX, Costume.rotationCenterY)
        TargetCostume.ID = ID

        Target.Costumes[ID] = TargetCostume
    end

    for ID, Sound in pairs(TargetJSON.sounds) do
        local DeserializedSound = Electro.Project.Sound()
        DeserializedSound.Source = love.audio.newSource(MountName..Sound.md5ext, "static")
        DeserializedSound.Name = Sound.name

        Target.Sounds[ID] = DeserializedSound
    end

    Electro.Data.SetupData(TargetID)

    for ID, Variable in pairs(TargetJSON.variables) do
        Electro.Data.SetVariable(TargetID, ID, Variable[2])
    end

    Deserializer.DeserializeBlocks(TargetJSON.blocks, Target)

    Electro.Project.Targets[TargetID] = Target
end

function Deserializer.Deserialize(MountNameIn)
    MountName = MountNameIn.."/"

    local ProjectJSON = Deserializer.Read("project.json")
    ProjectJSON = JSON.decode(ProjectJSON)

    for ID, Target in pairs(ProjectJSON.targets) do
        Deserializer.DeserializeTarget(CreateUUID(), Target)
    end
end

return Deserializer