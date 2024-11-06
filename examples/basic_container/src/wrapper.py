import requests
import pandas as pd

def prepare_input_data(files: dict):
    for k,v in files.items():
        response = requests.get(v)
        with open(k, 'wb') as f:
            f.write(response.content)
            f.close()


def upload_output_data(files: dict):
    for k,v in files.items():
        with open(k, 'rb') as f:
            http_response = requests.put(v, f)
            f.close()