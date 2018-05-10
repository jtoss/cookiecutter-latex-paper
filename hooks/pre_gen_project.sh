#!/usr/bin/bash
#
# Copyright (c) 2016, Abdó Roig-Maranges <abdo.roig@gmail.com>
# All rights reserved.
#
# This file may be modified and distributed under the terms of the 3-clause BSD
# license. See the LICENSE file for details.

set -e

echo $(pwd)

#if [ ! -e ".git" ]; then
git submodule sync --recursive
git submodule update --init --recursive
#fi
