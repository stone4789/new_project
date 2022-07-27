#!/usr/bin/env python3
import sys
import os
from pathlib import Path

"""
This will setup directories and files to start an ML project.
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
