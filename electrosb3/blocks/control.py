import electrosb3.block_engine as BlockEngine

class BlocksControl:
    def __init__(self):
        self.block_map = {
            "forever": {
                "type": BlockEngine.Enum.BLOCK_C,
                "function": self.forever
            },
            "wait": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.wait
            },
            "if": {
                "type": BlockEngine.Enum.BLOCK_C,
                "function": self.block_if
            }
        }

    def forever(self, args, script):
        script.set_yield(BlockEngine.Enum.YIELD_TILL_NEXT_FRAME)
        script.branch_to(args["SUBSTACK"])

    def wait(self, args, script):
        pass
        #if script.is_yielding():
            #print(args)
        #else:
            #script.set_yield(BlockEngine.Enum.YIELD)

    def block_if(self, args, script):
        if args["CONDITION"] == True:
            script.branch_to(args["SUBSTACK"])

# This stays unregistered until we actually make progress on it
BlockEngine.register_extension("control", BlocksControl())