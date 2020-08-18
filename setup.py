import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='jsonMetadata',
    version='1.1.1',
    author='Maximiliano Rocamora',
    author_email='maxirocamora@gmail.com',
    description='Save/Load metadata from classes to json files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/MaxRocamora/jsonMetadata',
    license='GNU GENERAL PUBLIC LICENSE',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
    zip_safe=False)
