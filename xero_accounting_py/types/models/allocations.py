import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .allocation import Allocation


class Allocations(pydantic.BaseModel):
    """
    Allocations
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    allocations: typing.Optional[typing.List["Allocation"]] = pydantic.Field(
        alias="Allocations", default=None
    )
