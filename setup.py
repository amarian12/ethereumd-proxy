#!/usr/bin/env python
from setuptools import find_packages, setup


VERSION = '0.1.dev'

with open('README.rst', 'rb') as f:
    readme = f.read().decode('utf-8')


setup(
    name='ethereumd-proxy',
    version=VERSION,
    description='Ethereum proxy to geth node',
    long_description=readme,
    author='Bogdan Kurinnyi',
    author_email='bogdankurinnyi.dev1@gmail.com',
    url='https://github.com/DeV1doR/ethereumd-proxy',
    py_modules=['ethereumd_cli'],
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'sanic==0.5.4',
        'aiohttp==2.2.3',
        'APScheduler==3.3.1',
        'colorlog==2.10.0',
        'click==6.7',
        'requests==2.9.1',
    ],
    entry_points='''
    [console_scripts]
    ethereumd-cli=ethereumd_cli:cli
    '''
)
