import pydantic
import typing
import typing_extensions

from .address_for_organisation import AddressForOrganisation
from .external_link import ExternalLink
from .payment_term import PaymentTerm
from .phone import Phone


class Organisation(pydantic.BaseModel):
    """
    Organisation
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    api_key: typing.Optional[str] = pydantic.Field(alias="APIKey", default=None)
    """
    Display a unique key used for Xero-to-Xero transactions
    """
    addresses: typing.Optional[typing.List[AddressForOrganisation]] = pydantic.Field(
        alias="Addresses", default=None
    )
    """
    Address details for organisation – see Addresses
    """
    base_currency: typing.Optional[
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
    ] = pydantic.Field(alias="BaseCurrency", default=None)
    """
    3 letter alpha code for the currency – see list of currency codes
    """
    class_: typing.Optional[
        typing_extensions.Literal[
            "COMPREHENSIVE",
            "DEMO",
            "GROW",
            "GST_CASHBOOK",
            "IGNITE",
            "LEDGER",
            "LITE",
            "NON_GST_CASHBOOK",
            "PREMIUM",
            "PREMIUM_100",
            "PREMIUM_20",
            "PREMIUM_50",
            "SIMPLE",
            "STANDARD",
            "STARTER",
            "TRIAL",
            "ULTIMATE",
            "ULTIMATE_10",
            "ULTIMATE_100",
            "ULTIMATE_20",
            "ULTIMATE_50",
        ]
    ] = pydantic.Field(alias="Class", default=None)
    """
    Organisation Classes describe which plan the Xero organisation is on (e.g. DEMO, TRIAL, PREMIUM)
    """
    country_code: typing.Optional[
        typing_extensions.Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CW",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "EH",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GG",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IO",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JE",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PS",
            "PT",
            "PW",
            "PY",
            "QA",
            "RE",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SJ",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "SS",
            "ST",
            "SV",
            "SX",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "XK",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ]
    ] = pydantic.Field(alias="CountryCode", default=None)
    created_date_utc: typing.Optional[str] = pydantic.Field(
        alias="CreatedDateUTC", default=None
    )
    """
    Timestamp when the organisation was created in Xero
    """
    default_purchases_tax: typing.Optional[str] = pydantic.Field(
        alias="DefaultPurchasesTax", default=None
    )
    """
    The default for LineAmountTypes on purchase transactions
    """
    default_sales_tax: typing.Optional[str] = pydantic.Field(
        alias="DefaultSalesTax", default=None
    )
    """
    The default for LineAmountTypes on sales transactions
    """
    edition: typing.Optional[typing_extensions.Literal["BUSINESS", "PARTNER"]] = (
        pydantic.Field(alias="Edition", default=None)
    )
    """
    BUSINESS or PARTNER. Partner edition organisations are sold exclusively through accounting partners and have restricted functionality (e.g. no access to invoicing)
    """
    employer_identification_number: typing.Optional[str] = pydantic.Field(
        alias="EmployerIdentificationNumber", default=None
    )
    """
    Shown if set. US Only.
    """
    end_of_year_lock_date: typing.Optional[str] = pydantic.Field(
        alias="EndOfYearLockDate", default=None
    )
    """
    Shown if set. See lock dates
    """
    external_links: typing.Optional[typing.List[ExternalLink]] = pydantic.Field(
        alias="ExternalLinks", default=None
    )
    """
    Organisation profile links for popular services such as Facebook,Twitter, GooglePlus and LinkedIn. You can also add link to your website here. Shown if Organisation settings  is updated in Xero. See ExternalLinks below
    """
    financial_year_end_day: typing.Optional[int] = pydantic.Field(
        alias="FinancialYearEndDay", default=None
    )
    """
    Calendar day e.g. 0-31
    """
    financial_year_end_month: typing.Optional[int] = pydantic.Field(
        alias="FinancialYearEndMonth", default=None
    )
    """
    Calendar Month e.g. 1-12
    """
    is_demo_company: typing.Optional[bool] = pydantic.Field(
        alias="IsDemoCompany", default=None
    )
    """
    Boolean to describe if organisation is a demo company.
    """
    legal_name: typing.Optional[str] = pydantic.Field(alias="LegalName", default=None)
    """
    Organisation name shown on Reports
    """
    line_of_business: typing.Optional[str] = pydantic.Field(
        alias="LineOfBusiness", default=None
    )
    """
    Description of business type as defined in Organisation settings
    """
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    """
    Display name of organisation shown in Xero
    """
    organisation_entity_type: typing.Optional[
        typing_extensions.Literal[
            "ACCOUNTING_PRACTICE",
            "CHARITY",
            "CLUB_OR_SOCIETY",
            "COMPANY",
            "INDIVIDUAL",
            "LOOK_THROUGH_COMPANY",
            "NOT_FOR_PROFIT",
            "PARTNERSHIP",
            "SELF_MANAGED_SUPERANNUATION_FUND",
            "SOLE_TRADER",
            "SUPERANNUATION_FUND",
            "S_CORPORATION",
            "TRUST",
        ]
    ] = pydantic.Field(alias="OrganisationEntityType", default=None)
    """
    Organisation Entity Type
    """
    organisation_id: typing.Optional[str] = pydantic.Field(
        alias="OrganisationID", default=None
    )
    """
    Unique Xero identifier
    """
    organisation_status: typing.Optional[str] = pydantic.Field(
        alias="OrganisationStatus", default=None
    )
    """
    Will be set to ACTIVE if you can connect to organisation via the Xero API
    """
    organisation_type: typing.Optional[
        typing_extensions.Literal[
            "ACCOUNTING_PRACTICE",
            "CHARITY",
            "CLUB_OR_SOCIETY",
            "COMPANY",
            "INDIVIDUAL",
            "LOOK_THROUGH_COMPANY",
            "NOT_FOR_PROFIT",
            "PARTNERSHIP",
            "SELF_MANAGED_SUPERANNUATION_FUND",
            "SOLE_TRADER",
            "SUPERANNUATION_FUND",
            "S_CORPORATION",
            "TRUST",
        ]
    ] = pydantic.Field(alias="OrganisationType", default=None)
    """
    Organisation Type
    """
    payment_terms: typing.Optional[PaymentTerm] = pydantic.Field(
        alias="PaymentTerms", default=None
    )
    pays_tax: typing.Optional[bool] = pydantic.Field(alias="PaysTax", default=None)
    """
    Boolean to describe if organisation is registered with a local tax authority i.e. true, false
    """
    period_lock_date: typing.Optional[str] = pydantic.Field(
        alias="PeriodLockDate", default=None
    )
    """
    Shown if set. See lock dates
    """
    phones: typing.Optional[typing.List[Phone]] = pydantic.Field(
        alias="Phones", default=None
    )
    """
    Phones details for organisation – see Phones
    """
    registration_number: typing.Optional[str] = pydantic.Field(
        alias="RegistrationNumber", default=None
    )
    """
    Shows for New Zealand, Australian and UK organisations
    """
    sales_tax_basis: typing.Optional[
        typing_extensions.Literal[
            "ACCRUAL",
            "ACCRUALS",
            "CASH",
            "FLATRATEACCRUAL",
            "FLATRATECASH",
            "INVOICE",
            "NONE",
            "PAYMENTS",
        ]
    ] = pydantic.Field(alias="SalesTaxBasis", default=None)
    """
    The accounting basis used for tax returns. See Sales Tax Basis
    """
    sales_tax_period: typing.Optional[
        typing_extensions.Literal[
            "1MONTHLY",
            "2MONTHLY",
            "3MONTHLY",
            "6MONTHLY",
            "ANNUALLY",
            "MONTHLY",
            "NONE",
            "ONEMONTHS",
            "QUARTERLY",
            "QUARTERLY1",
            "QUARTERLY2",
            "QUARTERLY3",
            "SIXMONTHS",
            "TWOMONTHS",
            "YEARLY",
        ]
    ] = pydantic.Field(alias="SalesTaxPeriod", default=None)
    """
    The frequency with which tax returns are processed. See Sales Tax Period
    """
    short_code: typing.Optional[str] = pydantic.Field(alias="ShortCode", default=None)
    """
    A unique identifier for the organisation. Potential uses.
    """
    tax_number: typing.Optional[str] = pydantic.Field(alias="TaxNumber", default=None)
    """
    Shown if set. Displays in the Xero UI as Tax File Number (AU), GST Number (NZ), VAT Number (UK) and Tax ID Number (US & Global).
    """
    timezone: typing.Optional[
        typing_extensions.Literal[
            "AFGHANISTANSTANDARDTIME",
            "ALASKANSTANDARDTIME",
            "ALEUTIANSTANDARDTIME",
            "ALTAISTANDARDTIME",
            "ARABIANSTANDARDTIME",
            "ARABICSTANDARDTIME",
            "ARABSTANDARDTIME",
            "ARGENTINASTANDARDTIME",
            "ASTRAKHANSTANDARDTIME",
            "ATLANTICSTANDARDTIME",
            "AUSCENTRALSTANDARDTIME",
            "AUSCENTRALWSTANDARDTIME",
            "AUSEASTERNSTANDARDTIME",
            "AZERBAIJANSTANDARDTIME",
            "AZORESSTANDARDTIME",
            "BAHIASTANDARDTIME",
            "BANGLADESHSTANDARDTIME",
            "BELARUSSTANDARDTIME",
            "BOUGAINVILLESTANDARDTIME",
            "CANADACENTRALSTANDARDTIME",
            "CAPEVERDESTANDARDTIME",
            "CAUCASUSSTANDARDTIME",
            "CENAUSTRALIASTANDARDTIME",
            "CENTRALAMERICASTANDARDTIME",
            "CENTRALASIASTANDARDTIME",
            "CENTRALBRAZILIANSTANDARDTIME",
            "CENTRALEUROPEANSTANDARDTIME",
            "CENTRALEUROPESTANDARDTIME",
            "CENTRALPACIFICSTANDARDTIME",
            "CENTRALSTANDARDTIME",
            "CENTRALSTANDARDTIME(MEXICO)",
            "CHATHAMISLANDSSTANDARDTIME",
            "CHINASTANDARDTIME",
            "CUBASTANDARDTIME",
            "DATELINESTANDARDTIME",
            "EAFRICASTANDARDTIME",
            "EASTERISLANDSTANDARDTIME",
            "EASTERNSTANDARDTIME",
            "EASTERNSTANDARDTIME(MEXICO)",
            "EAUSTRALIASTANDARDTIME",
            "EEUROPESTANDARDTIME",
            "EGYPTSTANDARDTIME",
            "EKATERINBURGSTANDARDTIME",
            "ESOUTHAMERICASTANDARDTIME",
            "FIJISTANDARDTIME",
            "FLESTANDARDTIME",
            "GEORGIANSTANDARDTIME",
            "GMTSTANDARDTIME",
            "GREENLANDSTANDARDTIME",
            "GREENWICHSTANDARDTIME",
            "GTBSTANDARDTIME",
            "HAITISTANDARDTIME",
            "HAWAIIANSTANDARDTIME",
            "INDIASTANDARDTIME",
            "IRANSTANDARDTIME",
            "ISRAELSTANDARDTIME",
            "JORDANSTANDARDTIME",
            "KALININGRADSTANDARDTIME",
            "KAMCHATKASTANDARDTIME",
            "KOREASTANDARDTIME",
            "LIBYASTANDARDTIME",
            "LINEISLANDSSTANDARDTIME",
            "LORDHOWESTANDARDTIME",
            "MAGADANSTANDARDTIME",
            "MAGALLANESSTANDARDTIME",
            "MARQUESASSTANDARDTIME",
            "MAURITIUSSTANDARDTIME",
            "MIDATLANTICSTANDARDTIME",
            "MIDDLEEASTSTANDARDTIME",
            "MONTEVIDEOSTANDARDTIME",
            "MOROCCOSTANDARDTIME",
            "MOUNTAINSTANDARDTIME",
            "MOUNTAINSTANDARDTIME(MEXICO)",
            "MYANMARSTANDARDTIME",
            "NAMIBIASTANDARDTIME",
            "NCENTRALASIASTANDARDTIME",
            "NEPALSTANDARDTIME",
            "NEWFOUNDLANDSTANDARDTIME",
            "NEWZEALANDSTANDARDTIME",
            "NORFOLKSTANDARDTIME",
            "NORTHASIAEASTSTANDARDTIME",
            "NORTHASIASTANDARDTIME",
            "NORTHKOREASTANDARDTIME",
            "OMSKSTANDARDTIME",
            "PACIFICSASTANDARDTIME",
            "PACIFICSTANDARDTIME",
            "PACIFICSTANDARDTIME(MEXICO)",
            "PAKISTANSTANDARDTIME",
            "PARAGUAYSTANDARDTIME",
            "QYZYLORDASTANDARDTIME",
            "ROMANCESTANDARDTIME",
            "RUSSIANSTANDARDTIME",
            "RUSSIATIMEZONE10",
            "RUSSIATIMEZONE11",
            "RUSSIATIMEZONE3",
            "SAEASTERNSTANDARDTIME",
            "SAINTPIERRESTANDARDTIME",
            "SAKHALINSTANDARDTIME",
            "SAMOASTANDARDTIME",
            "SAOTOMESTANDARDTIME",
            "SAPACIFICSTANDARDTIME",
            "SARATOVSTANDARDTIME",
            "SAWESTERNSTANDARDTIME",
            "SEASIASTANDARDTIME",
            "SINGAPORESTANDARDTIME",
            "SOUTHAFRICASTANDARDTIME",
            "SOUTHSUDANSTANDARDTIME",
            "SRILANKASTANDARDTIME",
            "SUDANSTANDARDTIME",
            "SYRIASTANDARDTIME",
            "TAIPEISTANDARDTIME",
            "TASMANIASTANDARDTIME",
            "TOCANTINSSTANDARDTIME",
            "TOKYOSTANDARDTIME",
            "TOMSKSTANDARDTIME",
            "TONGASTANDARDTIME",
            "TRANSBAIKALSTANDARDTIME",
            "TURKEYSTANDARDTIME",
            "TURKSANDCAICOSSTANDARDTIME",
            "ULAANBAATARSTANDARDTIME",
            "USEASTERNSTANDARDTIME",
            "USMOUNTAINSTANDARDTIME",
            "UTC",
            "UTC+12",
            "UTC+13",
            "UTC02",
            "UTC08",
            "UTC09",
            "UTC11",
            "VENEZUELASTANDARDTIME",
            "VLADIVOSTOKSTANDARDTIME",
            "VOLGOGRADSTANDARDTIME",
            "WAUSTRALIASTANDARDTIME",
            "WCENTRALAFRICASTANDARDTIME",
            "WESTASIASTANDARDTIME",
            "WESTBANKSTANDARDTIME",
            "WESTPACIFICSTANDARDTIME",
            "WEUROPESTANDARDTIME",
            "WMONGOLIASTANDARDTIME",
            "YAKUTSKSTANDARDTIME",
            "YUKONSTANDARDTIME",
        ]
    ] = pydantic.Field(alias="Timezone", default=None)
    """
    Timezone specifications
    """
    version: typing.Optional[
        typing_extensions.Literal[
            "AU",
            "AUONRAMP",
            "GLOBAL",
            "GLOBALONRAMP",
            "NZ",
            "NZONRAMP",
            "UK",
            "UKONRAMP",
            "US",
            "USONRAMP",
        ]
    ] = pydantic.Field(alias="Version", default=None)
    """
    See Version Types
    """
