from requests import get, RequestException
import logging as log
from Env import repo_owner, repo_name, github_token


def get_latest_release():
    # GitHub API endpoint for releases
    api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest'

    headers = {}
    if github_token:
        headers['Authorization'] = f'Token {github_token}'

    try:
        response = get(api_url, headers=headers)
        data = response.json()
        latest_version = data['tag_name']
        return latest_version
    except RequestException as e:
        log.warning(f"Error getting latest release information: {e}")
        return None
