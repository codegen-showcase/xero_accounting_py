# reports

## Module Functions

### Retrieves a list of the organistaions unique reports that require a uuid to fetch <a name="list"></a>

**API Endpoint**: `GET /Reports`

#### Parameters

| Parameter        | Required | Description                | Example                 |
| ---------------- | :------: | -------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant | `"YOUR_XERO_TENANT_ID"` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = client.reports.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.reports.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
```

#### Response

##### Type

[ReportWithRows](/xero_accounting_py/types/models/report_with_rows.py)

##### Example

```python
{}
```

### Retrieves report for aged payables by contact <a name="get_aged_payables_by_contact"></a>

**API Endpoint**: `GET /Reports/AgedPayablesByContact`

#### Parameters

| Parameter        | Required | Description                                           | Example                                  |
| ---------------- | :------: | ----------------------------------------------------- | ---------------------------------------- |
| `contact_id`     |    ✓     | Unique identifier for a Contact                       | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                            | `"YOUR_XERO_TENANT_ID"`                  |
| `date`           |    ✗     | The date of the Aged Payables By Contact report       | `"2019-10-31"`                           |
| `from_date`      |    ✗     | filter by the from date of the report e.g. 2021-02-01 | `"2019-10-31"`                           |
| `to_date`        |    ✗     | filter by the to date of the report e.g. 2021-02-28   | `"2019-10-31"`                           |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = client.reports.get_aged_payables_by_contact(
    contact_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    date="2019-10-31",
    from_date="2019-10-31",
    to_date="2019-10-31",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.reports.get_aged_payables_by_contact(
    contact_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    date="2019-10-31",
    from_date="2019-10-31",
    to_date="2019-10-31",
)
```

#### Response

##### Type

[ReportWithRows](/xero_accounting_py/types/models/report_with_rows.py)

##### Example

```python
{}
```

### Retrieves report for aged receivables by contact <a name="get_aged_receivables_by_contact"></a>

**API Endpoint**: `GET /Reports/AgedReceivablesByContact`

#### Parameters

