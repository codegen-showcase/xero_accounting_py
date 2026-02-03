import pydantic
import typing


class ImportSummaryAccounts(pydantic.BaseModel):
    """
    A summary of the accounts changes
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    deleted: typing.Optional[int] = pydantic.Field(alias="Deleted", default=None)
    """
    The number of accounts deleted
    """
    errored: typing.Optional[int] = pydantic.Field(alias="Errored", default=None)
    """
    The number of accounts that had an error
    """
    locked: typing.Optional[int] = pydantic.Field(alias="Locked", default=None)
    """
    The number of locked accounts
    """
    new: typing.Optional[int] = pydantic.Field(alias="New", default=None)
    """
    The number of new accounts created
    """
    new_or_updated: typing.Optional[int] = pydantic.Field(
        alias="NewOrUpdated", default=None
    )
    """
    The number of new or updated accounts
    """
    present: typing.Optional[bool] = pydantic.Field(alias="Present", default=None)
    system: typing.Optional[int] = pydantic.Field(alias="System", default=None)
    """
    The number of system accounts
    """
    total: typing.Optional[int] = pydantic.Field(alias="Total", default=None)
    """
    The total number of accounts in the org
    """
    updated: typing.Optional[int] = pydantic.Field(alias="Updated", default=None)
    """
    The number of accounts updated
    """
