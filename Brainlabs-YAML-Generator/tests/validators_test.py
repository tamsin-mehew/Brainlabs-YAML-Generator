import src.validators as validators


def test_valid_email_prefix() -> None:
    assert validators.valid_email_prefix("james")
    assert validators.valid_email_prefix("james.f")
    assert not validators.valid_email_prefix("james@brainlabsdigital.com")
    assert not validators.valid_email_prefix("james f")


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
