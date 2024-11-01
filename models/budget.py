from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base, Session

class Budget(Base):
    __tablename__ = 'budgets'

    id = Column(Integer, primary_key=True)
    category = Column(String, nullable=False)
    limit = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    # Relationships
    user = relationship("User", back_populates="budgets")
    expenses = relationship("Expense", back_populates="budget")

    def __init__(self, category, limit, user_id):
        self.category = category
        self.limit = limit
        self.user_id = user_id

    @classmethod
    def create_budget(cls, category, limit, user_id):
        session = Session()
        budget = cls(category=category, limit=limit, user_id=user_id)
        session.add(budget)
        session.commit()
        session.close()
        return budget

    @classmethod
    def get_all_budgets(cls):
        session = Session()
        budgets = session.query(cls).all()
        session.close()
        return budgets
