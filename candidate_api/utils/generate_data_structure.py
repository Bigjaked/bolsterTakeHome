from typing import Dict, List

from candidate_api.models import Experience, User


def generate_user_map(users: List[User] | None = None) -> Dict[str, User]:
    if users:
        return {user.id: user for user in users}


def generate_object_map_array(exps: List[Experience]) -> Dict[str, List[Experience]]:
    if exps:
        experiences = dict()
        for exp in exps:
            e = experiences.get(exp.id)
            if e:
                e.append(exp)
            else:
                experiences[exp.id] = [exp]
        return experiences
