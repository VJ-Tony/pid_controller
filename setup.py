from setuptools import setup, find_packages

import pid_controller

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='pid_controller',
    version=pid_controller.__version__,
    description='Simple PID controller implementation',
    long_description=readme(),
    url='http://github.com/jrheling/pid_controller',
    author='Joshua Heling',
    author_email='jrh@netfluvia.org',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False)
