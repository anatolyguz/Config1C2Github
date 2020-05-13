# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:54:20 2019

@author: Guz
"""

import os
from datetime  import datetime 
import subprocess
import shlex
import configparser

pathtocnfig = 'config.ini' 
config = configparser.ConfigParser()
config.read(pathtocnfig)   
bingit = config.get('Settings', 'bingit')

os.environ['GIT_PYTHON_GIT_EXECUTABLE'] = bingit

print('GIT_PYTHON_GIT_EXECUTABLE=' + os.environ['GIT_PYTHON_GIT_EXECUTABLE'] )



from git import Repo

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
    os.chdir(localRepoPath)
    repo.git.add(A=True)
#    repo.git.add(localRepoPath)
#    repo.git.add(os.path.join(localRepoPath, filesforUpdate))


def commit(repo):
	COMMIT_MESSAGE = 'Auto update ' + datetime.today().strftime("%Y%m%d")
	# repo.git.commit(commit_message)
	repo.index.commit(COMMIT_MESSAGE)
	origin = repo.remote(name='origin')
	origin.push()


