import typing


class Dataclass(typing.Protocol):
    __dataclass_fields__: typing.ClassVar[typing.Dict[str, typing.Any]]


T = typing.TypeVar("T", bound=Dataclass)
T_contra = typing.TypeVar("T_contra", bound=Dataclass, contravariant=True)
