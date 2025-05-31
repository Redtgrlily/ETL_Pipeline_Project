import pandas as pd

def transform_data(df):
    df = df[['country', 'cases', 'deaths', 'recovered', 'updated']]
    df['updated'] = pd.to_datetime(df['updated'], unit='ms')
    df['ingestion_time'] = pd.to_datetime('now')
    return df