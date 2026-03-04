# projects.time

## Module Functions

### Deletes a time entry for a specific project <a name="delete"></a>

Allows you to delete a specific time entry

**API Endpoint**: `DELETE /Projects/{projectId}/Time/{timeEntryId}`

#### Parameters

| Parameter        | Required | Description                                                                      | Example                                  |
| ---------------- | :------: | -------------------------------------------------------------------------------- | ---------------------------------------- |
| `project_id`     |    ✓     | You can specify an individual project by appending the projectId to the endpoint | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `time_entry_id`  |    ✓     | You can specify an individual task by appending the id to the endpoint           | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                       | `"string"`                               |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.projects.time.delete(
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    xero_tenant_id="string",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.projects.time.delete(
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    xero_tenant_id="string",
)
```

### Retrieves all time entries associated with a specific project <a name="list"></a>

Allows you to retrieve the time entries associated with a specific project

**API Endpoint**: `GET /Projects/{projectId}/Time`

#### Parameters

| Parameter         | Required | Description                                                                                                                            | Example                                  |
| ----------------- | :------: | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `project_id`      |    ✓     | Identifier of the project, that the task (which the time entry is logged against) belongs to.                                          | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `xero_tenant_id`  |    ✓     | Xero identifier for Tenant                                                                                                             | `"string"`                               |
| `contact_id`      |    ✗     | Finds all time entries for this contact identifier.                                                                                    | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `date_after_utc`  |    ✗     | ISO 8601 UTC date. Finds all time entries on or after this date filtered on the `dateUtc` field.                                       | `"1970-01-01T00:00:00"`                  |
| `date_before_utc` |    ✗     | ISO 8601 UTC date. Finds all time entries on or before this date filtered on the `dateUtc` field.                                      | `"1970-01-01T00:00:00"`                  |
| `invoice_id`      |    ✗     | Finds all time entries for this invoice.                                                                                               | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `is_chargeable`   |    ✗     | Finds all time entries which relate to tasks with the charge type `TIME` or `FIXED`.                                                   | `True`                                   |
| `page`            |    ✗     | Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.                             | `1`                                      |
| `page_size`       |    ✗     | Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500. | `10`                                     |
| `states`          |    ✗     | Comma-separated list of states to find. Will find all time entries that are in the status of whatever is specified.                    | `["string"]`                             |
| `task_id`         |    ✗     | Identifier of the task that time entry is logged against.                                                                              | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `user_id`         |    ✗     | The xero user identifier of the person who logged time.                                                                                | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.projects.time.list(
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    xero_tenant_id="string",
    page=1,
    page_size=10,
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.projects.time.list(
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    xero_tenant_id="string",
    page=1,
    page_size=10,
)
```

#### Response

##### Type

[TimeEntries](/xero_accounting_py/types/models/time_entries.py)

##### Example

```python
{}
```

### Retrieves a single time entry for a specific project <a name="get"></a>

Allows you to get a single time entry in a project

**API Endpoint**: `GET /Projects/{projectId}/Time/{timeEntryId}`

#### Parameters

| Parameter        | Required | Description                                                                      | Example                                  |
| ---------------- | :------: | -------------------------------------------------------------------------------- | ---------------------------------------- |
| `project_id`     |    ✓     | You can specify an individual project by appending the projectId to the endpoint | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `time_entry_id`  |    ✓     | You can specify an individual time entry by appending the id to the endpoint     | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                       | `"string"`                               |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.projects.time.get(
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    xero_tenant_id="string",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.projects.time.get(
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    xero_tenant_id="string",
)
```

#### Response

##### Type

[TimeEntry](/xero_accounting_py/types/models/time_entry.py)

##### Example

```python
{"project_id": "00000000-0000-0000-000-000000000000", "task_id": "00000000-0000-0000-000-000000000000", "time_entry_id": "00000000-0000-0000-000-000000000000", "user_id": "00000000-0000-0000-000-000000000000"}
```

### Creates a time entry for a specific project <a name="create"></a>

Allows you to create a specific task

**API Endpoint**: `POST /Projects/{projectId}/Time`

#### Parameters

| Parameter        | Required | Description                                                                                   | Example                                  |
| ---------------- | :------: | --------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `date_utc`       |    ✓     | Date time entry is logged on. UTC Date Time in ISO-8601 format.                               | `"1970-01-01T00:00:00"`                  |
| `duration`       |    ✓     | Number of minutes to be logged. Duration is between 1 and 59940 inclusively.                  | `123`                                    |
| `project_id`     |    ✓     | You can specify an individual project by appending the projectId to the endpoint              | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `task_id`        |    ✓     | Identifier of the task that time entry is logged against.                                     | `"00000000-0000-0000-000-000000000000"`  |
| `user_id`        |    ✓     | The xero user identifier of the person logging the time.                                      | `"00000000-0000-0000-000-000000000000"`  |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                    | `"string"`                               |
| `description`    |    ✗     | An optional description of the time entry, will be set to null if not provided during update. | `"string"`                               |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.projects.time.create(
    date_utc="2020-02-26T15:00:00Z",
    duration=30,
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    task_id="00000000-0000-0000-0000-000000000000",
    user_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="string",
    description="My description",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.projects.time.create(
    date_utc="2020-02-26T15:00:00Z",
    duration=30,
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    task_id="00000000-0000-0000-0000-000000000000",
    user_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="string",
    description="My description",
)
```

#### Response

##### Type

[TimeEntry](/xero_accounting_py/types/models/time_entry.py)

##### Example

```python
{"project_id": "00000000-0000-0000-000-000000000000", "task_id": "00000000-0000-0000-000-000000000000", "time_entry_id": "00000000-0000-0000-000-000000000000", "user_id": "00000000-0000-0000-000-000000000000"}
```

### Updates a time entry for a specific project <a name="update"></a>

Allows you to update time entry in a project

**API Endpoint**: `PUT /Projects/{projectId}/Time/{timeEntryId}`

#### Parameters

| Parameter        | Required | Description                                                                                   | Example                                  |
| ---------------- | :------: | --------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `date_utc`       |    ✓     | Date time entry is logged on. UTC Date Time in ISO-8601 format.                               | `"1970-01-01T00:00:00"`                  |
| `duration`       |    ✓     | Number of minutes to be logged. Duration is between 1 and 59940 inclusively.                  | `123`                                    |
| `project_id`     |    ✓     | You can specify an individual project by appending the projectId to the endpoint              | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `task_id`        |    ✓     | Identifier of the task that time entry is logged against.                                     | `"00000000-0000-0000-000-000000000000"`  |
| `time_entry_id`  |    ✓     | You can specify an individual time entry by appending the id to the endpoint                  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `user_id`        |    ✓     | The xero user identifier of the person logging the time.                                      | `"00000000-0000-0000-000-000000000000"`  |
| `xero_tenant_id` |    ✓     | Xero identifier for Tenant                                                                    | `"string"`                               |
| `description`    |    ✗     | An optional description of the time entry, will be set to null if not provided during update. | `"string"`                               |

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(oauth_token=getenv("API_TOKEN"))
res = client.projects.time.update(
    date_utc="2020-02-27T15:00:00Z",
    duration=45,
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    task_id="00000000-0000-0000-0000-000000000000",
    time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    user_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="string",
    description="My UPDATED description",
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(oauth_token=getenv("API_TOKEN"))
res = await client.projects.time.update(
    date_utc="2020-02-27T15:00:00Z",
    duration=45,
    project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    task_id="00000000-0000-0000-0000-000000000000",
    time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    user_id="00000000-0000-0000-0000-000000000000",
    xero_tenant_id="string",
    description="My UPDATED description",
)
```
