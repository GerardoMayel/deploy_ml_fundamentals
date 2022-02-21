

# dvc remote add -d remote_data_storage gs://ml-ops-fundamentals-bucket/DVC_DATA

# dvc add data/finantials.csv

# dvc push

# git add data/finantials.csv.dvc

from shutil import move
from dvc import api
import pandas as pd


def remote_dvc_to_df(csv_path):

    try:
        df_path = api.get_url(csv_path)
        df = pd.read_csv(df_path)
        return df
    except:
        return print('Error: File not found')


if __name__ == '__main__':

    finantials_path = 'data/finantials.csv'
    movies_path = 'data/movies.csv'
    opening_path = 'data/opening_gross.csv'

    fin_data = remote_dvc_to_df(finantials_path)
    movie_data = remote_dvc_to_df(movies_path)
    opening_data = remote_dvc_to_df(opening_path)

    # print(fin_data)
    # print(movie_data)
    # print(opening_data)

    numeric_columns_mask = (movie_data.dtypes == float) | (
        movie_data.dtypes == int)
    numeric_columns = [
        column for column in numeric_columns_mask.index if numeric_columns_mask[column]]
    movie_data = movie_data[numeric_columns + ['movie_title']]

    fin_data = fin_data[['movie_title',
                         'production_budget', 'worldwide_gross']]

    fin_movie_data = pd.merge(movie_data, fin_data,
                              on='movie_title', how='left')

    full_movie_data = pd.merge(
        opening_data, fin_movie_data, on='movie_title', how='left')

    full_movie_data = full_movie_data.drop(['movie_title', 'gross'], axis=1)

    full_movie_data.to_csv(
        r'/Users/mayel/fixdesktop/virtual/deploy_ml_fundamentals/data/full_data.csv', index=False)
