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
            },
            "contains": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.contains
            },
            "round": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.round
            },
            "letter_of": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.letter_of
            },
            "length": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.length
            }
        }

        self.operations = {
            "floor": math.floor,
            "cos": math.cos,
            "sin": math.sin
        }

    def add(self, args, util): 
        return args.num1+float(args.num2)
    
    def divide(self, args, util): return float(args.num1)/float(args.num2)
    
    def multiply(self, args, util): 
        return float(args.num1)*float(args.num2)
    
    def contains(self, args, util):
        return (str(args.string2) in str(args.string1))
    
    def length(self, args, util):
        return len(args.string)
    
    def letter_of(self, args, util):
        return args.string[int(args.letter)]
    
    def round(self, args, util):
        return math.round(args.num)

    def mod(self, args, util): 
        print(args.__dict__)
        return args.num1%args.num2

    def block_not(self,args,api):
        try:
            return not args.operand
        except:
            return True

    def random(self, args, util): 
        # Fucking nasty hack because python hates when you use a keyword in syntax like that
        rand_from = float(args.__dict__["from"])
        rand_to = float(args.to)

        return rand_from + (random.random() * (rand_to - rand_from))

    def equals(self, args, util): 
        return str(args.operand1) == str(args.operand2)
    
    def join(self, args, util): 
        return str(args.string1)+str(args.string2)

    def subtract(self, args, util): 
        return float(args.num1)-float(args.num2)

    def mathop(self, args, util): return self.operations[args.operator.name](args.num)

    def compare_or(self, args, util):
        return args.operand1 or args.operand2
    
    def compare_and(self, args, util):
        return args.operand1 and args.operand2

    def gt(self, args, util): return float(args.operand1)>float(args.operand2)
    def lt(self, args, util): return float(args.operand1)<float(args.operand2)

BlockEngine.register_extension("operator", BlocksOperator())