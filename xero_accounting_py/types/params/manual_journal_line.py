import pydantic
import typing
import typing_extensions

from .tracking_category import TrackingCategory, _SerializerTrackingCategory


class ManualJournalLine(typing_extensions.TypedDict):
    """
    ManualJournalLine
    """

    account_code: typing_extensions.NotRequired[str]
    """
    See Accounts
    """

    account_id: typing_extensions.NotRequired[str]
    """
    See Accounts
    """

    description: typing_extensions.NotRequired[str]
    """
    Description for journal line
    """

    is_blank: typing_extensions.NotRequired[bool]
    """
    is the line blank
    """

    line_amount: typing_extensions.NotRequired[float]
    """
    total for line. Debits are positive, credits are negative value
    """

    tax_amount: typing_extensions.NotRequired[float]
    """
    The calculated tax amount based on the TaxType and LineAmount
    """

    tax_type: typing_extensions.NotRequired[str]
    """
    The tax type from TaxRates
    """

    tracking: typing_extensions.NotRequired[typing.List[TrackingCategory]]
    """
    Optional Tracking Category – see Tracking. Any JournalLine can have a maximum of 2 <TrackingCategory> elements.
    """


class _SerializerManualJournalLine(pydantic.BaseModel):
    """
    Serializer for ManualJournalLine handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_code: typing.Optional[str] = pydantic.Field(
        alias="AccountCode", default=None
    )
    account_id: typing.Optional[str] = pydantic.Field(alias="AccountID", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="Description", default=None
    )
    is_blank: typing.Optional[bool] = pydantic.Field(alias="IsBlank", default=None)
    line_amount: typing.Optional[float] = pydantic.Field(
        alias="LineAmount", default=None
    )
    tax_amount: typing.Optional[float] = pydantic.Field(alias="TaxAmount", default=None)
    tax_type: typing.Optional[str] = pydantic.Field(alias="TaxType", default=None)
    tracking: typing.Optional[typing.List[_SerializerTrackingCategory]] = (
        pydantic.Field(alias="Tracking", default=None)
    )
