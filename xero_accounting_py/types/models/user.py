import pydantic
import typing
import typing_extensions


class User(pydantic.BaseModel):
    """
    User
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email_address: typing.Optional[str] = pydantic.Field(
        alias="EmailAddress", default=None
    )
    """
    Email address of user
    """
    first_name: typing.Optional[str] = pydantic.Field(alias="FirstName", default=None)
    """
    First name of user
    """
    is_subscriber: typing.Optional[bool] = pydantic.Field(
        alias="IsSubscriber", default=None
    )
    """
    Boolean to indicate if user is the subscriber
    """
    last_name: typing.Optional[str] = pydantic.Field(alias="LastName", default=None)
    """
    Last name of user
    """
    organisation_role: typing.Optional[
        typing_extensions.Literal[
            "CASHBOOKCLIENT",
            "FINANCIALADVISER",
            "INVOICEONLY",
            "MANAGEDCLIENT",
            "READONLY",
            "REMOVED",
            "STANDARD",
            "UNKNOWN",
        ]
    ] = pydantic.Field(alias="OrganisationRole", default=None)
    """
    User role that defines permissions in Xero and via API (READONLY, INVOICEONLY, STANDARD, FINANCIALADVISER, etc)
    """
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    """
    Timestamp of last change to user
    """
    user_id: typing.Optional[str] = pydantic.Field(alias="UserID", default=None)
    """
    Xero identifier
    """
