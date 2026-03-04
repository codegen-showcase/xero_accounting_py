import pydantic
import typing
import typing_extensions

from .amount import Amount


class Project(pydantic.BaseModel):
    """
    Project
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    contact_id: typing.Optional[str] = pydantic.Field(alias="contactId", default=None)
    """
    Identifier of the contact this project was created for.
    """
    credit_note_amount: typing.Optional[Amount] = pydantic.Field(
        alias="creditNoteAmount", default=None
    )
    currency_code: typing.Optional[
        typing_extensions.Literal[
            "AED",
            "AFN",
            "ALL",
            "AMD",
            "ANG",
            "AOA",
            "ARS",
            "AUD",
            "AWG",
            "AZN",
            "BAM",
            "BBD",
            "BDT",
            "BGN",
            "BHD",
            "BIF",
            "BMD",
            "BND",
            "BOB",
            "BRL",
            "BSD",
            "BTN",
            "BWP",
            "BYN",
            "BZD",
            "CAD",
            "CDF",
            "CHF",
            "CLP",
            "CNY",
            "COP",
            "CRC",
            "CUC",
            "CUP",
            "CVE",
            "CZK",
            "DJF",
            "DKK",
            "DOP",
            "DZD",
            "EGP",
            "ERN",
            "ETB",
            "EUR",
            "FJD",
            "FKP",
            "GBP",
            "GEL",
            "GGP",
            "GHS",
            "GIP",
            "GMD",
            "GNF",
            "GTQ",
            "GYD",
            "HKD",
            "HNL",
            "HRK",
            "HTG",
            "HUF",
            "IDR",
            "ILS",
            "IMP",
            "INR",
            "IQD",
            "IRR",
            "ISK",
            "JEP",
            "JMD",
            "JOD",
            "JPY",
            "KES",
            "KGS",
            "KHR",
            "KMF",
            "KPW",
            "KRW",
            "KWD",
            "KYD",
            "KZT",
            "LAK",
            "LBP",
            "LKR",
            "LRD",
            "LSL",
            "LYD",
            "MAD",
            "MDL",
            "MGA",
            "MKD",
            "MMK",
            "MNT",
            "MOP",
            "MRU",
            "MUR",
            "MVR",
            "MWK",
            "MXN",
            "MYR",
            "MZN",
            "NAD",
            "NGN",
            "NIO",
            "NOK",
            "NPR",
            "NZD",
            "OMR",
            "PAB",
            "PEN",
            "PGK",
            "PHP",
            "PKR",
            "PLN",
            "PYG",
            "QAR",
            "RON",
            "RSD",
            "RUB",
            "RWF",
            "SAR",
            "SBD",
            "SCR",
            "SDG",
            "SEK",
            "SGD",
            "SHP",
            "SLL",
            "SOS",
            "SPL",
            "SRD",
            "STN",
            "SVC",
            "SYP",
            "SZL",
            "THB",
            "TJS",
            "TMT",
            "TND",
            "TOP",
            "TRY",
            "TTD",
            "TVD",
            "TWD",
            "TZS",
            "UAH",
            "UGX",
            "USD",
            "UYU",
            "UZS",
            "VEF",
            "VND",
            "VUV",
            "WST",
            "XAF",
            "XCD",
            "XDR",
            "XOF",
            "XPF",
            "YER",
            "ZAR",
            "ZMK",
            "ZMW",
            "ZWD",
        ]
    ] = pydantic.Field(alias="currencyCode", default=None)
    """
    3 letter alpha code for the ISO-4217 currency code, e.g. USD, AUD.
    """
    deadline_utc: typing.Optional[str] = pydantic.Field(
        alias="deadlineUtc", default=None
    )
    """
    Deadline for the project. UTC Date Time in ISO-8601 format.
    """
    deposit: typing.Optional[Amount] = pydantic.Field(alias="deposit", default=None)
    deposit_applied: typing.Optional[Amount] = pydantic.Field(
        alias="depositApplied", default=None
    )
    estimate: typing.Optional[Amount] = pydantic.Field(alias="estimate", default=None)
    estimate_amount: typing.Optional[Amount] = pydantic.Field(
        alias="estimateAmount", default=None
    )
    expense_amount_invoiced: typing.Optional[Amount] = pydantic.Field(
        alias="expenseAmountInvoiced", default=None
    )
    expense_amount_to_be_invoiced: typing.Optional[Amount] = pydantic.Field(
        alias="expenseAmountToBeInvoiced", default=None
    )
    minutes_logged: typing.Optional[int] = pydantic.Field(
        alias="minutesLogged", default=None
    )
    """
    A total of minutes logged against all tasks on the Project.
    """
    minutes_to_be_invoiced: typing.Optional[int] = pydantic.Field(
        alias="minutesToBeInvoiced", default=None
    )
    """
    Minutes which have not been invoiced across all chargeable tasks in the project.
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    Name of the project.
    """
    project_amount_invoiced: typing.Optional[Amount] = pydantic.Field(
        alias="projectAmountInvoiced", default=None
    )
    project_id: typing.Optional[str] = pydantic.Field(alias="projectId", default=None)
    """
    Identifier of the project.
    """
    status: typing.Optional[typing_extensions.Literal["CLOSED", "INPROGRESS"]] = (
        pydantic.Field(alias="status", default=None)
    )
    """
    Status for project
    """
    task_amount_invoiced: typing.Optional[Amount] = pydantic.Field(
        alias="taskAmountInvoiced", default=None
    )
    task_amount_to_be_invoiced: typing.Optional[Amount] = pydantic.Field(
        alias="taskAmountToBeInvoiced", default=None
    )
    total_expense_amount: typing.Optional[Amount] = pydantic.Field(
        alias="totalExpenseAmount", default=None
    )
    total_invoiced: typing.Optional[Amount] = pydantic.Field(
        alias="totalInvoiced", default=None
    )
    total_task_amount: typing.Optional[Amount] = pydantic.Field(
        alias="totalTaskAmount", default=None
    )
    total_to_be_invoiced: typing.Optional[Amount] = pydantic.Field(
        alias="totalToBeInvoiced", default=None
    )
