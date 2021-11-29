from typing import List
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

def get_chicago_data() -> pd.DataFrame:
    """Gets Chicago's data from a csv file and returns a panda DataFrame."""
    data = pd.read_csv("./raw_data/chicago.csv")
    data["city"] = "chicago"
    return data


def get_new_york_data() -> pd.DataFrame:
    """Gets New York's data from a csv file and returns a panda DataFrame."""
    data = pd.read_csv("./raw_data/new_york_city.csv")
    data["city"] = "new_york"
    return data


def get_washington_data() -> pd.DataFrame:
    """Gets Washington's data from a csv file and returns a panda DataFrame,"""
    data = pd.read_csv("./raw_data/washington.csv")
    # add missing columns
    data["Gender"] = np.nan
    data["Birth Year"] = np.nan
    data["city"] = "washington"
    return data


def get_data_by_city(cities: list[str]) -> pd.DataFrame:
    """Receives a list of strings that represent cities and returns a panda DataFrame."""
    data = pd.DataFrame(columns=["Unnamed: 0", "Start Time", "End Time", "Trip Duration", "Start Station", "End Station", "User Type", "Gender", "Birth Year", "city"])

    if "chicago" in cities or "Chicago" in cities or "CHICAGO" in cities:
        data = data.append(get_chicago_data())

    if "new york" in cities or "New York" in cities or "NEW YORK" in cities:
        data = data.append(get_new_york_data())

    if "washington" in cities or "Washington" in cities or "WASHINGTON" in cities:
        data = data.append(get_washington_data())

    return data
