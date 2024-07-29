import os

import git

from git_contributions_importer import *
from datetime import datetime, timedelta

# Clone the remote repository to a local folder
url = "https://github.com/lukacspapp/mock-repo"
local_path = "/Users/lukacspapp/CODING/mock-repo"
if not os.path.exists(local_path):
    git.Repo.clone_from(url, local_path)

# Clone the private repository to a local folder
private_repo_url = "https://bitbucket.org/jentis/cronjob-raw-data-export/src/master/"
private_repo_local_path = "/Users/lukacspapp/JENTIS/cronjob-raw-data-export"  # Replace with your desired local path
if not os.path.exists(private_repo_local_path):
    git.Repo.clone_from(private_repo_url, private_repo_local_path)

# Your private repo or Bitbucket repo
repo = git.Repo(private_repo_local_path)
# Your mock repo
mock_repo = git.Repo(local_path)
importer = Importer([repo], mock_repo)
one_year_ago = int((datetime.now() - timedelta(days=365)).timestamp())
importer.set_ignore_before_date(one_year_ago)

# Do not collapse multiple changes into one
importer.set_collapse_multiple_changes_to_one(False)

# Allow the importer to shift commits up to a certain maximum past date
importer.set_commit_time_max_past(365 * 24 * 60 * 60)  # up to 1 year in the past

# Do not limit the number of changes per commit
importer.set_commit_max_amount_changes(-1) # start importing from the last commit date in the mock repo

# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['papplukacs@hotmail.com', 'lukacs.papp@jentis.com', '90268306+lukacspapp@users.noreply.github.com'])

importer.import_repository()

# pipenv shell
# python3 run_script.py