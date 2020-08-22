
class light_provider():

    def __init__(self):
        self.colour = None
        self.brightness = 0
        self.power = False
    
    def config(configuration: dict):
        raise NotImplementedError

    def set_colour(self, colour):
        raise NotImplementedError
    
    def set_brightness(self, brightness: int):
        raise NotImplementedError

    def render_bitmap(self, bitmap):
        raise NotImplementedError

    def set_power(self, power: bool):
        raise NotImplementedError

    def toggle_power(self):
        raise NotImplementedError
