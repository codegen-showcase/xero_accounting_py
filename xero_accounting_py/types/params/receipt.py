import pydantic
import typing
import typing_extensions

from .attachment import Attachment, _SerializerAttachment
from .line_item import LineItem, _SerializerLineItem
from .user import User, _SerializerUser
from .validation_error import ValidationError, _SerializerValidationError

if typing_extensions.TYPE_CHECKING:
    from .contact import Contact, _SerializerContact


class Receipt(typing_extensions.TypedDict):
    """
    Receipt
    """

    attachments: typing_extensions.NotRequired[typing.List[Attachment]]
    """
    Displays array of attachments from the API
    """

    contact: typing_extensions.NotRequired["Contact"]

    date: typing_extensions.NotRequired[str]
    """
    Date of receipt – YYYY-MM-DD
    """

    has_attachments: typing_extensions.NotRequired[bool]
    """
    boolean to indicate if a receipt has an attachment
    """

    line_amount_types: typing_extensions.NotRequired[
        typing_extensions.Literal["Exclusive", "Inclusive", "NoTax"]
    ]
    """
    Line amounts are exclusive of tax by default if you don’t specify this element. See Line Amount Types
    """

    line_items: typing_extensions.NotRequired[typing.List[LineItem]]

    receipt_id: typing_extensions.NotRequired[str]
    """
    Xero generated unique identifier for receipt
    """

    receipt_number: typing_extensions.NotRequired[str]
    """
    Xero generated sequence number for receipt in current claim for a given user
    """

    reference: typing_extensions.NotRequired[str]
    """
    Additional reference number
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "AUTHORISED", "DECLINED", "DRAFT", "SUBMITTED", "VOIDED"
        ]
    ]
    """
    Current status of receipt – see status types
    """

    sub_total: typing_extensions.NotRequired[float]
    """
    Total of receipt excluding taxes
    """

    total: typing_extensions.NotRequired[float]
    """
    Total of receipt tax inclusive (i.e. SubTotal + TotalTax)
    """

    total_tax: typing_extensions.NotRequired[float]
    """
    Total tax on receipt
    """

    updated_date_utc: typing_extensions.NotRequired[str]
    """
    Last modified date UTC format
    """

    url: typing_extensions.NotRequired[str]
    """
    URL link to a source document – shown as “Go to [appName]” in the Xero app
    """

    user: typing_extensions.NotRequired[User]

    validation_errors: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of validation error messages from the API
    """

    warnings: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of warning messages from the API
    """


class _SerializerReceipt(pydantic.BaseModel):
    """
    Serializer for Receipt handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attachments: typing.Optional[typing.List[_SerializerAttachment]] = pydantic.Field(
        alias="Attachments", default=None
    )
    contact: typing.Optional["_SerializerContact"] = pydantic.Field(
        alias="Contact", default=None
    )
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    line_amount_types: typing.Optional[
        typing_extensions.Literal["Exclusive", "Inclusive", "NoTax"]
    ] = pydantic.Field(alias="LineAmountTypes", default=None)
    line_items: typing.Optional[typing.List[_SerializerLineItem]] = pydantic.Field(
        alias="LineItems", default=None
    )
    receipt_id: typing.Optional[str] = pydantic.Field(alias="ReceiptID", default=None)
    receipt_number: typing.Optional[str] = pydantic.Field(
        alias="ReceiptNumber", default=None
    )
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    status: typing.Optional[
        typing_extensions.Literal[
            "AUTHORISED", "DECLINED", "DRAFT", "SUBMITTED", "VOIDED"
        ]
    ] = pydantic.Field(alias="Status", default=None)
    sub_total: typing.Optional[float] = pydantic.Field(alias="SubTotal", default=None)
    total: typing.Optional[float] = pydantic.Field(alias="Total", default=None)
    total_tax: typing.Optional[float] = pydantic.Field(alias="TotalTax", default=None)
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    url: typing.Optional[str] = pydantic.Field(alias="Url", default=None)
    user: typing.Optional[_SerializerUser] = pydantic.Field(alias="User", default=None)
    validation_errors: typing.Optional[typing.List[_SerializerValidationError]] = (
        pydantic.Field(alias="ValidationErrors", default=None)
    )
    warnings: typing.Optional[typing.List[_SerializerValidationError]] = pydantic.Field(
        alias="Warnings", default=None
    )
