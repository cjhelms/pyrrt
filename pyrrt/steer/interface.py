import typing

from pyrrt import space


class SteerFunction(typing.Generic[space.T], typing.Protocol):
    def __call__(self, current: space.T, target: space.T) -> space.T:
        ...
