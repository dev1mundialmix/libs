from setuptools import setup, find_packages

setup(
    name='common_libs',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'cx_Oracle',
    ],
)