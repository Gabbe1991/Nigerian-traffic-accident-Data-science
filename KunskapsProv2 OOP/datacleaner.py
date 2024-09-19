#datacleaner
import pandas as pd

def extract_wanted_data(df):
    
    
    condition = df['Quarter'].str.contains('2022')

    extracted_rows = df[condition]
    return extracted_rows

#Funktionen tar en dataframe som argument och filterar rader där kolumnen "Quarter"
#innehåller "2022". där filterar raderna returneras som en ny dataframe