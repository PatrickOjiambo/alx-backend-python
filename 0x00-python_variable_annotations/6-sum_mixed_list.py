#!/usr/bin/env python3
"""
File for type annotated function
"""
from typing import List


def sum_mixed_list(mxd_list: List[int | float]) -> float:
    """
    Type annotated function
    """
    sum_list: float | int = 0
    for item in mxd_list:
        sum_list = item + sum_list
    return sum_list
