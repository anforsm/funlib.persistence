from dataclasses import dataclass
from typing import Union

@dataclass
class Vec:
    dtype: Union[type, str]
    size: int


def type_to_str(type):
    if isinstance(type, Vec):
        return f"Vec({type_to_str(type.dtype)}, {type.size})"
    else:
        return type.__name__
