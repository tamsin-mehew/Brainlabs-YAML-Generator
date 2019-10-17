# Brainlabs YAML Generator

A CLI to create Brainlabs YAML files interactively.

Primarily powered by [PyInquirer](https://github.com/CITGuru/PyInquirer).

This is an internal Brainlabs tool. While it may be interesting to see an implementation of PyInquirer, it will not be usefully useable outside of Brainlabs.

## Features
- Dynamic questions based on previous answers
- Prefilled selection lists that get their values from the Sesame API
- Multiselect and single select lists
- Offline caching of lists
- Answer validation
- Saves your yaml to a file
- Copies your yaml into the clipboard
- Valdiates your yaml with the Sesame API

## Install from PyPI
```shell
pip3 install -U blyaml
```

## Install from local files
```
make install
```

## Run
```
blyaml
```

This should start an interactive CLI which asks you questions.
You will need the Sesame API token, take it from the [announcement post](https://brainlabsdigital.slack.com/archives/G8QSQ2VL1/p1570799465004300) or speak to James F or Sam D U .

## Test

Currently has testing for validators, but not much of the core functionality.
```shell
make test
```

## Update on PyPI

Update version in [setup.py](setup.py).
```shell
make deploy
```
Currently published under the JamesF user on PyPI.

## Uninstall

The tool also creates a hidden folder in your home directory.
```shell
pip3 uninstall blyaml
rm -rf ~/.blyaml
```

# Technical File Structure

The project primarily exists in the [blyaml](blyaml) folder.
The [main file](blyaml/main.py) runs the CLI using [PyInquirer](https://github.com/CITGuru/PyInquirer).
[questions.py](blyaml/questions.py) contains functions that return lists of dictionaries of PyInquirer structured questions.
[validators.py](blyaml/validators.py) contains Validator classes that are used by the questions, and validation functions used by the validators.
[lists.py](blyaml/lists.py) contains functions that return lists of choices to be used in the questions. Most of these lists come from the Sesame API and are cached locally using shelve.
[answers_to_yaml.py](blyaml/answers_to_yaml.py) contains functions that process the PyInquirer answers dict into a `brainlabs.yaml` format YAML str.
