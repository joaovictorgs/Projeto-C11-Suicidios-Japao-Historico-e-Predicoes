import pandas as pd
import numpy as np


def process_brazil_data(input_filepath: str, output_filepath: str = None) -> pd.DataFrame:
    df = pd.read_csv(input_filepath)
    df_brazil = df[df['Country Name'] == 'Brazil'].copy()
    
    df_aggregated = df_brazil.groupby('Year').agg({
        'Region Name': 'first',
        'Country Name': 'first',
        '0 Year': 'sum',
        '1-4 Years': 'sum',
        '5-9 Years': 'sum',
        '10-14 Years': 'sum',
        '15-19 Years': 'sum',
        '20-24 Years': 'sum',
        '25-29 Years': 'sum',
        '30-34 Years': 'sum',
        '35-39 Years': 'sum',
        '40-44 Years': 'sum',
        '45-49 Years': 'sum',
        '50-54 Years': 'sum',
        '55-59 Years': 'sum',
        '60-64 Years': 'sum',
        '65-69 Years': 'sum',
        '70-74 Years': 'sum',
        '75-79 Years': 'sum',
        '80-84 Years': 'sum',
        '85+ Years': 'sum',
        'Unknown Age': 'sum',
        'No of Suicides': 'sum',
        'Percentage of cause-specific deaths out of total deaths': 'mean',
        'Death rate per 100 000 population': 'mean'
    }).reset_index()
    
    if output_filepath:
        df_aggregated.to_csv(output_filepath, index=False)
    
    return df_aggregated
