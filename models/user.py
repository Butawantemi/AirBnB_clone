#!/usr/bin/python3
"""Defines the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """child class of BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
