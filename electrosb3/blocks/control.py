import electrosb3.block_engine as BlockEngine

class BlocksControl:
    def __init__(self):
        self.block_map = {
            "forever": {
                "type": BlockEngine.Enum.BLOCK_C,
                "function": self.forever
            },
        }

    def forever(self, args, script):
        print(args)
        #script.step_next_to()

# This stays unregistered until we actually make progress on it
BlockEngine.register_extension("control", BlocksControl())