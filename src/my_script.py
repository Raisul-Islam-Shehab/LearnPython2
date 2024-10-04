import requests
import re
import pprint
import os

token = os.getenv("GITHUB_TOKEN")

repo_url = "https://api.github.com/repos/Raisul-Islam-Shehab/LearnPython2"

github_headers = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "Authorization": f"Bearer {token}",
}


# Function to fetch paginated data
def get_paginated_data(url, headers=None, params=None):
    next_pattern = re.compile(r'(?<=<)([\S]*)(?=>; rel="next")', re.IGNORECASE)
    pages_remaining = True
    data = []

    # Continue fetching pages as long as there is a next page
    while pages_remaining:
        response = requests.get(f"{url}", headers=headers, params=params)

        # Parse the response JSON data
        parsed_data = parse_data(response.json())
        data.extend(parsed_data)

        # Check the 'link' header for pagination
        link_header = response.headers.get("link")
        pages_remaining = link_header and 'rel="next"' in link_header

        # Update the URL for the next page if it exists
        if pages_remaining:
            url = re.search(next_pattern, link_header).group(0)

    return data


# Function to parse data from the response
def parse_data(data):
    # If data is already a list, return it
    if isinstance(data, list):
        return data

    # Return empty list if there's no data
    if not data:
        return []

    # Remove unwanted keys from the response
    data.pop("incomplete_results", None)
    data.pop("repository_selection", None)
    data.pop("total_count", None)

    # Extract the first key which contains the array of items
    namespace_key = list(data.keys())[0]
    # print(namespace_key)
    return data[namespace_key]


def get_latest_commit():
    response = requests.get(
        f"{repo_url}/commits", headers=github_headers, params={"per_page": 1}
    )
    latestCommit = response.json()[0]

    return latestCommit


def get_open_issues():
    # Fetch data using pagination
    open_issues = get_paginated_data(
        f"{repo_url}/issues", github_headers, {"per_page": 1}
    )

    return open_issues


def get_pull_requests():
    pull_requests = get_paginated_data(
        f"{repo_url}/pulls", github_headers, {"per_page": 1}
    )

    return pull_requests


def print_latest_commit():
    latestCommit = get_latest_commit()
    pprint.pprint(latestCommit)


def print_open_issues_details():
    open_issues = get_open_issues()
    i = 1
    for issue in open_issues:
        print(f"Issue {i}: {issue['title']:}")
        print(f"\t Description: {issue['body']}")
        print(f"\t Status: {issue['state']}")
        i += 1


def print_pull_requests_details():
    pull_requests = get_pull_requests()
    i = 1
    for request in pull_requests:
        print(f"Pull_Request {i}: {request['title']:}")
        print(f"\t Description: {request['body']}")
        print(f"\t Status: {request['state']}")
        i += 1


# print_open_issues_details()
print_latest_commit()
# print_pull_requests_details()

get_latest_commit()
