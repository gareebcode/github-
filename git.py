import requests

# Your GitHub personal access token
token = 
headers = {"Authorization": f"token {token}"}

# API endpoint to fetch user repositories
url = "https://api.github.com/user/repos"

# Repositories to keep safe
exclude_repos = [
    "devgaganin/Save-Restricted-Content-Bot-V2",
    "devgaganin/Auto-Forward-Bot-V2"
]

# Fetch all repositories
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"Failed to fetch repositories: {response.status_code}")
    exit()

repos = response.json()

for repo in repos:
    repo_name = repo['full_name']
    visibility = repo['visibility']

    # Skip private repositories and the specified public repositories
    if visibility == "private" or repo_name in exclude_repos:
        print(f"Skipping {repo_name}")
        continue

    # Delete the repository
    delete_url = f"https://api.github.com/repos/{repo_name}"
    delete_response = requests.delete(delete_url, headers=headers)

    if delete_response.status_code == 204:
        print(f"Deleted {repo_name}")
    else:
        print(f"Failed to delete {repo_name}: {delete_response.status_code}")
