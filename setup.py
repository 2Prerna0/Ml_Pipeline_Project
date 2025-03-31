from setuptools import find_packages, setup
from typing import List
 
HYPHON_E_DOT = "-e ."

def get_requirements(filepath: str) -> List[str]:
    requirements = []
    
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n", "") for i in requirements]
        
        if HYPHON_E_DOT  in requirements:
            requirements.remove(HYPHON_E_DOT)
            
            
            
setup(name='ML_Pipeline_Project',
      version='0.01',
      description='Machine Learning Pipeline Project',
      author='Prerna Prashar',
      author_email='prernaprashar7170@gmail.com',
      packages = find_packages(),
      install_requires = get_requirements("requirements.txt")
     )