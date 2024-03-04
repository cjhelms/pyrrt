import typing

from pyrrt import space


class Planner(typing.Protocol, typing.Generic[space.T_contra]):
    def explore(self, initial_point: space.T_contra) -> None: ...

    def __len__(self) -> int: ...
