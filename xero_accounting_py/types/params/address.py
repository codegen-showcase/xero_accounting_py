import pydantic
import typing
import typing_extensions


class Address(typing_extensions.TypedDict):
    """
    Address
    """

    address_line1: typing_extensions.NotRequired[str]
    """
    max length = 500
    """

    address_line2: typing_extensions.NotRequired[str]
    """
    max length = 500
    """

    address_line3: typing_extensions.NotRequired[str]
    """
    max length = 500
    """

    address_line4: typing_extensions.NotRequired[str]
    """
    max length = 500
    """

    address_type: typing_extensions.NotRequired[
        typing_extensions.Literal["POBOX", "STREET"]
    ]
    """
    define the type of address
    """

    attention_to: typing_extensions.NotRequired[str]
    """
    max length = 255
    """

    city: typing_extensions.NotRequired[str]
    """
    max length = 255
    """

    country: typing_extensions.NotRequired[str]
    """
    max length = 50, [A-Z], [a-z] only
    """

    postal_code: typing_extensions.NotRequired[str]
    """
    max length = 50
    """

    region: typing_extensions.NotRequired[str]
    """
    max length = 255
    """


class _SerializerAddress(pydantic.BaseModel):
    """
    Serializer for Address handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address_line1: typing.Optional[str] = pydantic.Field(
        alias="AddressLine1", default=None
    )
    address_line2: typing.Optional[str] = pydantic.Field(
        alias="AddressLine2", default=None
    )
    address_line3: typing.Optional[str] = pydantic.Field(
        alias="AddressLine3", default=None
    )
    address_line4: typing.Optional[str] = pydantic.Field(
        alias="AddressLine4", default=None
    )
    address_type: typing.Optional[typing_extensions.Literal["POBOX", "STREET"]] = (
        pydantic.Field(alias="AddressType", default=None)
    )
    attention_to: typing.Optional[str] = pydantic.Field(
        alias="AttentionTo", default=None
    )
    city: typing.Optional[str] = pydantic.Field(alias="City", default=None)
    country: typing.Optional[str] = pydantic.Field(alias="Country", default=None)
    postal_code: typing.Optional[str] = pydantic.Field(alias="PostalCode", default=None)
    region: typing.Optional[str] = pydantic.Field(alias="Region", default=None)
