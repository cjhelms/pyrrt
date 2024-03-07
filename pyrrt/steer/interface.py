import typing

import pyrrt.space.interface
import pyrrt.space.point_in_time


class SteerFunction(typing.Generic[pyrrt.space.interface.T], typing.Protocol):
    def __call__(
        self,
        current: pyrrt.space.point_in_time.PointInTime[pyrrt.space.interface.T],
        target: pyrrt.space.interface.T,
    ) -> pyrrt.space.point_in_time.PointInTime[pyrrt.space.interface.T]: ...
