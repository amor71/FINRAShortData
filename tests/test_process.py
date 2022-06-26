import os

import pandas as pd
import pytest

from finrashortdata import auth, get_chunk_and_size, process


async def test_process_positive() -> bool:
    client_id = os.getenv("TEST_API_CLIENT_ID", None)
    secret = os.getenv("TEST_API_SECRET", None)

    if not client_id or not secret:
        raise AssertionError(
            "tests require env variables TEST_API_CLIENT_ID, TEST_API_SECRET"
        )
    token = auth(client_id, secret)
    chunk, max_data = get_chunk_and_size(token)
    _df: pd.DataFrame = await process(
        token=token, offset=max_data - 10 * chunk
    )
    print(_df)

    return True
