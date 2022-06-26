# FINRAShortData
Process FINRA Short Daily Data feeds

## Prerequisite

* FINRA Developer Credentials are required. If you do not yet have an account, [create one here](https://developer.finra.org/create-account?Forward_URL=https://gateway.finra.org/app/dfo-console?rcpRedirNum=1).

* Once you have access, you will need to create an API key. Daily Short Data feeds are free. [click here](https://gateway.finra.org/app/api-console/add-credential) to create API credential and follow the instructions.

## Install

To install the package type:

`pip install finrashortdata`

## Quick start

### Authenticate

```python
import FINRAShortData as sho
token = sho.authorize(id=<your api client id>, secret=<your api secret>)
```

### Basic data loading & processing

```python
import pandas as pd
df : pd.DataFrame = sho.process(token)
```
