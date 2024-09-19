import pandas as pd

# raw_pd = pd.read_csv("Nigerian_Road_Traffic_Crashes_2020_2024.csv")

# # print(raw_pd.head())
# # print(raw_pd.info())


# extracted_condition = raw_pd['Quarter'].str.contains('2022')
# extracted_pd = raw_pd[extracted_condition]
# print(extracted_condition)

# extracted_pd = [raw_pd[idx] for idx,x in enumerate(raw_pd["Quarter"]) if "2022" in x]  
# print(extracted_pd)      


from datacleaner import extract_wanted_data
from datasaver import save_to_db
from datareader import read_data
import logging

logging.basicConfig(filename='data_extraction.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# Konfigurerar loggning med en fil 'data_extraction.log', sätter loggningsnivån till DEBUG
# och anger formatet för loggmeddelandena med tidsstämpel, nivå och meddelande....
try:
    df = read_data("Nigerian_Road_Traffic_Crashes_2020_2024.csv")
    logging.info("data has been read in to the system succesfully")
    
    results = extract_wanted_data(df)
    logging.info("Wanted data has been extracted")
    
    save_to_db(results,"Trafic Accidents","Year 2022")
    logging.info("Data has been writen to SQLlite")
except Exception as e:
    # Vid ett fel skrivs felmeddelandet ut och loggas som ett ERROR-meddelande...
    print(e)
    logging.error(f"An error has occured {e}")
    





    
    #testerna testar funktionerna som att dom gör de vi vill
    #kör funktionerna och dom returnerar rätt data typ
    
    
