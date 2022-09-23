import io
from datetime import date, datetime, timezone
from typing import List, Optional

import pandas as pd
import pandas_market_calendars
import requests

from .decorators import timeit


def _short_by_date(d: datetime) -> pd.DataFrame:
    base_url = f'https://cdn.finra.org/equity/regsho/daily/CNMSshvol{d.strftime("%Y%m%d")}.txt'
    content = requests.get(base_url).content
    df = pd.read_csv(
        io.StringIO(content.decode("utf-8")),
        sep="|",
        engine="python",
        skipfooter=1,
        keep_default_na=False,
    )
    df["date"] = d.date()

    if not df.empty:
        del df["Date"]
        df["ShortPercent"] = round(
            100.0 * df["ShortVolume"] / df["TotalVolume"], 2
        )
        df["ShortExemptPercent"] = round(
            100.0 * df["ShortExemptVolume"] / df["TotalVolume"], 2
        )
        return df.set_index(["Symbol", "date"]).sort_index().dropna()

    return df


def _get_trading_holidays(
    mcal: pandas_market_calendars.MarketCalendar,
) -> List[str]:
    return mcal.holidays().holidays


def _calc_start_date_from_offset(
    mcal: pandas_market_calendars.MarketCalendar, end_date: date, offset: int
) -> date:
    cbd_offset = pd.tseries.offsets.CustomBusinessDay(
        n=offset - 1, holidays=_get_trading_holidays(mcal)
    )
    return (datetime.now(timezone.utc) - cbd_offset).date()


def _short_iterator(days: List) -> pd.DataFrame:
    df = pd.DataFrame()
    for day in days:
        day_df = _short_by_date(day)
        if not day_df.empty:
            df = (
                day_df
                if df.empty
                else pd.concat([df, day_df], axis=0).sort_index()
            )

    return df


@timeit
async def daily_shorts(
    start_date: Optional[date] = None,
    end_date: Optional[date] = date.today(),
    offset: Optional[int] = None,
) -> pd.DataFrame:
    """Download Daily Short details

    Input Arguments:
        start_date -> Optional, start date for pulling short-date.
        end_date -> last date (inclusive) for pulling short-date.
        offset -> If start_date not provided, calculate start date as offset from end_date.
    Returns: If successful returns DataFrame with all details
    """
    if not start_date and not offset:
        raise ValueError(
            "daily_shorts(): must have either start_date or offset"
        )
    elif not start_date and offset < 1:  # type: ignore
        raise ValueError("daily_shorts(): offset >= 1")

    nyse = pandas_market_calendars.get_calendar("NYSE")
    if not start_date:
        start_date = _calc_start_date_from_offset(nyse, end_date, offset)  # type: ignore

    schedule = nyse.schedule(start_date=start_date, end_date=end_date)
    days = schedule.index.to_list()

    return _short_iterator(days) if len(days) else pd.DataFrame()
