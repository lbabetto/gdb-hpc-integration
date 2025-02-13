import argparse
import os
from src.process import process_data
from shutil import make_archive


if __name__ == "__main__":

    # parser = argparse.ArgumentParser()
    # parser.add_argument('--input', type=str)
    # parser.add_argument('--output', type=str)
    # args = parser.parse_args()

    input_files = os.listdir("/input")

    process_data(input_files)

    # make_archive("output", "zip", "/output")

    print("Done!")
