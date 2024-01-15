import abc
import datetime
import typing

from pyrrt import space


class IRegion(typing.Generic[space.T], abc.ABC):
    @abc.abstractmethod
    def __contains__(self, point: space.T, elapsed_time: datetime.timedelta) -> bool:
        raise NotImplementedError("Implement me!")
