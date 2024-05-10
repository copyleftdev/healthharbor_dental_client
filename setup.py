from setuptools import setup, find_packages

setup(
    name='healthharbor_dental_client',
    version='0.1.0',
    description='A Unoffical client library for interacting with Health Harbor Dental API',
    author='Don Johnson ',
    author_email='donj@zuub.com',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
