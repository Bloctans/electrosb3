class Drawer:
    def __init__(self):
        self.drawables = []

    def get_highest_layer(self):
        return len(self.drawables)

    def sort_drawables(self): 
        self.drawables.sort(key = lambda a: a.layer_order)

    def add(self, object):
        self.drawables.append(object)

    def update(self, screen):
        for drawable in self.drawables:
            if drawable.visible:
                image, rect = drawable.get_image()
                screen.blit(
                    image, 
                    rect
                )