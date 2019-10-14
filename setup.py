from setuptools import setup

setup(
    name="blyaml",
    packages=["blyaml"],
    version="19",
    description="Tool for generating brainlabs.yaml files.",
    author="James Freeman",
    author_email="james.f@brainlabsdigital.com",
    url="https://github.com/Brainlabs-Digital/Brainlabs-YAML-Generator",
    install_requires=["pyyaml>=5.1.1", "pyinquirer", "requests"],
    entry_points={"console_scripts": ["blyaml = blyaml.main:main"]},
)
