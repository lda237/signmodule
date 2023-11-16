# setup.py

from setuptools import setup, find_packages

setup(
    name='signmodule',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
)
