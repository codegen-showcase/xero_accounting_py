import pydantic
import typing
import typing_extensions


class Phone(pydantic.BaseModel):
    """
    Phone
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    phone_area_code: typing.Optional[str] = pydantic.Field(
        alias="PhoneAreaCode", default=None
    )
    """
    max length = 10
    """
    phone_country_code: typing.Optional[str] = pydantic.Field(
        alias="PhoneCountryCode", default=None
    )
    """
    max length = 20
    """
    phone_number: typing.Optional[str] = pydantic.Field(
        alias="PhoneNumber", default=None
    )
    """
    max length = 50
    """
    phone_type: typing.Optional[
        typing_extensions.Literal["DDI", "DEFAULT", "FAX", "MOBILE", "OFFICE"]
    ] = pydantic.Field(alias="PhoneType", default=None)
