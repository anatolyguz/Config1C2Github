# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:54:20 2019

@author: Guz
"""
from git import Repo
import os
from datetime  import datetime 
import subprocess
import shlex

def clone(localRepoPath, githubUrl):
    repo = Repo.clone_from(githubUrl, localRepoPath)
    return repo


def rmdir(localRepoPath):
    cmd = 'rmdir /S /Q "' + os.path.join(localRepoPath) + '"'
    print(cmd);
    args = shlex.split(cmd)
    print(args)
    subprocess.run(args, shell=True) 
   


def add(repo, localRepoPath, filesforUpdate):
    repo.git.add(localRepoPath)
#    repo.git.add(os.path.join(localRepoPath, filesforUpdate))


def commit(repo):
	COMMIT_MESSAGE = 'Auto update ' + datetime.today().strftime("%Y%m%d")
	# repo.git.commit(commit_message)
	repo.index.commit(COMMIT_MESSAGE)
	origin = repo.remote(name='origin')
	origin.push()


