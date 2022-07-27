#!/usr/bin/env python3
import sys
import os
from pathlib import Path

"""
This will setup directories and files to start an ML project, in your current directory.
- input will contain train/test data
- src will contain all the scripts for training/inference etc
- models will contain serialized final models
- notebooks will be for exploration etc in jupyter

Files that would still need to be created would be:

./src/inference.py
./src/models.py
./src/model_dispatcher.py

./models/model_1.bin
./models/model_2.bin
...etc
"""


def start_project():

    path1 = os.path.join(os.getcwd(), "new_project")
    path2 = os.path.join("new_project", "input")
    path3 = os.path.join("new_project", "src")
    path4 = os.path.join("new_project", "notebooks")
    path5 = os.path.join("new_project", "models")

    os.makedirs(path1)
    os.makedirs(path2)
    os.makedirs(path3)
    os.makedirs(path4)
    os.makedirs(path5)


if __name__ == "__main__":
    start_project()
