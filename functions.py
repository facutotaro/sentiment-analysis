import pandas as pd

def saveDF(df,fileName):
    df.to_csv("./data/" + fileName, encoding='utf-8')

def readCSV(fileName):
    return pd.read_csv("./data/" + fileName, encoding='utf-8',index_col=0)