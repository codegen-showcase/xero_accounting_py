import pydantic
import typing
import typing_extensions


class User(typing_extensions.TypedDict):
    """
    User
    """

    email_address: typing_extensions.NotRequired[str]
    """
    Email address of user
    """

    first_name: typing_extensions.NotRequired[str]
    """
    First name of user
    """

    is_subscriber: typing_extensions.NotRequired[bool]
    """
    Boolean to indicate if user is the subscriber
    """

    last_name: typing_extensions.NotRequired[str]
    """
    Last name of user
    """

    organisation_role: typing_extensions.NotRequired[
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
    ]
    """
    User role that defines permissions in Xero and via API (READONLY, INVOICEONLY, STANDARD, FINANCIALADVISER, etc)
    """

    updated_date_utc: typing_extensions.NotRequired[str]
    """
    Timestamp of last change to user
    """

    user_id: typing_extensions.NotRequired[str]
    """
    Xero identifier
    """


class _SerializerUser(pydantic.BaseModel):
    """
    Serializer for User handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    email_address: typing.Optional[str] = pydantic.Field(
        alias="EmailAddress", default=None
    )
    first_name: typing.Optional[str] = pydantic.Field(alias="FirstName", default=None)
    is_subscriber: typing.Optional[bool] = pydantic.Field(
        alias="IsSubscriber", default=None
    )
    last_name: typing.Optional[str] = pydantic.Field(alias="LastName", default=None)
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
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    user_id: typing.Optional[str] = pydantic.Field(alias="UserID", default=None)
