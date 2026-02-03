import pydantic
import typing
import typing_extensions


class ContactPerson(typing_extensions.TypedDict):
    """
    ContactPerson
    """

    email_address: typing_extensions.NotRequired[str]
    """
    Email address of person
    """

    first_name: typing_extensions.NotRequired[str]
    """
    First name of person
    """

    include_in_emails: typing_extensions.NotRequired[bool]
    """
    boolean to indicate whether contact should be included on emails with invoices etc.
    """

    last_name: typing_extensions.NotRequired[str]
    """
    Last name of person
    """


class _SerializerContactPerson(pydantic.BaseModel):
    """
    Serializer for ContactPerson handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    email_address: typing.Optional[str] = pydantic.Field(
        alias="EmailAddress", default=None
    )
    first_name: typing.Optional[str] = pydantic.Field(alias="FirstName", default=None)
    include_in_emails: typing.Optional[bool] = pydantic.Field(
        alias="IncludeInEmails", default=None
    )
    last_name: typing.Optional[str] = pydantic.Field(alias="LastName", default=None)
