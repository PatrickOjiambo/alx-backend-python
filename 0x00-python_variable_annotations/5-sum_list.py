#!/usr/bin/env python3
"""
File to add list contents
"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Function to add list contents
    """
    sumlist: float = 0
    for item in input_list:
        sumlist = sumlist +  item
    return sumlist
