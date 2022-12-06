from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    """
    This is a Pydantic model for parsing a user dictionary from the csv reader. If there
    are more fields in the csv file they will be ignored unless they are added to this
    model.
    """

    id: Union[str, None] = None
    bio: Union[str, None] = None
    name: Union[str, None] = None
    picture: Union[str, None] = None


class Experience(BaseModel):
    """
    This is a Pydantic model for parsing an Experience dictionary from the csv reader. If
    there are more fields in the csv file they will be ignored unless they are added to
    this model.
    """

    id: Union[str, None] = None
    company: Union[str, None] = None
    dates: Union[str, None] = None
    description: Union[str, None] = None
    title: Union[str, None] = None
