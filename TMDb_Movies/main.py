from extract import fetch_popular_movies
from transform import transform_movies
from load import load_to_sql

if __name__ == "__main__":
    movies = fetch_popular_movies(page=1)
    df = transform_movies(movies)
    load_to_sql(df)
    print("ETL pipeline successfully executed")
