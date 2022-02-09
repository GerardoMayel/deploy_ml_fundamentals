
from os import read
from dvc import api
import pandas as pd
from io import StringIO
import sys
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name): (message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

logging.info('Fetching data...')

movie_data_path = api.read('movies.csv', remote='dvc_origin_data')

# finantial_data_path = api.read(
#     'DVC_DATA/finantials.csv', remote='dvc_origin')
# opening_gross_data_path = api.read(
#     'DVC_DATA/opening_gross.csv', remote='dvc_origin')

#full_data_data_path = api.read('/DVC_DATA/full_data.csv.dvc', remote='dvc_origin')


movie_data = pd.read_csv(StringIO(movie_data_path))
# fin_data = pd.read_csv(StringIO(finantial_data_path))
# opening_data = pd.read_csv(StringIO(opening_gross_data_path))

breakpoint()
#import pdb; pdb.set_trace()
