import os

import pandas as pd
import subprocess

from src.is_prime import is_prime_series


def test_is_prime_series():
    test_data = pd.read_csv('./csv/is_prime/output_expected.csv')
    inputs    = test_data['Number']
    expected  = test_data['IsPrime']
    actual    = is_prime_series(inputs)
    assert actual.equals(expected)


def test_is_prime_csv():
    exec_path     = './gravity_is_prime.py'
    input_path    = './csv/is_prime/input.csv'
    output_path   = './csv/is_prime/output.csv'
    expected_path = './csv/is_prime/output_expected.csv'

    # os.remove(output_path)
    subprocess.check_output([exec_path, 'run', input_path, output_path])
    assert os.path.exists(output_path)

    input_df    = pd.read_csv(input_path)
    output_df   = pd.read_csv(output_path)
    expected_df = pd.read_csv(expected_path)

    assert input_df.columns.tolist()    == ['Number']
    assert output_df.columns.tolist()   == ['Number', 'IsPrime']
    assert expected_df.columns.tolist() == ['Number', 'IsPrime']

    assert input_df['Number'].equals(output_df['Number'])
    assert output_df['Number'].equals(expected_df['Number'])
    assert output_df['IsPrime'].equals(expected_df['IsPrime'])

    pd.testing.assert_frame_equal( output_df, expected_df )
