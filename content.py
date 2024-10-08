import os

import git

from git_contributions_importer import *

# Clone the remote repository to a local folder
url = "https://github.com/lukacspapp/mock-repo"
local_path = "/Users/lukacspapp/CODING/mock-repo"
if not os.path.exists(local_path):
    git.Repo.clone_from(url, local_path)

# Clone the private repository to a local folder
private_repo_url = "https://bitbucket.org/jentis/service-enrichment-xxxlutz-product-data-loader/src/master/"
private_repo_local_path = "/Users/lukacspapp/JENTIS/service-enrichment-xxxlutz-product-data-loader"  # Replace with your desired local path
if not os.path.exists(private_repo_local_path):
    git.Repo.clone_from(private_repo_url, private_repo_local_path)

# Your private repo or Bitbucket repo
repo = git.Repo(private_repo_local_path)
# Your mock repo
mock_repo = git.Repo(local_path)
importer = Importer([repo], mock_repo)

# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['papplukacs@hotmail.com', 'lukacs.papp@jentis.com'])

importer.import_repository()
