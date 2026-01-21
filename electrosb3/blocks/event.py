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
                "restart_existing": True,
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
            "whenbackdropswitchesto": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.whenbackdropswitchesto
            },
        }

    def broadcast(self,args,api: API):
        #print("broadcasting")
        #print(args.broadcast_input)
        api.start_hats("event_whenbroadcastreceived", {
            "broadcast_option": args.broadcast_input
        })

    def whenbackdropswitchesto(self,args,api: API):
        pass

    def broadcastandwait(self,args,api: API):
        info = api.info

        if not ("recorded" in info.keys()):
            api.info.update({"recorded": None})

        if info["recorded"] == None:
            print("broadcasting and wait")
            print(args.broadcast_input)
            print(api.sprite.name)
            result = api.start_hats("event_whenbroadcastreceived", {
                "broadcast_option": args.broadcast_input
            })
            info["recorded"] = result
            api.do_yield()
        else:
            do_yield = False

            for script in info["recorded"]:
                if script.running:
                    do_yield = True

            if do_yield:
                api.do_yield()
            else:
                info["recorded"] = None

    # Rarely used
    def whenkeypressed(self, args, util):
        pass

    def whenthisspriteclicked(self, args, util):
        pass

    # Usually used as a when stop clicked, will not implement.
    def whengreaterthan(self, args, util): pass
    
BlockEngine.register_extension("event", BlocksEvent())