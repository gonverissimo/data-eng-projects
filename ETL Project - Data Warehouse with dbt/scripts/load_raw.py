import pandas as pd
from sqlalchemy import create_engine

# CSV Path
csv_path = "../data/vendas.csv"

# Read CSV
df = pd.read_csv(csv_path)

# Connect to PostgreSQL (raw)
engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/warehouse")

# Load to raw (table vendas_raw)
df.to_sql("vendas_raw", engine, schema="raw", if_exists="replace", index=False)

print("Data successfully loaded into the raw.vendas_raw!")
