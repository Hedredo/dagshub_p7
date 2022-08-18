import pandas as pd
from deepchecks.tabular.suites import data_integrity
from deepchecks.tabular import Dataset
import argparse


def datacheck(file_path):
    data = pd.read_csv(file_path)
    ds = Dataset(data)
    # Run Suite:
    integ_suite = data_integrity()
    suite_result = integ_suite.run(ds)
    suite_result.save_as_html()
    suite_result.show()

# Instantiate the parser
parser = argparse.ArgumentParser(description='Data Checks using DeepCheck')
args = parser.parse_args()
parser.add_argument('data_file', type=str,
                    help='Path to your CSV file containing the data')

args = parser.parse_args()
data = args.data_file

if __name__ == "__main__":
    datacheck(data)
