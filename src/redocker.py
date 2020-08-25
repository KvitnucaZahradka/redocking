#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2020 June 01 23:42:50 (EST) 

@author: KanExtension
"""

import argparse
import os
import yaml
import importlib

## TODO: create the README.md generator

try:
    import redocker_utils as uu
except:
    from . import redocker_utils as uu

importlib.reload(uu)

# import the config file
with open(os.path.join(os.path.split(__file__)[0], 'config', 'config.md'), 'r') as handle:
    _config = yaml.safe_load(handle)

'''
M A I N   M E T H O D S
'''

def main():
    """

    Attributes
    ----------
    --path_to_config: str
        this is a full path to the configuration markdown file and this is also this is also a folder where the resulting
        shell script will be dumped.

    --tmux_session_name: str
        -- default -- is `redocker`. Is the optional name, with the tmux session in which the shell script will run.

    Returns
    -------

    Notes
    -----
    $ python universality.py --path_to_config "<FULL>/<PATH>/<TO>/<config.md>"

    """

    # -- step 0 -- grab arguments
    _parser = argparse.ArgumentParser()

    # -- step 1 -- grab the 2 external args
    _parser.add_argument("-path_to_config", "--path_to_config", help="This is a full path to the config file.")

    _parser.add_argument("-tmux_session_name", "--tmux_session_name", help="this is optional name of the tmux "
                                                                           "session name where we will run the "
                                                                           "Docker creation.", type=str,
                         default=_config['tmux_session_name'])

    # -- step 2 -- parse them
    _args = _parser.parse_args()

    # -- step 3 -- grab the workdir
    _work_dir, _ = os.path.split(_args.path_to_config)

    # -- step 4 -- open the config file
    with open(_args.path_to_config, 'r') as handle:
        _user_config = yaml.safe_load(handle)

    # -- step 5 -- figure out which class from `uu` you want
    _redocker_class = uu.__dict__[_user_config['redocker_name']]

    # -- step 6 -- create the redocker class
    _redocker: uu.Redocker = _redocker_class(path_to_config=_args.path_to_config)

    # -- step 7 -- orchestrate with `redocker`
    _redocker.orchestrate()

    # -- step 8 -- depending on user preference; execute
    if not _user_config['script_only']:
        uu.execute_shell(path_to_config=_work_dir, script_name=_user_config.get('script_name',
                                                                                _config['default_shell_name']))

