from __future__ import annotations

import math
import typing

import pyrrt.space.interface


def euclidean_distance(
    first: pyrrt.space.interface.T, second: pyrrt.space.interface.T
) -> float:
    def distance() -> float:
        return math.sqrt(squared_distance())

    def squared_distance() -> float:
        field_names = vars(first).keys()
        return sum([field_squared_distance(fn) for fn in field_names])

    def field_squared_distance(field_name: str) -> float:
        return (getattr(first, field_name) - getattr(second, field_name)) ** 2

    return distance()


class DistanceFunction(typing.Protocol, typing.Generic[pyrrt.space.interface.T_contra]):
    def __call__(
        self,
        first: pyrrt.space.interface.T_contra,
        second: pyrrt.space.interface.T_contra,
    ) -> float: ...
