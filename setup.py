from setuptools import setup, find_packages

setup(
    name='mundialmix',
    version='0.1',
    packages=find_packages(include=['mundialmix', 'mundialmix.*']),
    install_requires=[
        'cx_Oracle',
    ],
    include_package_data=True,
)