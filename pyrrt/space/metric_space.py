from __future__ import annotations

import abc
import typing

import typing_extensions


def euclidean_distance(first: T, second: T) -> float:
    return 0.0


class MetricSpace(abc.ABC):
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
