import os

import pandas as pd
import pytest

from finrashortdata import (auth, bi_monthly_shorts,
                            bi_monthly_shorts_chunk_and_size)


async def test_bi_monthly_shorts_positive() -> bool:
    client_id = os.getenv("TEST_API_CLIENT_ID", None)
    secret = os.getenv("TEST_API_SECRET", None)

    if not client_id or not secret:
        raise AssertionError(
            "tests require env variables TEST_API_CLIENT_ID, TEST_API_SECRET"
        )
    token = auth(client_id, secret)
    chunk, max_data = bi_monthly_shorts_chunk_and_size(token)
    _df: pd.DataFrame = await bi_monthly_shorts(
        token=token, offset=max_data - chunk
    )
    print(_df)

    return True


async def test_bi_monthly_shorts_positive_limit() -> bool:
    client_id = os.getenv("TEST_API_CLIENT_ID", None)
    secret = os.getenv("TEST_API_SECRET", None)

    if not client_id or not secret:
        raise AssertionError(
            "tests require env variables TEST_API_CLIENT_ID, TEST_API_SECRET"
        )
    token = auth(client_id, secret)
    chunk, max_data = bi_monthly_shorts_chunk_and_size(token)
    _df: pd.DataFrame = await bi_monthly_shorts(
        token=token, offset=0, limit=chunk
    )
    print(_df)

    return True
