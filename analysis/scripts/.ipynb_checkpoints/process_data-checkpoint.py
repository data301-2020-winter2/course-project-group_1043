import pandas as pd

def load_and_process(path):
    df = (
        pd.read_csv(path,encoding='latin1')
        .rename(columns=lambda x: x.strip())
        .dropna()
    )
    return df