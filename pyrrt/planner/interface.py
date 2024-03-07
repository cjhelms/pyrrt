import typing

import pyrrt.space.interface


class Planner(typing.Protocol, typing.Generic[pyrrt.space.interface.T_contra]):
    def explore(self, initial_point: pyrrt.space.interface.T_contra) -> None: ...

    def __len__(self) -> int: ...
