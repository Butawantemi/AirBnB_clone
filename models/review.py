#!/usr/bin/python3
"""defines the review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """child class of BaseModel """

    place_id = ""
    user_id = ""
    text = ""
