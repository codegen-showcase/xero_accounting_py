import pydantic
import typing

from .attachment import Attachment


class Attachments(pydantic.BaseModel):
    """
    Attachments
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attachments: typing.Optional[typing.List[Attachment]] = pydantic.Field(
        alias="Attachments", default=None
    )
