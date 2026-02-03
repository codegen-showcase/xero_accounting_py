import pydantic
import typing


class ContactPerson(pydantic.BaseModel):
    """
    ContactPerson
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email_address: typing.Optional[str] = pydantic.Field(
        alias="EmailAddress", default=None
    )
    """
    Email address of person
    """
    first_name: typing.Optional[str] = pydantic.Field(alias="FirstName", default=None)
    """
    First name of person
    """
    include_in_emails: typing.Optional[bool] = pydantic.Field(
        alias="IncludeInEmails", default=None
    )
    """
    boolean to indicate whether contact should be included on emails with invoices etc.
    """
    last_name: typing.Optional[str] = pydantic.Field(alias="LastName", default=None)
    """
    Last name of person
    """
