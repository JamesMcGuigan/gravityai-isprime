#!/usr/bin/env python3
import pandas as pd
from pandas import Series
import sympy as sympy


def is_prime_series(input_series: Series) -> Series:
    output_series = Series(input_series).map( sympy.ntheory.primetest.isprime )
    return output_series


def is_prime_csv(input_path, output_path, verbose=True):
    input_data  = pd.read_csv(input_path, header=0)
    output_data = input_data.copy()
    output_data['IsPrime'] = is_prime_series( input_data['Number'] )
    output_data.to_csv(output_path, index=False)

    if verbose:
        print( open(output_path,"r").read() )
