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
        info = util.get_script_info()
        info["procedure_args"] = {}

        def find_block(hat):
            block = hat.run_block(util.script)
            
            mutations = util.get_mutations()

            if "log" in mutations.proc_code:
                print(args.__dict__)

            if block.mutations.proc_code == mutations.proc_code:
                for input in args.__dict__:
                    value = args.__dict__[input]
                    name = block.mutations.args[input]["name"]

                    info["procedure_args"].update({
                        name: value
                    })
                
                util.script.branch_to(hat.id, False, mutations.warp)

        util.stepper.each_hat("procedures_definition", {}, find_block)

class BlocksArg:
    def __init__(self):
        self.block_map = {
            "reporter_string_number": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.reporter_string_number
            },
            "reporter_boolean": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.reporter_boolean
            },
        }

    def reporter_string_number(self, args, util):
        value = args.value.name
        info = util.get_script_info()
        
        if value in info["procedure_args"].keys():
            return info["procedure_args"][value]
        else:
            return 0
        
    def reporter_boolean(self, args, util):
        value = args.value.name
        info = util.get_script_info()
        
        if value in info["procedure_args"].keys():
            return info["procedure_args"][value]
        else:
            return False

BlockEngine.register_extension("procedures", BlocksProcedures())
BlockEngine.register_extension("argument", BlocksArg())