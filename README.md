jsonMetadata
============

Load, save, and update data from your class to a json file, and viceversa.

Example
-------

```python

from jsonmd.json_metadata import JsonMetadata

class Car():
    def __init__(self, name):
        self.meta = JsonMetadata(name)


ferrari = Car('ferrari')
ferrari.meta.path = your_path_for_save_the_json_file
ferrari.meta.insert('fuel', 200)
ferrari.meta.save()

```

#### this will generate a json file on the path location specified, that look like this

MD_ferrari.json

<dl>
  <dt>
{
   "_about": "Saved by JsonMetada",
   "_version": "1.0.0",
   "fuel": 200,
   "system": {
        "PC": "Your_User",
        "User": "Max",
        "app": "python.exe",
        "name": "ferrari", 
        "time": {
            "day": "11", 
            "month": "Oct", 
            "save_time": "Sun Oct 11 17:27:05 2047", 
            "time": "17:27", 
            "year": "2047", 
            "year_day": "047"
        }
    }
}
  </dt>
</dl>

#### Loading your data

```python

from jsonmd.json_metadata import JsonMetadata

class Car():
    def __init__(self, name):
        self.meta = JsonMetadata(name)


ferrari = Car('ferrari')
ferrari.meta.path = your_path_for_save_the_json_file
ferrari.meta.load()

ferrari.meta.data['fuel']  # 200
ferrari.meta.save()

```

#### Load the data as an object, the json is converted to a class with attributes

```python

from jsonmd.json_metadata import JsonMetadata

class Car():
    def __init__(self, name):
        self.meta = JsonMetadata(name)


ferrari = Car('ferrari')
ferrari.meta.path = your_path_for_save_the_json_file
ferrari.metadata = ferrari.meta.load_as_class()

ferrari.metadata.fuel  # 200

```

#### Install
pip install json-metada
https://pypi.org/project/json-metadata/1.1.0/
