import pydantic
import typing
import typing_extensions

from .validation_error import ValidationError


class LinkedTransaction(pydantic.BaseModel):
    """
    LinkedTransaction
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    contact_id: typing.Optional[str] = pydantic.Field(alias="ContactID", default=None)
    """
    Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID=4bb34b03-3378-4bb2-a0ed-6345abf3224e&Status=APPROVED.
    """
    linked_transaction_id: typing.Optional[str] = pydantic.Field(
        alias="LinkedTransactionID", default=None
    )
    """
    The Xero identifier for an Linked Transaction e.g./LinkedTransactions/297c2dc5-cc47-4afd-8ec8-74990b8761e9
    """
    source_line_item_id: typing.Optional[str] = pydantic.Field(
        alias="SourceLineItemID", default=None
    )
    """
    The line item identifier from the source transaction.
    """
    source_transaction_id: typing.Optional[str] = pydantic.Field(
        alias="SourceTransactionID", default=None
    )
    """
    Filter by the SourceTransactionID. Get all the linked transactions created from a particular ACCPAY invoice
    """
    source_transaction_type_code: typing.Optional[
        typing_extensions.Literal["ACCPAY", "SPEND"]
    ] = pydantic.Field(alias="SourceTransactionTypeCode", default=None)
    """
    The Type of the source tranasction. This will be ACCPAY if the linked transaction was created from an invoice and SPEND if it was created from a bank transaction.
    """
    status: typing.Optional[
        typing_extensions.Literal["APPROVED", "BILLED", "DRAFT", "ONDRAFT", "VOIDED"]
    ] = pydantic.Field(alias="Status", default=None)
    """
    Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID=4bb34b03-3378-4bb2-a0ed-6345abf3224e&Status=APPROVED.
    """
    target_line_item_id: typing.Optional[str] = pydantic.Field(
        alias="TargetLineItemID", default=None
    )
    """
    The line item identifier from the target transaction. It is possible  to link multiple billable expenses to the same TargetLineItemID.
    """
    target_transaction_id: typing.Optional[str] = pydantic.Field(
        alias="TargetTransactionID", default=None
    )
    """
    Filter by the TargetTransactionID. Get all the linked transactions  allocated to a particular ACCREC invoice
    """
    type_: typing.Optional[typing_extensions.Literal["BILLABLEEXPENSE"]] = (
        pydantic.Field(alias="Type", default=None)
    )
    """
    This will always be BILLABLEEXPENSE. More types may be added in future.
    """
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    """
    The last modified date in UTC format
    """
    validation_errors: typing.Optional[typing.List[ValidationError]] = pydantic.Field(
        alias="ValidationErrors", default=None
    )
    """
    Displays array of validation error messages from the API
    """
