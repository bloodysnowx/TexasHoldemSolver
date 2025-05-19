import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'requirements.txt')) as req_file:
    requirements = [line.strip() for line in req_file if line.strip()]

setup(
    name='texas_holdem_solver',
    version='0.1.0',
    description="No-limit 6-handed Texas Hold'em Solver using Deep CFR",
    author='',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ths=texas_holdem_solver.cli:main',
        ],
    },
    install_requires=requirements,
    python_requires='>=3.7',
)