import electrosb3.block_engine as BlockEngine
from electrosb3.block_engine.block_support import API

class BlocksEvent:
    def __init__(self):
        self.block_map = {
            "whenflagclicked": {
                "type": BlockEngine.Enum.BLOCK_HAT
            },
            "broadcast": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.broadcast
            },
            "broadcastandwait": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.broadcastandwait
            },
            "whenbroadcastreceived": {
                "type": BlockEngine.Enum.BLOCK_HAT,
            },
            "whenkeypressed": {
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.whenkeypressed
            },
            "whenthisspriteclicked": {
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.whenthisspriteclicked
            },
            "whengreaterthan": {
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.whenthisspriteclicked
            },
        }

    def broadcast(self,args,api: API):
        #print("do broadcast")
        print(args.broadcast_input)
        api.start_hats("event_whenbroadcastreceived", {
            "broadcast_option": args.broadcast_input
        })

    def broadcastandwait(self,args,api: API):
        #print("do broadcast")
        print(args.broadcast_input)
        api.start_hats("event_whenbroadcastreceived", {
            "broadcast_option": args.broadcast_input
        })

    # Rarely used
    def whenkeypressed(self, args, util):
        pass

    def whenthisspriteclicked(self, args, util):
        pass

    # Usually used as a when stop clicked, will not implement.
    def whengreaterthan(self, args, util): pass
    
BlockEngine.register_extension("event", BlocksEvent())