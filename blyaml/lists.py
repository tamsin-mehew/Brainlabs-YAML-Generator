import requests


def tags(token: str) -> list:
    return [
        "247-bidding",
        "ab-labs",
        "ad-params",
        "analysing",
        "auction-insights",
        "audiences",
        "bidding",
        "big-red-stop-button",
        "brsb",
        "budget-tracker",
        "budgets",
        "building",
        "ckp-tech",
        "gantt",
        "keyword-bidding",
        "managing",
        "monitoring",
        "pausing/unpausing",
        "protecting",
        "reporting",
        "sesame",
        "shopping",
        "spend",
        "syncing",
        "tech-adoption",
        "tech-tracking",
        "testing",
        "tv",
    ]


def platforms(token: str) -> list:
    return [
        "amazon-advertising",
        "amazon-s3",
        "apple-search-ads",
        "aws-lambda",
        "aws-sns",
        "bing-ads",
        "bob",
        "clockify",
        "dv360",
        "facebook-ads",
        "file-processing",
        "github",
        "google-admin",
        "google-ads",
        "google-analytics",
        "google-bigquery",
        "google-calendar",
        "google-campaign-manager",
        "google-content",
        "google-docs",
        "google-drive",
        "google-forms",
        "google-mail",
        "google-sheets",
        "google-slides",
        "hubspot",
        "ltd-api",
        "pepper",
        "search-ads-360",
        "sesame",
        "similarweb",
        "slack",
        "snapchat-ads",
        "timetastic",
        "trello",
        "twitter-ads",
        "web-scraping",
    ]


def deployments(token: str) -> list:
    return [
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


def departments(token: str) -> list:
    return [
        "All",
        "Analytics & CRO",
        "Biddable",
        "Biddable/Programmatic",
        "Biddable/Search",
        "Biddable/Social",
        "Finance",
        "New Business & Marketing",
        "Office Management",
        "Onboarding & Strategy",
        "Operations",
        "People Operations",
        "Tech",
    ]


def servers(token: str) -> list:
    return [
        "amazon-lambda",
        "binghorse",
        "brand-protect",
        "campaign-builder",
        "old-project-y",
        "project-y",
        "shiny-playground",
        "shopping",
        "shopping-builder",
        "sqrt",
        "workhorse1",
        "workhorse2",
        "workhorse3",
        "workhorse4",
    ]
