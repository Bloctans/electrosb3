import electrosb3.block_engine as BlockEngine
from electrosb3.block_engine.block_support import API

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
            },
            "whenkeypressed": {
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.whenkeypressed
            },
        }

    def broadcast(self,args,api: API):
        print(args.broadcast_input)
        api.start_hats("event_whenbroadcastreceived", {
            "broadcast_option": args.broadcast_input
        })

    def whenkeypressed(self, args, api):
        pass
    
BlockEngine.register_extension("event", BlocksEvent())