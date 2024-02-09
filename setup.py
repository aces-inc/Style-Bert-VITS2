from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements

setup(
    name='style_bert_vits2',
    version='0.1.0',
    description='Style-Bert-VITS2 Clone',
    author='sinhat98',
    author_email='sinhat897205@gmail.com',
    packages=find_packages(),
    install_requires=read_requirements(),
)