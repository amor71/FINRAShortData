[![Python 3](https://pyup.io/repos/github/amor71/FINRAShortData/python-3-shield.svg)](https://pyup.io/repos/github/amor71/FINRAShortData/)
[![Updates](https://pyup.io/repos/github/amor71/FINRAShortData/shield.svg)](https://pyup.io/repos/github/amor71/FINRAShortData/)
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)
[![codecov](https://codecov.io/gh/amor71/FINRAShortData/branch/main/graph/badge.svg?token=Gy7JKcpOqh)](https://codecov.io/gh/amor71/FINRAShortData)

# FINRAShortData

Process FINRA Short Daily Data [feeds](https://www.finra.org/finra-data/browse-catalog/short-sale-volume-data/daily-short-sale-volume-files)

## Install

To install the package type:

`pip install finrashortdata`

## Quick start

### Example 1: Daily Short Volumes for past 2 days (inclusive)

```python
import asyncio
from finrashortdata import daily_shorts
import pandas as pd

df : pd.DataFrame = asyncio.run(daily_shorts(offset=2))
```

### Example 2: Daily Short Volumes for time_range

```python
import asyncio
from finrashortdata import daily_shorts
from datetime import date
import pandas as pd

df : pd.DataFrame = asyncio.run(daily_shorts(
    start_date=date(year=2022, month=9, day=1), 
    end_date=date(year=2022, month=9, day=10)))
```

*Scripts work as-is*

## Licensing

[GNU GPL v.3](https://github.com/amor71/FINRAShortData/blob/main/LICENSE)

## Questions & Comments

Use the [Issues](https://github.com/amor71/FINRAShortData/issues) section

## Contributing

If you'd like to contribute to the project, drop me a line at mailto:amor71@sgeltd.com
