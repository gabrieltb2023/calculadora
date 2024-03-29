Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['calculadora.py']
DATA_FILES = ['ico.gif']
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
