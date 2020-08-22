"""
This file contains the configuration reading and module loading
TODO Implement configuration processing
TODO Implement module Loading
"""
from importlib import import_module
from classes.state import state_class
import os, sys, yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def load_light_configuration(state: state_class, configuration: dict):
    """
    handles loading the light module and the configuration of the module

    :param state: the internal state of the light controller
    :param configuration: a dict containing the configuration from the yaml
   """
    name = configuration['name']
    module = import_module(
            f"modules.lights.{name}")
    light_class = getattr(module, name)
    state.light = light_class()
    state.light.config(configuration["settings"])
    raise NotImplementedError


def load_network_configuration(state: state_class, configuration: dict):
    raise NotImplementedError


handlers = {
    "light": load_light_configuration,
    "network": load_network_configuration,
}


def load_configration(state: state_class, config_dir: str):

    if config_dir is None:
        config_dir = "~/.light_controller"
        if not os.path.exists(config_dir):
            os.mkdir(config_dir)
            open(config_dir + "configuration.yaml", 'w').close()
    
    if os.path.exists(config_dir+"configuration.yaml"):
        config = yaml.load(open(config_dir + "configuration.yaml"))
        for component in config.keys:
            handlers[component](state, config[component])
    else:
        sys.exit(FileNotFoundError)
