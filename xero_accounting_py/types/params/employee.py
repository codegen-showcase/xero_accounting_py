import pydantic
import typing
import typing_extensions

from .external_link import ExternalLink, _SerializerExternalLink
from .validation_error import ValidationError, _SerializerValidationError


class Employee(typing_extensions.TypedDict):
    """
    Employee
    """

    employee_id: typing_extensions.NotRequired[str]
    """
    The Xero identifier for an employee e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
    """

    external_link: typing_extensions.NotRequired[ExternalLink]

    first_name: typing_extensions.NotRequired[str]
    """
    First name of an employee (max length = 255)
    """

    last_name: typing_extensions.NotRequired[str]
    """
    Last name of an employee (max length = 255)
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED", "GDPRREQUEST"]
    ]
    """
    Current status of an employee – see contact status types
    """

    status_attribute_string: typing_extensions.NotRequired[str]
    """
    A string to indicate if a invoice status
    """

    updated_date_utc: typing_extensions.NotRequired[str]

    validation_errors: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of validation error messages from the API
    """


class _SerializerEmployee(pydantic.BaseModel):
    """
    Serializer for Employee handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    employee_id: typing.Optional[str] = pydantic.Field(alias="EmployeeID", default=None)
    external_link: typing.Optional[_SerializerExternalLink] = pydantic.Field(
        alias="ExternalLink", default=None
    )
    first_name: typing.Optional[str] = pydantic.Field(alias="FirstName", default=None)
    last_name: typing.Optional[str] = pydantic.Field(alias="LastName", default=None)
    status: typing.Optional[
        typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED", "GDPRREQUEST"]
    ] = pydantic.Field(alias="Status", default=None)
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    validation_errors: typing.Optional[typing.List[_SerializerValidationError]] = (
        pydantic.Field(alias="ValidationErrors", default=None)
    )
