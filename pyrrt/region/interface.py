from __future__ import annotations

import abc
import typing

from pyrrt import space


class IRegion(typing.Generic[space.T], abc.ABC):
    @abc.abstractmethod
    def __contains__(self, point: space.PointInTime[space.T]) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def draw_sample(self) -> space.T:
        raise NotImplementedError()
