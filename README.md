# pyDeadlineAPI

This is the first implemention of DeadlineAPI for python. The following classes are provided:
+ Endpoint
+ DeadlineObject
+ Location
+ Contact


## The API
In this short section we describe how the API works. 

### How to load a directory?
Loading a directory is easy. You can use the following code to load the default directory at `directory.deadlineapi.org/directory.json`:

```python
directory = api.Loader.load_directory_by_url()
```

Alternatively you can load from a specific url, a string or a local file on your computer/server:
```python
api.Loader.load_directory_by_url("https://directory.deadlineapi.org/directory.json")
api.Loader.load_directory_by_string("{ "endpointname": "url" }")
api.Loader.load_directory_by_path(os.path.join('my","path"))
```

The loader will provide you with a list of [Endpoints](Endpoints).

### Endpoints
Endpoints represent the endpoints of the api. You can use all the fields specified in the JSON schema. E.g.:
```python
for endpoint in directory:
    print(f"Endpoint is compatible to: {endpoint.api_compatibility}")
    print(f"Deadlines provide by {endpoint.name}:")
    for d in endpoint.deadlines:
        print(f"{d.name}: {d.deadline}")
```

Note that `endpoint.name` is an alias for `endpoint.endpointname`. In the following table we list all the functionality that is on top of the API fields.


| Name                   | Description                    |
| ---------------------- | ------------------------------ |
|  `name`                | Alias for `endpointname`       | 

Note further that you can also load endpoints directly. E.g. 
```python
api.Loader.load_endpoint_by_string(s)
api.Loader.load_endpoint_by_path(path)
api.Loader.load_endpoint_by_url(url)
```

Endpoints get automatically validated against the [JSON schema](https://schema.deadlineapi.org/) and other requirements, like url in url field, emails in email field and so on. If you think that something is wrong with the schema files please discuss in the [schema repository](https://github.com/DeadlineAPI/Schema).

### DeadlineObject
The DeadlineObject correspond to the individual deadlines. They also got all field provided by API. 

```pyhton
for d in endpoint.deadlines:
        print(f"{d.name}: {d.deadline} ({d.daysleft()}d)")
```

Note the DeadlineObject also provides some additional functionality:
 
| Name                   | Description                                               |
| ---------------------- | --------------------------------------------------------- |
|  `daysleft()`          | How many (full) days are left until the deadline.         |
|  `hoursleft()`         | How many (full) hours are left until the deadline.        |
|  `minutesleft()`       | How many (full) minutes are left until the deadline.      |
|  `countdown()`         | How much time is left in a useful format (string)         |

### Location
This class just wraps the location. It provides the following additional methods:

| Name                   | Description                                                               |
| ---------------------- | ------------------------------------------------------------------------- |
|  `toStr()`             | Provides the location as string, e.g.`virtual` or `Germany, Karlsruhe`    |


### Contact
The last class is Concat. This also provides a `toStr()` function:

| Name                   | Description                                                               |
| ---------------------- | ------------------------------------------------------------------------- |
|  `toStr()`             | Provides the contact as string, e.g.`info@kit.edu, @kitde`                |




## Install

WORK IN PROGRESS

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