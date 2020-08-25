#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2020 June 01 23:43:01 (EST) 

@author: KanExtension
"""
from abc import ABC, abstractmethod
import yaml
from typing import List
import os
import tempfile as temp
import subprocess
from functools import reduce

# import the config file
with open(os.path.join(os.path.split(__file__)[0], 'config', 'config.md'), 'r') as handle:
    _config = yaml.safe_load(handle)


'''
ABSTRACT CLASSES
'''


class Redocker(ABC):
    """This class takes the configuration file and creates appropriate docker file, then it will actually create the
    docker image and finally it pushes the image to the appropriate repository.

    Parameters
    ----------
    path_to_config: str
        is a full path to the `<name>.md` markdown with the config.
    """
    def __init__(self, path_to_config: str):
        self._path_to_config: str = None
        self._config: dict = None

        self._image_tag: str = None
        self._docker_tag: str = None

        self._ssh_port: str = None
        self._ssh_psswd: str = None

        # here I am keeping the list of services added to a docker
        self.fish: list = []

        # here you will keep the conglomerated commands that after the join will create the Dockerfile
        self.dockerfile: list = []

        # @ property handling
        self.path_to_config = path_to_config

    @property
    def path_to_config(self) -> str:
        """

        Returns
        -------

        """
        return self._path_to_config

    @path_to_config.setter
    def path_to_config(self, path_to_config: str):
        """

        Parameters
        ----------
        path_to_config: str
            is a full path to the `<name>.md` config file.

        Returns
        -------

        """
        assert isinstance(path_to_config, str) and os.path.split(path_to_config)[-1] == '.md',\
        f'The value of variable: {path_to_config} must be string and represents full path to the markdown config file.'

        # ok upload the path
        self._path_to_config = path_to_config

        # and open it
        with open(path_to_config, 'r') as handle:
            self._config = yaml.safe_load(handle)

        # also check whether you have all the minimal requirements in `_config`
        assert (lambda conf: conf & self._config.keys() == conf)(set(_config['required_variables'])), \
        f'Your configuration keys: {self._config.keys()} are not a proper superset of minimal config requirements:' \
        f' {_config["required_variables"]}'

        assert any(map(lambda x: repr(x) == repr(self._config["docker_registry"]), _config["allowed_registries"])), \
        f'It seems that in your config file, you are trying to use has an unregistered registry: ' \
        f'{self._config["docker_registry"]}. Allowed registries are: {_config["allowed_registries"]}.'


'''
CONCRETE CLASSES
'''


class UbuntuCpuRasaTF2Redocker(Redocker):
    pass

