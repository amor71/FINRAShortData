[![Python 3](https://pyup.io/repos/github/amor71/FINRAShortData/python-3-shield.svg)](https://pyup.io/repos/github/amor71/FINRAShortData/)
[![Updates](https://pyup.io/repos/github/amor71/FINRAShortData/shield.svg)](https://pyup.io/repos/github/amor71/FINRAShortData/)
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)
[![codecov](https://codecov.io/gh/amor71/FINRAShortData/branch/main/graph/badge.svg?token=Gy7JKcpOqh)](https://codecov.io/gh/amor71/FINRAShortData)

# FINRAShortData
Process FINRA Short Daily Data [feeds](https://developer.finra.org/docs#query_api-equity-equity_short_interest_standardized)

## Prerequisite

* FINRA Developer Credentials are required. If you do not yet have an account, [create one here](https://developer.finra.org/create-account?Forward_URL=https://gateway.finra.org/app/dfo-console?rcpRedirNum=1).

* Once you have access, you will need to create an API key. Daily Short Data feeds are free. [click here](https://gateway.finra.org/app/api-console/add-credential) to create API credential and follow the instructions.

## Install

To install the package type:

`pip install finrashortdata`

## Quick start

### Authenticate

```python
from finrashortdata import auth
token = auth(client_id=<your api client id>, secret=<your api secret>)
```

### Example 1: Basic data loading & processing

```python
from finrashortdata import process
import pandas as pd
df : pd.DataFrame = process(token)
```

### Example 2: load latest data
from finrashortdata import get_chunk_and_size, process

chunk, max_data = get_chunk_and_size(token)
df : pd.DataFrame = process(token=token, offset=max_data-10*chunk)



## Licensing

[GNU GPL v.3](https://github.com/amor71/FINRAShortData/blob/main/LICENSE)

## Questions & Comments

Use the [Issues](https://github.com/amor71/FINRAShortData/issues) section

## Contributing

If you'd like to contribute to the project, drop me a line at mailto:amor71@sgeltd.com



