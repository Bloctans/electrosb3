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
            "wait_until": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.wait_until
            },
            "start_as_clone": {
                "type": BlockEngine.Enum.BLOCK_HAT
            },
            "delete_this_clone": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.delete_this_clone
            },
            "create_clone_of": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.create_clone_of
            },
            "create_clone_of_menu": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.create_clone_of_menu
            }
        }

    def forever(self, args, util):
        util.script.branch_to(args.get("substack"), True)

    def repeat(self, args, util):
        if util.loops <= util.int(args.get("times")):
            util.script.branch_to(args.get("substack"), True)
        else:
            util.loops = 0

    def stop(self, args, util):
        stop_option = args.get("stop_option").name

        if stop_option == "other scripts in sprite":
            def other_scripts(script):
                if (script.sprite == util.sprite) and (not (script == util.script)): 
                    script.kill()

            util.stepper.each_script(other_scripts)
        elif stop_option == "this script":
            util.script.kill()
        else:
            print("Invalid stop option: "+stop_option)

    def repeat_until(self, args, util):
        #print(args.get("condition"))
        if not args.get("condition"): util.script.branch_to(args.get("substack"), True)

    def wait_until(self, args, util):
        if not args.get("condition"): util.do_yield()

    def delete_this_clone(self, args, util): util.sprite.delete_this_clone()

    def create_clone_of(self, args, util):
        if args.get("clone_option") == "myself":
            util.sprite.create_clone()
        else:
            pass

    def create_clone_of_menu(self, args, util): return "myself"

    def wait(self, args, util):
        if (not util.timer_started):
            util.do_yield()
            util.request_redraw()
            util.start_timer(args.get("duration"))
        elif (not util.timer_finished()):
            util.do_yield()
        else:
            util.end_timer()

    def block_if(self, args, util):
        if args.get("condition"):
            util.script.branch_to(args.get("substack"), False)

    def block_if_else(self, args, util):
        if args.get("condition"):
            util.script.branch_to(args.get("substack"), False)
        else:
            util.script.branch_to(args.get("substack2"), False)

BlockEngine.register_extension("control", BlocksControl())