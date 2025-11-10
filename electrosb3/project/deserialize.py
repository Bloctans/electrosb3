# This idea is partially stolen from the actual vm
from zipfile import ZipFile
import json
import io

from pygame import Vector2, image, mixer

mixer.init()

from electrosb3.project.sound import *
from electrosb3.project.costume import *
from electrosb3.project.sprite import *
from electrosb3.project.deserialize import *
import electrosb3.block_engine as BlockEngine

# TODO: Reuse field

# is there a way to put all the json values into the class variables without this mess, cuz i havent touched python in a WHILE - bloctans
class Deserialize:
    def __init__(self, ProjectFile: ZipFile, Project):
        print("Started Deserializing")
        self.file = ProjectFile

        project_json = self.get_as_json("project.json")

        for target in project_json["targets"]:
            sprite = self.deserialize_target(target, Project)
            Project.sprites.update({sprite.name: sprite})

        print("Deserialization finished!")

    def deserialize_costume(self, costume,id):
        image_file = self.get(costume["md5ext"])

        costume_object = Costume()
        costume_object.image = image.load(io.BytesIO(image_file))
        costume_object.rotation_center = Vector2(costume["rotationCenterX"],-costume["rotationCenterY"]) # HACK: For the displaying to work properly, we need to make rotationCenterY negative
        costume_object.name = costume["name"]
        costume_object.id = id

        return costume_object
    
    def deserialize_sounds(self, serialized_sounds):
        sounds = []

        for sound in serialized_sounds:
            audio = Sound()

            audio_file = io.BytesIO(self.get(sound["md5ext"]))

            audio.sound = mixer.Sound(audio_file)
            audio.name = sound["name"]

            sounds.append(audio)

        return sounds
    
    def deserialize_blocks(self, serialized_blocks, sprite, project):
        sprite.debug_blocks = serialized_blocks

        stepper = project.script_stepper

        for block_id in serialized_blocks:
            block_value = serialized_blocks[block_id]

            #print(block_id)
            #print(block_value)

            if type(block_value) == list:
                stepper.add_block(block_id, block) # add and pray because im too lazy
                continue
            
            block_data,opcode,set = BlockEngine.get_raw_block(block_value["opcode"])

            block = BlockEngine.Block(sprite)

            block.next = block_value["next"]
            block.parent = block_value["parent"]

            block.opcode = opcode
            block.set = set
            block.info = block_data
            block.id = block_id

            if "mutation" in block_value.keys():
                block.mutations = BlockEngine.Mutation(block_value["mutation"])

            block.args = {
                "inputs": block_value["inputs"],
                "fields": block_value["fields"]
            }

            # Every hat we encounter, add a new script object
            if block_data["type"] == BlockEngine.Enum.BLOCK_HAT:
                project.script_stepper.add_hat(block)

            stepper.add_block(block_id, block)

        for block in stepper.blocks: # Go through all blocks and assign next and parent properly
            current_block = stepper.blocks[block]

            if not (type(block) == list):
                if current_block.next:
                    current_block.next = stepper.get_block(current_block.next)

                if current_block.parent:
                    current_block.parent = stepper.get_block(current_block.parent)

    def deserialize_target(self, target, project):
        sprite = Sprite()

        if (not target["isStage"]): # The stage target always will not have any transformation info
            sprite.position = Vector2(target["x"],target["y"])
            sprite.size = target["size"]
            sprite.rotation = -target["direction"]
            sprite.visible = target["visible"]
            sprite.layer_order = target["layerOrder"]
        
        for variable_id in target["variables"]:
            variable = target["variables"][variable_id]
            sprite.variables.update({variable_id: Variable(variable)})

        for list_id in target["lists"]:
            list = target["lists"][list_id]
            sprite.lists.update({list_id: List(list)})

        sprite.is_stage = target["isStage"]
        sprite.name = target["name"]
        sprite.project = project

        sprite.renderer = project.drawer

        project.drawer.add(sprite)

        self.deserialize_blocks(target["blocks"], sprite, project)
        sounds = self.deserialize_sounds(target["sounds"])

        sprite.sounds = sounds
        
        # Load costumes
        i = 0
        for costume in target["costumes"]: 
            sprite.costumes.append(self.deserialize_costume(costume,i))
            i += 1

        sprite.setup() # Sorta temporary

        return sprite 

    # Get a file and return its bytes, If there is no file, a FileNotFound error is raised.
    def get(self, File: str):
        if File in self.file.namelist():
            return self.file.read(File)
        else:
            raise FileNotFoundError(File)
        
    def get_as_json(self, File: str): return json.loads(self.get(File))