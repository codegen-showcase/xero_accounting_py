import pydantic
import typing
import typing_extensions

from .tracking_category import TrackingCategory


class JournalLine(pydantic.BaseModel):
    """
    JournalLine
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
    account_name: typing.Optional[str] = pydantic.Field(
        alias="AccountName", default=None
    )
    """
    See AccountCodes
    """
    account_type: typing.Optional[
        typing_extensions.Literal[
            "BANK",
            "CURRENT",
            "CURRLIAB",
            "DEPRECIATN",
            "DIRECTCOSTS",
            "EQUITY",
            "EXPENSE",
            "FIXED",
            "INVENTORY",
            "LIABILITY",
            "NONCURRENT",
            "OTHERINCOME",
            "OVERHEADS",
            "PAYG",
            "PREPAYMENT",
            "REVENUE",
            "SALES",
            "TERMLIAB",
        ]
    ] = pydantic.Field(alias="AccountType", default=None)
    """
    See Account Types
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="Description", default=None
    )
    """
    The description from the source transaction line item. Only returned if populated.
    """
    gross_amount: typing.Optional[float] = pydantic.Field(
        alias="GrossAmount", default=None
    )
    """
    Gross amount of journal line (NetAmount + TaxAmount).
    """
    journal_line_id: typing.Optional[str] = pydantic.Field(
        alias="JournalLineID", default=None
    )
    """
    Xero identifier for Journal
    """
    net_amount: typing.Optional[float] = pydantic.Field(alias="NetAmount", default=None)
    """
    Net amount of journal line. This will be a positive value for a debit and negative for a credit
    """
    tax_amount: typing.Optional[float] = pydantic.Field(alias="TaxAmount", default=None)
    """
    Total tax on a journal line
    """
    tax_name: typing.Optional[str] = pydantic.Field(alias="TaxName", default=None)
    """
    see TaxRates
    """
    tax_type: typing.Optional[str] = pydantic.Field(alias="TaxType", default=None)
    """
    The tax type from taxRates
    """
    tracking_categories: typing.Optional[typing.List[TrackingCategory]] = (
        pydantic.Field(alias="TrackingCategories", default=None)
    )
    """
    Optional Tracking Category – see Tracking. Any JournalLine can have a maximum of 2 <TrackingCategory> elements.
    """
