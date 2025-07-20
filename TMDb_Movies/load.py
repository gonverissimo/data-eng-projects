from sqlalchemy import create_engine
import urllib

def get_engine():
    params = urllib.parse.quote_plus(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=LAPTOP-30AJPAFE;"
        "DATABASE=projeto1;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
    return engine

def load_to_sql(df, table_name='popular_movies'):
    engine = get_engine()
    df.to_sql(table_name, engine, if_exists='replace', index=False)
