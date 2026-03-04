import enum
import typing
import typing_extensions


class Environment(enum.Enum):
    """Pre-defined base URLs for the API"""

    ACCOUNTING = "https://api.xero.com/api.xro/2.0"
    PROJECTS = "https://api.xero.com/projects.xro/2.0"
    XERO_ACCOUNTING_MOCK_SERVER = (
        "https://api.sideko.dev/v1/mock/public/xero-accounting/0.1.3"
    )
    XERO_PROJECTS_MOCK_SERVER = (
        "https://api.sideko.dev/v1/mock/public/xero-projects/0.1.0"
    )


class ServerGroup(typing_extensions.TypedDict):
    """Pre-defined set of base URLs for the APIs serviced by this SDK"""

    accounting: typing_extensions.NotRequired[typing.Union[Environment, str]]
    projects: typing_extensions.NotRequired[typing.Union[Environment, str]]


DEFAULT: ServerGroup = {
    "accounting": Environment.ACCOUNTING.value,
    "projects": Environment.PROJECTS.value,
}

SIDEKO_MOCK_SERVER: ServerGroup = {
    "accounting": Environment.XERO_ACCOUNTING_MOCK_SERVER.value,
    "projects": Environment.XERO_PROJECTS_MOCK_SERVER.value,
}


def _get_base_url(
    server_group: ServerGroup,
    api: typing.Literal["accounting", "projects"],
    default: typing.Union[Environment, str],
) -> str:
    env_or_str = server_group.get(api, default)
    if isinstance(env_or_str, Environment):
        return env_or_str.value
    else:
        return str(env_or_str)
