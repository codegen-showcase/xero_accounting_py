import pydantic
import typing
import typing_extensions

from .attachment import Attachment
from .line_item import LineItem
from .user import User
from .validation_error import ValidationError

if typing_extensions.TYPE_CHECKING:
    from .contact import Contact


class Receipt(pydantic.BaseModel):
    """
    Receipt
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
    contact: typing.Optional["Contact"] = pydantic.Field(alias="Contact", default=None)
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    """
    Date of receipt – YYYY-MM-DD
    """
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    """
    boolean to indicate if a receipt has an attachment
    """
    line_amount_types: typing.Optional[
        typing_extensions.Literal["Exclusive", "Inclusive", "NoTax"]
    ] = pydantic.Field(alias="LineAmountTypes", default=None)
    """
    Line amounts are exclusive of tax by default if you don’t specify this element. See Line Amount Types
    """
    line_items: typing.Optional[typing.List[LineItem]] = pydantic.Field(
        alias="LineItems", default=None
    )
    receipt_id: typing.Optional[str] = pydantic.Field(alias="ReceiptID", default=None)
    """
    Xero generated unique identifier for receipt
    """
    receipt_number: typing.Optional[str] = pydantic.Field(
        alias="ReceiptNumber", default=None
    )
    """
    Xero generated sequence number for receipt in current claim for a given user
    """
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    """
    Additional reference number
    """
    status: typing.Optional[
        typing_extensions.Literal[
            "AUTHORISED", "DECLINED", "DRAFT", "SUBMITTED", "VOIDED"
        ]
    ] = pydantic.Field(alias="Status", default=None)
    """
    Current status of receipt – see status types
    """
    sub_total: typing.Optional[float] = pydantic.Field(alias="SubTotal", default=None)
    """
    Total of receipt excluding taxes
    """
    total: typing.Optional[float] = pydantic.Field(alias="Total", default=None)
    """
    Total of receipt tax inclusive (i.e. SubTotal + TotalTax)
    """
    total_tax: typing.Optional[float] = pydantic.Field(alias="TotalTax", default=None)
    """
    Total tax on receipt
    """
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    """
    Last modified date UTC format
    """
    url: typing.Optional[str] = pydantic.Field(alias="Url", default=None)
    """
    URL link to a source document – shown as “Go to [appName]” in the Xero app
    """
    user: typing.Optional[User] = pydantic.Field(alias="User", default=None)
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
