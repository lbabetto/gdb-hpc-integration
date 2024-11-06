import pandas as pd

def process_data(infile, outfile):
    df = pd.read_parquet(infile)
    df.to_json(outfile, orient="records")
    