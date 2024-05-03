#!/usr/bin/env python3
from typing import List


def sum_list(input_list: List[float]) -> float:
    """5-sum_list.py"""
    acc: float = 0
    for i in range(len(input_list)):
        acc = acc + input_list[i]
    return acc
