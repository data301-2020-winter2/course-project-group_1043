import pandas as pd

def load_and_process(path):
    df = (
        pd.read_csv(path,encoding='latin1')
        .rename(columns=lambda x: x.strip())    # remove whitespace from header
        .dropna()                               # drop any empty rows
    )
    return df
