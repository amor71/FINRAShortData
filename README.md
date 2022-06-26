[![Updates](https://pyup.io/repos/github/amor71/finrashortdata/shield.svg)](https://pyup.io/repos/github/amor71/finrashortdata/)
[![Python 3](https://pyup.io/repos/github/amor71/finrashortdata/python-3-shield.svg)](https://pyup.io/repos/github/amor71/finrashortdata/)
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)

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
import finrashortdata as sho
token = sho.auth(id=<your api client id>, secret=<your api secret>)
```

### Basic data loading & processing

```python
import pandas as pd
df : pd.DataFrame = sho.process(token)
```

## Licensing

[GNU GPL v.3](https://github.com/amor71/FINRAShortData/blob/main/LICENSE)

## Questions & Comments

Use the [Issues](https://github.com/amor71/FINRAShortData/issues) section

## Contributing

If you'd like to contribute to the project, drop me a line at mailto:amor71@sgeltd.com



