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
        if Block.opcode then
            local DeserializedBlock = BlockEngine.Block()

            if Block.mutation then
                local Mutation = Block.mutation
                local Arguments = {}

                if Mutation.argumentids and Mutation.argumentnames then -- what the actual fuck why do i need to parse twice scratch\
                    local ArgumentIds = JSON.parse_array(Mutation.argumentids,1)
                    local ArgumentNames = JSON.parse_array(Mutation.argumentnames,1)

                    for i, ArgumentId in pairs(ArgumentIds) do
                        Arguments[ArgumentId] = ArgumentNames[i]
                    end
                end

                DeserializedBlock.Mutation = {
                    Name = Mutation.proccode,
                    Warp = (Mutation.warp == "true") and true or false,
                    Arguments = Arguments
                }
            end

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
        else
            print("Got orphaned block, skipping")
        end
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
    Target.Layer = TargetJSON.layerOrder or Electro.Renderer.GetTopLayer()

    if Target.IsStage then
        Electro.Project.StageID = Target.ID
    end

    for ID, Costume in pairs(TargetJSON.costumes) do
        assert(Costume.md5ext, "Costume w/o md5ext not supported yet")

        local Image, Size
        
        if Costume.dataFormat == "svg" then
            Image, Size = Resvg.CreateImage(Deserializer.Read(Costume.md5ext))
        else
            local Data = love.filesystem.newFileData(Deserializer.Read(Costume.md5ext), Costume.md5ext)

            Image = love.graphics.newImage(Data)
            Size = Vector2.new(Image:getWidth(), Image:getHeight())
        end

        local TargetCostume = Electro.Project.Costume()
        TargetCostume.Image = Image
        TargetCostume.Size = Size
        TargetCostume.Name = Costume.name
        TargetCostume.RotationCenter = Vector2.new(Costume.rotationCenterX, Costume.rotationCenterY)
        TargetCostume.ID = ID

        Target.Costumes[ID] = TargetCostume
    end

    for ID, Sound in pairs(TargetJSON.sounds) do
        local Sucess, Message = pcall(function()
            return love.audio.newSource(MountName..Sound.md5ext, "static")
        end)
        
        local Source

        if Sucess then
            Source = Message
        else
            print("Failed to load WAV")
            Source = love.audio.newSource("Electro/Project/error.wav", "static")
        end

        local DeserializedSound = Electro.Project.Sound()
        DeserializedSound.Source = Source
        DeserializedSound.Name = Sound.name
        DeserializedSound.ID = CreateUUID()

        Target.Sounds[ID] = DeserializedSound
    end

    Electro.Data.SetupData(TargetID)

    for ID, Variable in pairs(TargetJSON.variables) do
        Electro.Data.SetVariable(TargetID, ID, Variable[2])
    end

    for ID, SerializedList in pairs(TargetJSON.lists) do
        local List = Electro.Data.GetList(Target.ID,ID)

        for i,v in pairs(SerializedList[2]) do
            List[i] = v
        end
    end

    Deserializer.DeserializeBlocks(TargetJSON.blocks, Target)

    Electro.Project.Targets[TargetID] = Target
end

function Deserializer.Deserialize(MountNameIn)
    local DeserializeBench = Electro.Profiler.Benchmark("Deserialize Project")

    MountName = MountNameIn.."/"

    local ProjectJSON = Deserializer.Read("project.json")
    ProjectJSON = JSON.decode(ProjectJSON)

    for ID, Target in pairs(ProjectJSON.targets) do
        Deserializer.DeserializeTarget(CreateUUID(), Target)
    end

    DeserializeBench.End()
end

return Deserializer