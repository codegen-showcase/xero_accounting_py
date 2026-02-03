import pydantic
import typing
import typing_extensions

from .address import Address, _SerializerAddress
from .attachment import Attachment, _SerializerAttachment
from .balances import Balances, _SerializerBalances
from .batch_payment_details import BatchPaymentDetails, _SerializerBatchPaymentDetails
from .branding_theme import BrandingTheme, _SerializerBrandingTheme
from .contact_person import ContactPerson, _SerializerContactPerson
from .payment_term import PaymentTerm, _SerializerPaymentTerm
from .phone import Phone, _SerializerPhone
from .sales_tracking_category import (
    SalesTrackingCategory,
    _SerializerSalesTrackingCategory,
)
from .validation_error import ValidationError, _SerializerValidationError

if typing_extensions.TYPE_CHECKING:
    from .contact_group import ContactGroup, _SerializerContactGroup


class Contact(typing_extensions.TypedDict):
    """
    Contact
    """

    account_number: typing_extensions.NotRequired[str]
    """
    A user defined account number. This can be updated via the API and the Xero UI (max length = 50)
    """

    accounts_payable_tax_type: typing_extensions.NotRequired[str]
    """
    The tax type from TaxRates
    """

    accounts_receivable_tax_type: typing_extensions.NotRequired[str]
    """
    The tax type from TaxRates
    """

    addresses: typing_extensions.NotRequired[typing.List[Address]]
    """
    Store certain address types for a contact – see address types
    """

    attachments: typing_extensions.NotRequired[typing.List[Attachment]]
    """
    Displays array of attachments from the API
    """

    balances: typing_extensions.NotRequired[Balances]
    """
    The raw AccountsReceivable(sales invoices) and AccountsPayable(bills) outstanding and overdue amounts, not converted to base currency (read only)
    """

    bank_account_details: typing_extensions.NotRequired[str]
    """
    Bank account number of contact
    """

    batch_payments: typing_extensions.NotRequired[BatchPaymentDetails]
    """
    Bank details for use on a batch payment stored with each contact
    """

    branding_theme: typing_extensions.NotRequired[BrandingTheme]

    company_number: typing_extensions.NotRequired[str]
    """
    Company registration number (max length = 50)
    """

    contact_groups: typing_extensions.NotRequired[typing.List["ContactGroup"]]
    """
    Displays which contact groups a contact is included in
    """

    contact_id: typing_extensions.NotRequired[str]
    """
    Xero identifier
    """

    contact_number: typing_extensions.NotRequired[str]
    """
    This can be updated via the API only i.e. This field is read only on the Xero contact screen, used to identify contacts in external systems (max length = 50). If the Contact Number is used, this is displayed as Contact Code in the Contacts UI in Xero.
    """

    contact_persons: typing_extensions.NotRequired[typing.List[ContactPerson]]
    """
    See contact persons
    """

    contact_status: typing_extensions.NotRequired[
        typing_extensions.Literal["ACTIVE", "ARCHIVED", "GDPRREQUEST"]
    ]
    """
    Current status of a contact – see contact status types
    """

    default_currency: typing_extensions.NotRequired[
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
            "BYR",
            "BZD",
            "CAD",
            "CDF",
            "CHF",
            "CLF",
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
            "EEK",
            "EGP",
            "ERN",
            "ETB",
            "EUR",
            "FJD",
            "FKP",
            "GBP",
            "GEL",
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
            "INR",
            "IQD",
            "IRR",
            "ISK",
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
            "LTL",
            "LVL",
            "LYD",
            "MAD",
            "MDL",
            "MGA",
            "MKD",
            "MMK",
            "MNT",
            "MOP",
            "MRO",
            "MRU",
            "MUR",
            "MVR",
            "MWK",
            "MXN",
            "MXV",
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
            "SKK",
            "SLE",
            "SLL",
            "SOS",
            "SRD",
            "STD",
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
            "TWD",
            "TZS",
            "UAH",
            "UGX",
            "USD",
            "UYU",
            "UZS",
            "VEF",
            "VES",
            "VND",
            "VUV",
            "WST",
            "XAF",
            "XCD",
            "XOF",
            "XPF",
            "YER",
            "ZAR",
            "ZMK",
            "ZMW",
            "ZWD",
        ]
    ]
    """
    3 letter alpha code for the currency – see list of currency codes
    """

    discount: typing_extensions.NotRequired[float]
    """
    The default discount rate for the contact (read only)
    """

    email_address: typing_extensions.NotRequired[str]
    """
    Email address of contact person (umlauts not supported) (max length  = 255)
    """

    first_name: typing_extensions.NotRequired[str]
    """
    First name of contact person (max length = 255)
    """

    has_attachments: typing_extensions.NotRequired[bool]
    """
    A boolean to indicate if a contact has an attachment
    """

    has_validation_errors: typing_extensions.NotRequired[bool]
    """
    A boolean to indicate if a contact has an validation errors
    """

    is_customer: typing_extensions.NotRequired[bool]
    """
    true or false – Boolean that describes if a contact has any AR invoices entered against them. Cannot be set via PUT or POST – it is automatically set when an accounts receivable invoice is generated against this contact.
    """

    is_supplier: typing_extensions.NotRequired[bool]
    """
    true or false – Boolean that describes if a contact that has any AP  invoices entered against them. Cannot be set via PUT or POST – it is automatically set when an accounts payable invoice is generated against this contact.
    """

    last_name: typing_extensions.NotRequired[str]
    """
    Last name of contact person (max length = 255)
    """

    merged_to_contact_id: typing_extensions.NotRequired[str]
    """
    ID for the destination of a merged contact. Only returned when using paging or when fetching a contact by ContactId or ContactNumber.
    """

    name: typing_extensions.NotRequired[str]
    """
    Full name of contact/organisation (max length = 255)
    """

    payment_terms: typing_extensions.NotRequired[PaymentTerm]

    phones: typing_extensions.NotRequired[typing.List[Phone]]
    """
    Store certain phone types for a contact – see phone types
    """

    purchases_default_account_code: typing_extensions.NotRequired[str]
    """
    The default purchases account code for contacts
    """

    purchases_default_line_amount_type: typing_extensions.NotRequired[
        typing_extensions.Literal["EXCLUSIVE", "INCLUSIVE", "NONE"]
    ]
    """
    The default purchases line amount type for a contact Only available when summaryOnly parameter or paging is used, or when fetch by ContactId or ContactNumber.
    """

    purchases_tracking_categories: typing_extensions.NotRequired[
        typing.List[SalesTrackingCategory]
    ]
    """
    The default purchases tracking categories for contacts
    """

    sales_default_account_code: typing_extensions.NotRequired[str]
    """
    The default sales account code for contacts
    """

    sales_default_line_amount_type: typing_extensions.NotRequired[
        typing_extensions.Literal["EXCLUSIVE", "INCLUSIVE", "NONE"]
    ]
    """
    The default sales line amount type for a contact. Only available when summaryOnly parameter or paging is used, or when fetch by ContactId or ContactNumber.
    """

    sales_tracking_categories: typing_extensions.NotRequired[
        typing.List[SalesTrackingCategory]
    ]
    """
    The default sales tracking categories for contacts
    """

    status_attribute_string: typing_extensions.NotRequired[str]
    """
    Status of object
    """

    tax_number: typing_extensions.NotRequired[str]
    """
    Tax number of contact – this is also known as the ABN (Australia), GST Number (New Zealand), VAT Number (UK) or Tax ID Number (US and global) in the Xero UI depending on which regionalized version of Xero you are using (max length = 50)
    """

    tax_number_type: typing_extensions.NotRequired[
        typing_extensions.Literal["ATIN", "EIN", "ITIN", "SSN"]
    ]
    """
    Identifier of the regional type of tax number, such as US, UK, or other regional tax identifiers
    """

    tracking_category_name: typing_extensions.NotRequired[str]
    """
    The name of the Tracking Category assigned to the contact under SalesTrackingCategories and PurchasesTrackingCategories
    """

    tracking_category_option: typing_extensions.NotRequired[str]
    """
    The name of the Tracking Option assigned to the contact under SalesTrackingCategories and PurchasesTrackingCategories
    """

    updated_date_utc: typing_extensions.NotRequired[str]
    """
    UTC timestamp of last update to contact
    """

    validation_errors: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays validation errors returned from the API
    """

    website: typing_extensions.NotRequired[str]
    """
    Website address for contact (read only)
    """

    xero_network_key: typing_extensions.NotRequired[str]
    """
    Store XeroNetworkKey for contacts.
    """


class _SerializerContact(pydantic.BaseModel):
    """
    Serializer for Contact handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_number: typing.Optional[str] = pydantic.Field(
        alias="AccountNumber", default=None
    )
    accounts_payable_tax_type: typing.Optional[str] = pydantic.Field(
        alias="AccountsPayableTaxType", default=None
    )
    accounts_receivable_tax_type: typing.Optional[str] = pydantic.Field(
        alias="AccountsReceivableTaxType", default=None
    )
    addresses: typing.Optional[typing.List[_SerializerAddress]] = pydantic.Field(
        alias="Addresses", default=None
    )
    attachments: typing.Optional[typing.List[_SerializerAttachment]] = pydantic.Field(
        alias="Attachments", default=None
    )
    balances: typing.Optional[_SerializerBalances] = pydantic.Field(
        alias="Balances", default=None
    )
    bank_account_details: typing.Optional[str] = pydantic.Field(
        alias="BankAccountDetails", default=None
    )
    batch_payments: typing.Optional[_SerializerBatchPaymentDetails] = pydantic.Field(
        alias="BatchPayments", default=None
    )
    branding_theme: typing.Optional[_SerializerBrandingTheme] = pydantic.Field(
        alias="BrandingTheme", default=None
    )
    company_number: typing.Optional[str] = pydantic.Field(
        alias="CompanyNumber", default=None
    )
    contact_groups: typing.Optional[typing.List["_SerializerContactGroup"]] = (
        pydantic.Field(alias="ContactGroups", default=None)
    )
    contact_id: typing.Optional[str] = pydantic.Field(alias="ContactID", default=None)
    contact_number: typing.Optional[str] = pydantic.Field(
        alias="ContactNumber", default=None
    )
    contact_persons: typing.Optional[typing.List[_SerializerContactPerson]] = (
        pydantic.Field(alias="ContactPersons", default=None)
    )
    contact_status: typing.Optional[
        typing_extensions.Literal["ACTIVE", "ARCHIVED", "GDPRREQUEST"]
    ] = pydantic.Field(alias="ContactStatus", default=None)
    default_currency: typing.Optional[
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
            "BYR",
            "BZD",
            "CAD",
            "CDF",
            "CHF",
            "CLF",
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
            "EEK",
            "EGP",
            "ERN",
            "ETB",
            "EUR",
            "FJD",
            "FKP",
            "GBP",
            "GEL",
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
            "INR",
            "IQD",
            "IRR",
            "ISK",
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
            "LTL",
            "LVL",
            "LYD",
            "MAD",
            "MDL",
            "MGA",
            "MKD",
            "MMK",
            "MNT",
            "MOP",
            "MRO",
            "MRU",
            "MUR",
            "MVR",
            "MWK",
            "MXN",
            "MXV",
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
            "SKK",
            "SLE",
            "SLL",
            "SOS",
            "SRD",
            "STD",
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
            "TWD",
            "TZS",
            "UAH",
            "UGX",
            "USD",
            "UYU",
            "UZS",
            "VEF",
            "VES",
            "VND",
            "VUV",
            "WST",
            "XAF",
            "XCD",
            "XOF",
            "XPF",
            "YER",
            "ZAR",
            "ZMK",
            "ZMW",
            "ZWD",
        ]
    ] = pydantic.Field(alias="DefaultCurrency", default=None)
    discount: typing.Optional[float] = pydantic.Field(alias="Discount", default=None)
    email_address: typing.Optional[str] = pydantic.Field(
        alias="EmailAddress", default=None
    )
    first_name: typing.Optional[str] = pydantic.Field(alias="FirstName", default=None)
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    has_validation_errors: typing.Optional[bool] = pydantic.Field(
        alias="HasValidationErrors", default=None
    )
    is_customer: typing.Optional[bool] = pydantic.Field(
        alias="IsCustomer", default=None
    )
    is_supplier: typing.Optional[bool] = pydantic.Field(
        alias="IsSupplier", default=None
    )
    last_name: typing.Optional[str] = pydantic.Field(alias="LastName", default=None)
    merged_to_contact_id: typing.Optional[str] = pydantic.Field(
        alias="MergedToContactID", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    payment_terms: typing.Optional[_SerializerPaymentTerm] = pydantic.Field(
        alias="PaymentTerms", default=None
    )
    phones: typing.Optional[typing.List[_SerializerPhone]] = pydantic.Field(
        alias="Phones", default=None
    )
    purchases_default_account_code: typing.Optional[str] = pydantic.Field(
        alias="PurchasesDefaultAccountCode", default=None
    )
    purchases_default_line_amount_type: typing.Optional[
        typing_extensions.Literal["EXCLUSIVE", "INCLUSIVE", "NONE"]
    ] = pydantic.Field(alias="PurchasesDefaultLineAmountType", default=None)
    purchases_tracking_categories: typing.Optional[
        typing.List[_SerializerSalesTrackingCategory]
    ] = pydantic.Field(alias="PurchasesTrackingCategories", default=None)
    sales_default_account_code: typing.Optional[str] = pydantic.Field(
        alias="SalesDefaultAccountCode", default=None
    )
    sales_default_line_amount_type: typing.Optional[
        typing_extensions.Literal["EXCLUSIVE", "INCLUSIVE", "NONE"]
    ] = pydantic.Field(alias="SalesDefaultLineAmountType", default=None)
    sales_tracking_categories: typing.Optional[
        typing.List[_SerializerSalesTrackingCategory]
    ] = pydantic.Field(alias="SalesTrackingCategories", default=None)
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    tax_number: typing.Optional[str] = pydantic.Field(alias="TaxNumber", default=None)
    tax_number_type: typing.Optional[
        typing_extensions.Literal["ATIN", "EIN", "ITIN", "SSN"]
    ] = pydantic.Field(alias="TaxNumberType", default=None)
    tracking_category_name: typing.Optional[str] = pydantic.Field(
        alias="TrackingCategoryName", default=None
    )
    tracking_category_option: typing.Optional[str] = pydantic.Field(
        alias="TrackingCategoryOption", default=None
    )
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    validation_errors: typing.Optional[typing.List[_SerializerValidationError]] = (
        pydantic.Field(alias="ValidationErrors", default=None)
    )
    website: typing.Optional[str] = pydantic.Field(alias="Website", default=None)
    xero_network_key: typing.Optional[str] = pydantic.Field(
        alias="XeroNetworkKey", default=None
    )