| Parameter        | Required | Description                                           | Example                                  |
| ---------------- | :------: | ----------------------------------------------------- | ---------------------------------------- |
| `contact_id`     |    ✓     | Unique identifier for a Contact                       | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                            | `"YOUR_XERO_TENANT_ID"`                  |
| `date`           |    ✗     | The date of the Aged Receivables By Contact report    | `"2019-10-31"`                           |
| `from_date`      |    ✗     | filter by the from date of the report e.g. 2021-02-01 | `"2019-10-31"`                           |
| `to_date`        |    ✗     | filter by the to date of the report e.g. 2021-02-28   | `"2019-10-31"`                           |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = client.reports.get_aged_receivables_by_contact(
    contact_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    date="2019-10-31",
    from_date="2019-10-31",
    to_date="2019-10-31",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.reports.get_aged_receivables_by_contact(
    contact_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    date="2019-10-31",
    from_date="2019-10-31",
    to_date="2019-10-31",
)
```

#### Response

##### Type

[ReportWithRows](/xero_accounting_py/types/models/report_with_rows.py)

##### Example

```python
{}
```

### Retrieves report for balancesheet <a name="get_balance_sheet"></a>

**API Endpoint**: `GET /Reports/BalanceSheet`

#### Parameters

| Parameter             | Required | Description                                              | Example                                  |
| --------------------- | :------: | -------------------------------------------------------- | ---------------------------------------- |
| `xero_tenant_id`      |    ✓     | Xero identifier for Tenant                               | `"YOUR_XERO_TENANT_ID"`                  |
| `date`                |    ✗     | The date of the Balance Sheet report                     | `"2019-11-01"`                           |
| `payments_only`       |    ✗     | return a cash basis for the Balance Sheet report         | `False`                                  |
| `periods`             |    ✗     | The number of periods for the Balance Sheet report       | `3`                                      |
| `standard_layout`     |    ✗     | The standard layout boolean for the Balance Sheet report | `True`                                   |
| `timeframe`           |    ✗     | The period size to compare to (MONTH, QUARTER, YEAR)     | `"MONTH"`                                |
| `tracking_option_id1` |    ✗     | The tracking option 1 for the Balance Sheet report       | `"00000000-0000-0000-0000-000000000000"` |
| `tracking_option_id2` |    ✗     | The tracking option 2 for the Balance Sheet report       | `"00000000-0000-0000-0000-000000000000"` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = client.reports.get_balance_sheet(
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

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.reports.get_balance_sheet(
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

#### Response

##### Type

[ReportWithRows](/xero_accounting_py/types/models/report_with_rows.py)

##### Example

```python
{}
```

### Retrieves report for bank summary <a name="get_bank_summary"></a>

**API Endpoint**: `GET /Reports/BankSummary`

#### Parameters

| Parameter        | Required | Description                                           | Example                 |
| ---------------- | :------: | ----------------------------------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                            | `"YOUR_XERO_TENANT_ID"` |
| `from_date`      |    ✗     | filter by the from date of the report e.g. 2021-02-01 | `"2019-10-31"`          |
| `to_date`        |    ✗     | filter by the to date of the report e.g. 2021-02-28   | `"2019-10-31"`          |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = client.reports.get_bank_summary(
    xero_tenant_id="YOUR_XERO_TENANT_ID", from_date="2019-10-31", to_date="2019-10-31"
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.reports.get_bank_summary(
    xero_tenant_id="YOUR_XERO_TENANT_ID", from_date="2019-10-31", to_date="2019-10-31"
)
```

#### Response

##### Type

[ReportWithRows](/xero_accounting_py/types/models/report_with_rows.py)

##### Example

```python
{}
```

### Retrieves report for budget summary <a name="get_budget_summary"></a>

**API Endpoint**: `GET /Reports/BudgetSummary`

#### Parameters

| Parameter        | Required | Description                                                 | Example                 |
| ---------------- | :------: | ----------------------------------------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                  | `"YOUR_XERO_TENANT_ID"` |
| `date`           |    ✗     | The date for the Bank Summary report e.g. 2018-03-31        | `"2019-03-31"`          |
| `periods`        |    ✗     | The number of periods to compare (integer between 1 and 12) | `2`                     |
| `timeframe`      |    ✗     | The period size to compare to (1=month, 3=quarter, 12=year) | `3`                     |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = client.reports.get_budget_summary(
    xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-03-31", periods=2, timeframe=3
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.reports.get_budget_summary(
    xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-03-31", periods=2, timeframe=3
)
```

#### Response

##### Type

[ReportWithRows](/xero_accounting_py/types/models/report_with_rows.py)

##### Example

```python
{}
```

### Retrieves report for executive summary <a name="get_executive_summary"></a>

**API Endpoint**: `GET /Reports/ExecutiveSummary`

#### Parameters

| Parameter        | Required | Description                                          | Example                 |
| ---------------- | :------: | ---------------------------------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                           | `"YOUR_XERO_TENANT_ID"` |
| `date`           |    ✗     | The date for the Bank Summary report e.g. 2018-03-31 | `"2019-03-31"`          |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = client.reports.get_executive_summary(
    xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-03-31"
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.reports.get_executive_summary(
    xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-03-31"
)
```

#### Response

##### Type

[ReportWithRows](/xero_accounting_py/types/models/report_with_rows.py)

##### Example

```python
{}
```

### Retrieves report for profit and loss <a name="get_profit_and_loss"></a>

**API Endpoint**: `GET /Reports/ProfitAndLoss`

#### Parameters

| Parameter               | Required | Description                                                 | Example                                  |
| ----------------------- | :------: | ----------------------------------------------------------- | ---------------------------------------- |
| `xero_tenant_id`        |    ✓     | Xero identifier for Tenant                                  | `"YOUR_XERO_TENANT_ID"`                  |
| `from_date`             |    ✗     | filter by the from date of the report e.g. 2021-02-01       | `"2019-10-31"`                           |
| `payments_only`         |    ✗     | Return cash only basis for the ProfitAndLoss report         | `True`                                   |
| `periods`               |    ✗     | The number of periods to compare (integer between 1 and 12) | `3`                                      |
| `standard_layout`       |    ✗     | Return the standard layout for the ProfitAndLoss report     | `True`                                   |
| `timeframe`             |    ✗     | The period size to compare to (MONTH, QUARTER, YEAR)        | `"MONTH"`                                |
| `to_date`               |    ✗     | filter by the to date of the report e.g. 2021-02-28         | `"2019-10-31"`                           |
| `tracking_category_id`  |    ✗     | The trackingCategory 1 for the ProfitAndLoss report         | `"00000000-0000-0000-0000-000000000000"` |
| `tracking_category_id2` |    ✗     | The trackingCategory 2 for the ProfitAndLoss report         | `"00000000-0000-0000-0000-000000000000"` |
| `tracking_option_id`    |    ✗     | The tracking option 1 for the ProfitAndLoss report          | `"00000000-0000-0000-0000-000000000000"` |
| `tracking_option_id2`   |    ✗     | The tracking option 2 for the ProfitAndLoss report          | `"00000000-0000-0000-0000-000000000000"` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = client.reports.get_profit_and_loss(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    from_date="2019-10-31",
    payments_only=True,
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

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.reports.get_profit_and_loss(
    xero_tenant_id="YOUR_XERO_TENANT_ID",
    from_date="2019-10-31",
    payments_only=True,
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

#### Response

##### Type

[ReportWithRows](/xero_accounting_py/types/models/report_with_rows.py)

##### Example

```python
{}
```

### Retrieve reports for 1099 <a name="get_ten_ninety_nine"></a>

**API Endpoint**: `GET /Reports/TenNinetyNine`

#### Parameters

| Parameter        | Required | Description                 | Example                 |
| ---------------- | :------: | --------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant  | `"YOUR_XERO_TENANT_ID"` |
| `report_year`    |    ✗     | The year of the 1099 report | `"2019"`                |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = client.reports.get_ten_ninety_nine(
    xero_tenant_id="YOUR_XERO_TENANT_ID", report_year="2019"
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.reports.get_ten_ninety_nine(
    xero_tenant_id="YOUR_XERO_TENANT_ID", report_year="2019"
)
```

#### Response

##### Type

[Reports](/xero_accounting_py/types/models/reports.py)

##### Example

```python
{}
```

### Retrieves report for trial balance <a name="get_trial_balance"></a>

**API Endpoint**: `GET /Reports/TrialBalance`

#### Parameters

| Parameter        | Required | Description                                           | Example                 |
| ---------------- | :------: | ----------------------------------------------------- | ----------------------- |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                            | `"YOUR_XERO_TENANT_ID"` |
| `date`           |    ✗     | The date for the Trial Balance report e.g. 2018-03-31 | `"2019-10-31"`          |
| `payments_only`  |    ✗     | Return cash only basis for the Trial Balance report   | `True`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = client.reports.get_trial_balance(
    xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-10-31", payments_only=True
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.reports.get_trial_balance(
    xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-10-31", payments_only=True
)
```

#### Response

##### Type

[ReportWithRows](/xero_accounting_py/types/models/report_with_rows.py)

##### Example

```python
{}
```

### Retrieves a specific report using a unique ReportID <a name="get"></a>

**API Endpoint**: `GET /Reports/{ReportID}`

#### Parameters

| Parameter        | Required | Description                    | Example                                  |
| ---------------- | :------: | ------------------------------ | ---------------------------------------- |
| `report_id`      |    ✓     | Unique identifier for a Report | `"00000000-0000-0000-0000-000000000000"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant     | `"YOUR_XERO_TENANT_ID"`                  |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = client.reports.get(
    report_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.reports.get(
    report_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="YOUR_XERO_TENANT_ID",
)
```

#### Response

##### Type

[ReportWithRows](/xero_accounting_py/types/models/report_with_rows.py)

##### Example

```python
{}
```
