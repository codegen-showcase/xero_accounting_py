import pydantic
import typing
import typing_extensions


class Phone(typing_extensions.TypedDict):
    """
    Phone
    """

    phone_area_code: typing_extensions.NotRequired[str]
    """
    max length = 10
    """

    phone_country_code: typing_extensions.NotRequired[str]
    """
    max length = 20
    """

    phone_number: typing_extensions.NotRequired[str]
    """
    max length = 50
    """

    phone_type: typing_extensions.NotRequired[
        typing_extensions.Literal["DDI", "DEFAULT", "FAX", "MOBILE", "OFFICE"]
    ]


class _SerializerPhone(pydantic.BaseModel):
    """
    Serializer for Phone handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    phone_area_code: typing.Optional[str] = pydantic.Field(
        alias="PhoneAreaCode", default=None
    )
    phone_country_code: typing.Optional[str] = pydantic.Field(
        alias="PhoneCountryCode", default=None
    )
    phone_number: typing.Optional[str] = pydantic.Field(
        alias="PhoneNumber", default=None
    )
    phone_type: typing.Optional[
        typing_extensions.Literal["DDI", "DEFAULT", "FAX", "MOBILE", "OFFICE"]
    ] = pydantic.Field(alias="PhoneType", default=None)
