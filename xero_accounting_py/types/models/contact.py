import pydantic
import typing
import typing_extensions

from .address import Address
from .attachment import Attachment
from .balances import Balances
from .batch_payment_details import BatchPaymentDetails
from .branding_theme import BrandingTheme
from .contact_person import ContactPerson
from .payment_term import PaymentTerm
from .phone import Phone
from .sales_tracking_category import SalesTrackingCategory
from .validation_error import ValidationError

if typing_extensions.TYPE_CHECKING:
    from .contact_group import ContactGroup


class Contact(pydantic.BaseModel):
    """
    Contact
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_number: typing.Optional[str] = pydantic.Field(
        alias="AccountNumber", default=None
    )
    """
    A user defined account number. This can be updated via the API and the Xero UI (max length = 50)
    """
    accounts_payable_tax_type: typing.Optional[str] = pydantic.Field(
        alias="AccountsPayableTaxType", default=None
    )
    """
    The tax type from TaxRates
    """
    accounts_receivable_tax_type: typing.Optional[str] = pydantic.Field(
        alias="AccountsReceivableTaxType", default=None
    )
    """
    The tax type from TaxRates
    """
    addresses: typing.Optional[typing.List[Address]] = pydantic.Field(
        alias="Addresses", default=None
    )
    """
    Store certain address types for a contact – see address types
    """
    attachments: typing.Optional[typing.List[Attachment]] = pydantic.Field(
        alias="Attachments", default=None
    )
    """
    Displays array of attachments from the API
    """
    balances: typing.Optional[Balances] = pydantic.Field(alias="Balances", default=None)
    """
    The raw AccountsReceivable(sales invoices) and AccountsPayable(bills) outstanding and overdue amounts, not converted to base currency (read only)
    """
    bank_account_details: typing.Optional[str] = pydantic.Field(
        alias="BankAccountDetails", default=None
    )
    """
    Bank account number of contact
    """
    batch_payments: typing.Optional[BatchPaymentDetails] = pydantic.Field(
        alias="BatchPayments", default=None
    )
    """
    Bank details for use on a batch payment stored with each contact
    """
    branding_theme: typing.Optional[BrandingTheme] = pydantic.Field(
        alias="BrandingTheme", default=None
    )
    company_number: typing.Optional[str] = pydantic.Field(
        alias="CompanyNumber", default=None
    )
    """
    Company registration number (max length = 50)
    """
    contact_groups: typing.Optional[typing.List["ContactGroup"]] = pydantic.Field(
        alias="ContactGroups", default=None
    )
    """
    Displays which contact groups a contact is included in
    """
    contact_id: typing.Optional[str] = pydantic.Field(alias="ContactID", default=None)
    """
    Xero identifier
    """
    contact_number: typing.Optional[str] = pydantic.Field(
        alias="ContactNumber", default=None
    )
    """
    This can be updated via the API only i.e. This field is read only on the Xero contact screen, used to identify contacts in external systems (max length = 50). If the Contact Number is used, this is displayed as Contact Code in the Contacts UI in Xero.
    """
    contact_persons: typing.Optional[typing.List[ContactPerson]] = pydantic.Field(
        alias="ContactPersons", default=None
    )
    """
    See contact persons
    """
    contact_status: typing.Optional[
        typing_extensions.Literal["ACTIVE", "ARCHIVED", "GDPRREQUEST"]
    ] = pydantic.Field(alias="ContactStatus", default=None)
    """
    Current status of a contact – see contact status types
    """
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
    """
    3 letter alpha code for the currency – see list of currency codes
    """
    discount: typing.Optional[float] = pydantic.Field(alias="Discount", default=None)
    """
    The default discount rate for the contact (read only)
    """
    email_address: typing.Optional[str] = pydantic.Field(
        alias="EmailAddress", default=None
    )
    """
    Email address of contact person (umlauts not supported) (max length  = 255)
    """
    first_name: typing.Optional[str] = pydantic.Field(alias="FirstName", default=None)
    """
    First name of contact person (max length = 255)
    """
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    """
    A boolean to indicate if a contact has an attachment
    """
    has_validation_errors: typing.Optional[bool] = pydantic.Field(
        alias="HasValidationErrors", default=None
    )
    """
    A boolean to indicate if a contact has an validation errors
    """
    is_customer: typing.Optional[bool] = pydantic.Field(
        alias="IsCustomer", default=None
    )
    """
    true or false – Boolean that describes if a contact has any AR invoices entered against them. Cannot be set via PUT or POST – it is automatically set when an accounts receivable invoice is generated against this contact.
    """
    is_supplier: typing.Optional[bool] = pydantic.Field(
        alias="IsSupplier", default=None
    )
    """
    true or false – Boolean that describes if a contact that has any AP  invoices entered against them. Cannot be set via PUT or POST – it is automatically set when an accounts payable invoice is generated against this contact.
    """
    last_name: typing.Optional[str] = pydantic.Field(alias="LastName", default=None)
    """
    Last name of contact person (max length = 255)
    """
    merged_to_contact_id: typing.Optional[str] = pydantic.Field(
        alias="MergedToContactID", default=None
    )
    """
    ID for the destination of a merged contact. Only returned when using paging or when fetching a contact by ContactId or ContactNumber.
    """
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    """
    Full name of contact/organisation (max length = 255)
    """
    payment_terms: typing.Optional[PaymentTerm] = pydantic.Field(
        alias="PaymentTerms", default=None
    )
    phones: typing.Optional[typing.List[Phone]] = pydantic.Field(
        alias="Phones", default=None
    )
    """
    Store certain phone types for a contact – see phone types
    """
    purchases_default_account_code: typing.Optional[str] = pydantic.Field(
        alias="PurchasesDefaultAccountCode", default=None
    )
    """
    The default purchases account code for contacts
    """
    purchases_default_line_amount_type: typing.Optional[
        typing_extensions.Literal["EXCLUSIVE", "INCLUSIVE", "NONE"]
    ] = pydantic.Field(alias="PurchasesDefaultLineAmountType", default=None)
    """
    The default purchases line amount type for a contact Only available when summaryOnly parameter or paging is used, or when fetch by ContactId or ContactNumber.
    """
    purchases_tracking_categories: typing.Optional[
        typing.List[SalesTrackingCategory]
    ] = pydantic.Field(alias="PurchasesTrackingCategories", default=None)
    """
    The default purchases tracking categories for contacts
    """
    sales_default_account_code: typing.Optional[str] = pydantic.Field(
        alias="SalesDefaultAccountCode", default=None
    )
    """
    The default sales account code for contacts
    """
    sales_default_line_amount_type: typing.Optional[
        typing_extensions.Literal["EXCLUSIVE", "INCLUSIVE", "NONE"]
    ] = pydantic.Field(alias="SalesDefaultLineAmountType", default=None)
    """
    The default sales line amount type for a contact. Only available when summaryOnly parameter or paging is used, or when fetch by ContactId or ContactNumber.
    """
    sales_tracking_categories: typing.Optional[typing.List[SalesTrackingCategory]] = (
        pydantic.Field(alias="SalesTrackingCategories", default=None)
    )
    """
    The default sales tracking categories for contacts
    """
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    """
    Status of object
    """
    tax_number: typing.Optional[str] = pydantic.Field(alias="TaxNumber", default=None)
    """
    Tax number of contact – this is also known as the ABN (Australia), GST Number (New Zealand), VAT Number (UK) or Tax ID Number (US and global) in the Xero UI depending on which regionalized version of Xero you are using (max length = 50)
    """
    tax_number_type: typing.Optional[
        typing_extensions.Literal["ATIN", "EIN", "ITIN", "SSN"]
    ] = pydantic.Field(alias="TaxNumberType", default=None)
    """
    Identifier of the regional type of tax number, such as US, UK, or other regional tax identifiers
    """
    tracking_category_name: typing.Optional[str] = pydantic.Field(
        alias="TrackingCategoryName", default=None
    )
    """
    The name of the Tracking Category assigned to the contact under SalesTrackingCategories and PurchasesTrackingCategories
    """
    tracking_category_option: typing.Optional[str] = pydantic.Field(
        alias="TrackingCategoryOption", default=None
    )
    """
    The name of the Tracking Option assigned to the contact under SalesTrackingCategories and PurchasesTrackingCategories
    """
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    """
    UTC timestamp of last update to contact
    """
    validation_errors: typing.Optional[typing.List[ValidationError]] = pydantic.Field(
        alias="ValidationErrors", default=None
    )
    """
    Displays validation errors returned from the API
    """
    website: typing.Optional[str] = pydantic.Field(alias="Website", default=None)
    """
    Website address for contact (read only)
    """
    xero_network_key: typing.Optional[str] = pydantic.Field(
        alias="XeroNetworkKey", default=None
    )
    """
    Store XeroNetworkKey for contacts.
    """
