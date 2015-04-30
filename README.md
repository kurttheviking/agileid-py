agileid.py
==========

## Description

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

>>> agile_id = agileid.create()
>>> print agile_id
XXX

>>> agile_id = agileid.cast('user', bson.objectid.ObjectId())
>>> print agile_id
XXX

>>> print agileid.to_hex_string(agile_id)
XXX

>>> print agileid.to_ObjectId(agile_id)
XXX
```


## API

#### `agileid.cast(id, type=None)`

**Arguments**

- `id`: an AgileId, ObjectId, or String-formatted ObjectId
- `type`: any valid String or any input that can be cast to a String

**Returns**

An AgileId string

**Example**

```
>>> import agileid
>>> agile_id = agileid.cast(bson.objectid.ObjectId(), 'user')
>>> print agile_id
XXX
```

#### `agileid.create(type=None)`

**Arguments**

- `type`: any valid String or any input that can be cast to a String

**Returns**

An AgileId string

**Example**

```
>>> import agileid
>>> agile_id = agileid.create()
>>> print agile_id
XXX
```

#### `agileid.is_valid(id)`

**Arguments**

- `id`: A String or ObjectID

**Returns**

A Boolean indicating whether or not the input is a valid AgileId

**Example**

```
>>> import agileid
>>> print agileid.is_valid('foo')
False

>>> print agileid.is_valid(agileid.create())
True
```

#### `agileid.to_hex_string(id)`

**Arguments**

- `id`: an AgileId, ObjectId, or String-formatted ObjectId

**Returns**

A String-formatted ObjectId

**Example**

```
>>> import agileid
>>> print agileid.to_hex_string(agileid.create())
XXX
```

#### `agileid.to_ObjectId(id)`

**Arguments**

- `id`: an AgileId, ObjectId, or String-formatted ObjectId

**Returns**

A ObjectId

**Example**

```
>>> import agileid
>>> print agileid.to_ObjectId(agileid.create())
XXX
```