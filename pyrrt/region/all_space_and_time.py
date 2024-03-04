import typing_extensions

from pyrrt import space

from .interface import IRegion


class AllSpaceAndTime(IRegion[space.T]):
    @typing_extensions.override
    def __contains__(self, point: space.PointInTime[space.T]) -> bool:
        return True

    @typing_extensions.override
    def draw_sample(self) -> space.T:
        ...
