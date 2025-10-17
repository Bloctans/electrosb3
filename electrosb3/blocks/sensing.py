# TODO
import electrosb3.block_engine as BlockEngine
import time

from pygame import key

class BlocksSensing:
    def __init__(self):
        self.block_map = {
            "mousedown": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.mouse_down
            },
            "touchingobject": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.mouse_down
            },
            "touchingobjectmenu": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.mouse_down
            },
            "keypressed": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.keypressed
            },
            "keyoptions": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.keyoptions
            },
            "timer": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.timer
            },
        }

        self.start_time = time.time()

    def mouse_down(self, api):
        pass

    def keypressed(self, args, api):
        return BlockEngine.BlockUtil.is_key_down(args.key_option)

    def keyoptions(self, args, api):
        return args.key_option.name

    def timer(self, api):
        return time.time() - self.start_time

    def touchingobject(self, api):
        pass

BlockEngine.register_extension("sensing", BlocksSensing())