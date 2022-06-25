from setuptools import setup
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Aditya Jaiswal"
DESCRIPTION="This is a first ML Project"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mentioned in requirements.txt file

    return: This function is going to return a list which cotain name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)

