import datetime

from pyrrt import space

from .interface import IRegion


class AllSpaceAndTime(IRegion[space.MetricSpace]):
    def __contains__(
        self, point: space.MetricSpace, elapsed_time: datetime.timedelta
    ) -> bool:
        return True
