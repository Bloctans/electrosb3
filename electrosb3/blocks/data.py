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
            "deleteoflist": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.deleteoflist
            },

            "hidelist": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.hide_variable
            },
            "showlist": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.hide_variable
            },
        }
    
    def hide_variable(self, args, util):
        return 0

    def setvariableto(self, args, util): 
        variable = util.get_variable(args.get("variable"))
        variable.value = args.get("value")

    def deletealloflist(self, args, util):
        list = util.get_list(args.get("list"))
        return list.clear()

    def deleteoflist(self, args, util):
        list = util.get_list(args.get("list"))

        print(list.__dict__)

        return list.delete_item(util.int(args.get("index"))-1)

    def itemoflist(self, args, util):
        list = util.get_list(args.get("list"))

        return list.get_item(util.int(args.get("index"))-1)
    
    def itemnumoflist(self, args, util):
        list = util.get_list(args.get("list"))

        return list.number_of(args.get("item"))
    
    def listcontainsitem(self, args, util):
        list = util.get_list(args.get("list"))

        return list.contains(args.get("index")-1)

    def replaceitemoflist(self, args, util):
        list = util.get_list(args.get("list"))

        return list.replace(util.int(args.get("index"))-1, args.get("item"))

    def insertatlist(self, args, util):
        list = util.get_list(args.get("list"))

        return list.insert_at(util.int(args.get("index"))-1, args.get("item"))

    def addtolist(self, args, util):
        list = util.get_list(args.get("list"))

        return list.add(args.get("item"))

    def lengthoflist(self, args, util):
        list = util.get_list(args.get("list"))

        return list.get_length()

    def changevariableby(self, args, util):
        variable = util.get_variable(args.get("variable"))
        variable.value = util.float(variable.value) + float(args.get("value")) # Always assume this will be a float


BlockEngine.register_extension("data", BlocksData())