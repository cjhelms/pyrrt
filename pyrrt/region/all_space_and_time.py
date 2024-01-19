import datetime
import typing

from .interface import IRegion


class AllSpaceAndTime(IRegion[typing.Any]):
    def __contains__(self, point: typing.Any, elapsed_time: datetime.timedelta) -> bool:
        return True
