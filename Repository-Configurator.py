from pickle import TRUE
import sys
from github import Github
import requests
import json 

# Repositories settings to apply
allowsquashmerge = False
allowrebasemerge = False
allowmergecommit = True
deletebranchonmerge = False

args = sys.argv[1:]
token=sys.argv[1]
repo_name=sys.argv[2]

print(token)
print(repo_name)

g = Github(token)
print(f"Logged in as {g.get_user().name}")

repo = g.get_repo(repo_name)
branch_to_protect = g.get_repo(repo_name).get_branch(repo.default_branch)


################################### Configuring Repository Settings ##############################################
repo.edit(allow_squash_merge=allowsquashmerge,
          allow_merge_commit=allowmergecommit,
          allow_rebase_merge=allowrebasemerge,
          delete_branch_on_merge=deletebranchonmerge
          )
print(f"Configured {repo_name} with the following settings")
print(f"Allow Squash Merge: {allowsquashmerge}")
print(f"Allow Rebase Merge: {allowrebasemerge}")
print(f"Allow Merge Commits: {allowmergecommit}")
print(f"Delete Branch On Merge: {deletebranchonmerge}")
