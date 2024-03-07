import typing

import pyrrt.region.interface
import pyrrt.space.interface
import pyrrt.space.point_in_time


class AllSpaceAndTime(pyrrt.region.interface.IRegion[pyrrt.space.interface.T]):
    @typing.override
    def __contains__(
        self, point: pyrrt.space.point_in_time.PointInTime[pyrrt.space.interface.T]
    ) -> bool:
        return True

    @typing.override
    def draw_sample(self) -> pyrrt.space.interface.T: ...
