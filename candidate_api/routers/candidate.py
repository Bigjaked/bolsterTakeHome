from typing import List, Union
from fastapi import APIRouter, Body, HTTPException, Path
from pydantic import BaseModel

from candidate_api.data import load_data
from candidate_api.models import Experience, User

users, experiences = load_data()
router = APIRouter(prefix="/candidate", tags=["candidate"])

ID_PATH = Path(example="cindyhall", description="The id of the candidate.")
NOT_FOUND = HTTPException(status_code=404, detail="Candidate not found.")


@router.get("/list")
async def list_candidates():
    """
    Returns a list of all candidates stored on the server. If no candidates are found then
    it returns a 404.
    \f
    :return: Returns a list of candidates or a 404 if no candidates are found.
    """
    if len(users) == 0:
        raise HTTPException(status_code=404, detail="No candidates were found.")
    return dict(results=[u.dict() for u in users.values()])


class ExperienceWithoutId(BaseModel):
    """
    A Pydantic model that doesn't include the id. It will remove the id from existing
    dictionaries or models.
    """

    company: Union[str, None] = ""
    dates: Union[str, None] = ""
    description: Union[str, None] = ""
    title: Union[str, None] = ""


class UserWithoutId(BaseModel):
    """
    A Pydantic model that doesn't include the id. It will remove the id from existing
    dictionaries or models.
    """

    bio: Union[str, None] = None
    name: Union[str, None] = None
    picture: Union[str, None] = None


class GetCandidateUser(UserWithoutId):
    experience: List[ExperienceWithoutId] | None = []


class GetCandidateResponse(BaseModel):
    results: GetCandidateUser


@router.get("/{id}", response_model=GetCandidateResponse)
async def get_candidate(id: str = ID_PATH):
    """
    Return a single candidate with the id of {id}
    \f
    :param id: the id of the candidate to return.
    :return: Returns a candidate joined with its experiences if found, otherwise returns
             a 404
    """
    if id in users:
        user = users.get(id)
        exps = experiences.get(id)
        return dict(
            results=dict(**user.dict(), experience=[exp.dict() for exp in exps] or [])
        )
    else:
        raise NOT_FOUND


class UpdateCandidateResponse(UserWithoutId):
    """
    This model represents the fields and types that will be parsed from the json body of
    the update_candidate endpoint
    """

    experience: List[ExperienceWithoutId]


@router.put("/{id}")
async def update_candidate(
    id: str = ID_PATH,
    json: UpdateCandidateResponse = Body(
        description="The json data containing the user profile and experiences of the "
        "user to be updated",
        example={
            "name": "Some User",
            "bio": "Some user information",
            "picture": "www.example.com/some-user-image",
            "experience": [
                {
                    "company": "Some Company",
                    "dates": "2010|2012",
                    "description": "I worked here for a time and did stuff",
                    "title": "Major idiot",
                }
            ],
        },
    ),
):
    """
    Allows the user to update the profile and experience data for a single candidate. All
    data will be overridden. If the candidate is not found, it will return a 404.
    \f
    :param id: The id of the candidate to return.
    :param json: The Json body of the put request
    :return:
    """
    if id in users:
        users[id] = User(id=id, **json.dict())
        experiences[id] = [
            Experience(id=id, **exp.dict(exclude={"id"})) for exp in json.experience
        ]
        return dict(results="ok")
    else:
        raise NOT_FOUND
