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
            "subtract": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.subtract
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

    def add(self, args, script): return args.num1+args.num2
    
    def divide(self, args, script): 
        return args.num1/args.num2

    def mod(self, args, script): return args.num1%args.num2

    def subtract(self, args, script): return args.num1-args.num2

    def mathop(self, args, script): return self.operations[args.operator.name](args.num)

    def gt(self, args, script): return args.operand1>args.operand2
# This stays unregistered until we actually make progress on it
BlockEngine.register_extension("operator", BlocksOperator())