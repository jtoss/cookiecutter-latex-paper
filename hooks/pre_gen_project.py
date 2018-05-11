#!/usr/bin/env python

from cookiecutter.repository import determine_repo_dir
from cookiecutter.config import get_user_config

import os
import sys
import json

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def recurse_submodule(template):
    # get the cloned repo

    config_dict = get_user_config()
    print(config_dict)

    repo_dir, cleanup = determine_repo_dir(
        template=template,
        checkout=None,
        no_input=False,
        abbreviations=config_dict['abbreviations'],
        clone_to_dir=config_dict['cookiecutters_dir']
    )

    # run a git submodule update
    print("repo_dir: ", repo_dir)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as fd:
        context = json.load(fd)

    recurse_submodule(context['_template'])
