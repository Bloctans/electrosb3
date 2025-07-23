# This idea is partially stolen from the actual vm
from zipfile import ZipFile
import json
import io

from pygame import Vector2, image

from electrosb3.project.costume import Costume
from electrosb3.project.sprite import Sprite
import electrosb3.block_engine as BlockEngine

# is there a way to put all the json values into the class variables without this mess, cuz i havent touched python in a WHILE - bloctans
class Deserialize:
    def __init__(self, ProjectFile: ZipFile, Project):
        print("Started Deserializing")
        self.file = ProjectFile

        project_json = self.get_as_json("project.json")

        for target in project_json["targets"]: Project.sprites.append(self.deserialize_target(target))

        # lemme js sort by layer
        # just learned you could also just use a lambda for this
        Project.sprites.sort(key=lambda sprite: sprite.layer_order)

        print("Deserialization finished!")

    def deserialize_costume(self, costume):
        image_file = self.get(costume["md5ext"])

        costume_object = Costume()
        costume_object.image = image.load(io.BytesIO(image_file))
        costume_object.rotation_center = Vector2(costume["rotationCenterX"],-costume["rotationCenterY"]) # HACK: For the displaying to work properly, we need to make rotationCenterY negative
        costume_object.name = costume["name"]

        return costume_object
    
    def deserialize_sounds(self, sounds):
        print(sounds)

        #audio_file = self.get(sounds[])
    
    def deserialize_blocks(self, serialized_blocks, sprite):
        missing_opcodes = 0

        sprite.debug_blocks = serialized_blocks

        for block_id in serialized_blocks:
            block_value = serialized_blocks[block_id]

            print(block_id)
            print(block_value)

            #try:
            block_data,opcode,map = BlockEngine.get_raw_block(block_value["opcode"])

            block = BlockEngine.Block(sprite)

            block.next = block_value["next"]
            block.parent = block_value["parent"]

            block.opcode = opcode
            block.info = block_data
            block.id = block_id

            block.args = {
                "inputs": block_value["inputs"],
                "fields": block_value["fields"]
            }

            if block_data["type"] == BlockEngine.Enum.BLOCK_HAT:
                script = BlockEngine.Script()
                script.start_block = block
                script.sprite = sprite

                sprite.scripts.append(script)

            sprite.blocks.update({block_id: block})
            #except:
            #    missing_opcodes += 1
            #    print(f"{block_value["opcode"]} Could not be found! Skipping!")

        for block in sprite.blocks: # Go through all blocks and assign next and parent properly
            current_block = sprite.blocks[block]

            if current_block.next:
                current_block.next = sprite.blocks[current_block.next]

            if current_block.parent:
                current_block.parent = sprite.blocks[current_block.parent]

        print(f"{missing_opcodes} Missing opcodes for {sprite.name}")

    def deserialize_target(self, target):
        sprite = Sprite()

        if (not target["isStage"]): # The stage target always will not have any transformation info
            sprite.position = Vector2(target["x"],target["y"])
            sprite.size = target["size"]
            sprite.rotation = target["direction"]
            sprite.visible = target["visible"]
            sprite.layer_order = target["layerOrder"]

        sprite.name = target["name"]

        self.deserialize_blocks(target["blocks"], sprite)

        # Load costumes
        for costume in target["costumes"]: sprite.costumes.append(self.deserialize_costume(costume))

        sprite.setup() # Sorta temporary

        return sprite 

    # Get a file and return its bytes, If there is no file, a FileNotFound error is raised.
    def get(self, File: str):
        if File in self.file.namelist():
            return self.file.read(File)
        else:
            raise FileNotFoundError(File)
        
    def get_as_json(self, File: str): return json.loads(self.get(File))