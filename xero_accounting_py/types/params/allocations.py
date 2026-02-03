import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .allocation import Allocation, _SerializerAllocation


class Allocations(typing_extensions.TypedDict):
    """
    Allocations
    """

    allocations: typing_extensions.NotRequired[typing.List["Allocation"]]


class _SerializerAllocations(pydantic.BaseModel):
    """
    Serializer for Allocations handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    allocations: typing.Optional[typing.List["_SerializerAllocation"]] = pydantic.Field(
        alias="Allocations", default=None
    )
