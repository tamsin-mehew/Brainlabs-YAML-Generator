from blyaml.questions import list_to_list_of_checkbox_dicts


def test_list_to_list_of_checkbox_dicts() -> None:
    input = [
        "server-cronjob",
        "tech-managed-google-ads-script",
        "user-managed-google-ads-script",
        "server-button-press",
        "web-app",
        "tech-managed-apps-script",
        "user-managed-apps-script",
        "command-line",
        "glitch",
        "aws-lambda-function",
        "pepper",
    ]
    output = [
        {"name": "server-cronjob"},
        {"name": "tech-managed-google-ads-script"},
        {"name": "user-managed-google-ads-script"},
        {"name": "server-button-press"},
        {"name": "web-app"},
        {"name": "tech-managed-apps-script"},
        {"name": "user-managed-apps-script"},
        {"name": "command-line"},
        {"name": "glitch"},
        {"name": "aws-lambda-function"},
        {"name": "pepper"},
    ]
    assert list_to_list_of_checkbox_dicts(input) == output
