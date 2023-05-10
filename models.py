"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""

from sqlalchemy import ForeignKey, Column, INTEGER, TEXT, String, Boolean
import enum
from sqlalchemy.orm import relationship
from database import Base, db_session, init_db

# TODO: Complete your models

class User(Base):
    __tablename__ = 'users'
    user_id = Column("id", INTEGER, primary_key=True)
    username = Column("username", String(50), unique=True)
    name = Column("name", TEXT)
    university = Column("university", String(50))
    password = Column("password", String(50))
    gender = Column("gender", String(50))
    bio = Column("bio", String(250))
    sports = Column("sports", Boolean)
    music = Column("music", Boolean)
    traveling = Column("traveling", Boolean)
    reading = Column("reading", Boolean)
    art = Column("art", Boolean)
    dance = Column("dance", Boolean)
    video_games = Column("video_games", Boolean)
    working_out = Column("working_out", Boolean)
    cooking = Column("cooking", Boolean)


    #relationships

    def __init__(self, username, password, name, university, gender, bio, sports, music, traveling, reading, art, dance, video_games, working_out, cooking):
        self.username=username
        self.password=password
        self.name=name
        self.university=university
        self.gender=gender
        self.bio=bio
        self.sports=sports
        self.music=music
        self.traveling=traveling
        self.reading=reading
        self.art=art
        self.dance=dance
        self.video_games=video_games
        self.working_out=working_out
        self.cooking=cooking

        

    def __repr__(self):
        return "@" + self.username
    
