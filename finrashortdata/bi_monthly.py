import asyncio
import concurrent.futures
import time
from typing import Optional, Tuple

import pandas as pd
import requests

from .decorators import timeit

url: str = "https://api.finra.org/data/group/otcMarket/name/equityShortInterestStandardized"


def _requests_get(token: str, chunk_size: int, offset: int) -> pd.DataFrame:
    r = requests.get(
        url=url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        },
        params={"limit": chunk_size, "offset": offset},
    )
    r.raise_for_status()

    if r.status_code in (429, 502):
        print(f"{url} return {r.status_code}, waiting and re-trying")
        time.sleep(10)
        return _requests_get(token, chunk_size, offset)

    x = r.json()
    df = pd.DataFrame(x)
    df.rename(
        columns={
            "securitiesInformationProcessorSymbolIdentifier": "symbol",
        },
        inplace=True,
    )
    df.drop(["issueName", "marketClassCode"], axis=1, inplace=True)
    return df


def bi_monthly_shorts_chunk_and_size(token: str) -> Tuple[int, int]:
    """Return the optimal chunk size and total number of data-points,

    Chunk size is used internally, by the bi_monthly_shorts() function
    to reduce the number of calls to the FINRA end-point,
    it is also used as the 'offset' step when calling bi_monthly_shorts() directly with restrictions.

    Input Arguments: token obtained from the auth() function.
    Returns: tuple with chunk size followed by number of data-points to be loaded from FINRA end-point.
    """
    r = requests.get(
        url=url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        },
        params={"limit": 1},
    )
    print(r.headers)
    r.raise_for_status()
    return int(r.headers["Record-Max-Limit"]), int(r.headers["Record-Total"])


@timeit
async def bi_monthly_shorts(
    token: str, offset: int = 0, limit: Optional[int] = None
) -> pd.DataFrame:
    """Download Bi-Monthly Short details

    Input Arguments:
        token -> obtained from the auth() function.
        offset -> starting point (default 0).
        limit -> end point (default not limit).
    Returns: If successful returns DataFrame with all details
    """
    chunk_size, max_records = bi_monthly_shorts_chunk_and_size(token)
    if limit:
        max_records = min(max_records, limit)

    print(
        f"loading data (chunk_size={chunk_size}, offset={offset}, max_records={max_records-offset})..."
    )
    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor, _requests_get, token, chunk_size, offset
            )
            for offset in range(offset, max_records, chunk_size)
        ]
        df = pd.concat(await asyncio.gather(*futures)).set_index(
            ["settlementDate", "symbol"]
        )

    return df
