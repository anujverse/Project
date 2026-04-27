import sqlite3
import pandas as pd

def create_connection():
    conn = sqlite3.connect('project.db')
    return conn

def insert_data(df):
    conn = create_connection()
    df.to_sql('customers', conn, if_exists='replace', index=False)
    conn.close()

def run_query(query):
    conn = create_connection()
    result = pd.read_sql(query, conn)
    conn.close()
    return result