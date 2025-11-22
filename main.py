import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.data_processing import process_brazil_data


def main():
    df_brazil = process_brazil_data(
        input_filepath='data/combined_processed_data.csv',
        output_filepath='data/brazil_aggregated.csv'
    )
    
    print(df_brazil)


if __name__ == "__main__":
    main()
