import typing

from pyrrt import space


class SteerFunction(typing.Generic[space.T], typing.Protocol):
    def __call__(
        self, current: space.PointInTime[space.T], target: space.T
    ) -> space.PointInTime[space.T]: ...
