import pandas as pd
from os.path import splitext

def process_data(files_list):
    for file in files_list:
        df = pd.read_parquet(f"/input/{file}")
        df.to_json(f"/output/{splitext(file)}.json", orient="records")
    