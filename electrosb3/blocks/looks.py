import electrosb3.block_engine as BlockEngine

class BlocksLooks:
    def __init__(self):
        self.block_map = {
            "switchcostumeto": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.switchcostumeto
            },
            "switchbackdropto": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.switchbackdropto
            },
            "costume": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.costume
            },
            "backdrops": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.backdrops
            },
            "costumenumbername": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.costumenumbername
            },
            "nextcostume": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.nextcostume
            },
            "changesizeby": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.changesizeby
            },
            "changeeffectby": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.changesizeby
            },
            "seteffectto": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.changesizeby
            },
            "cleargraphiceffects": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.changesizeby
            },
            "setsizeto": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.changesizeby
            },
            "hide": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.hide
            },
            "show": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.show
            },
            "size": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.size
            },

            # Layering blocks will be passed for now
            "gotofrontback": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.gotofrontback
            },
            "goforwardbackwardlayers": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.gotofrontback
            }
        }

    def costume_from_name(self, name, costumes):
        for costume in costumes:
            if costume.name == name: return costume

    def hide(self, args, util): util.sprite.visible = False
    def show(self, args, util): util.sprite.visible = True

    def switchcostumeto(self, args, util):
        sprite = util.sprite

        costume = args.costume or 0

        sprite.set_costume(costume)

    def switchbackdropto(self, args, util):
        sprite = util.sprite

        costume = args.backdrop or 0

        

        sprite.set_costume(costume)

    def size(self, args, util):
        return util.sprite.size

    def changesizeby(self, args, util):
        util.request_redraw()
        #util.sprite.size += args.

    def changeeffectby(self, args, util):
        pass

    def gotofrontback(self, args, util):
        pass

    def costumenumbername(self, args, util):
        sprite = util.sprite
        number_or_name = args.number_name.name
        
        if number_or_name == "number":
            return sprite.current_costume.id+1
        
    def nextcostume(self, args, util):
        #print("next costume")
        util.request_redraw()
        sprite = util.sprite

        sprite.set_costume(sprite.current_costume.id+1)

    def costume(self, args, script):
        sprite = script.sprite

        return self.costume_from_name(args.costume.name, sprite.costumes)
    
    def backdrops(self, args, script):
        sprite = script.sprite

        return self.costume_from_name(args.backdrop.name, sprite.get_stage().costumes)

BlockEngine.register_extension("looks", BlocksLooks())