#!/usr/bin/env python

""" This script is a workarround to fetch submodules recusively . 

This script will be useless once the pull request https://github.com/audreyr/cookiecutter/pull/1048 is merged 

"""

from cookiecutter.repository import determine_repo_dir
from cookiecutter.config import get_user_config

import os
import sys
import json
import shutil
import subprocess

TEMPLATE_NAME = "{{cookiecutter._template}}"
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def recurse_submodule(template):
    
    # get the cloned repo
    config_dict = get_user_config()
    print(config_dict)

    repo_dir, cleanup = determine_repo_dir(
        template=template,
        checkout=None,
        no_input=True,
        abbreviations=config_dict['abbreviations'],
        clone_to_dir=config_dict['cookiecutters_dir']
    )

    # run a git submodule update
    print("repo_dir: ", repo_dir)

    # check any submodule not initialzed
    result = subprocess.run(["git", "submodule",  "status"], cwd=repo_dir , stdout=subprocess.PIPE)

    output = result.stdout.decode()
    
    print(output)

    if (output[0] != ' ') :
        subprocess.run(["git", "submodule",  "sync", "--recursive"], cwd=repo_dir)
        subprocess.run(["git", "submodule",  "update", "--init", "--recursive"], cwd=repo_dir)
        commit = False

    else : 
        commit = True


    return commit
    

if __name__ == '__main__':
    print("cur_dir: ", PROJECT_DIRECTORY);

    print("template: {{cookiecutter._template}} " );

    recurse_submodule(TEMPLATE_NAME)

