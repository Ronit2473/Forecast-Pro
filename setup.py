from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as f:
            lines = f.readlines()
            for line in lines:
                requirements=line.strip()
                #ignore empty lines and -e .
                if requirements and requirements != '-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found.")
        
    return requirements_lst


setup(
    name='forecast_pro',
    version='0.1',
    author='Ronit Singha Roy',
    author_email="ronit.singha.roy@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)


    