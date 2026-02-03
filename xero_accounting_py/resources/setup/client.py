import typing

from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from xero_accounting_py.types import models, params


class SetupClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        xero_tenant_id: str,
        accounts: typing.Union[
            typing.Optional[typing.List[params.Account]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        conversion_balances: typing.Union[
            typing.Optional[typing.List[params.ConversionBalances]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        conversion_date: typing.Union[
            typing.Optional[params.ConversionDate], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ImportSummaryObject:
        """
        Sets the chart of accounts, the conversion date and conversion balances

        POST /Setup

        Args:
            accounts: typing.List[Account]
            conversion_balances: Balance supplied for each account that has a value as at the conversion date.
            conversion_date: The date when the organisation starts using Xero
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - returns a summary of the chart of accounts updates

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.setup.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            accounts=[
                {
                    "code": "200",
                    "name": "Sales",
                    "reporting_code": "REV.TRA.GOO",
                    "type_": "SALES",
                },
                {
                    "code": "400",
                    "name": "Advertising",
                    "reporting_code": "EXP",
                    "type_": "OVERHEADS",
                },
                {
                    "code": "610",
                    "name": "Accounts Receivable",
                    "reporting_code": "ASS.CUR.REC.TRA",
                    "system_account": "DEBTORS",
                    "type_": "CURRENT",
                },
                {
                    "code": "800",
                    "name": "Accounts Payable",
                    "reporting_code": "LIA.CUR.PAY",
                    "system_account": "CREDITORS",
                    "type_": "CURRLIAB",
                },
            ],
            conversion_balances=[{}],
            conversion_date={},
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "accounts": accounts,
                "conversion_balances": conversion_balances,
                "conversion_date": conversion_date,
            },
            dump_with=params._SerializerSetup,
        )
        return self._base_client.request(
            method="POST",
            path="/Setup",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.ImportSummaryObject,
            request_options=request_options or default_request_options(),
        )


class AsyncSetupClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        xero_tenant_id: str,
        accounts: typing.Union[
            typing.Optional[typing.List[params.Account]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        conversion_balances: typing.Union[
            typing.Optional[typing.List[params.ConversionBalances]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        conversion_date: typing.Union[
            typing.Optional[params.ConversionDate], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ImportSummaryObject:
        """
        Sets the chart of accounts, the conversion date and conversion balances

        POST /Setup

        Args:
            accounts: typing.List[Account]
            conversion_balances: Balance supplied for each account that has a value as at the conversion date.
            conversion_date: The date when the organisation starts using Xero
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - returns a summary of the chart of accounts updates

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.setup.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            accounts=[
                {
                    "code": "200",
                    "name": "Sales",
                    "reporting_code": "REV.TRA.GOO",
                    "type_": "SALES",
                },
                {
                    "code": "400",
                    "name": "Advertising",
                    "reporting_code": "EXP",
                    "type_": "OVERHEADS",
                },
                {
                    "code": "610",
                    "name": "Accounts Receivable",
                    "reporting_code": "ASS.CUR.REC.TRA",
                    "system_account": "DEBTORS",
                    "type_": "CURRENT",
                },
                {
                    "code": "800",
                    "name": "Accounts Payable",
                    "reporting_code": "LIA.CUR.PAY",
                    "system_account": "CREDITORS",
                    "type_": "CURRLIAB",
                },
            ],
            conversion_balances=[{}],
            conversion_date={},
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "accounts": accounts,
                "conversion_balances": conversion_balances,
                "conversion_date": conversion_date,
            },
            dump_with=params._SerializerSetup,
        )
        return await self._base_client.request(
            method="POST",
            path="/Setup",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.ImportSummaryObject,
            request_options=request_options or default_request_options(),
        )
