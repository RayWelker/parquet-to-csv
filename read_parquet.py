import pyarrow.parquet as pq
from datetime import datetime

date_time = datetime.now().strftime("%Y-%m-%dT%H%M%S")
parquet_file = '' #Add the files path and file name here

df = pq.read_table(source=parquet_file).to_pandas()

df.to_csv(f'results_{date_time}.csv')