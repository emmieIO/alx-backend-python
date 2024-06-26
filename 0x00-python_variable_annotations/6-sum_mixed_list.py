#!/usr/bin/env python3
"""6-sum_mixed_list.py"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """6-sum_mixed_list.py"""
    acc: float = 0
    for i in range(len(mxd_lst)):
        acc = acc + mxd_lst[i]
    return acc
