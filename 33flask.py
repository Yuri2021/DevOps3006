import requests
response = requests.get("https://api.github.com/users/avielb/repos")
for repo in response.json():
    print(repo["full_name"])

import requests
response = requests.get("https://api.github.com/users/avielb/repos")
# short
repos_with_first = [{"name": repo["full_name"], "tags": repo["git_tags_url"]} for repo in response.json() if repo["private"] == False]

for repo in repos_with_first:
    print(repo)
# full
# for repo in response.json():
#     if "first" in repo["full_name"]:
#         result.append(repo["full_name"])