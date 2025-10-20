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
            "stop": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.stop,
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
        }

    def forever(self, args, api):
        api.script.branch_to(args.substack, True)

    def repeat(self, args, api):
        if api.loops <= args.times:
            #print("Branch repeat")
            api.script.branch_to(args.substack, True)

    def stop(self, args, api):
        if args.stop_option == "other scripts in sprite":
            def other_scripts(script):
                if script.sprite == api.sprite: script.kill()

            api.stepper.each_script(other_scripts)
        else:
            print("Invalid stop option: "+args.stop_option)

    def repeat_until(self, args, api):
        #print("Branch repeat")
        if not args.condition:
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