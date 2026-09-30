import os, sqlite3, pandas as pd, matplotlib.pyplot as plt
def plot_data():
    db_path = '/home/airflow/gene_data.db'
    chart_path = '/home/airflow/gene_expression_chart.png'
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query('SELECT * FROM og_message_source_details', conn)
    conn.close()
    if df.empty: return
    plt.figure(figsize=(10, 6))
    plt.bar(df['gene_name'], df['expression_value'], color='skyblue')
    plt.savefig(chart_path)
    plt.close()
