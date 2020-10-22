import pandas as pd


def CountiesDataSetReader():
    df = pd.read_csv("../data/us-counties.csv")
    return df

def StateDataSetReader():
    df = pd.read_csv("../data/us-states.csv")
    return df

def UsDataSetReader():
    df = pd.read_csv("../data/us.csv")
    return df


