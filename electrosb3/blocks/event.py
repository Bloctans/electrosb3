import electrosb3.block_engine as BlockEngine

class BlocksEvent:
    def __init__(self):
        self.block_map = {
            "whenflagclicked": {
                "type": BlockEngine.Enum.BLOCK_HAT
            },
            "broadcast": {
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.broadcast
            },
            "whenbroadcastreceived": {
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.broadcast
            },
            "whenkeypressed": {
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.whenkeypressed
            },
        }

    def broadcast(self,args,api):
        pass

    def whenkeypressed(self, args, api):
        pass
    
BlockEngine.register_extension("event", BlocksEvent())