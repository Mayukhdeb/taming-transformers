from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='taming-transformers',
    version='0.0.1-eden',
    description='Taming Transformers for High-Resolution Image Synthesis',
    packages=find_packages(),
    include_package_data=True,
    install_requires= required,
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)
