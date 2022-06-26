#!/usr/bin/env python3
"""type annotations"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


"""define NoneType"""
NoneType = type(None)


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, NoneType]
        ) -> Union[Any, T]:
    """Given the parameters and the return values,
    add type annotations to the function"""
    if key in dct:
        return (dct[key])
    else:
        return (default)
