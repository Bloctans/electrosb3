import electrosb3.block_engine as BlockEngine

class BlocksEvent:
    def __init__(self):
        self.block_map = {
            "whenflagclicked": {
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.whenflagclicked
            },
            "broadcast": {
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.broadcast
            },
            "whenbroadcastreceived": {
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.broadcast
            }
        }

    def broadcast(self,args,api):
        pass

    def whenflagclicked(self, args, api):
        if api.loops == 1:
            return True
    
BlockEngine.register_extension("event", BlocksEvent())