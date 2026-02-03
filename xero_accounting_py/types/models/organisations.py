import pydantic
import typing

from .organisation import Organisation


class Organisations(pydantic.BaseModel):
    """
    Organisations
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    organisations: typing.Optional[typing.List[Organisation]] = pydantic.Field(
        alias="Organisations", default=None
    )
