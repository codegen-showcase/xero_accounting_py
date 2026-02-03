import pydantic
import typing


class TaxComponent(pydantic.BaseModel):
    """
    TaxComponent
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    is_compound: typing.Optional[bool] = pydantic.Field(
        alias="IsCompound", default=None
    )
    """
    Boolean to describe if Tax rate is compounded.
    """
    is_non_recoverable: typing.Optional[bool] = pydantic.Field(
        alias="IsNonRecoverable", default=None
    )
    """
    Boolean to describe if tax rate is non-recoverable. Non-recoverable rates are only applicable to Canadian organisations
    """
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    """
    Name of Tax Component
    """
    rate: typing.Optional[float] = pydantic.Field(alias="Rate", default=None)
    """
    Tax Rate (up to 4dp)
    """
