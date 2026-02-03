import pydantic
import typing
import typing_extensions

from .validation_error import ValidationError, _SerializerValidationError


class LinkedTransaction(typing_extensions.TypedDict):
    """
    LinkedTransaction
    """

    contact_id: typing_extensions.NotRequired[str]
    """
    Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID=4bb34b03-3378-4bb2-a0ed-6345abf3224e&Status=APPROVED.
    """

    linked_transaction_id: typing_extensions.NotRequired[str]
    """
    The Xero identifier for an Linked Transaction e.g./LinkedTransactions/297c2dc5-cc47-4afd-8ec8-74990b8761e9
    """

    source_line_item_id: typing_extensions.NotRequired[str]
    """
    The line item identifier from the source transaction.
    """

    source_transaction_id: typing_extensions.NotRequired[str]
    """
    Filter by the SourceTransactionID. Get all the linked transactions created from a particular ACCPAY invoice
    """

    source_transaction_type_code: typing_extensions.NotRequired[
        typing_extensions.Literal["ACCPAY", "SPEND"]
    ]
    """
    The Type of the source tranasction. This will be ACCPAY if the linked transaction was created from an invoice and SPEND if it was created from a bank transaction.
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["APPROVED", "BILLED", "DRAFT", "ONDRAFT", "VOIDED"]
    ]
    """
    Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID=4bb34b03-3378-4bb2-a0ed-6345abf3224e&Status=APPROVED.
    """

    target_line_item_id: typing_extensions.NotRequired[str]
    """
    The line item identifier from the target transaction. It is possible  to link multiple billable expenses to the same TargetLineItemID.
    """

    target_transaction_id: typing_extensions.NotRequired[str]
    """
    Filter by the TargetTransactionID. Get all the linked transactions  allocated to a particular ACCREC invoice
    """

    type_: typing_extensions.NotRequired[typing_extensions.Literal["BILLABLEEXPENSE"]]
    """
    This will always be BILLABLEEXPENSE. More types may be added in future.
    """

    updated_date_utc: typing_extensions.NotRequired[str]
    """
    The last modified date in UTC format
    """

    validation_errors: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of validation error messages from the API
    """


class _SerializerLinkedTransaction(pydantic.BaseModel):
    """
    Serializer for LinkedTransaction handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    contact_id: typing.Optional[str] = pydantic.Field(alias="ContactID", default=None)
    linked_transaction_id: typing.Optional[str] = pydantic.Field(
        alias="LinkedTransactionID", default=None
    )
    source_line_item_id: typing.Optional[str] = pydantic.Field(
        alias="SourceLineItemID", default=None
    )
    source_transaction_id: typing.Optional[str] = pydantic.Field(
        alias="SourceTransactionID", default=None
    )
    source_transaction_type_code: typing.Optional[
        typing_extensions.Literal["ACCPAY", "SPEND"]
    ] = pydantic.Field(alias="SourceTransactionTypeCode", default=None)
    status: typing.Optional[
        typing_extensions.Literal["APPROVED", "BILLED", "DRAFT", "ONDRAFT", "VOIDED"]
    ] = pydantic.Field(alias="Status", default=None)
    target_line_item_id: typing.Optional[str] = pydantic.Field(
        alias="TargetLineItemID", default=None
    )
    target_transaction_id: typing.Optional[str] = pydantic.Field(
        alias="TargetTransactionID", default=None
    )
    type_: typing.Optional[typing_extensions.Literal["BILLABLEEXPENSE"]] = (
        pydantic.Field(alias="Type", default=None)
    )
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    validation_errors: typing.Optional[typing.List[_SerializerValidationError]] = (
        pydantic.Field(alias="ValidationErrors", default=None)
    )
