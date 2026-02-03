import pydantic
import typing
import typing_extensions

from .journal_line import JournalLine


class Journal(pydantic.BaseModel):
    """
    Journal
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_date_utc: typing.Optional[str] = pydantic.Field(
        alias="CreatedDateUTC", default=None
    )
    """
    Created date UTC format
    """
    journal_date: typing.Optional[str] = pydantic.Field(
        alias="JournalDate", default=None
    )
    """
    Date the journal was posted
    """
    journal_id: typing.Optional[str] = pydantic.Field(alias="JournalID", default=None)
    """
    Xero identifier
    """
    journal_lines: typing.Optional[typing.List[JournalLine]] = pydantic.Field(
        alias="JournalLines", default=None
    )
    """
    See JournalLines
    """
    journal_number: typing.Optional[int] = pydantic.Field(
        alias="JournalNumber", default=None
    )
    """
    Xero generated journal number
    """
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    """
    reference field for additional indetifying information
    """
    source_id: typing.Optional[str] = pydantic.Field(alias="SourceID", default=None)
    """
    The identifier for the source transaction (e.g. InvoiceID)
    """
    source_type: typing.Optional[
        typing_extensions.Literal[
            "ACCPAY",
            "ACCPAYCREDIT",
            "ACCPAYPAYMENT",
            "ACCREC",
            "ACCRECCREDIT",
            "ACCRECPAYMENT",
            "APCREDITPAYMENT",
            "APOVERPAYMENT",
            "APPREPAYMENT",
            "ARCREDITPAYMENT",
            "AROVERPAYMENT",
            "ARPREPAYMENT",
            "CASHPAID",
            "CASHREC",
            "EXPCLAIM",
            "EXPPAYMENT",
            "EXTERNALSPENDMONEY",
            "INTEGRATEDPAYROLLCN",
            "INTEGRATEDPAYROLLPE",
            "INTEGRATEDPAYROLLPT",
            "INTEGRATEDPAYROLLPTPAYMENT",
            "MANJOURNAL",
            "PAYSLIP",
            "TRANSFER",
            "WAGEPAYABLE",
        ]
    ] = pydantic.Field(alias="SourceType", default=None)
    """
    The journal source type. The type of transaction that created the journal
    """
