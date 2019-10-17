from blyaml.answers_to_yaml import yaml_str


def yaml_str_test() -> None:
    assert yaml_str("true") is True
    assert yaml_str("false") is False
    assert yaml_str("null") == "null"
