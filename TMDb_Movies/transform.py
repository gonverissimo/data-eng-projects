import pandas as pd

def transform_movies(movies):
    df = pd.DataFrame(movies)

    # Converter release_date para datetime, tratar erros
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

    # Filter important columns
    cols_to_keep = ['id', 'title', 'release_date', 'popularity', 'vote_average', 'vote_count', 'overview', 'adult']
    df = df[cols_to_keep]

    # Handling null values
    # For example, eliminating films with no release date
    df = df.dropna(subset=['release_date'])

    # Clean up strings: remove spaces and lowercase (in title and overview)
    df['title'] = df['title'].str.strip().str.lower()
    df['overview'] = df['overview'].fillna('').str.strip()

    # Add release year column
    df['release_year'] = df['release_date'].dt.year

    # Remove duplicates by id
    df = df.drop_duplicates(subset='id')

    return df
