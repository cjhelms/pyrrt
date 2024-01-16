from __future__ import annotations

import math
import typing

import typing_extensions


def euclidean_distance(first: T, second: T) -> float:
    def distance() -> float:
        return math.sqrt(squared_distance())

    def squared_distance() -> float:
        field_names = vars(first).keys()
        return sum([field_squared_distance(fn) for fn in field_names])

    def field_squared_distance(field_name: str) -> float:
        return (getattr(first, field_name) - getattr(second, field_name)) ** 2

    return distance()


class MetricSpace:
    def __init__(
        self,
        distance_function: DistanceFunction[
            typing_extensions.Self
        ] = euclidean_distance,
    ) -> None:
        self._distance_function = distance_function

    def distance_to(self, other: typing_extensions.Self) -> float:
        return self._distance_function(self, other)


T = typing.TypeVar("T", bound=MetricSpace)
T_contra = typing.TypeVar("T_contra", bound=MetricSpace, contravariant=True)


class DistanceFunction(typing.Protocol, typing.Generic[T_contra]):
    def __call__(self, first: T_contra, second: T_contra) -> float:
        ...
