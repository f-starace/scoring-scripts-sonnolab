import csv
from io import TextIOWrapper


class SeparatorNotFound(Exception):
    def __init__(self, message):
        self.message = message

def get_csv_sep(csvfile: TextIOWrapper) -> str:
    """Retrieves the separator from a csv file
    Args:
        csvfile (str): A csv file
    Returns:
        sep (str): The separator (can be '\\t',',', ';', '|')
    """
    try:
        sep = csv.Sniffer().sniff(csvfile.read(), ["\t", ",", ";", "|"]).delimiter
        return sep
    except csv.Error:
        raise SeparatorNotFound("Separator not found")


