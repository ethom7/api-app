import pytest
from src import helpers


def test_transform_data():
    # test input csv to tsv
    tsv_output = helpers.transform_data_return_str("resources/test_csv.csv", "csv", "tsv")
    csv_output = helpers.transform_data_return_str("resources/test_tsv.tsv", "tsv", "csv")
    assert tsv_output == csv_output.replace(',', '\t')
    assert csv_output == tsv_output.replace('\t', ',')

    # test json to csv
