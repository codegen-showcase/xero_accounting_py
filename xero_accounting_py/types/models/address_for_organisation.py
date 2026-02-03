import pydantic
import typing
import typing_extensions


class AddressForOrganisation(pydantic.BaseModel):
    """
    AddressForOrganisation
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address_line1: typing.Optional[str] = pydantic.Field(
        alias="AddressLine1", default=None
    )
    """
    max length = 500
    """
    address_line2: typing.Optional[str] = pydantic.Field(
        alias="AddressLine2", default=None
    )
    """
    max length = 500
    """
    address_line3: typing.Optional[str] = pydantic.Field(
        alias="AddressLine3", default=None
    )
    """
    max length = 500
    """
    address_line4: typing.Optional[str] = pydantic.Field(
        alias="AddressLine4", default=None
    )
    """
    max length = 500
    """
    address_type: typing.Optional[
        typing_extensions.Literal["DELIVERY", "POBOX", "STREET"]
    ] = pydantic.Field(alias="AddressType", default=None)
    """
    define the type of address
    """
    attention_to: typing.Optional[str] = pydantic.Field(
        alias="AttentionTo", default=None
    )
    """
    max length = 255
    """
    city: typing.Optional[str] = pydantic.Field(alias="City", default=None)
    """
    max length = 255
    """
    country: typing.Optional[str] = pydantic.Field(alias="Country", default=None)
    """
    max length = 50, [A-Z], [a-z] only
    """
    postal_code: typing.Optional[str] = pydantic.Field(alias="PostalCode", default=None)
    """
    max length = 50
    """
    region: typing.Optional[str] = pydantic.Field(alias="Region", default=None)
    """
    max length = 255
    """
