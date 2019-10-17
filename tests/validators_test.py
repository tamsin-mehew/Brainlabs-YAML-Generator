from pytest import raises
from PyInquirer import ValidationError
from prompt_toolkit.document import Document

import blyaml.validators as validators


def test_valid_email_prefix() -> None:
    email_validator = validators.ValidEmailPrefix()
    assert email_validator.validate(Document("james"))
    assert email_validator.validate(Document("james.f"))
    with raises(ValidationError):
        email_validator.validate(Document("james@brainlabsdigital.com"))
    with raises(ValidationError):
        email_validator.validate(Document("james f"))


def test_valid_email_prefix_list() -> None:
    email_list_validator = validators.ValidEmailPrefixList()
    assert email_list_validator.validate(Document("james"))
    assert email_list_validator.validate(Document("james.f"))
    assert email_list_validator.validate(Document("james, sam"))
    assert email_list_validator.validate(Document("james.f, sam.d"))
    assert email_list_validator.validate(Document("james,sam.d"))
    assert email_list_validator.validate(Document("james,sam,marie"))
    assert email_list_validator.validate(Document("james,  sam,  marie"))
    with raises(ValidationError):
        email_list_validator.validate(Document("james f, sam d,  marie"))
    with raises(ValidationError):
        email_list_validator.validate(Document("james f"))


def test_valid_client_id() -> None:
    pass


def test_valid_date() -> None:
    pass


def test_valid_url() -> None:
    pass


def test_valid_url_list() -> None:
    pass


def test_valid_cron() -> None:
    cron_validator = validators.ValidCron()
    assert cron_validator.validate(Document("* * * * *"))
    assert cron_validator.validate(Document("7 7 7 7 6"))
    assert cron_validator.validate(Document("7 7 * * *"))
    assert cron_validator.validate(Document("07 07 * * *"))
    assert cron_validator.validate(Document("07 07 1 1 1"))
    with raises(ValidationError):
        cron_validator.validate(Document("Hello World!"))
    with raises(ValidationError):
        cron_validator.validate(Document("1 1 1 1 1 1"))
    with raises(ValidationError):
        cron_validator.validate(Document("* * * * * *"))


def test_valid_directory() -> None:
    pass
