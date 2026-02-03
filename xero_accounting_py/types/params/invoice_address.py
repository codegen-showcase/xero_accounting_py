import pydantic
import typing
import typing_extensions


class InvoiceAddress(typing_extensions.TypedDict):
    """
    InvoiceAddress
    """

    address_line1: typing_extensions.NotRequired[str]
    """
    First line of a physical address
    """

    address_line2: typing_extensions.NotRequired[str]
    """
    Second line of a physical address
    """

    address_line3: typing_extensions.NotRequired[str]
    """
    Third line of a physical address
    """

    address_line4: typing_extensions.NotRequired[str]
    """
    Fourth line of a physical address
    """

    city: typing_extensions.NotRequired[str]
    """
    City of a physical address
    """

    country: typing_extensions.NotRequired[str]
    """
    Country of a physical address
    """

    invoice_address_type: typing_extensions.NotRequired[
        typing_extensions.Literal["FROM", "TO"]
    ]
    """
    Indicates whether the address is defined as origin (FROM) or destination (TO)
    """

    postal_code: typing_extensions.NotRequired[str]
    """
    Postal code of a physical address
    """

    region: typing_extensions.NotRequired[str]
    """
    Region or state of a physical address
    """


class _SerializerInvoiceAddress(pydantic.BaseModel):
    """
    Serializer for InvoiceAddress handling case conversions
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
    city: typing.Optional[str] = pydantic.Field(alias="City", default=None)
    country: typing.Optional[str] = pydantic.Field(alias="Country", default=None)
    invoice_address_type: typing.Optional[typing_extensions.Literal["FROM", "TO"]] = (
        pydantic.Field(alias="InvoiceAddressType", default=None)
    )
    postal_code: typing.Optional[str] = pydantic.Field(alias="PostalCode", default=None)
    region: typing.Optional[str] = pydantic.Field(alias="Region", default=None)
