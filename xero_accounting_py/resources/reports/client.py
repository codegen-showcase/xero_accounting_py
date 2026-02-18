import typing
import typing_extensions

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
from xero_accounting_py.types import models


class ReportsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves a list of the organistaions unique reports that require a uuid to fetch

        GET /Reports

        Args:
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/Reports",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    def get_aged_payables_by_contact(
        self,
        *,
        contact_id: str,
        xero_tenant_id: str,
        date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        from_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        to_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves report for aged payables by contact

        GET /Reports/AgedPayablesByContact

        Args:
            date: The date of the Aged Payables By Contact report
            from_date: filter by the from date of the report e.g. 2021-02-01
            to_date: filter by the to date of the report e.g. 2021-02-28
            contact_id: Unique identifier for a Contact
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.get_aged_payables_by_contact(
            contact_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            date="2019-10-31",
            from_date="2019-10-31",
            to_date="2019-10-31",
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "contactId",
            to_encodable(item=contact_id, dump_with=str),
            style="form",
            explode=True,
        )
        if not isinstance(date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "date",
                to_encodable(item=date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(from_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "fromDate",
                to_encodable(item=from_date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(to_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "toDate",
                to_encodable(item=to_date, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/Reports/AgedPayablesByContact",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    def get_aged_receivables_by_contact(
        self,
        *,
        contact_id: str,
        xero_tenant_id: str,
        date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        from_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        to_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves report for aged receivables by contact

        GET /Reports/AgedReceivablesByContact

        Args:
            date: The date of the Aged Receivables By Contact report
            from_date: filter by the from date of the report e.g. 2021-02-01
            to_date: filter by the to date of the report e.g. 2021-02-28
            contact_id: Unique identifier for a Contact
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.get_aged_receivables_by_contact(
            contact_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            date="2019-10-31",
            from_date="2019-10-31",
            to_date="2019-10-31",
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "contactId",
            to_encodable(item=contact_id, dump_with=str),
            style="form",
            explode=True,
        )
        if not isinstance(date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "date",
                to_encodable(item=date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(from_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "fromDate",
                to_encodable(item=from_date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(to_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "toDate",
                to_encodable(item=to_date, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/Reports/AgedReceivablesByContact",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    def get_balance_sheet(
        self,
        *,
        xero_tenant_id: str,
        date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payments_only: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        periods: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        standard_layout: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        timeframe: typing.Union[
            typing.Optional[typing_extensions.Literal["MONTH", "QUARTER", "YEAR"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tracking_option_id1: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tracking_option_id2: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves report for balancesheet

        GET /Reports/BalanceSheet

        Args:
            date: The date of the Balance Sheet report
            payments_only: return a cash basis for the Balance Sheet report
            periods: The number of periods for the Balance Sheet report
            standard_layout: The standard layout boolean for the Balance Sheet report
            timeframe: The period size to compare to (MONTH, QUARTER, YEAR)
            tracking_option_id1: The tracking option 1 for the Balance Sheet report
            tracking_option_id2: The tracking option 2 for the Balance Sheet report
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.get_balance_sheet(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            date="2019-11-01",
            payments_only=False,
            periods=3,
            standard_layout=True,
            timeframe="MONTH",
            tracking_option_id1="00000000-0000-0000-0000-000000000000",
            tracking_option_id2="00000000-0000-0000-0000-000000000000",
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "date",
                to_encodable(item=date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(payments_only, type_utils.NotGiven):
            encode_query_param(
                _query,
                "paymentsOnly",
                to_encodable(item=payments_only, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(periods, type_utils.NotGiven):
            encode_query_param(
                _query,
                "periods",
                to_encodable(item=periods, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(standard_layout, type_utils.NotGiven):
            encode_query_param(
                _query,
                "standardLayout",
                to_encodable(item=standard_layout, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(timeframe, type_utils.NotGiven):
            encode_query_param(
                _query,
                "timeframe",
                to_encodable(
                    item=timeframe,
                    dump_with=typing_extensions.Literal["MONTH", "QUARTER", "YEAR"],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(tracking_option_id1, type_utils.NotGiven):
            encode_query_param(
                _query,
                "trackingOptionID1",
                to_encodable(item=tracking_option_id1, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(tracking_option_id2, type_utils.NotGiven):
            encode_query_param(
                _query,
                "trackingOptionID2",
                to_encodable(item=tracking_option_id2, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/Reports/BalanceSheet",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    def get_bank_summary(
        self,
        *,
        xero_tenant_id: str,
        from_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        to_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves report for bank summary

        GET /Reports/BankSummary

        Args:
            from_date: filter by the from date of the report e.g. 2021-02-01
            to_date: filter by the to date of the report e.g. 2021-02-28
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.get_bank_summary(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            from_date="2019-10-31",
            to_date="2019-10-31",
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(from_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "fromDate",
                to_encodable(item=from_date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(to_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "toDate",
                to_encodable(item=to_date, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/Reports/BankSummary",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    def get_budget_summary(
        self,
        *,
        xero_tenant_id: str,
        date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        periods: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        timeframe: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves report for budget summary

        GET /Reports/BudgetSummary

        Args:
            date: The date for the Bank Summary report e.g. 2018-03-31
            periods: The number of periods to compare (integer between 1 and 12)
            timeframe: The period size to compare to (1=month, 3=quarter, 12=year)
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            success- return a Report with Rows object

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.get_budget_summary(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            date="2019-03-31",
            periods=2,
            timeframe=3,
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "date",
                to_encodable(item=date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(periods, type_utils.NotGiven):
            encode_query_param(
                _query,
                "periods",
                to_encodable(item=periods, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(timeframe, type_utils.NotGiven):
            encode_query_param(
                _query,
                "timeframe",
                to_encodable(item=timeframe, dump_with=int),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/Reports/BudgetSummary",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    def get_executive_summary(
        self,
        *,
        xero_tenant_id: str,
        date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves report for executive summary

        GET /Reports/ExecutiveSummary

        Args:
            date: The date for the Bank Summary report e.g. 2018-03-31
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.get_executive_summary(
            xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-03-31"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "date",
                to_encodable(item=date, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/Reports/ExecutiveSummary",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    def get_profit_and_loss(
        self,
        *,
        xero_tenant_id: str,
        from_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payments_only: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        periods: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        standard_layout: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        timeframe: typing.Union[
            typing.Optional[typing_extensions.Literal["MONTH", "QUARTER", "YEAR"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        to_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tracking_category_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tracking_category_id2: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tracking_option_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tracking_option_id2: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves report for profit and loss

        GET /Reports/ProfitAndLoss

        Args:
            from_date: filter by the from date of the report e.g. 2021-02-01
            payments_only: Return cash only basis for the ProfitAndLoss report
            periods: The number of periods to compare (integer between 1 and 12)
            standard_layout: Return the standard layout for the ProfitAndLoss report
            timeframe: The period size to compare to (MONTH, QUARTER, YEAR)
            to_date: filter by the to date of the report e.g. 2021-02-28
            tracking_category_id: The trackingCategory 1 for the ProfitAndLoss report
            tracking_category_id2: The trackingCategory 2 for the ProfitAndLoss report
            tracking_option_id: The tracking option 1 for the ProfitAndLoss report
            tracking_option_id2: The tracking option 2 for the ProfitAndLoss report
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.get_profit_and_loss(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            from_date="2019-10-31",
            payments_only=False,
            periods=3,
            standard_layout=True,
            timeframe="MONTH",
            to_date="2019-10-31",
            tracking_category_id="00000000-0000-0000-0000-000000000000",
            tracking_category_id2="00000000-0000-0000-0000-000000000000",
            tracking_option_id="00000000-0000-0000-0000-000000000000",
            tracking_option_id2="00000000-0000-0000-0000-000000000000",
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(from_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "fromDate",
                to_encodable(item=from_date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(payments_only, type_utils.NotGiven):
            encode_query_param(
                _query,
                "paymentsOnly",
                to_encodable(item=payments_only, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(periods, type_utils.NotGiven):
            encode_query_param(
                _query,
                "periods",
                to_encodable(item=periods, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(standard_layout, type_utils.NotGiven):
            encode_query_param(
                _query,
                "standardLayout",
                to_encodable(item=standard_layout, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(timeframe, type_utils.NotGiven):
            encode_query_param(
                _query,
                "timeframe",
                to_encodable(
                    item=timeframe,
                    dump_with=typing_extensions.Literal["MONTH", "QUARTER", "YEAR"],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(to_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "toDate",
                to_encodable(item=to_date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(tracking_category_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "trackingCategoryID",
                to_encodable(item=tracking_category_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(tracking_category_id2, type_utils.NotGiven):
            encode_query_param(
                _query,
                "trackingCategoryID2",
                to_encodable(item=tracking_category_id2, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(tracking_option_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "trackingOptionID",
                to_encodable(item=tracking_option_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(tracking_option_id2, type_utils.NotGiven):
            encode_query_param(
                _query,
                "trackingOptionID2",
                to_encodable(item=tracking_option_id2, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/Reports/ProfitAndLoss",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    def get_ten_ninety_nine(
        self,
        *,
        xero_tenant_id: str,
        report_year: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Reports:
        """
        Retrieve reports for 1099

        GET /Reports/TenNinetyNine

        Args:
            report_year: The year of the 1099 report
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Reports

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.get_ten_ninety_nine(
            xero_tenant_id="YOUR_XERO_TENANT_ID", report_year="2019"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(report_year, type_utils.NotGiven):
            encode_query_param(
                _query,
                "reportYear",
                to_encodable(item=report_year, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/Reports/TenNinetyNine",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Reports,
            request_options=request_options or default_request_options(),
        )

    def get_trial_balance(
        self,
        *,
        xero_tenant_id: str,
        date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payments_only: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves report for trial balance

        GET /Reports/TrialBalance

        Args:
            date: The date for the Trial Balance report e.g. 2018-03-31
            payments_only: Return cash only basis for the Trial Balance report
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.get_trial_balance(
            xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-10-31", payments_only=True
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "date",
                to_encodable(item=date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(payments_only, type_utils.NotGiven):
            encode_query_param(
                _query,
                "paymentsOnly",
                to_encodable(item=payments_only, dump_with=bool),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/Reports/TrialBalance",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        report_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves a specific report using a unique ReportID

        GET /Reports/{ReportID}

        Args:
            report_id: Unique identifier for a Report
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.get(
            report_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Reports/{report_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )


class AsyncReportsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves a list of the organistaions unique reports that require a uuid to fetch

        GET /Reports

        Args:
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/Reports",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    async def get_aged_payables_by_contact(
        self,
        *,
        contact_id: str,
        xero_tenant_id: str,
        date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        from_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        to_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves report for aged payables by contact

        GET /Reports/AgedPayablesByContact

        Args:
            date: The date of the Aged Payables By Contact report
            from_date: filter by the from date of the report e.g. 2021-02-01
            to_date: filter by the to date of the report e.g. 2021-02-28
            contact_id: Unique identifier for a Contact
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.get_aged_payables_by_contact(
            contact_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            date="2019-10-31",
            from_date="2019-10-31",
            to_date="2019-10-31",
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "contactId",
            to_encodable(item=contact_id, dump_with=str),
            style="form",
            explode=True,
        )
        if not isinstance(date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "date",
                to_encodable(item=date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(from_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "fromDate",
                to_encodable(item=from_date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(to_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "toDate",
                to_encodable(item=to_date, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/Reports/AgedPayablesByContact",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    async def get_aged_receivables_by_contact(
        self,
        *,
        contact_id: str,
        xero_tenant_id: str,
        date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        from_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        to_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves report for aged receivables by contact

        GET /Reports/AgedReceivablesByContact

        Args:
            date: The date of the Aged Receivables By Contact report
            from_date: filter by the from date of the report e.g. 2021-02-01
            to_date: filter by the to date of the report e.g. 2021-02-28
            contact_id: Unique identifier for a Contact
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.get_aged_receivables_by_contact(
            contact_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            date="2019-10-31",
            from_date="2019-10-31",
            to_date="2019-10-31",
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "contactId",
            to_encodable(item=contact_id, dump_with=str),
            style="form",
            explode=True,
        )
        if not isinstance(date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "date",
                to_encodable(item=date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(from_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "fromDate",
                to_encodable(item=from_date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(to_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "toDate",
                to_encodable(item=to_date, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/Reports/AgedReceivablesByContact",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    async def get_balance_sheet(
        self,
        *,
        xero_tenant_id: str,
        date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payments_only: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        periods: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        standard_layout: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        timeframe: typing.Union[
            typing.Optional[typing_extensions.Literal["MONTH", "QUARTER", "YEAR"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tracking_option_id1: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tracking_option_id2: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves report for balancesheet

        GET /Reports/BalanceSheet

        Args:
            date: The date of the Balance Sheet report
            payments_only: return a cash basis for the Balance Sheet report
            periods: The number of periods for the Balance Sheet report
            standard_layout: The standard layout boolean for the Balance Sheet report
            timeframe: The period size to compare to (MONTH, QUARTER, YEAR)
            tracking_option_id1: The tracking option 1 for the Balance Sheet report
            tracking_option_id2: The tracking option 2 for the Balance Sheet report
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.get_balance_sheet(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            date="2019-11-01",
            payments_only=False,
            periods=3,
            standard_layout=True,
            timeframe="MONTH",
            tracking_option_id1="00000000-0000-0000-0000-000000000000",
            tracking_option_id2="00000000-0000-0000-0000-000000000000",
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "date",
                to_encodable(item=date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(payments_only, type_utils.NotGiven):
            encode_query_param(
                _query,
                "paymentsOnly",
                to_encodable(item=payments_only, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(periods, type_utils.NotGiven):
            encode_query_param(
                _query,
                "periods",
                to_encodable(item=periods, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(standard_layout, type_utils.NotGiven):
            encode_query_param(
                _query,
                "standardLayout",
                to_encodable(item=standard_layout, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(timeframe, type_utils.NotGiven):
            encode_query_param(
                _query,
                "timeframe",
                to_encodable(
                    item=timeframe,
                    dump_with=typing_extensions.Literal["MONTH", "QUARTER", "YEAR"],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(tracking_option_id1, type_utils.NotGiven):
            encode_query_param(
                _query,
                "trackingOptionID1",
                to_encodable(item=tracking_option_id1, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(tracking_option_id2, type_utils.NotGiven):
            encode_query_param(
                _query,
                "trackingOptionID2",
                to_encodable(item=tracking_option_id2, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/Reports/BalanceSheet",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    async def get_bank_summary(
        self,
        *,
        xero_tenant_id: str,
        from_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        to_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves report for bank summary

        GET /Reports/BankSummary

        Args:
            from_date: filter by the from date of the report e.g. 2021-02-01
            to_date: filter by the to date of the report e.g. 2021-02-28
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.get_bank_summary(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            from_date="2019-10-31",
            to_date="2019-10-31",
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(from_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "fromDate",
                to_encodable(item=from_date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(to_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "toDate",
                to_encodable(item=to_date, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/Reports/BankSummary",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    async def get_budget_summary(
        self,
        *,
        xero_tenant_id: str,
        date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        periods: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        timeframe: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves report for budget summary

        GET /Reports/BudgetSummary

        Args:
            date: The date for the Bank Summary report e.g. 2018-03-31
            periods: The number of periods to compare (integer between 1 and 12)
            timeframe: The period size to compare to (1=month, 3=quarter, 12=year)
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            success- return a Report with Rows object

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.get_budget_summary(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            date="2019-03-31",
            periods=2,
            timeframe=3,
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "date",
                to_encodable(item=date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(periods, type_utils.NotGiven):
            encode_query_param(
                _query,
                "periods",
                to_encodable(item=periods, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(timeframe, type_utils.NotGiven):
            encode_query_param(
                _query,
                "timeframe",
                to_encodable(item=timeframe, dump_with=int),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/Reports/BudgetSummary",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    async def get_executive_summary(
        self,
        *,
        xero_tenant_id: str,
        date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves report for executive summary

        GET /Reports/ExecutiveSummary

        Args:
            date: The date for the Bank Summary report e.g. 2018-03-31
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.get_executive_summary(
            xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-03-31"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "date",
                to_encodable(item=date, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/Reports/ExecutiveSummary",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    async def get_profit_and_loss(
        self,
        *,
        xero_tenant_id: str,
        from_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payments_only: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        periods: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        standard_layout: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        timeframe: typing.Union[
            typing.Optional[typing_extensions.Literal["MONTH", "QUARTER", "YEAR"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        to_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tracking_category_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tracking_category_id2: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tracking_option_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tracking_option_id2: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves report for profit and loss

        GET /Reports/ProfitAndLoss

        Args:
            from_date: filter by the from date of the report e.g. 2021-02-01
            payments_only: Return cash only basis for the ProfitAndLoss report
            periods: The number of periods to compare (integer between 1 and 12)
            standard_layout: Return the standard layout for the ProfitAndLoss report
            timeframe: The period size to compare to (MONTH, QUARTER, YEAR)
            to_date: filter by the to date of the report e.g. 2021-02-28
            tracking_category_id: The trackingCategory 1 for the ProfitAndLoss report
            tracking_category_id2: The trackingCategory 2 for the ProfitAndLoss report
            tracking_option_id: The tracking option 1 for the ProfitAndLoss report
            tracking_option_id2: The tracking option 2 for the ProfitAndLoss report
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.get_profit_and_loss(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            from_date="2019-10-31",
            payments_only=False,
            periods=3,
            standard_layout=True,
            timeframe="MONTH",
            to_date="2019-10-31",
            tracking_category_id="00000000-0000-0000-0000-000000000000",
            tracking_category_id2="00000000-0000-0000-0000-000000000000",
            tracking_option_id="00000000-0000-0000-0000-000000000000",
            tracking_option_id2="00000000-0000-0000-0000-000000000000",
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(from_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "fromDate",
                to_encodable(item=from_date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(payments_only, type_utils.NotGiven):
            encode_query_param(
                _query,
                "paymentsOnly",
                to_encodable(item=payments_only, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(periods, type_utils.NotGiven):
            encode_query_param(
                _query,
                "periods",
                to_encodable(item=periods, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(standard_layout, type_utils.NotGiven):
            encode_query_param(
                _query,
                "standardLayout",
                to_encodable(item=standard_layout, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(timeframe, type_utils.NotGiven):
            encode_query_param(
                _query,
                "timeframe",
                to_encodable(
                    item=timeframe,
                    dump_with=typing_extensions.Literal["MONTH", "QUARTER", "YEAR"],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(to_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "toDate",
                to_encodable(item=to_date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(tracking_category_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "trackingCategoryID",
                to_encodable(item=tracking_category_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(tracking_category_id2, type_utils.NotGiven):
            encode_query_param(
                _query,
                "trackingCategoryID2",
                to_encodable(item=tracking_category_id2, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(tracking_option_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "trackingOptionID",
                to_encodable(item=tracking_option_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(tracking_option_id2, type_utils.NotGiven):
            encode_query_param(
                _query,
                "trackingOptionID2",
                to_encodable(item=tracking_option_id2, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/Reports/ProfitAndLoss",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    async def get_ten_ninety_nine(
        self,
        *,
        xero_tenant_id: str,
        report_year: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Reports:
        """
        Retrieve reports for 1099

        GET /Reports/TenNinetyNine

        Args:
            report_year: The year of the 1099 report
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Reports

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.get_ten_ninety_nine(
            xero_tenant_id="YOUR_XERO_TENANT_ID", report_year="2019"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(report_year, type_utils.NotGiven):
            encode_query_param(
                _query,
                "reportYear",
                to_encodable(item=report_year, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/Reports/TenNinetyNine",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Reports,
            request_options=request_options or default_request_options(),
        )

    async def get_trial_balance(
        self,
        *,
        xero_tenant_id: str,
        date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payments_only: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves report for trial balance

        GET /Reports/TrialBalance

        Args:
            date: The date for the Trial Balance report e.g. 2018-03-31
            payments_only: Return cash only basis for the Trial Balance report
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.get_trial_balance(
            xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-10-31", payments_only=True
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "date",
                to_encodable(item=date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(payments_only, type_utils.NotGiven):
            encode_query_param(
                _query,
                "paymentsOnly",
                to_encodable(item=payments_only, dump_with=bool),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/Reports/TrialBalance",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        report_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportWithRows:
        """
        Retrieves a specific report using a unique ReportID

        GET /Reports/{ReportID}

        Args:
            report_id: Unique identifier for a Report
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ReportWithRows

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.get(
            report_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Reports/{report_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.ReportWithRows,
            request_options=request_options or default_request_options(),
        )
