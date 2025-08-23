import pandas as pd

def read_csv_auto(path_file, **kwargs):
    return pd.read_csv( path_file, encoding= "latin1", sep=';', **kwargs)

if __name__ == "__main__":
    df=read_csv_auto(r"C:\Users\Abubakir\Downloads\sales_data_sample.csv")
    print(df.head())
