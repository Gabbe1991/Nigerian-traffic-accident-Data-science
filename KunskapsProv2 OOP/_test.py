import pytest
import pandas as pd
from datacleaner import extract_wanted_data
from datareader import read_data
from datasaver import save_to_db
import sqlite3

# test
@pytest.fixture
def sample_df():
    data = {
        'Quarter': ['2021 Q1', '2022 Q2', '2022 Q3', '2021 Q4'],
        'Value': [100, 200, 300, 400]
    }
    return pd.DataFrame(data)

# Test för datacleaner.py
def test_extract_wanted_data(sample_df):
    result = extract_wanted_data(sample_df)
    assert len(result) == 2  # förväntar sig 2 rows wmed '2022'
    assert all(result['Quarter'].str.contains('2022'))

# Test för datareader.py
def test_read_data(tmp_path):
    # skapa temporär csv
    file_path = tmp_path / "test_data.csv"
    df = pd.DataFrame({
        'Quarter': ['2021 Q1', '2022 Q2', '2022 Q3'],
        'Value': [100, 200, 300]
    })
    df.to_csv(file_path, index=False)

    result = read_data(file_path)
    assert len(result) == 3
    assert 'Quarter' in result.columns
    assert result['Quarter'][1] == '2022 Q2'

# Test for datasaver.py
def test_save_to_db(sample_df, tmp_path):
    db_path = tmp_path / "test_db.sqlite"
    db_name = str(db_path)
    table_name = "traffic_data"
    
    # sparar df till db
    save_to_db(sample_df, db_name, table_name)

    # läser tillbaka databasen
    connection = sqlite3.connect(db_name)
    result = pd.read_sql(f"SELECT * FROM {table_name}", connection)
    connection.close()


    # se om vi sparar datan rätt
    assert len(result) == len(sample_df)
    assert 'Quarter' in result.columns
