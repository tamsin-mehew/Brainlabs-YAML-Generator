from setuptools import setup
from setuptools.command.install import install
from pathlib import Path


class MakeFolder(install):
    def run(self) -> None:
        (Path.home() / ".blyaml").mkdir(exist_ok=True)
        install.run(self)


setup(
    name="blyaml",
    packages=["blyaml"],
    version="15",
    description="Tool for generating brainlabs.yaml files.",
    author="James Freeman",
    author_email="james.f@brainlabsdigital.com",
    url="https://github.com/Brainlabs-Digital/Brainlabs-YAML-Generator",
    install_requires=["pyyaml>=5.1.1", "pyinquirer", "requests"],
    entry_points={"console_scripts": ["blyaml = blyaml.main:main"]},
    cmdclass={"install": MakeFolder},
)
