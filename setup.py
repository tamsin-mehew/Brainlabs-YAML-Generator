from setuptools import setup, find_packages

setup(
    name="Brainlabs YAML Generator",
    packages=find_packages(),
    version="4",
    description="Tool for generating brainlabs.yaml files.",
    author="James Freeman",
    author_email="james.f@brainlabsdigital.com",
    url="https://github.com/Brainlabs-Digital/Brainlabs-YAML-Generator",
    scripts=["Brainlabs-YAML-Generator/bl-yaml"],
    install_requires=["pyinquirer", "pyyaml"],
)
