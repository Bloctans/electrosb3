import electrosb3.block_engine as BlockEngine
import math

class BlocksOperator:
    def __init__(self):
        self.block_map = {
            "add": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.add
            },
            "divide": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.divide
            },
            "mod": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.mod
            },
            "mathop": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.mathop
            },
            "gt": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.gt
            }
        }

        self.operations = {
            "floor": math.floor
        }

    def add(self, args, script): return args["NUM1"]/args["NUM2"]
    
    def divide(self, args, script): return args["NUM1"]/args["NUM2"]

    def mod(self, args, script): return args["NUM1"]%args["NUM2"]

    def mathop(self, args, script): return self.operations[args["OPERATOR"].name](args["NUM"])

    def gt(self, args, script): return args["OPERAND1"]>args["OPERAND2"]

# This stays unregistered until we actually make progress on it
BlockEngine.register_extension("operator", BlocksOperator())