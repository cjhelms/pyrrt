import typing

from pyrrt import space

_T = typing.TypeVar("_T")


class KDTree(typing.Generic[space.T, _T]):
    def __init__(
        self,
        get_point: typing.Callable[[_T], space.T],
        distance_function: space.DistanceFunction[space.T],
    ) -> None:
        self._get_point = get_point
        self._distance_function = distance_function

    def insert(self, node: _T) -> None:
        # TODO
        raise NotImplementedError()

    def find_nearest_neighbor(self, point: space.T) -> _T:
        # TODO
        raise NotImplementedError()

    def __len__(self) -> int:
        # TODO
        raise NotImplementedError()
