#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2020 June 01 23:43:01 (EST) 

@author: KanExtension
"""

from abc import ABC

'''
A B S T R A C T   C L A S S E S
'''


class Redocker(ABC):
    """This abstract class defines the blueprint for all the other `Redocker` classes. The aim of this class
    is to take the config file and actually create/compile/push the docker image.

    Notes
    -----
    ## aim of this module is to enable easy and fast creation of docker environments
    ##
    ## - take the config file
    ##
    ## - VIRTENV: the config file will have the path to the virtual environment you want to replicate
    ## - DEPEND: - it also must have all the other dependencies (like )
    ##          - now the dependencies are resolved by user and here the shell scripts are provided, that
    ##              will be actually injected into the Dockerfile
    ## - DOCKER_REGISTRY : - is the docker registry you want to use, once the image is ready and compiled to push
    ## OR if you specify the <path>/<to>/<zip>.zip then it will be zipped (from the )
    ##
    ## -



    """
    def __init__(self):
        pass

    '''
    HELPER METHODS
    '''

    '''
    MAIN METHODS
    '''
    def make_docker(self):
        """ For this you have to have the make config

        Returns
        -------

        """
        pass

    def launch_docker(self):
        """
        For this you need to have the launch config

        Returns
        -------

        """
        pass

    pass


'''
C L A S S E S
'''


class NvidiaRedocker(Redocker):
    """This class implements the Docker file creation from `Nvidia` image

    """
    pass

