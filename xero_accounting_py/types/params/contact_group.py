import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .contact import Contact, _SerializerContact


class ContactGroup(typing_extensions.TypedDict):
    """
    ContactGroup
    """

    contact_group_id: typing_extensions.NotRequired[str]
    """
    The Xero identifier for an contact group – specified as a string following the endpoint name. e.g. /297c2dc5-cc47-4afd-8ec8-74990b8761e9
    """

    contacts: typing_extensions.NotRequired[typing.List["Contact"]]
    """
    The ContactID and Name of Contacts in a contact group. Returned on GETs when the ContactGroupID is supplied in the URL.
    """

    name: typing_extensions.NotRequired[str]
    """
    The Name of the contact group. Required when creating a new contact  group
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["ACTIVE", "DELETED"]
    ]
    """
    The Status of a contact group. To delete a contact group update the status to DELETED. Only contact groups with a status of ACTIVE are returned on GETs.
    """


class _SerializerContactGroup(pydantic.BaseModel):
    """
    Serializer for ContactGroup handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    contact_group_id: typing.Optional[str] = pydantic.Field(
        alias="ContactGroupID", default=None
    )
    contacts: typing.Optional[typing.List["_SerializerContact"]] = pydantic.Field(
        alias="Contacts", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    status: typing.Optional[typing_extensions.Literal["ACTIVE", "DELETED"]] = (
        pydantic.Field(alias="Status", default=None)
    )
