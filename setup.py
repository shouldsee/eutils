from setuptools.config import read_configuration
from setuptools import setup
config = read_configuration("setup.cfg")
setup(use_scm_version=False, **config)
