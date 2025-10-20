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
                "type": Enum.BLOCK_INPUT,
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
            "touchingobject": {
                "type": Enum.BLOCK_INPUT,
                "function": self.touchingobject
            },
            "touchingobjectmenu": {
                "type": Enum.BLOCK_INPUT,
                "function": self.touchingobjectmenu
            },
        }

        self.start_time = time.time()

    def of(self, args, util):
        property = args.property.name

        if property == "x position":
            pass

    def mousex(self, args, util):
        return util.get_cursor().x
    
    def mousey(self, args, util):
        return util.get_cursor().y
    
    def touchingobject(self, args, util):
        return util.is_touching(args.touchingobjectmenu, util.sprite)
    
    def touchingobjectmenu(self, args, util): return args.touchingobjectmenu

    def keypressed(self, args, util):
        return util.is_key_down(args.key_option)

    def keyoptions(self, args, util):
        return args.key_option.name

    def timer(self, util):
        return time.time() - self.start_time
    
    def resettimer(self, util):
        self.start_time = time.time()

register_extension("sensing", BlocksSensing())