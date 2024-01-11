#!/usr/bin/env python3
"""
Complex types - string and int/float to type
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    squared_v: Union[int, float] = v**2
    returned_tuple: Tuple[str, Union[int, float]] = (k, squared_v)
    return returned_tuple
