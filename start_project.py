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
    pathList = [path1, path2, path3, path4, path5]

    for i in pathList:
        os.makedirs(i)

    def write_boilerplate_files(location: str, boilerplate: list):
        newFile = open(location, "w")
        for i in boilerplate:
            i += "\n"
            newFile.write(i)
        newFile.close()

    write_boilerplate_files(
        "./new_project/src/config.py",
        [
            "'''This is a new project, insert config here'''",
            "import os",
            "HOME_DIR = ",
            "MODEL_PATH = ",
            "TRAINING_FILE = ",
            "MODEL_OUTPUT = ",
        ],
    )
    write_boilerplate_files(
        "./new_project/src/project_test.py",
        ["'''This is a new project, insert tests here'''", "import pytest"],
    )
    write_boilerplate_files(
        "./new_project/src/requirements.txt",
        ["'''This is a new project, insert docker requirements here'''"],
    )
    write_boilerplate_files(
        "./new_project/README.txt",
        ["'''This is a new project, a description will be found here...later'''"],
    )
    write_boilerplate_files(
        "./new_project/src/train.py",
        [
            "import joblib",
            "import pytest",
            "from sklearn import metrics",
            "import xgboost as xgb",
            "from sklearn import preprocessing",
            "import numpy as np",
            "import matplotlib.pyplot as plt",
            "%matplotlib inline",
            "import pandas as pd",
        ],
    )
    write_boilerplate_files(
        "./new_project/notebooks/exploration.ipynb",
        [
            "import pandas as pd",
            "import numpy as np",
            "import matplotlib.pyplot as plt",
            "%matplotlib inline" "import seaborn as sns",
        ],
    )
    write_boilerplate_files(
        "./new_project/notebooks/check_data.ipynb",
        [
            "import numpy as np",
            "import pandas as pd",
            "import matplotlib.pyplot as plt",
            "%matplotlib inline",
            "import seaborn as sns",
        ],
    )


if __name__ == "__main__":
    start_project()
