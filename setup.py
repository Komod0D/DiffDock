#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='diffdock',
      version='1.0',
      description='DiffDock: Diffusion Steps, Twists, and Turns for Molecular Docking',
      author='Gabriele Corso',
      packages=find_packages(include=['diffdock', 'diffdock.*']),
     )
