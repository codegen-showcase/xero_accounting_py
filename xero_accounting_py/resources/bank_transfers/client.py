import typing

from make_api_request import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from xero_accounting_py.resources.bank_transfers.attachments import (
    AsyncAttachmentsClient,
    AttachmentsClient,
)
from xero_accounting_py.resources.bank_transfers.history import (
    AsyncHistoryClient,
    HistoryClient,
)
from xero_accounting_py.types import models, params


class BankTransfersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.attachments = AttachmentsClient(base_client=self._base_client)
        self.history = HistoryClient(base_client=self._base_client)

    def list(
        self,
        *,
        xero_tenant_id: str,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BankTransfers:
        """
        Retrieves all bank transfers

        GET /BankTransfers

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of BankTransfers array of 0 to N BankTransfer

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bank_transfers.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Amount ASC",
            where="HasAttachments==true",
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(order, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order",
                to_encodable(item=order, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(where, type_utils.NotGiven):
            encode_query_param(
                _query,
                "where",
                to_encodable(item=where, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/BankTransfers",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.BankTransfers,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        bank_transfer_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BankTransfers:
        """
        Retrieves specific bank transfers by using a unique bank transfer Id

        GET /BankTransfers/{BankTransferID}

        Args:
            bank_transfer_id: Xero generated unique identifier for a bank transfer
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of BankTransfers array with one BankTransfer

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bank_transfers.get(
            bank_transfer_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/BankTransfers/{bank_transfer_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.BankTransfers,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        bank_transfers: typing.Union[
            typing.Optional[typing.List[params.BankTransfer]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BankTransfers:
        """
        Creates a bank transfer

        PUT /BankTransfers

        Args:
            bank_transfers: typing.List[BankTransfer]
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of BankTransfers array of one BankTransfer

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bank_transfers.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            bank_transfers=[
                {
                    "amount": 123.0,
                    "from_bank_account": {
                        "account_id": "00000000-0000-0000-0000-000000000000",
                        "bank_account_number": "123455",
                        "bank_account_type": "BANK",
                        "class_": "ASSET",
                        "code": "090",
                        "currency_code": "USD",
                        "enable_payments_to_account": False,
                        "has_attachments": False,
                        "name": "My Savings",
                        "reporting_code": "ASS",
                        "reporting_code_name": "Assets",
                        "show_in_expense_claims": False,
                        "status": "ACTIVE",
                        "tax_type": "NONE",
                        "type_": "BANK",
                        "updated_date_utc": "2016-10-17T13:45:33.993-07:00",
                    },
                    "from_is_reconciled": True,
                    "reference": "Sub 098801",
                    "to_bank_account": {
                        "account_id": "00000000-0000-0000-0000-000000000000",
                        "bank_account_number": "123455",
                        "bank_account_type": "BANK",
                        "class_": "ASSET",
                        "code": "088",
                        "currency_code": "USD",
                        "enable_payments_to_account": False,
                        "has_attachments": False,
                        "name": "Business Wells Fargo",
                        "reporting_code": "ASS",
                        "reporting_code_name": "Assets",
                        "show_in_expense_claims": False,
                        "status": "ACTIVE",
                        "tax_type": "NONE",
                        "type_": "BANK",
                        "updated_date_utc": "2016-06-03T08:31:14.517-07:00",
                    },
                    "to_is_reconciled": True,
                }
            ],
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"bank_transfers": bank_transfers},
            dump_with=params._SerializerBankTransfers,
        )
        return self._base_client.request(
            method="PUT",
            path="/BankTransfers",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.BankTransfers,
            request_options=request_options or default_request_options(),
        )


class AsyncBankTransfersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.attachments = AsyncAttachmentsClient(base_client=self._base_client)
        self.history = AsyncHistoryClient(base_client=self._base_client)

    async def list(
        self,
        *,
        xero_tenant_id: str,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BankTransfers:
        """
        Retrieves all bank transfers

        GET /BankTransfers

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of BankTransfers array of 0 to N BankTransfer

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bank_transfers.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Amount ASC",
            where="HasAttachments==true",
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(order, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order",
                to_encodable(item=order, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(where, type_utils.NotGiven):
            encode_query_param(
                _query,
                "where",
                to_encodable(item=where, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/BankTransfers",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.BankTransfers,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        bank_transfer_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BankTransfers:
        """
        Retrieves specific bank transfers by using a unique bank transfer Id

        GET /BankTransfers/{BankTransferID}

        Args:
            bank_transfer_id: Xero generated unique identifier for a bank transfer
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of BankTransfers array with one BankTransfer

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bank_transfers.get(
            bank_transfer_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/BankTransfers/{bank_transfer_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.BankTransfers,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        bank_transfers: typing.Union[
            typing.Optional[typing.List[params.BankTransfer]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BankTransfers:
        """
        Creates a bank transfer

        PUT /BankTransfers

        Args:
            bank_transfers: typing.List[BankTransfer]
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of BankTransfers array of one BankTransfer

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bank_transfers.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            bank_transfers=[
                {
                    "amount": 123.0,
                    "from_bank_account": {
                        "account_id": "00000000-0000-0000-0000-000000000000",
                        "bank_account_number": "123455",
                        "bank_account_type": "BANK",
                        "class_": "ASSET",
                        "code": "090",
                        "currency_code": "USD",
                        "enable_payments_to_account": False,
                        "has_attachments": False,
                        "name": "My Savings",
                        "reporting_code": "ASS",
                        "reporting_code_name": "Assets",
                        "show_in_expense_claims": False,
                        "status": "ACTIVE",
                        "tax_type": "NONE",
                        "type_": "BANK",
                        "updated_date_utc": "2016-10-17T13:45:33.993-07:00",
                    },
                    "from_is_reconciled": True,
                    "reference": "Sub 098801",
                    "to_bank_account": {
                        "account_id": "00000000-0000-0000-0000-000000000000",
                        "bank_account_number": "123455",
                        "bank_account_type": "BANK",
                        "class_": "ASSET",
                        "code": "088",
                        "currency_code": "USD",
                        "enable_payments_to_account": False,
                        "has_attachments": False,
                        "name": "Business Wells Fargo",
                        "reporting_code": "ASS",
                        "reporting_code_name": "Assets",
                        "show_in_expense_claims": False,
                        "status": "ACTIVE",
                        "tax_type": "NONE",
                        "type_": "BANK",
                        "updated_date_utc": "2016-06-03T08:31:14.517-07:00",
                    },
                    "to_is_reconciled": True,
                }
            ],
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"bank_transfers": bank_transfers},
            dump_with=params._SerializerBankTransfers,
        )
        return await self._base_client.request(
            method="PUT",
            path="/BankTransfers",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.BankTransfers,
            request_options=request_options or default_request_options(),
        )
