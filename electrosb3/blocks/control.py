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
                "function": self.block_if,
            },
            "repeat": {
                "type": BlockEngine.Enum.BLOCK_C,
                "function": self.repeat
            },
            "create_clone_of": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.create_clone_of
            },
            "create_clone_of_menu": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.create_clone_of
            }
        }

    def forever(self, args, api):
        api.do_yield()
        api.script.branch_to(args.substack, True)

    def repeat(self, args, api):
        if api.loops <= args.times:
            api.script.branch_to(args.substack, True)

    def wait(self, args, api):
        print("Wait started")
        if (not api.timer_started):
            print("timer start")
            api.do_yield()
            api.start_timer(args.duration)
        elif api.timer_finished():
            print("timer finished")
            api.stop_yield()

    def create_clone_of(self,args,api):
        pass # TODO

    def block_if(self, args, api):
        if args.condition:
            api.script.branch_to(args.substack, False)

# This stays unregistered until we actually make progress on it
BlockEngine.register_extension("control", BlocksControl())