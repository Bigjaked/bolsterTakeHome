import os.path
from typing import List, Callable, Any
from candidate_api.models import Experience, User
import csv


def load_tsv_file(path: str, loader: Callable) -> List[Any] | None:
    """
    Checks if a tsv file exists, then loads and parses it with the csv module.
    Each line gets parsed into a dictionary and then the `loader` function passed in
    is called on it before appending it to the output
    :param path: The path of the file to load.
    :param loader: A callable function or class that takes in a dictionary and returns
                   a value.
    :return: Returns the array of parsed data.
    """
    data = []
    if os.path.exists(path) and os.path.isfile(path):
        with open(path, encoding="utf8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter="\t")
            for entry in reader:
                data.append(loader(**entry))
        return data
    else:
        raise FileNotFoundError(f"Could not find file at: {path}")


def load_experience_data(path: str) -> List[Experience]:
    """Calls the load_tsv_file function and parses each entry into an Experience."""
    return load_tsv_file(path, Experience)


def load_users_data(path: str) -> List[User]:
    """Calls the load_tsv_file function and parses each entry into a User."""
    return load_tsv_file(path, User)
