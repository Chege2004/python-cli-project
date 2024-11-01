from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base, Session

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    budgets = relationship("Budget", back_populates="user", cascade="all, delete-orphan")

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

    @classmethod
    def get_user_details(cls, user_id):
        session = Session()
        user = session.query(cls).filter_by(id=user_id).first()
        
        if user:
            user_details = {
                'name': user.name,
                'email': user.email,
                'budgets': [
                    {
                        'category': budget.category,
                        'limit': budget.limit,
                        'expenses': [
                            {
                                'description': expense.description,
                                'amount': expense.amount
                            } for expense in budget.expenses
                        ]
                    } for budget in user.budgets
                ]
            }
            session.close()
            return user_details
        else:
            session.close()
            return None

    @classmethod
    def delete_user(cls, user_id):
        session = Session()
        user = session.query(cls).filter_by(id=user_id).first()
        
        if user:
            session.delete(user)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False
