import electrosb3.block_engine as BlockEngine

class BlocksProcedures:
    def __init__(self):
        self.custom_blocks = {}

        self.block_map = {
            "definition": { # Base block, assuming for scratch renderer, ignore.
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.definition
            },
            "prototype": { # Actual definition part we care about.
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.prototype
            },
            "call": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.call
            },
        }

    def definition(self, args, util):
        return args.custom_block

    def prototype(self, args, util):
        return util.block

    def call(self, args, util):
        for input in args.__dict__:
            print(input)

        def find_block(hat):
            block = hat.run_block(util.script)

            if block.mutations.proc_code == util.get_mutations().proc_code:
                print("Branch to procedure")
                util.script.branch_to(hat.id, False, True)

        util.stepper.each_hat("procedures_definition", {}, find_block)

class BlocksArg:
    def __init__(self):
        self.block_map = {
            "reporter_string_number": {
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.reporter_string_number
            },
            "reporter_boolean": {
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.reporter_boolean
            },
        }

    def reporter_string_number(self, args, util):
        value = args.value.name
        info = util.get_script_info()
        
        if "procedure_args" in info.keys():
            return info["procedure_args"][value]
        else:
            return 0
        
    def reporter_boolean(self, args, util):
        value = args.value.name
        info = util.get_script_info()
        
        if "procedure_args" in info.keys():
            return info["procedure_args"][value]
        else:
            return False

    def prototype(self, args, util):
        pass

BlockEngine.register_extension("procedures", BlocksProcedures())
BlockEngine.register_extension("argument", BlocksArg())