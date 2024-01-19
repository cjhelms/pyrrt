import typing

from pyrrt import region, space, steer

from .interface import IPlanner


class RRT(IPlanner, typing.Generic[space.T]):
    def __init__(
        self,
        space: typing.Type[space.T],
        distance_function: space.DistanceFunction[space.T],
        steer_function: steer.SteerFunction[space.T],
        free_space: region.IRegion[space.T],
    ) -> None:
        pass
