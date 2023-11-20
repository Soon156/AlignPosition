import requests
import logging as log
from Env import current_version, repo_owner, repo_name, github_token
from Funtionality.Config import get_config


def get_latest_release():
    # GitHub API endpoint for releases
    api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest'

    headers = {}
    if github_token:
        headers['Authorization'] = f'Token {github_token}'

    try:
        response = requests.get(api_url, headers=headers)
        data = response.json()
        latest_version = data['tag_name']
        return latest_version
    except requests.RequestException as e:
        log.warning(f"Error getting latest release information: {e}")
        return None


def check_for_update():
    values = get_config()
    if values['check_update'] == "No":
        return None
    latest_version = get_latest_release()
    latest_version = '0.5.4'
    if latest_version is not None:
        if latest_version > current_version:
            return latest_version
        else:
            log.warning("Your application is up to date.")
            return None
    else:
        log.warning("Unable to check for updates.")
        return None
