import electrosb3.block_engine as BlockEngine
import math
import random

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
            "multiply": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.multiply
            },
            "not": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.block_not
            },
            "equals": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.equals
            },
            "or": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.compare_or
            },
            "and": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.compare_and
            },
            "mod": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.mod
            },
            "subtract": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.subtract
            },
            "random": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.random
            },
            "mathop": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.mathop
            },
            "gt": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.gt
            },
            "lt": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.lt
            },
            "join": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.join
            }
        }

        self.operations = {
            "floor": math.floor
        }

    def add(self, args, util): return args.num1+args.num2
    
    def divide(self, args, util): return float(args.num1)/float(args.num2)
    
    def multiply(self, args, util): 
        return float(args.num1)*float(args.num2)

    def mod(self, args, util): return args.num1%args.num2

    def block_not(self,args,api):
        return not args.operand

    def random(self, args, util): 
        # Fucking nasty hack because python hates when you use a keyword in syntax like that
        return random.randint(args.__dict__["from"], args.to)

    def equals(self, args, util): 
        return str(args.operand1) == str(args.operand2)
    
    def join(self, args, util): 
        return str(args.string1)+str(args.string2)

    def subtract(self, args, util): return args.num1-args.num2

    def mathop(self, args, util): return self.operations[args.operator.name](args.num)

    def compare_or(self, args, util):
        return args.operand1 or args.operand2
    
    def compare_and(self, args, util):
        return args.operand1 and args.operand2

    def gt(self, args, util): return float(args.operand1)>float(args.operand2)
    def lt(self, args, util): return float(args.operand1)<float(args.operand2)

BlockEngine.register_extension("operator", BlocksOperator())