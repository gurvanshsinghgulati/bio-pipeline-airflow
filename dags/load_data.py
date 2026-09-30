import os, sqlite3, pandas as pd
def load_data():
    db_path = '/home/airflow/gene_data.db'
    csv_path = '/home/airflow/sample_gene_expression.csv'
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    df.to_sql('og_message_source_details', conn, if_exists='append', index=False)
    conn.close()
