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
            "seteffectto": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.seteffectto
            },
            "changeeffectby": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.changeeffectby
            },
            "cleargraphiceffects": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.cleargraphiceffects
            },
            "setsizeto": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.setsizeto
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
                "function": self.gotoforwardbackwardlayers
            },
            "say": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.say
            },
        }

    def hide(self, args, util): util.sprite.visible = False
    def show(self, args, util): util.sprite.visible = True

    def say(self, args, util):
        print(args.__dict__) # no renderer for say rn

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
        util.sprite.size += args.change

    def cleargraphiceffects(self, args, util):
        pass

    def setsizeto(self, args, util):
        util.request_redraw()
        util.sprite.size = args.size

    def changeeffectby(self, args, util):
        util.request_redraw()
        if args.effect.name == "GHOST":
            util.sprite.alpha += float(args.change)*2.5

    def seteffectto(self, args, util):
        util.request_redraw()
        if args.effect.name == "GHOST":
            util.sprite.alpha = float(args.value)*2.5

    def gotofrontback(self, args, util):
        renderer = util.sprite.renderer
        layer_to_set = 0

        if args.front_back.name == "front":
            layer_to_set = renderer.get_highest_layer()
        else:
            layer_to_set = 0

        util.sprite.set_layer(layer_to_set)

    def gotoforwardbackwardlayers(self, args, util):
        layer = util.sprite.layer_order

        if args.forward_backward.name == "forward":
            util.sprite.set_layer(layer+args.num)
        else:
            util.sprite.set_layer(layer-args.num)

    def costumenumbername(self, args, util):
        sprite = util.sprite
        number_or_name = args.number_name.name
        
        if number_or_name == "number":
            return sprite.current_costume.id
        elif number_or_name == "name":
            return sprite.current_costume.name
        
    def nextcostume(self, args, util):
        #print("next costume")
        util.request_redraw()
        sprite = util.sprite

        sprite.set_costume(sprite.current_costume.id+1)

    def costume(self, args, script):
        sprite = script.sprite

        return sprite.costume_from_name(args.costume.name) or sprite.costumes[0]
    
    def backdrops(self, args, script):
        sprite = script.sprite
        stage = script.get_stage()

        return stage.costume_from_name(args.backdrop.name)

BlockEngine.register_extension("looks", BlocksLooks())