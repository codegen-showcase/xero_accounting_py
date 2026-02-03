import pydantic
import typing
import typing_extensions

from .line_item_item import LineItemItem, _SerializerLineItemItem
from .line_item_tracking1 import LineItemTracking1, _SerializerLineItemTracking1
from .tax_breakdown_component import (
    TaxBreakdownComponent,
    _SerializerTaxBreakdownComponent,
)


class LineItem(typing_extensions.TypedDict):
    """
    LineItem
    """

    account_code: typing_extensions.NotRequired[str]
    """
    See Accounts
    """

    account_id: typing_extensions.NotRequired[str]
    """
    The associated account ID related to this line item
    """

    description: typing_extensions.NotRequired[str]
    """
    Description needs to be at least 1 char long. A line item with just a description (i.e no unit amount or quantity) can be created by specifying just a <Description> element that contains at least 1 character
    """

    discount_amount: typing_extensions.NotRequired[float]
    """
    Discount amount being applied to a line item. Only supported on ACCREC invoices and quotes. ACCPAY invoices and credit notes in Xero do not support discounts.
    """

    discount_rate: typing_extensions.NotRequired[float]
    """
    Percentage discount being applied to a line item (only supported on  ACCREC invoices – ACC PAY invoices and credit notes in Xero do not support discounts
    """

    item: typing_extensions.NotRequired[LineItemItem]

    item_code: typing_extensions.NotRequired[str]
    """
    See Items
    """

    line_amount: typing_extensions.NotRequired[float]
    """
    If you wish to omit either the Quantity or UnitAmount you can provide a LineAmount and Xero will calculate the missing amount for you. The line amount reflects the discounted price if either a DiscountRate or DiscountAmount has been used i.e. LineAmount = Quantity * Unit Amount * ((100 - DiscountRate)/100) or LineAmount = (Quantity * UnitAmount) - DiscountAmount
    """

    line_item_id: typing_extensions.NotRequired[str]
    """
    LineItem unique ID
    """

    quantity: typing_extensions.NotRequired[float]
    """
    LineItem Quantity
    """

    repeating_invoice_id: typing_extensions.NotRequired[str]
    """
    The Xero identifier for a Repeating Invoice
    """

    sales_tax_code_id: typing_extensions.NotRequired[float]
    """
    The ID of the sales tax code
    """

    tax_amount: typing_extensions.NotRequired[float]
    """
    The tax amount is auto calculated as a percentage of the line amount (see below) based on the tax rate. This value can be overriden if the calculated <TaxAmount> is not correct.
    """

    tax_breakdown: typing_extensions.NotRequired[typing.List[TaxBreakdownComponent]]
    """
    An array of tax components defined for this line item
    """

    tax_type: typing_extensions.NotRequired[str]
    """
    The tax type from TaxRates
    """

    taxability: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "EXEMPT", "NON_TAXABLE", "NOT_APPLICABLE", "PART_TAXABLE", "TAXABLE"
        ]
    ]
    """
    The type of taxability
    """

    tracking: typing_extensions.NotRequired[typing.List[LineItemTracking1]]
    """
    Optional Tracking Category – see Tracking.  Any LineItem can have a  maximum of 2 <TrackingCategory> elements.
    """

    unit_amount: typing_extensions.NotRequired[float]
    """
    LineItem Unit Amount
    """


class _SerializerLineItem(pydantic.BaseModel):
    """
    Serializer for LineItem handling case conversions
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
    discount_amount: typing.Optional[float] = pydantic.Field(
        alias="DiscountAmount", default=None
    )
    discount_rate: typing.Optional[float] = pydantic.Field(
        alias="DiscountRate", default=None
    )
    item: typing.Optional[_SerializerLineItemItem] = pydantic.Field(
        alias="Item", default=None
    )
    item_code: typing.Optional[str] = pydantic.Field(alias="ItemCode", default=None)
    line_amount: typing.Optional[float] = pydantic.Field(
        alias="LineAmount", default=None
    )
    line_item_id: typing.Optional[str] = pydantic.Field(
        alias="LineItemID", default=None
    )
    quantity: typing.Optional[float] = pydantic.Field(alias="Quantity", default=None)
    repeating_invoice_id: typing.Optional[str] = pydantic.Field(
        alias="RepeatingInvoiceID", default=None
    )
    sales_tax_code_id: typing.Optional[float] = pydantic.Field(
        alias="SalesTaxCodeId", default=None
    )
    tax_amount: typing.Optional[float] = pydantic.Field(alias="TaxAmount", default=None)
    tax_breakdown: typing.Optional[typing.List[_SerializerTaxBreakdownComponent]] = (
        pydantic.Field(alias="TaxBreakdown", default=None)
    )
    tax_type: typing.Optional[str] = pydantic.Field(alias="TaxType", default=None)
    taxability: typing.Optional[
        typing_extensions.Literal[
            "EXEMPT", "NON_TAXABLE", "NOT_APPLICABLE", "PART_TAXABLE", "TAXABLE"
        ]
    ] = pydantic.Field(alias="Taxability", default=None)
    tracking: typing.Optional[typing.List[_SerializerLineItemTracking1]] = (
        pydantic.Field(alias="Tracking", default=None)
    )
    unit_amount: typing.Optional[float] = pydantic.Field(
        alias="UnitAmount", default=None
    )
