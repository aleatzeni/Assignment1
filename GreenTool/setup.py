from setuptools import setup, find_packages

setup(
    name = "greengraph",
    version = "0.1.0",
    packages = find_packages(exclude=['*test']),
	scripts=['greengraph.py'],
    install_requires = ['argparse','matplotlib','geopy','numpy','requests']
    )