from __future__ import annotations

import dataclasses
import datetime
import typing

import pyrrt.space.interface


@dataclasses.dataclass
class PointInTime(typing.Generic[pyrrt.space.interface.T]):
    time_stamp: datetime.timedelta
    point: pyrrt.space.interface.T

    @staticmethod
    def make_with_trivial_time_stamp(point: pyrrt.space.interface.T) -> PointInTime:
        return PointInTime.make_with_starting_time_stamp(point)

    @staticmethod
    def make_with_starting_time_stamp(point: pyrrt.space.interface.T) -> PointInTime:
        return PointInTime(datetime.timedelta(seconds=0), point)
