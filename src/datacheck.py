from importlib.resources import path
import pandas as pd
from deepchecks.tabular.suites import data_integrity
from deepchecks.tabular import Dataset
import argparse


def datacheck(file_path, labels):
    data = pd.read_csv(file_path)
    ds = Dataset(data, label=labels)
    # Run Suite:
    integ_suite = data_integrity()
    suite_result = integ_suite.run(ds)
    suite_result.to_json()


# Instantiate the parser
parser = argparse.ArgumentParser(description="Data Checks using DeepCheck")
parser.add_argument(
    "--file_path", type=str, help="Path to your CSV file containing the data"
)
parser.add_argument("--data_label", type=str, default="label", help="label")

args = parser.parse_args()
data = args.file_path
labels = args.data_label

if __name__ == "__main__":
    datacheck(data, labels)
