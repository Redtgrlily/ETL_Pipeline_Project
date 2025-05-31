import requests
import pandas as pd

def fetch_data():
    url = 'https://disease.sh/v3/covid-19/countries'
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)