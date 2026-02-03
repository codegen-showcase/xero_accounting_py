import pydantic
import typing
import typing_extensions

from .line_item_item import LineItemItem
from .line_item_tracking1 import LineItemTracking1
from .tax_breakdown_component import TaxBreakdownComponent


class LineItem(pydantic.BaseModel):
    """
    LineItem
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
    The associated account ID related to this line item
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="Description", default=None
    )
    """
    Description needs to be at least 1 char long. A line item with just a description (i.e no unit amount or quantity) can be created by specifying just a <Description> element that contains at least 1 character
    """
    discount_amount: typing.Optional[float] = pydantic.Field(
        alias="DiscountAmount", default=None
    )
    """
    Discount amount being applied to a line item. Only supported on ACCREC invoices and quotes. ACCPAY invoices and credit notes in Xero do not support discounts.
    """
    discount_rate: typing.Optional[float] = pydantic.Field(
        alias="DiscountRate", default=None
    )
    """
    Percentage discount being applied to a line item (only supported on  ACCREC invoices – ACC PAY invoices and credit notes in Xero do not support discounts
    """
    item: typing.Optional[LineItemItem] = pydantic.Field(alias="Item", default=None)
    item_code: typing.Optional[str] = pydantic.Field(alias="ItemCode", default=None)
    """
    See Items
    """
    line_amount: typing.Optional[float] = pydantic.Field(
        alias="LineAmount", default=None
    )
    """
    If you wish to omit either the Quantity or UnitAmount you can provide a LineAmount and Xero will calculate the missing amount for you. The line amount reflects the discounted price if either a DiscountRate or DiscountAmount has been used i.e. LineAmount = Quantity * Unit Amount * ((100 - DiscountRate)/100) or LineAmount = (Quantity * UnitAmount) - DiscountAmount
    """
    line_item_id: typing.Optional[str] = pydantic.Field(
        alias="LineItemID", default=None
    )
    """
    LineItem unique ID
    """
    quantity: typing.Optional[float] = pydantic.Field(alias="Quantity", default=None)
    """
    LineItem Quantity
    """
    repeating_invoice_id: typing.Optional[str] = pydantic.Field(
        alias="RepeatingInvoiceID", default=None
    )
    """
    The Xero identifier for a Repeating Invoice
    """
    sales_tax_code_id: typing.Optional[float] = pydantic.Field(
        alias="SalesTaxCodeId", default=None
    )
    """
    The ID of the sales tax code
    """
    tax_amount: typing.Optional[float] = pydantic.Field(alias="TaxAmount", default=None)
    """
    The tax amount is auto calculated as a percentage of the line amount (see below) based on the tax rate. This value can be overriden if the calculated <TaxAmount> is not correct.
    """
    tax_breakdown: typing.Optional[typing.List[TaxBreakdownComponent]] = pydantic.Field(
        alias="TaxBreakdown", default=None
    )
    """
    An array of tax components defined for this line item
    """
    tax_type: typing.Optional[str] = pydantic.Field(alias="TaxType", default=None)
    """
    The tax type from TaxRates
    """
    taxability: typing.Optional[
        typing_extensions.Literal[
            "EXEMPT", "NON_TAXABLE", "NOT_APPLICABLE", "PART_TAXABLE", "TAXABLE"
        ]
    ] = pydantic.Field(alias="Taxability", default=None)
    """
    The type of taxability
    """
    tracking: typing.Optional[typing.List[LineItemTracking1]] = pydantic.Field(
        alias="Tracking", default=None
    )
    """
    Optional Tracking Category – see Tracking.  Any LineItem can have a  maximum of 2 <TrackingCategory> elements.
    """
    unit_amount: typing.Optional[float] = pydantic.Field(
        alias="UnitAmount", default=None
    )
    """
    LineItem Unit Amount
    """
