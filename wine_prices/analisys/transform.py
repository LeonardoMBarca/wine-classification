import pandas as pd
import os

folder = '/Users/leona/OneDrive/Documentos/GitHub/wine-classification/wine_prices/wine_data'
files = os.listdir(folder)

dataframes = []

for i in files:
    path_file = os.path.join(folder, i)
    df = pd.read_csv(path_file)
    df.drop(columns='Unnamed: 0', axis=1, inplace=True)
    dataframes.append(df)

final = pd.concat(dataframes, ignore_index=True)
final.to_csv('final.csv', index=False)