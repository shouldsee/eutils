from setuptools.config import read_configuration
from setuptools import setup
config = read_configuration("setup.cfg")
setup(
install_requires =
	[
    'lxml',
    'pytz',
    'requests',
    ],

setup_requires='''
pytest-runner
setuptools_scm
wheel
'''.strip().splitlines(),

tests_require ='''
mock
pytest
pytest-cov
pyyaml
tox
vcrpy
'''.strip().splitlines(),
packages = ['src'],
python_requires = ">= 3.6",
zip_safe = True,
package_dir = {'':'src'})

	# **dict(config))


