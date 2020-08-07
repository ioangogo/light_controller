"""
This file contains the configuration reading and module loading
TODO Implement configuration processing
TODO Implement module Loading
"""

from yaml import load, dump
from importlib import import_module
from classes.state import state_class
import os

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
    import_module(
        f"modules.lights.{configuration['name']}.{configuration['name']}"
        )
    raise NotImplementedError


def load_network_configuration(state: state_class, configuration: dict):
    raise NotImplementedError


def load_configration(state: state_class, config_dir: str):

    raise NotImplementedError
