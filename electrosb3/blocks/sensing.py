# TODO
import electrosb3.block_engine as BlockEngine
import time

from pygame import key

class BlocksSensing:
    def __init__(self):
        self.block_map = {
            "keypressed": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.keypressed
            },
            "of": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.of
            },
            "keyoptions": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.keyoptions
            },
            "timer": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.timer
            },
            "mousex": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.mousex
            },
        }

        self.start_time = time.time()

    def of(self, args, api):
        property = args.property.name

        if property == "x position":
            pass

    def mousex(self, args, api):
        return 0

    def keypressed(self, args, api):
        return BlockEngine.BlockUtil.is_key_down(args.key_option)

    def keyoptions(self, args, api):
        return args.key_option.name

    def timer(self, api):
        return time.time() - self.start_time

BlockEngine.register_extension("sensing", BlocksSensing())