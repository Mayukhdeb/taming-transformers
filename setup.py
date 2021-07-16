from setuptools import setup, find_packages

setup(
    name='taming-transformers',
    version='0.0.1',
    description='Taming Transformers for High-Resolution Image Synthesis',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)
