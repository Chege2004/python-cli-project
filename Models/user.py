from sqlalchemy import Column, Integer, String
from .database import Base, Session

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def create_user(cls, name, email):
        session = Session()
        user = cls(name=name, email=email)
        session.add(user)
        session.commit()
        session.close()
        return user

    @classmethod
    def get_all_users(cls):
        session = Session()
        users = session.query(cls).all()
        session.close()
        return users
