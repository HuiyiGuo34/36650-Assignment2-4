import pytest
from src.Function import *
from src.Reader import *

class Test_data:
def test_StateDataSum_is_correct(self):
        num = UsDataSetReader().loc[:,'deaths'].sum()
        assert num == StateDataSum()

def test_UsDataFunction_output_has_two_columns():
    assert UsDataFunction().shape[1] == 2

def test_StateDataFunction_percentage_sum_is_about_1():
    assert StateDataFunction().sum() < 1.01 and StateDataFunction().sum() > 0.99

