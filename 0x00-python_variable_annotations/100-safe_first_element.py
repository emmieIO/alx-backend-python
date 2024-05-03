#!/usr/bin/env python3
"""100-safe_first_element.py"""
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """100-safe_first_element.py"""
    if lst:
        return lst[0]
    else:
        return None
