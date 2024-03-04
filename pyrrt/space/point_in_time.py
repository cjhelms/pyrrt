from __future__ import annotations

import dataclasses
import datetime
import typing

from .interface import T


@dataclasses.dataclass
class PointInTime(typing.Generic[T]):
    time_stamp: datetime.timedelta
    point: T

    @staticmethod
    def make_with_trivial_time_stamp(point: T) -> PointInTime:
        return PointInTime.make_with_starting_time_stamp(point)

    @staticmethod
    def make_with_starting_time_stamp(point: T) -> PointInTime:
        return PointInTime(datetime.timedelta(seconds=0), point)
