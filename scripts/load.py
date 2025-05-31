from sqlalchemy import create_engine
import pandas as pd
import os

def load_data(df):
    engine = create_engine(f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@localhost:5432/{os.getenv("DB_NAME")}')
    df.to_sql('covid_stats', engine, if_exists='replace', index=False)