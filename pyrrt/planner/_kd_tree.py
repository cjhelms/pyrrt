import typing

import pyrrt.space.distance
import pyrrt.space.interface

_T = typing.TypeVar("_T")


class KDTree(typing.Generic[pyrrt.space.interface.T, _T]):
    def __init__(
        self,
        get_point: typing.Callable[[_T], pyrrt.space.interface.T],
        distance_function: pyrrt.space.distance.DistanceFunction[
            pyrrt.space.interface.T
        ],
    ) -> None:
        self._get_point = get_point
        self._distance_function = distance_function

    def insert(self, node: _T) -> None:
        # TODO
        raise NotImplementedError()

    def find_nearest_neighbor(self, point: pyrrt.space.interface.T) -> _T:
        # TODO
        raise NotImplementedError()

    def __len__(self) -> int:
        # TODO
        raise NotImplementedError()
