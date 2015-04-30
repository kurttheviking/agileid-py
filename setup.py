from setuptools import setup


setup(
    description="Generate and manage AgileID identifiers",
    name='agileid',
    url='https://github.com/kurttheviking/agileid-py',
    version='0.0.1',
    packages=['agileid'],
    author='Kurt Ericson',
    author_email='kurttheviking@outlook.com',
    license='MIT',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],
    install_requires=[
        "pymongo >= 2.7.2"
    ]
)
