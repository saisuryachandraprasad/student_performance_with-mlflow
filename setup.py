from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = "-e ."


def get_requirements(file_path:str) -> List[str]:

    """
    This function is reponsible to get all requirements from requirements list

    ARGS: file_path -> requirements filpath

    """

    requirements = []

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [requirement.replace("/n", "")for requirement in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements




setup(
    name= "End to End MLPROJECT with MLFLOW",
    version= "0.0.1",
    author= "saisuryachandraprasad",
    author_email="saisuryachandraprasad@gmail.com",
    packages= find_packages(),
    install_requirements = get_requirements("requirements.txt")
)