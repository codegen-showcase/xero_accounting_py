import pydantic
import typing
import typing_extensions

from .account import Account, _SerializerAccount
from .validation_error import ValidationError, _SerializerValidationError


class BankTransfer(typing_extensions.TypedDict):
    """
    BankTransfer
    """

    amount: typing_extensions.Required[float]
    """
    amount of the transaction
    """

    bank_transfer_id: typing_extensions.NotRequired[str]
    """
    The identifier of the Bank Transfer
    """

    created_date_utc: typing_extensions.NotRequired[str]
    """
    UTC timestamp of creation date of bank transfer
    """

    currency_rate: typing_extensions.NotRequired[float]
    """
    The currency rate
    """

    date: typing_extensions.NotRequired[str]
    """
    The date of the Transfer YYYY-MM-DD
    """

    from_bank_account: typing_extensions.Required[Account]

    from_bank_transaction_id: typing_extensions.NotRequired[str]
    """
    The Bank Transaction ID for the source account
    """

    from_is_reconciled: typing_extensions.NotRequired[bool]
    """
    The Bank Transaction boolean to show if it is reconciled for the source account
    """

    has_attachments: typing_extensions.NotRequired[bool]
    """
    Boolean to indicate if a Bank Transfer has an attachment
    """

    reference: typing_extensions.NotRequired[str]
    """
    Reference for the transactions.
    """

    to_bank_account: typing_extensions.Required[Account]

    to_bank_transaction_id: typing_extensions.NotRequired[str]
    """
    The Bank Transaction ID for the destination account
    """

    to_is_reconciled: typing_extensions.NotRequired[bool]
    """
    The Bank Transaction boolean to show if it is reconciled for the destination account
    """

    validation_errors: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of validation error messages from the API
    """


class _SerializerBankTransfer(pydantic.BaseModel):
    """
    Serializer for BankTransfer handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: float = pydantic.Field(
        alias="Amount",
    )
    bank_transfer_id: typing.Optional[str] = pydantic.Field(
        alias="BankTransferID", default=None
    )
    created_date_utc: typing.Optional[str] = pydantic.Field(
        alias="CreatedDateUTC", default=None
    )
    currency_rate: typing.Optional[float] = pydantic.Field(
        alias="CurrencyRate", default=None
    )
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    from_bank_account: _SerializerAccount = pydantic.Field(
        alias="FromBankAccount",
    )
    from_bank_transaction_id: typing.Optional[str] = pydantic.Field(
        alias="FromBankTransactionID", default=None
    )
    from_is_reconciled: typing.Optional[bool] = pydantic.Field(
        alias="FromIsReconciled", default=None
    )
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    to_bank_account: _SerializerAccount = pydantic.Field(
        alias="ToBankAccount",
    )
    to_bank_transaction_id: typing.Optional[str] = pydantic.Field(
        alias="ToBankTransactionID", default=None
    )
    to_is_reconciled: typing.Optional[bool] = pydantic.Field(
        alias="ToIsReconciled", default=None
    )
    validation_errors: typing.Optional[typing.List[_SerializerValidationError]] = (
        pydantic.Field(alias="ValidationErrors", default=None)
    )
