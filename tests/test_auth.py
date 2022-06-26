import os

import pytest

from finrashortdata import auth


def test_auth_positive() -> bool:
    client_id = os.getenv("TEST_API_CLIENT_ID", None)
    secret = os.getenv("TEST_API_SECRET", None)

    if not client_id or not secret:
        raise AssertionError(
            "tests require env variables TEST_API_CLIENT_ID, TEST_API_SECRET"
        )

    token = auth(client_id, secret)

    print(token)

    return True


def test_auth_no_type() -> bool:
    try:
        auth()  # type: ignore
    except TypeError:
        return True

    raise AssertionError("Excepted TypeError exception")


def test_auth_no_secret() -> bool:
    try:
        auth("id1")  # type: ignore
    except TypeError:
        return True

    raise AssertionError("Excepted TypeError exception")


def test_auth_none_values() -> bool:
    try:
        auth(None, "secret")  # type: ignore
    except TypeError:
        return True

    raise AssertionError("Excepted TypeError exception")
