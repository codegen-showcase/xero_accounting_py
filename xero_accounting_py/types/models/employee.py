import pydantic
import typing
import typing_extensions

from .external_link import ExternalLink
from .validation_error import ValidationError


class Employee(pydantic.BaseModel):
    """
    Employee
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    employee_id: typing.Optional[str] = pydantic.Field(alias="EmployeeID", default=None)
    """
    The Xero identifier for an employee e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
    """
    external_link: typing.Optional[ExternalLink] = pydantic.Field(
        alias="ExternalLink", default=None
    )
    first_name: typing.Optional[str] = pydantic.Field(alias="FirstName", default=None)
    """
    First name of an employee (max length = 255)
    """
    last_name: typing.Optional[str] = pydantic.Field(alias="LastName", default=None)
    """
    Last name of an employee (max length = 255)
    """
    status: typing.Optional[
        typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED", "GDPRREQUEST"]
    ] = pydantic.Field(alias="Status", default=None)
    """
    Current status of an employee – see contact status types
    """
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    """
    A string to indicate if a invoice status
    """
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    validation_errors: typing.Optional[typing.List[ValidationError]] = pydantic.Field(
        alias="ValidationErrors", default=None
    )
    """
    Displays array of validation error messages from the API
    """
