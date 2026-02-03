import pydantic
import typing


class BatchPaymentDetails(pydantic.BaseModel):
    """
    Bank details for use on a batch payment stored with each contact
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank_account_name: typing.Optional[str] = pydantic.Field(
        alias="BankAccountName", default=None
    )
    """
    Name of bank for use with Batch Payments
    """
    bank_account_number: typing.Optional[str] = pydantic.Field(
        alias="BankAccountNumber", default=None
    )
    """
    Bank account number for use with Batch Payments
    """
    code: typing.Optional[str] = pydantic.Field(alias="Code", default=None)
    """
    (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.
    """
    details: typing.Optional[str] = pydantic.Field(alias="Details", default=None)
    """
    (Non-NZ Only) These details are sent to the org’s bank as a reference for the batch payment transaction. They will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement imported into Xero. Maximum field length = 18
    """
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    """
    (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.
    """
