from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Wander Wise",
    version="0.1",
    author="Saloni",
    packages=find_packages(),
    install_requires = requirements,
)