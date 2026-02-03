import pydantic
import typing
import typing_extensions


class InvoiceAddress(pydantic.BaseModel):
    """
    InvoiceAddress
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address_line1: typing.Optional[str] = pydantic.Field(
        alias="AddressLine1", default=None
    )
    """
    First line of a physical address
    """
    address_line2: typing.Optional[str] = pydantic.Field(
        alias="AddressLine2", default=None
    )
    """
    Second line of a physical address
    """
    address_line3: typing.Optional[str] = pydantic.Field(
        alias="AddressLine3", default=None
    )
    """
    Third line of a physical address
    """
    address_line4: typing.Optional[str] = pydantic.Field(
        alias="AddressLine4", default=None
    )
    """
    Fourth line of a physical address
    """
    city: typing.Optional[str] = pydantic.Field(alias="City", default=None)
    """
    City of a physical address
    """
    country: typing.Optional[str] = pydantic.Field(alias="Country", default=None)
    """
    Country of a physical address
    """
    invoice_address_type: typing.Optional[typing_extensions.Literal["FROM", "TO"]] = (
        pydantic.Field(alias="InvoiceAddressType", default=None)
    )
    """
    Indicates whether the address is defined as origin (FROM) or destination (TO)
    """
    postal_code: typing.Optional[str] = pydantic.Field(alias="PostalCode", default=None)
    """
    Postal code of a physical address
    """
    region: typing.Optional[str] = pydantic.Field(alias="Region", default=None)
    """
    Region or state of a physical address
    """
