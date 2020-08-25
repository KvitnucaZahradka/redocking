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

