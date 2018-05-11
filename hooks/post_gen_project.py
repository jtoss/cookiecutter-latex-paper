#!/usr/bin/env python

from cookiecutter.repository import determine_repo_dir
from cookiecutter.config import get_user_config
from cookiecutter.main import cookiecutter

import os
import sys
import json
import shutil
import subprocess

TEMPLATE_NAME = "cookiecutter-latex-paper"
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def recurse_submodule(template):
    submodule_init = 0
    
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

    if (output[0] != ' '):
        subprocess.run(["git", "submodule",  "sync", "--recursive"], cwd=repo_dir)
        subprocess.run(["git", "submodule",  "update", "--init", "--recursive"], cwd=repo_dir)
        # remove this folder as it is empty  
        submodule_dir = PROJECT_DIRECTORY+'/meerkat_adminlte'
        try:
            os.rmdir(submodule_dir)
        except OSError as ex:
            if ex.errno == errno.ENOTEMPTY:
                print("directory not empty")
                exit(1)
        
        # replay
        cookiecutter(template,replay=True, overwrite_if_exists=True, output_dir="../",)
        #submodule_init = 1;


    return submodule_init
    

if __name__ == '__main__':
    print("cur_dir: ", PROJECT_DIRECTORY);

    files = [ f for f in os.listdir('.') ]
    print(files)
    
    with open('.cookiecutter.json', 'r') as fd:
        context = json.load(fd)

    #submodules_initialized = recurse_submodule(context['_template'])
    submodule_init = recurse_submodule(TEMPLATE_NAME)

    if submodule_init == 0 :
        print("commit stuff")
        
#if [ ! -e ".git" ]; then
#    git init
#    git add -A
#    git commit -m 'Initial commit'
#fi
    
