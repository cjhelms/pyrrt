from __future__ import annotations

import abc
import typing

import pyrrt.space.interface
import pyrrt.space.point_in_time


class IRegion(typing.Generic[pyrrt.space.interface.T], abc.ABC):
    @abc.abstractmethod
    def __contains__(
        self, point: pyrrt.space.point_in_time.PointInTime[pyrrt.space.interface.T]
    ) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def draw_sample(self) -> pyrrt.space.interface.T:
        raise NotImplementedError()
