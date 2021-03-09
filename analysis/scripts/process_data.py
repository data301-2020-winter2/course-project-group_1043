#autoreload module to prevent IPython caching issues
import autoreload
autoreload

import pandas as pd

def load_and_process(path):
    df = (
        pd.read_csv(path,encoding='latin1')
        .rename(columns=lambda x: x.strip())
        .dropna()
        .assign(launched = lambda x: pd.to_datetime(x['launched'], utc=True))
        .assign(deadline = lambda x: pd.to_datetime(x['deadline'], utc=True))
    )
    return df
