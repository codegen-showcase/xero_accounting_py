import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .contact_group import ContactGroup


class ContactGroups(pydantic.BaseModel):
    """
    ContactGroups
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    contact_groups: typing.Optional[typing.List["ContactGroup"]] = pydantic.Field(
        alias="ContactGroups", default=None
    )
