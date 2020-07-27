from classes.light_provider import light_provider
from asyncio import Event


class state_class():
    """
    Represents the internal state of the light bridge for access by diffrent
    threads
    """

    def __init__(self, effects, light: light_provider):
        self.current_effect = None
        self.running = True
        self.avalible_effects = effects
        self.light = light
        self.light_state = {
            "brightness": 0,
            "colour": 0,
        }  # Im not expecting to support monocrome or colour temprature lights
        self.bitmap = None  # This will be a pilow image for simplicity
        self.light_power = False
        self.new_message_event = Event()
        self.state_processed_event = Event()
        self.mqtt_configuration = {
            "hostname": "",
        }
