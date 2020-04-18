import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(name='json_metadata',
      version='1.1.0',
      description='Save/Load metadata json files',
      long_description=README,
      long_description_content_type="text/markdown",
      url='https://github.com/MaxRocamora/jsonMetadata',
      author='Maximiliano Rocamora',
      author_email='maxirocamora@gmail.com',
      license='GNU GENERAL PUBLIC LICENSE',
      packages=['jsonmd'],
      zip_safe=False)
