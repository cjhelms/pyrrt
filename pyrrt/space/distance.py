from __future__ import annotations

import math
import typing

T = typing.TypeVar("T")
T_contra = typing.TypeVar("T_contra", contravariant=True)


def euclidean_distance(first: T, second: T) -> float:
    def distance() -> float:
        return math.sqrt(squared_distance())

    def squared_distance() -> float:
        field_names = vars(first).keys()
        return sum([field_squared_distance(fn) for fn in field_names])

    def field_squared_distance(field_name: str) -> float:
        return (getattr(first, field_name) - getattr(second, field_name)) ** 2

    return distance()


class DistanceFunction(typing.Protocol, typing.Generic[T_contra]):
    def __call__(self, first: T_contra, second: T_contra) -> float:
        ...
