import pandas as pd
from src.Reader import CountiesDataSetReader
from src.Reader import StateDataSetReader
from src.Reader import UsDataSetReader
import math

def UsDataFunction():
    return UsDataSetReader().filter(items=['cases','deaths'])

def StateDataFunction():
    deathSum = StateDataSetReader().loc[:,'deaths'].sum()
    return StateDataSetReader().loc[:,'deaths'].map(lambda x : x/deathSum)

def CountiesDataFunction(name):
    return CountiesDataSetReader()[CountiesDataSetReader().state==name]


def StateDataSum():
    sum = StateDataSetReader().loc[:, 'deaths'].sum()
    return sum
