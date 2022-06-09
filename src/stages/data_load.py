
from typing import Text
import pandas as pd
from sklearn.datasets import load_iris
import yaml
import argparse


def data_load(config_path: Text) -> None:

    with open(config_path) as conf_file:
        config = yaml.safe_load(conf_file)

    data = load_iris(as_frame=True)
    dataset = data.frame

    dataset.columns = [colname.strip(' (cm)').replace(' ', '_') for colname in dataset.columns.tolist()]

    dataset.to_csv(config['data_load']['dataset_csv'], index=False)

    print("Data load completed.")

if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()
    
    data_load(config_path=args.config)
