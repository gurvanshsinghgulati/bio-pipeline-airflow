import os, sqlite3
def create_table():
    db_path = '/home/airflow/gene_data.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS og_message_source_details (gene_name TEXT, expression_value REAL)')
    conn.commit()
    conn.close()
