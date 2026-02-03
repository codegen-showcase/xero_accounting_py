import pydantic
import typing
import typing_extensions

from .tax_component import TaxComponent


class TaxRate(pydantic.BaseModel):
    """
    TaxRate
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    can_apply_to_assets: typing.Optional[bool] = pydantic.Field(
        alias="CanApplyToAssets", default=None
    )
    """
    Boolean to describe if tax rate can be used for asset accounts i.e.  true,false
    """
    can_apply_to_equity: typing.Optional[bool] = pydantic.Field(
        alias="CanApplyToEquity", default=None
    )
    """
    Boolean to describe if tax rate can be used for equity accounts i.e true,false
    """
    can_apply_to_expenses: typing.Optional[bool] = pydantic.Field(
        alias="CanApplyToExpenses", default=None
    )
    """
    Boolean to describe if tax rate can be used for expense accounts  i.e. true,false
    """
    can_apply_to_liabilities: typing.Optional[bool] = pydantic.Field(
        alias="CanApplyToLiabilities", default=None
    )
    """
    Boolean to describe if tax rate can be used for liability accounts  i.e. true,false
    """
    can_apply_to_revenue: typing.Optional[bool] = pydantic.Field(
        alias="CanApplyToRevenue", default=None
    )
    """
    Boolean to describe if tax rate can be used for revenue accounts i.e. true,false
    """
    display_tax_rate: typing.Optional[float] = pydantic.Field(
        alias="DisplayTaxRate", default=None
    )
    """
    Tax Rate (decimal to 4dp) e.g 12.5000
    """
    effective_rate: typing.Optional[float] = pydantic.Field(
        alias="EffectiveRate", default=None
    )
    """
    Effective Tax Rate (decimal to 4dp) e.g 12.5000
    """
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    """
    Name of tax rate
    """
    report_tax_type: typing.Optional[
        typing_extensions.Literal[
            "ACC28PLUS",
            "ACCRUAL",
            "ACCRUALS",
            "ACCUPTO28",
            "AVALARA",
            "BADDEBT",
            "BADDEBTRECOVERY",
            "BADDEBTRELIEF",
            "BASEXCLUDED",
            "BLINPUT2",
            "BLINPUT3",
            "CAPEXINPUT",
            "CAPEXOUTPUT",
            "CAPIMPORTS",
            "CAPINPUT",
            "CAPITALEXINPUT",
            "CAPITALEXPENSESINPUT",
            "CAPITALSALESOUTPUT",
            "CAPOUTPUT",
            "CASH",
            "CIUINPUT",
            "CIUOUTPUT",
            "DRCHARGE",
            "DRCHARGESUPPLY",
            "DSOUTPUT",
            "ECACQUISITIONS",
            "ECINPUT",
            "ECOUTPUT",
            "ECOUTPUTSERVICES",
            "EPINPUT",
            "ES33OUTPUT",
            "ESN33OUTPUT",
            "EXEMPTCAPITAL",
            "EXEMPTEXPENSES",
            "EXEMPTEXPORT",
            "EXEMPTINPUT",
            "EXEMPTOUTPUT",
            "FLATRATEACCRUAL",
            "FLATRATECASH",
            "GOODSIMPORT",
            "GSTONCAPIMPORTS",
            "GSTONCAPITALIMPORTS",
            "GSTONIMPORTS",
            "IGDSINPUT2",
            "IGDSINPUT3",
            "IM",
            "IMESS",
            "IMINPUT",
            "IMINPUT2",
            "IMN33",
            "IMRE",
            "INPUT",
            "INPUT2",
            "INPUTTAXED",
            "INVOICE",
            "MEINPUT",
            "MOSSSALES",
            "NONE",
            "NONEINPUT",
            "NONEOUTPUT",
            "NOTREPORTED",
            "NRINPUT",
            "OPINPUT",
            "OSOUTPUT",
            "OTHERINPUT",
            "OTHEROUTPUT",
            "OUTPUT",
            "OUTPUT2",
            "PAYMENTS",
            "PURCHASESINPUT",
            "REVERSECHARGES",
            "SALESOUTPUT",
            "SHOUTPUT",
            "SRCAS",
            "SRINPUT",
            "SRLVG",
            "SROUTPUT",
            "SROUTPUT2",
            "SROVR",
            "SROVRLVG",
            "SROVRRS",
            "TOURISTREFUND",
            "TXCA",
            "TXESSINPUT",
            "TXN33INPUT",
            "TXPETINPUT",
            "TXRCESS",
            "TXRCN33",
            "TXRCRE",
            "TXRCTS",
            "TXREINPUT",
            "UNDEFINED",
            "USSALESTAX",
            "ZEROEXPOUTPUT",
            "ZERORATEDINPUT",
            "ZERORATEDOUTPUT",
            "ZREXPORT",
            "ZRINPUT",
            "ZROUTPUT",
        ]
    ] = pydantic.Field(alias="ReportTaxType", default=None)
    """
    See ReportTaxTypes
    """
    status: typing.Optional[
        typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED", "PENDING"]
    ] = pydantic.Field(alias="Status", default=None)
    """
    See Status Codes
    """
    tax_components: typing.Optional[typing.List[TaxComponent]] = pydantic.Field(
        alias="TaxComponents", default=None
    )
    """
    See TaxComponents
    """
    tax_type: typing.Optional[str] = pydantic.Field(alias="TaxType", default=None)
    """
    The tax type
    """
