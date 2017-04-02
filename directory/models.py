from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from flask_login import UserMixin

class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(128), unique=True)
    password = Column(String(128))
    profile = relationship("Profile", uselist=False, backref="account")
   
    
class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    surname = Column(String(100))
    faculty = Column(String(100))
    year = Column(String(4))
    location = Column(String(100))
    industry = Column(String(100))
    company = Column(String(100))
    position = Column(String(100))
    expertise = Column(Text)
    photo = Column(String(300))

    account_id = Column(Integer, ForeignKey('users.id'), nullable=False)

# Base.metadata.create_all(engine)