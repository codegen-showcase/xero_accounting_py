import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .contact import Contact


class ContactGroup(pydantic.BaseModel):
    """
    ContactGroup
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    contact_group_id: typing.Optional[str] = pydantic.Field(
        alias="ContactGroupID", default=None
    )
    """
    The Xero identifier for an contact group – specified as a string following the endpoint name. e.g. /297c2dc5-cc47-4afd-8ec8-74990b8761e9
    """
    contacts: typing.Optional[typing.List["Contact"]] = pydantic.Field(
        alias="Contacts", default=None
    )
    """
    The ContactID and Name of Contacts in a contact group. Returned on GETs when the ContactGroupID is supplied in the URL.
    """
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    """
    The Name of the contact group. Required when creating a new contact  group
    """
    status: typing.Optional[typing_extensions.Literal["ACTIVE", "DELETED"]] = (
        pydantic.Field(alias="Status", default=None)
    )
    """
    The Status of a contact group. To delete a contact group update the status to DELETED. Only contact groups with a status of ACTIVE are returned on GETs.
    """
