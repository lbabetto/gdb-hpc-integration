import argparse
from src.process import process_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str)
    parser.add_argument('--output', type=str)
    args = parser.parse_args()
    process_data(args.input, args.output)
    print("Done!")
