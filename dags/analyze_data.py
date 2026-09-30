import os, sqlite3, pandas as pd
def analyze_data():
    db_path = '/home/airflow/gene_data.db'
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query('SELECT * FROM og_message_source_details', conn)
    conn.close()
    print(df.groupby('gene_name')['expression_value'].mean().reset_index())
