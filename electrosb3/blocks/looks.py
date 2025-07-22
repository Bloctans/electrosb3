import electrosb3.block_engine as BlockEngine

class BlocksLooks:
    def __init__(self):
        self.block_map = {
            "switchcostumeto": {

            }
        }

    def forever(self, args, script):
        print(args)
        script.step_next_to(args["SUBSTACK"])

    def wait(self, args, script):
        if script.is_yielding():
            print(args)
        else:
            script.set_yield(BlockEngine.Enum.YIELD)

# This stays unregistered until we actually make progress on it
#BlockEngine.register_extension("looks", BlocksLooks())