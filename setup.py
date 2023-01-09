from setuptools import setup

setup(
    name='flask-keap',
    version='0.1.0',
    description='A Rest Client For Flask applications',
    author='will sexton',
    author_email='will@theapiguys.com',
    license='BSD 2-clause',
    packages=['flask-keap'],
    install_requires=['Flask',
                      'AuthLib',
                      'python-dateutil'
                      ],

    classifiers=[
        'License :: OSI Approved :: BSD License'
    ],
)
