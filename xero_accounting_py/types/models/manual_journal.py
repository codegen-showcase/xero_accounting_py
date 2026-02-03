import pydantic
import typing
import typing_extensions

from .attachment import Attachment
from .manual_journal_line import ManualJournalLine
from .validation_error import ValidationError


class ManualJournal(pydantic.BaseModel):
    """
    ManualJournal
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attachments: typing.Optional[typing.List[Attachment]] = pydantic.Field(
        alias="Attachments", default=None
    )
    """
    Displays array of attachments from the API
    """
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    """
    Date journal was posted – YYYY-MM-DD
    """
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    """
    Boolean to indicate if a manual journal has an attachment
    """
    journal_lines: typing.Optional[typing.List[ManualJournalLine]] = pydantic.Field(
        alias="JournalLines", default=None
    )
    """
    See JournalLines
    """
    line_amount_types: typing.Optional[
        typing_extensions.Literal["Exclusive", "Inclusive", "NoTax"]
    ] = pydantic.Field(alias="LineAmountTypes", default=None)
    """
    Line amounts are exclusive of tax by default if you don’t specify this element. See Line Amount Types
    """
    manual_journal_id: typing.Optional[str] = pydantic.Field(
        alias="ManualJournalID", default=None
    )
    """
    The Xero identifier for a Manual Journal
    """
    narration: str = pydantic.Field(
        alias="Narration",
    )
    """
    Description of journal being posted
    """
    show_on_cash_basis_reports: typing.Optional[bool] = pydantic.Field(
        alias="ShowOnCashBasisReports", default=None
    )
    """
    Boolean – default is true if not specified
    """
    status: typing.Optional[
        typing_extensions.Literal["ARCHIVED", "DELETED", "DRAFT", "POSTED", "VOIDED"]
    ] = pydantic.Field(alias="Status", default=None)
    """
    See Manual Journal Status Codes
    """
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    """
    A string to indicate if a invoice status
    """
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    """
    Last modified date UTC format
    """
    url: typing.Optional[str] = pydantic.Field(alias="Url", default=None)
    """
    Url link to a source document – shown as “Go to [appName]” in the Xero app
    """
    validation_errors: typing.Optional[typing.List[ValidationError]] = pydantic.Field(
        alias="ValidationErrors", default=None
    )
    """
    Displays array of validation error messages from the API
    """
    warnings: typing.Optional[typing.List[ValidationError]] = pydantic.Field(
        alias="Warnings", default=None
    )
    """
    Displays array of warning messages from the API
    """
