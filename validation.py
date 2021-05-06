from dataclasses import dataclass, field
from typing import NewType

from pytest import raises

from apischema import ValidationError, deserialize, schema, serialize