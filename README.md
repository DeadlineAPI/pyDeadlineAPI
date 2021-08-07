# pyDeadlineAPI

This is the first implemention of the [DeadlineAPI](https://DeadlineAPI.org) for python. It implement the whole functionality of the api plus some additional features. It also runs extensive validity checks before loading successfully loading a file.

The following classes are provided:
+ Endpoint
+ DeadlineObject
+ Location
+ Contact


## Install

You can easily install pyDeadlineAPI via pip:
```
pip install pyDeadlineAPI
```

## The API
In this section we describe how the API works. 

### How to load a directory?
Loading a directory is easy. You can use the following code to load the default directory at `directory.deadlineapi.org/directory.json`:

```python
import deadlineapi
directory = deadlineapi.Loader.load_directory_by_url()
```

Alternatively you can load from a specific url, a string or a local file on your computer/server:
```python
import deadlineapi
deadlineapi.Loader.load_directory_by_url("https://directory.deadlineapi.org/directory.json")
deadlineapi.Loader.load_directory_by_string("{ "endpointname": "url" }")
deadlineapi.Loader.load_directory_by_path(os.path.join('my","path"))
```

The loader will provide you with a list of [Endpoints](Endpoints).

### Endpoints
Endpoints represent the endpoints of the api. You can use all the fields specified in the JSON schema. E.g.:
```python
import deadlineapi
directory = deadlineapi.Loader.load_directory_by_url()
for endpoint in directory:
    print(f"Endpoint is compatible to: {endpoint.api_compatibility}")
    print(f"Deadlines provide by {endpoint.name}:")
    for d in endpoint.deadlines:
        print(f"{d.name}: {d.deadline}")
```

Note that `endpoint.name` is an alias for `endpoint.endpointname`. In the following table we list all the functionality that is on top of the API fields.


| Name                   | Description                                           |
| ---------------------- | ----------------------------------------------------- |
| `name`                 | Alias for `endpointname`                              |
| `loadedFrom`           | Only set if loaded via directory. Contains loaded url, where it was loaded from |
| `directoryName`        | Only set if loaded via directory, Contains loaded the name, as given in the directory |

Note further that you can also load endpoints directly. E.g. 
```python
import deadlineapi
deadlineapi.Loader.load_endpoint_by_string(s)
deadlineapi.Loader.load_endpoint_by_path(path)
deadlineapi.Loader.load_endpoint_by_url(url)
```

Endpoints get automatically validated against the [JSON schema](https://schema.deadlineapi.org/) and other requirements, like url in url field, emails in email field and so on. If you think that something is wrong with the schema files please discuss in the [schema repository](https://github.com/DeadlineAPI/Schema).

### DeadlineObject
The DeadlineObject correspond to the individual deadlines. They also got all field provided by API. 

```pyhton
import deadlineapi
directory = deadlineapi.Loader.load_directory_by_url()
for endpoint in directory:
        for d in endpoint.deadlines:
                print(f"{d.name}: {d.deadline} ({d.daysleft()}d)")
```

Note the DeadlineObject also provides some additional functionality:
 
| Name                   | Description                                               |
| ---------------------- | --------------------------------------------------------- |
|  `days_left()`         | How many (full) days are left until the deadline.         |
|  `hours_left()`        | How many (full) hours are left until the deadline.        |
|  `minutes_left()`      | How many (full) minutes are left until the deadline.      |
|  `countdown()`         | How much time is left in a useful format (string)         |
|  `time_left()`         | Provides the time diff as python object                   |

### Location
This class just wraps the location. It provides the following additional methods:

| Name                   | Description                                                               |
| ---------------------- | ------------------------------------------------------------------------- |
|  `to_str()`            | Provides the location as string, e.g.`virtual` or `Germany, Karlsruhe`    |

### Contact
The last class is Concat. This also provides a `toStr()` function:

| Name                   | Description                                                               |
| ---------------------- | ------------------------------------------------------------------------- |
|  `to_str()`            | Provides the contact as string, e.g.`info@kit.edu, @kitde`                |

## Contribute
Clone this repo and run

```bash
python3 -m venv venv
source venv/bin/activate
pip -r requirements.txt
```

We use the GitFlow method to organize our branches. Please work with PullRequests.


## Credits
Many many credits for [SpaceAPI](https://spaceapi.io/), who are the ultimative inspiration for this project also provided a lot of the code. E.g. our website is completely adapted by theirs. THANKS!