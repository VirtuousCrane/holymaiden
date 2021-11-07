from setuptools import find_packages, setup

setup(
    name='shrinemaiden',
    packages=['shrinemaiden'],
    version='0.1.0',
    description='An auxiliary library for deep learning with Audio data',
    author='virtuouscrane',
    license='MIT',
    install_requires=['librosa'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
