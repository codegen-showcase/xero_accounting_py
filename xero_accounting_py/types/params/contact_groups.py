import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .contact_group import ContactGroup, _SerializerContactGroup


class ContactGroups(typing_extensions.TypedDict):
    """
    ContactGroups
    """

    contact_groups: typing_extensions.NotRequired[typing.List["ContactGroup"]]


class _SerializerContactGroups(pydantic.BaseModel):
    """
    Serializer for ContactGroups handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    contact_groups: typing.Optional[typing.List["_SerializerContactGroup"]] = (
        pydantic.Field(alias="ContactGroups", default=None)
    )
