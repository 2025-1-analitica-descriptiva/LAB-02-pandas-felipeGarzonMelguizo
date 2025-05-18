import pandas as pd # type: ignore

def getCsv(number):
    return pd.read_csv(f'files/input/tbl{number}.tsv', sep='\t')
