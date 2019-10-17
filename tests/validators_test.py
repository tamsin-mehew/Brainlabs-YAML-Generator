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
    date_validator = validators.ValidDate()
    assert date_validator.validate(Document("2019-04-01"))
    assert date_validator.validate(Document("2012-11-21"))
    assert date_validator.validate(Document("2022-02-02"))
    with raises(ValidationError):
        date_validator.validate(Document(""))
    with raises(ValidationError):
        date_validator.validate(Document("2012/11/21"))
    with raises(ValidationError):
        date_validator.validate(Document("2012.11.21"))
    with raises(ValidationError):
        date_validator.validate(Document("21-11-2012"))
    with raises(ValidationError):
        date_validator.validate(Document("21 11 2012"))
    with raises(ValidationError):
        date_validator.validate(Document("2012 11 21"))
    with raises(ValidationError):
        date_validator.validate(Document("2019-13-01"))
    with raises(ValidationError):
        date_validator.validate(Document("2019-12-32"))


def test_valid_url() -> None:
    url_validator = validators.ValidUrl()
    assert url_validator.validate(Document("www.home.com"))
    assert url_validator.validate(Document("home.com"))
    assert url_validator.validate(Document("https://mail.google.com/mail/u/0/#inbox/"))
    assert url_validator.validate(Document("https://docs.gle.com/sheet/d/X/edit#gid=0"))
    assert url_validator.validate(Document("docs.gle.com/sheet/d/X/edit#gid=0"))
    with raises(ValidationError):
        url_validator.validate(Document("home"))
    with raises(ValidationError):
        url_validator.validate(Document("home.t"))
    with raises(ValidationError):
        url_validator.validate(Document("home com"))


def test_valid_url_list() -> None:
    url_list_validator = validators.ValidUrlList()
    urls = (
        "www.home.com",
        "home.com",
        "https://mail.google.com/mail/u/0/#inbox/",
        "https://docs.gle.com/sheet/d/X/edit#gid=0",
        "docs.gle.com/sheet/d/X/edit#gid=0",
    )
    for url in urls:
        assert url_list_validator.validate(Document(url))
    assert url_list_validator.validate(Document(",".join(urls)))
    assert url_list_validator.validate(Document(", ".join(urls)))
    assert url_list_validator.validate(Document(", ".join(urls[0:2])))
    assert url_list_validator.validate(Document(", ".join(urls[2:4])))
    with raises(ValidationError):
        url_list_validator.validate(Document("home com"))
    with raises(ValidationError):
        url_list_validator.validate(Document("home.com,,home.com"))
    with raises(ValidationError):
        url_list_validator.validate(Document("home.com, ,home.com"))


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
    directory_validator = validators.ValidDirectory()
    assert directory_validator.validate(Document(r"/home/projects"))
    assert directory_validator.validate(Document(r"home"))
    assert directory_validator.validate(Document(r"/home/projects_test-this"))
    assert directory_validator.validate(Document(r"/home/projects\ with\ spaces"))
    assert directory_validator.validate(Document(r'/home/!"@£$%^&*()_+)'))
    with raises(ValidationError):
        directory_validator.validate(Document("/home//project"))
