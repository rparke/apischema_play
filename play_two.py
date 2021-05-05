from dataclasses import dataclass
from typing import Union

from apischema import Undefined, UndefinedType, deserialize, serialize
from apischema.json_schema import deserialization_schema


@dataclass
class Foo:
    bar: Union[int, UndefinedType] = Undefined
    baz: Union[int, UndefinedType, None] = Undefined

