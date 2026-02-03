import pydantic
import typing
import typing_extensions


class TaxComponent(typing_extensions.TypedDict):
    """
    TaxComponent
    """

    is_compound: typing_extensions.NotRequired[bool]
    """
    Boolean to describe if Tax rate is compounded.
    """

    is_non_recoverable: typing_extensions.NotRequired[bool]
    """
    Boolean to describe if tax rate is non-recoverable. Non-recoverable rates are only applicable to Canadian organisations
    """

    name: typing_extensions.NotRequired[str]
    """
    Name of Tax Component
    """

    rate: typing_extensions.NotRequired[float]
    """
    Tax Rate (up to 4dp)
    """


class _SerializerTaxComponent(pydantic.BaseModel):
    """
    Serializer for TaxComponent handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    is_compound: typing.Optional[bool] = pydantic.Field(
        alias="IsCompound", default=None
    )
    is_non_recoverable: typing.Optional[bool] = pydantic.Field(
        alias="IsNonRecoverable", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    rate: typing.Optional[float] = pydantic.Field(alias="Rate", default=None)
