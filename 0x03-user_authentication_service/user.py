#!/usr/bin/env python3
""" creating a model named User for a databased table named users """


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy model for the 'users' table.
    
    Attributes:
        id (int): The integer primary key for the user.
        email (str): The non-nullable string representing
            the user's email address.
        hashed_password (str): The non-nullable string storing
            the hashed password of the user.
        session_id (str, optional): A nullable string for the
            user's session ID.
        reset_token (str, optional): A nullable string used
            for password reset tokens.
    """

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
