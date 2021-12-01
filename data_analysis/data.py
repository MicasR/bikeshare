import pandas as pd


def chicago_data() -> pd.DataFrame:
    """Get Chicago's data from a csv file and return a panda DataFrame."""
    data = pd.read_csv("./raw_data/chicago.csv")
    data["city"] = "Chicago"
    return data


def new_york_data() -> pd.DataFrame:
    """Get New York's data from a csv file and return a panda DataFrame."""
    data = pd.read_csv("./raw_data/new_york_city.csv")
    data["city"] = "New York"
    return data


def washington_data() -> pd.DataFrame:
    """Get Washington's data from a csv file and return a panda DataFrame."""
    data = pd.read_csv("./raw_data/washington.csv")
    data["city"] = "Washington"
    return data


CHICAGO = chicago_data()
NEW_YORK = new_york_data()
WASHINGTON = washington_data()


def casefold_str_items(listing:list)->list:
    """
    Receive a list and return a list with all string items casefolded

    # Examples:
    ``casefold_str_items(['cHicago','WASHINGTON']) # ->['chicago','washington']``
    ``casefold_str_items(['ChicaGO','1', 2, True]) # ->['chicago','1', 2, True]``
    """
    return [item.casefold() if type(item)==str else item for item in listing]


def get_by_city(cities: list[str]) -> pd.DataFrame:
    """
    Receive a list of strings that represent cities and return a panda DataFrame with the data.

    # Keyword arguments:\n
    cities:list[str]\n
    * The available cities are `"Chicago"`, `"New York"` and `"Washington"`.\n
    * Accept any string capitalization of this cities.\n
    * Return all city data if ["*"] is received.

    # Exceptions:\n
    Ignore if an unavailable city string is provided.\n

    # Examples:
    ``get_by_city(["New York"]) #-> New York data``\n
    ``get_by_city(["New York", "243"]) #-> New York data``\n
    ``get_by_city(["cHicAgo", "waSHINGton"]) #-> Chicago and Washington data``\n
    ``get_by_city(["*"]) #-> all data``\n
    ``get_by_city(["NYC"]) #-> no data``\n
    ``get_by_city([]) #-> no data``\n
    """
    frames = []
    cities_lower_case = casefold_str_items(cities)

    if "chicago" in cities_lower_case or "*" in cities_lower_case: frames.append(CHICAGO)
    if "new york" in cities_lower_case or "*" in cities_lower_case: frames.append(NEW_YORK)
    if "washington" in cities_lower_case or "*" in cities_lower_case: frames.append(WASHINGTON)

    if frames: return pd.concat(frames, ignore_index=True)
    else: return pd.DataFrame()