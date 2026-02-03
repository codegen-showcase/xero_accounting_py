import pydantic
import typing
import typing_extensions

from .attachment import Attachment, _SerializerAttachment
from .manual_journal_line import ManualJournalLine, _SerializerManualJournalLine
from .validation_error import ValidationError, _SerializerValidationError


class ManualJournal(typing_extensions.TypedDict):
    """
    ManualJournal
    """

    attachments: typing_extensions.NotRequired[typing.List[Attachment]]
    """
    Displays array of attachments from the API
    """

    date: typing_extensions.NotRequired[str]
    """
    Date journal was posted – YYYY-MM-DD
    """

    has_attachments: typing_extensions.NotRequired[bool]
    """
    Boolean to indicate if a manual journal has an attachment
    """

    journal_lines: typing_extensions.NotRequired[typing.List[ManualJournalLine]]
    """
    See JournalLines
    """

    line_amount_types: typing_extensions.NotRequired[
        typing_extensions.Literal["Exclusive", "Inclusive", "NoTax"]
    ]
    """
    Line amounts are exclusive of tax by default if you don’t specify this element. See Line Amount Types
    """

    manual_journal_id: typing_extensions.NotRequired[str]
    """
    The Xero identifier for a Manual Journal
    """

    narration: typing_extensions.Required[str]
    """
    Description of journal being posted
    """

    show_on_cash_basis_reports: typing_extensions.NotRequired[bool]
    """
    Boolean – default is true if not specified
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["ARCHIVED", "DELETED", "DRAFT", "POSTED", "VOIDED"]
    ]
    """
    See Manual Journal Status Codes
    """

    status_attribute_string: typing_extensions.NotRequired[str]
    """
    A string to indicate if a invoice status
    """

    updated_date_utc: typing_extensions.NotRequired[str]
    """
    Last modified date UTC format
    """

    url: typing_extensions.NotRequired[str]
    """
    Url link to a source document – shown as “Go to [appName]” in the Xero app
    """

    validation_errors: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of validation error messages from the API
    """

    warnings: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of warning messages from the API
    """


class _SerializerManualJournal(pydantic.BaseModel):
    """
    Serializer for ManualJournal handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attachments: typing.Optional[typing.List[_SerializerAttachment]] = pydantic.Field(
        alias="Attachments", default=None
    )
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    journal_lines: typing.Optional[typing.List[_SerializerManualJournalLine]] = (
        pydantic.Field(alias="JournalLines", default=None)
    )
    line_amount_types: typing.Optional[
        typing_extensions.Literal["Exclusive", "Inclusive", "NoTax"]
    ] = pydantic.Field(alias="LineAmountTypes", default=None)
    manual_journal_id: typing.Optional[str] = pydantic.Field(
        alias="ManualJournalID", default=None
    )
    narration: str = pydantic.Field(
        alias="Narration",
    )
    show_on_cash_basis_reports: typing.Optional[bool] = pydantic.Field(
        alias="ShowOnCashBasisReports", default=None
    )
    status: typing.Optional[
        typing_extensions.Literal["ARCHIVED", "DELETED", "DRAFT", "POSTED", "VOIDED"]
    ] = pydantic.Field(alias="Status", default=None)
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    url: typing.Optional[str] = pydantic.Field(alias="Url", default=None)
    validation_errors: typing.Optional[typing.List[_SerializerValidationError]] = (
        pydantic.Field(alias="ValidationErrors", default=None)
    )
    warnings: typing.Optional[typing.List[_SerializerValidationError]] = pydantic.Field(
        alias="Warnings", default=None
    )
