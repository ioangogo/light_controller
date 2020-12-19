"""
This file contains the configuration reading and module loading
TODO Implement configuration processing
TODO Implement module Loading
"""
from importlib import import_module
from classes.state import state_class
import os
import sys
import yaml


def load_module(mod_type: str, mod_name: str):
    module = import_module(
            f"modules.{mod_type}.{mod_name}")
    return getattr(module, mod_name)()


def load_light_configuration(state: state_class, configuration: dict):
    """
    handles loading the light module and the configuration of the module

    :param state: the internal state of the light controller
    :param configuration: a dict containing the configuration from the yaml
   """
    name = configuration['name']
    light_class = load_module("light", name)
    state.light = light_class()
    state.light.config(configuration["settings"])


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
