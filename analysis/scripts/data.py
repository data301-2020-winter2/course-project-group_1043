#autoreload module to prevent IPython caching issues
import autoreload
autoreload

import pandas as pd
import os
import config

def load_and_process(path = config.import_path):
    data = (
        pd.read_csv(path, encoding='latin1')
        .rename(columns=lambda x: x.strip())
        .dropna()
        .reset_index(drop=True)
        .assign(launched = lambda x: pd.to_datetime(x['launched'], utc=True))
        .assign(deadline = lambda x: pd.to_datetime(x['deadline'], utc=True))
    )
    df = data
    return data

df = load_and_process()

def export_dataset(path = config.export_path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.mkdir(directory)
    df.to_csv(path)