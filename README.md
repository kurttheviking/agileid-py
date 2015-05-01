agileid.py
==========

An AgileId is a scoped, string-based, url-friendly format of BSON ObjectIds. AgileIds are 33% shorter as strings than ObjectIds (16 characters vs 24) while preserving natural sortability. These are convenient properties for persistence in stores that do not support BSON while maintaining portability.

Built and tested in environments running Python 2.6 and Python 2.7.


## Dependencies

- [pymongo](https://pypi.python.org/pypi/pymongo/); for MongoDB-compatable ObjectIds


## Install

```
pip install agileid
```


## Basic use

```
>>> import agileid
>>> import bson

>>> print agileid.create()
VULGn4d-thEOg2Jb

>>> print agileid.cast(bson.objectid.ObjectId(), 'user')
user!VULG24d-thEOg2Jd

>>> print agileid.to_hexstring('user!VULG24d-thEOg2Jd')
5542c6db877eb6110e83625d

>>> oid = agileid.to_objectid('user!VULG24d-thEOg2Jd')
>>> oid
ObjectId('5542c6db877eb6110e83625d')
```


## API

Scoping is delimited using the `!` character. As a toy example, "user!1" would indicate scope (`id_type`) of `user` who has `id` of `1`. Scoping can be nested, such as "bigco!user!1". The scope itself cannot contain a bang character &ndash; a scope of `huzzah!` is invalid because it would result in an AgileId of `huzzah!!1`.

All api methods will raise a `ValueError` if an `id_type` is provided that contains `!`.

#### `agileid.cast(id, id_type=None)`

**Arguments**

- `id`: an AgileId, ObjectId, or String-formatted ObjectId
- `id_type`: any valid String or any input that can be cast to a String

**Returns**

An AgileId string

**Example**

```
>>> import agileid
>>> print agileid.cast(bson.objectid.ObjectId(), 'user')
user!VULHMYd-thEOg2Je
```

To provide safety when coercing an unknown or variable input id to an AgileId, an `id_type` that matches the highest scope will not cause "extra" scoping:

```
>>> import agileid
>>> print agileid.cast('user!VUKMsYd-tiItmsO5', 'user')
user!VUKMsYd-tiItmsO5
```

#### `agileid.create(id_type=None)`

**Arguments**

- `id_type`: any String or input that can be cast to a String

**Returns**

An AgileId string

**Example**

```
>>> import agileid
>>> print agileid.create()
VUKNcId-tiJpAMRH

>>> print agileid.create('user')
user!VUKOL4d-tiJpAMRI
```

#### `agileid.is_valid(id)`

**Arguments**

- `id`: A String

**Returns**

A Boolean indicating whether or not the input is a valid AgileId

**Example**

```
>>> import agileid
>>> print agileid.is_valid('foo')
False

>>> print agileid.is_valid(bson.objectid.ObjectId())
False

>>> print agileid.is_valid(agileid.create())
True
```

#### `agileid.to_hexstring(id)`

**Arguments**

- `id`: an AgileId, ObjectId, or String-formatted ObjectId

**Returns**

A String-formatted ObjectId

**Example**

```
>>> import agileid
>>> print agileid.to_hexstring(agileid.create())
5542c757877eb6110e836261
```

#### `agileid.to_objectid(id)`

**Arguments**

- `id`: an AgileId, ObjectId, or String-formatted ObjectId

**Returns**

An ObjectId

**Example**

```
>>> import agileid
>>> oid = agileid.to_objectid(agileid.create())
>>> oid
ObjectId('5542c76c877eb6110e836263')
```


## Tests

To run the unit test suite from the top-level agileid directory:

```
python -m unittest discover tests
```

Each test file provides a test case for a specific method, which can be executed in isolation if needed:

```
cd tests
python test_create.py
```

To verify test coverage with [coverage](https://pypi.python.org/pypi/coverage):

```
coverage run --source agileid -m unittest discover tests
coverage report --show-missing
```


## Contribute

PRs are welcome! This package operates with 100% test coverage. PRs must maintain this coverage metric to be accepted.

For bugs, please include a failing test which passes when your PR is applied.
