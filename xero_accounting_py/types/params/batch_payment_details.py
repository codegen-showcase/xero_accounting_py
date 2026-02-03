import pydantic
import typing
import typing_extensions


class BatchPaymentDetails(typing_extensions.TypedDict):
    """
    Bank details for use on a batch payment stored with each contact
    """

    bank_account_name: typing_extensions.NotRequired[str]
    """
    Name of bank for use with Batch Payments
    """

    bank_account_number: typing_extensions.NotRequired[str]
    """
    Bank account number for use with Batch Payments
    """

    code: typing_extensions.NotRequired[str]
    """
    (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.
    """

    details: typing_extensions.NotRequired[str]
    """
    (Non-NZ Only) These details are sent to the org’s bank as a reference for the batch payment transaction. They will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement imported into Xero. Maximum field length = 18
    """

    reference: typing_extensions.NotRequired[str]
    """
    (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.
    """


class _SerializerBatchPaymentDetails(pydantic.BaseModel):
    """
    Serializer for BatchPaymentDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_account_name: typing.Optional[str] = pydantic.Field(
        alias="BankAccountName", default=None
    )
    bank_account_number: typing.Optional[str] = pydantic.Field(
        alias="BankAccountNumber", default=None
    )
    code: typing.Optional[str] = pydantic.Field(alias="Code", default=None)
    details: typing.Optional[str] = pydantic.Field(alias="Details", default=None)
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
