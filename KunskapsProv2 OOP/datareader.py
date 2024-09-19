#datareader
import pandas as pd

def read_data(file):
    df = pd.read_csv(file)
    return df

#Funktionen tar ett filnamn som argument, läser in CSV filen med hjälp av pandas och returnerar datan som 
# en dataframe
