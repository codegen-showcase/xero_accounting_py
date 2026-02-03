import pydantic
import typing

from .import_summary_accounts import ImportSummaryAccounts
from .import_summary_organisation import ImportSummaryOrganisation


class ImportSummary(pydantic.BaseModel):
    """
    A summary of the import from setup endpoint
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    accounts: typing.Optional[ImportSummaryAccounts] = pydantic.Field(
        alias="Accounts", default=None
    )
    """
    A summary of the accounts changes
    """
    organisation: typing.Optional[ImportSummaryOrganisation] = pydantic.Field(
        alias="Organisation", default=None
    )
