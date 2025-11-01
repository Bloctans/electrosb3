import electrosb3.block_engine as BlockEngine

class BlocksData:
    def __init__(self):
        self.block_map = {
            "setvariableto": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.setvariableto
            },
            "changevariableby": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.changevariableby
            },
            "hidevariable": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.hide_variable
            },
            "showvariable": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.hide_variable
            },

            # TODO
            "lengthoflist": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.lengthoflist
            },
            "deletealloflist": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.deletealloflist
            },
            "itemoflist": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.itemoflist
            },
            "itemnumoflist": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.itemnumoflist
            },
            "replaceitemoflist": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.replaceitemoflist
            },
            "addtolist": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.addtolist
            },
            "listcontainsitem": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.listcontainsitem
            },
            "insertatlist": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.insertatlist
            },
        }
    
    def hide_variable(self, args, util):
        return 0

    def setvariableto(self, args, util): 
        variable = util.get_variable(args.variable.id)
        variable.value = args.value

    def deletealloflist(self, args, util):
        print(args.__dict__)

    def itemoflist(self, args, util):
        list = util.get_list(args.list.id)

        return list.get_item(args.index)
    
    def itemnumoflist(self, args, util):
        list = util.get_list(args.list.id)

        return list.get_item_from_number(args.index)
    
    def listcontainsitem(self, args, util):
        list = util.get_list(args.list.id)

        return list.contains(args.index)

    def replaceitemoflist(self, args, util):
        print(args.__dict__)

    def insertatlist(self, args, util):
        print(args.__dict__)

    def addtolist(self, args, util):
        print(args.__dict__)

    def lengthoflist(self, args, util):
        list = util.get_list(args.list.id)

        return list.get_length()

    def changevariableby(self, args, util):
        variable = util.get_variable(args.variable.id)
        variable.value = float(variable.value) + float(args.value) # Always assume this will be a float


BlockEngine.register_extension("data", BlocksData())