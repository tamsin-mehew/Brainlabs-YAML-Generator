from pytest import raises
from PyInquirer import ValidationError

import blyaml.validators as validators


def test_valid_email_prefix() -> None:
    email_validator = validators.ValidEmailPrefix()
    email_validator.validate("james")
    email_validator.validate("james.f")
    with raises(ValidationError):
        email_validator.validate("james@brainlabsdigital.com")
    with raises(ValidationError):
        email_validator.validate("james f")


def test_valid_email_prefix_list() -> None:
    pass


def test_valid_client_id() -> None:
    pass


def test_valid_date() -> None:
    pass


def test_valid_url() -> None:
    pass


def test_valid_url_list() -> None:
    pass


def test_valid_cron() -> None:
    pass


def test_valid_directory() -> None:
    pass
