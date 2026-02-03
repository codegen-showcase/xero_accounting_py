import pydantic
import typing

from .tracking_category import TrackingCategory


class ManualJournalLine(pydantic.BaseModel):
    """
    ManualJournalLine
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_code: typing.Optional[str] = pydantic.Field(
        alias="AccountCode", default=None
    )
    """
    See Accounts
    """
    account_id: typing.Optional[str] = pydantic.Field(alias="AccountID", default=None)
    """
    See Accounts
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="Description", default=None
    )
    """
    Description for journal line
    """
    is_blank: typing.Optional[bool] = pydantic.Field(alias="IsBlank", default=None)
    """
    is the line blank
    """
    line_amount: typing.Optional[float] = pydantic.Field(
        alias="LineAmount", default=None
    )
    """
    total for line. Debits are positive, credits are negative value
    """
    tax_amount: typing.Optional[float] = pydantic.Field(alias="TaxAmount", default=None)
    """
    The calculated tax amount based on the TaxType and LineAmount
    """
    tax_type: typing.Optional[str] = pydantic.Field(alias="TaxType", default=None)
    """
    The tax type from TaxRates
    """
    tracking: typing.Optional[typing.List[TrackingCategory]] = pydantic.Field(
        alias="Tracking", default=None
    )
    """
    Optional Tracking Category – see Tracking. Any JournalLine can have a maximum of 2 <TrackingCategory> elements.
    """
