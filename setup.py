from setuptools import find_packages, setup
from typing import List

HYPHON_E_DOT = '-e .'

def get_requrement(file_path:str)->List[str]:
    "this function is used for instaling all the requrement "

    requrements =[]
    with open(file_path) as file_obj:
        requrements = file_obj.readlines()
        requrements = [req.replace("\n","") for req in requrements]

        if HYPHON_E_DOT in requrements:
            requrements.remove(HYPHON_E_DOT)


    return requrements


setup(
    name='mlproject',
    version='0.0.1',
    author='alam',
    author_email='tanjirrank@gmail.com',
    packages=find_packages(),
    install_requires=get_requrement('requrements.txt')

)