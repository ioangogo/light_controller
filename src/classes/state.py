class state:
    """
    Represents the internal state of the light bridge for access by diffrent
    threads
    """

    def __init__(self, effects, light):
        self.current_effect = None
        self.avalible_effects = effects
        self.light = light
        self.light_state = {
            "brightness": 0,
            "colour": 0,
        }  # Im not expecting to support monocrome or colour temprature lights
        self.bitmap = None  # This will be a pilow image for simplicity
        self.light_power = False
