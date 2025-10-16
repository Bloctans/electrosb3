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
            "wait_until": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.wait_until
            },
            "if": {
                "type": BlockEngine.Enum.BLOCK_C,
                "function": self.block_if,
            },
            "if_else": {
                "type": BlockEngine.Enum.BLOCK_C,
                "function": self.block_if_else,
            },
            "repeat": {
                "type": BlockEngine.Enum.BLOCK_C,
                "function": self.repeat
            },
            "repeat_until": {
                "type": BlockEngine.Enum.BLOCK_C,
                "function": self.repeat_until
            },
            "create_clone_of": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.create_clone_of
            },
            "start_as_clone": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.start_as_clone
            },
            "delete_this_clone": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.start_as_clone
            },
            "stop": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.stop
            },
            "create_clone_of_menu": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.create_clone_of
            }
        }

    def forever(self, args, api):
        api.script.branch_to(args.substack, True)

    def repeat(self, args, api):
        if api.loops <= args.times:
            print("Branch repeat")
            api.script.branch_to(args.substack, True)

    def repeat_until(self, args, api):
        print("Branch repeat")
        api.script.branch_to(args.substack, True)

    def wait(self, args, api):
        if (not api.timer_started):
            #print("timer start")
            api.do_yield()
            api.request_redraw()
            api.start_timer(args.duration)
        elif (not api.timer_finished()):
            api.do_yield()
        else:
            api.end_timer()

    def wait_until(self, args, api):
        pass

    def create_clone_of(self,args,api):
        pass # TODO

    def start_as_clone(self,args,api):
        pass # TODO

    def stop(self,args,api):
        pass # TODO

    def block_if(self, args, api):
        if args.condition:
            api.script.branch_to(args.substack, False)

    def block_if_else(self, args, api):
        if args.condition:
            api.script.branch_to(args.substack, False)
        else:
            api.script.branch_to(args.substack2, False)

# This stays unregistered until we actually make progress on it
BlockEngine.register_extension("control", BlocksControl())