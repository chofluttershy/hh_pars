import pandas as pd


def conversion():
    df = pd.read_csv("data_jobs.scv")
    df.rename(columns={'Unnamed: 0': 'index'}, inplace=True)
    df.set_index('index', inplace=True)
    print(df.head)