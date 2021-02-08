from setuptools import setup

with open("README.md") as README:
    long_description = README.read()

setup(
    name='PIL-Tools',
    version='0.2',
    description='An extension module for Pillow to add functions that help simplify some processes.',
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Steven Shrewsbury',
    author_email='',
    url='https://github.com/stshrewsburyDev/PIL-Tools',
    packages=['PILTools'],
    install_requires=['Pillow', 'requests'],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
