from typing import Dict, List

from candidate_api.models import Experience, User
from candidate_api.utils.csv_utils import load_experience_data, load_users_data
from candidate_api.utils.generate_data_structure import (
    generate_object_map_array,
    generate_user_map,
)


def load_data() -> [Dict[str, User], Dict[str, List[Experience]]]:
    """
    Load the tsv files "users.tsv" and "experiences.tsv" and return their values.
    This function prints a message every time it is run for debugging purposes.
    """
    print("data loaded")
    return [
        generate_user_map(load_users_data("users.tsv")),
        generate_object_map_array(load_experience_data("experience.tsv")),
    ]
