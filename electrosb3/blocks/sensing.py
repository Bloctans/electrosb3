# TODO
from electrosb3.block_engine import Enum, register_extension
import time

from pygame import key

class BlocksSensing:
    def __init__(self):
        self.block_map = {
            "keypressed": {
                "type": Enum.BLOCK_INPUT,
                "function": self.keypressed
            },
            "of": {
                "type": Enum.BLOCK_INPUT,
                "function": self.of
            },
            "keyoptions": {
                "type": Enum.BLOCK_INPUT,
                "function": self.keyoptions
            },
            "timer": {
                "type": Enum.BLOCK_INPUT,
                "function": self.timer
            },
            "resettimer": {
                "type": Enum.BLOCK_STACK,
                "function": self.resettimer
            },
            "mousex": {
                "type": Enum.BLOCK_INPUT,
                "function": self.mousex
            },
            "mousey": {
                "type": Enum.BLOCK_INPUT,
                "function": self.mousey
            },
            "mousedown": {
                "type": Enum.BLOCK_INPUT,
                "function": self.mousedown
            },
            "touchingobject": {
                "type": Enum.BLOCK_INPUT,
                "function": self.touchingobject
            },
            "touchingobjectmenu": {
                "type": Enum.BLOCK_INPUT,
                "function": self.touchingobjectmenu
            },
            "loudness": {
                "type": Enum.BLOCK_INPUT,
                "function": self.loudness
            },
            "of_object_menu": {
                "type": Enum.BLOCK_INPUT,
                "function": self.of_object_menu
            },
            "username": {
                "type": Enum.BLOCK_INPUT,
                "function": self.username
            },
            "askandwait": {
                "type": Enum.BLOCK_STACK,
                "function": self.askandwait
            },
            "answer": {
                "type": Enum.BLOCK_STACK,
                "function": self.askandwait
            }
        }

        self.start_time = time.time()

    def username(self, args, util): return "ElectroUser"

    def askandwait(self, args, util):
        pass
        #print(args.__dict__) # no renderer for ask & wait rn

    def of(self, args, util):
        property = args.property.name
        object = args.object

        if property == "x position":
            return object.position.x
        elif property == "direction":
            return object.rotation
        elif property == "costume name":
            return object.current_costume.name
        else:
            var = util.variable_from_sprite(object, property)

            if var == None:
                print(property)
            else:
                return var

    def of_object_menu(self, args, util):
        return util.get_sprite(args.object.name)

    def mousex(self, args, util): return util.get_cursor()[0]
    def mousey(self, args, util): return util.get_cursor()[1]
    def mousedown(self, args, util): return util.get_mouse_down()

    def loudness(self, args, util): return 0
    
    def touchingobject(self, args, util):
        return util.is_touching(args.touchingobjectmenu, util.sprite)
    
    def touchingobjectmenu(self, args, util): return args.touchingobjectmenu

    def keypressed(self, args, util):
        return util.is_key_down(args.key_option)

    def keyoptions(self, args, util):
        return args.key_option.name

    def timer(self, args, util):
        return time.time() - self.start_time
    
    def resettimer(self, args, util):
        self.start_time = time.time()

register_extension("sensing", BlocksSensing())