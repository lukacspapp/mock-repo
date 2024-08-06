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
print("wablr")
print("owjss")
print("xpgoy")
print("xwdgm")
print("twkqv")
print("xkwjw")
print("wwtre")
print("erivm")
print("cmefq")
print("ykwax")
print("ppqgf")
print("vfcou")
print("fgqxj")
print("cjwoc")
print("fijsk")
print("krqjf")
print("lvhff")
print("hqrhg")
print("ylqfe")
print("stpqi")
print("oewpw")
print("whkrg")
print("wbaiq")
print("quhet")
print("jndrw")
print("hwmim")
print("oocdj")
print("xbyro")
print("sbill")
print("stjrh")
print("jjapy")
print("qydeb")
print("lrsqj")
