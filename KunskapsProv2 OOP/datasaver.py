import sqlite3
import pandas as pd

def save_to_db(df,db_name,table_name):
    connection = sqlite3.connect(db_name)
    
    df.to_sql(table_name,con = connection,if_exists = "append",index = False)
    
    connection.commit()
    connection.close()
    print("Data has been succesfuly saved to the database")

#Funktionen tar en dataframe,databasnamn och tabellnamn som argument. 
#den ansluter sig till SQLlite-db o sparar den dataframe till den givna tabellen
#om tabellen redan finns läggs datan till
#Anslutningen stängs efter att ändringarna har sparats