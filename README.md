jsonMetadata
============

Load, save, and update data from your class to a json file, and viceversa.

Example
-------

```python

from jsonmd.json_metadata import JsonMetadata

class Car():
    def __init__(self, name):
        self.metadata = JsonMetadata(name)


ferrari = Car('ferrari')
ferrari.metadata.path = your_path_for_save_the_json_file
ferrari.metadata.insert('fuel', 200)
ferrari.metadata.save()

```

# this will generate a json file on the path location spefified, that look like this

MD_ferrari.json

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
