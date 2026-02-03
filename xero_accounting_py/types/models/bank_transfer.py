import pydantic
import typing

from .account import Account
from .validation_error import ValidationError


class BankTransfer(pydantic.BaseModel):
    """
    BankTransfer
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: float = pydantic.Field(
        alias="Amount",
    )
    """
    amount of the transaction
    """
    bank_transfer_id: typing.Optional[str] = pydantic.Field(
        alias="BankTransferID", default=None
    )
    """
    The identifier of the Bank Transfer
    """
    created_date_utc: typing.Optional[str] = pydantic.Field(
        alias="CreatedDateUTC", default=None
    )
    """
    UTC timestamp of creation date of bank transfer
    """
    currency_rate: typing.Optional[float] = pydantic.Field(
        alias="CurrencyRate", default=None
    )
    """
    The currency rate
    """
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    """
    The date of the Transfer YYYY-MM-DD
    """
    from_bank_account: Account = pydantic.Field(
        alias="FromBankAccount",
    )
    from_bank_transaction_id: typing.Optional[str] = pydantic.Field(
        alias="FromBankTransactionID", default=None
    )
    """
    The Bank Transaction ID for the source account
    """
    from_is_reconciled: typing.Optional[bool] = pydantic.Field(
        alias="FromIsReconciled", default=None
    )
    """
    The Bank Transaction boolean to show if it is reconciled for the source account
    """
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    """
    Boolean to indicate if a Bank Transfer has an attachment
    """
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    """
    Reference for the transactions.
    """
    to_bank_account: Account = pydantic.Field(
        alias="ToBankAccount",
    )
    to_bank_transaction_id: typing.Optional[str] = pydantic.Field(
        alias="ToBankTransactionID", default=None
    )
    """
    The Bank Transaction ID for the destination account
    """
    to_is_reconciled: typing.Optional[bool] = pydantic.Field(
        alias="ToIsReconciled", default=None
    )
    """
    The Bank Transaction boolean to show if it is reconciled for the destination account
    """
    validation_errors: typing.Optional[typing.List[ValidationError]] = pydantic.Field(
        alias="ValidationErrors", default=None
    )
    """
    Displays array of validation error messages from the API
    """
