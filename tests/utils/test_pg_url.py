import os
from typing import Literal


def set_variable_for_context(local_value, CI_value):
    running_in_CI = os.environ.get("CI", False)
    if running_in_CI:
        return CI_value
    return local_value


port: int = set_variable_for_context(local_value=5433, CI_value=5432)
host: Literal["localhost", "postgres"] = set_variable_for_context(
    local_value="localhost", CI_value="postgres"
)

test_pg_url = f"postgresql://postgres:pg-password@{host}:{port}/xq-db"
