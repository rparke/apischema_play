from collections.abc import Collection
from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID, uuid4

from pytest import raises

from apischema import ValidationError, deserialize, serialize
from apischema.json_schema import deserialization_schema


#Create a resource schema
@dataclass
class Resource:
    id: UUID
    name: str


#Deserialization
assert(deserialization_schema(Resource)) == {'$schema': 'http://json-schema.org/draft/2019-09/schema#',
'type': 'object', 
'properties': {'id': {'type': 'string', 'format': 'uuid'}, 
'name': {'type': 'string'}}, 
'required': ['id', 'name'], 
'additionalProperties': False}
