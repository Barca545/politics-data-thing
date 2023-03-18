import pandas as pd

def make_data(file_path):
    df_raw = pd.read_csv(filepath_or_buffer=file_path)
    return df_raw

