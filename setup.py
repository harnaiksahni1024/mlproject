from setuptools import find_packages,setup
from typing import List

hypen_e_dot = '-e .'

def get_requirments(file_path:str)->List[str]:
    """ this func will return list of requirments
    """
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if hypen_e_dot in requirments:
            requirments.remove(hypen_e_dot)
    
    return requirments
        
setup(
    name ="mlproject",
    version= '0.0.1',
    author="Harnaik",
    author_email="harnaiksahni1024@gmail.com",
    packages = find_packages(),
    install_requires=get_requirments('requirment.txt')
)