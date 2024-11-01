from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .database import Base, Session

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    budget_id = Column(Integer, ForeignKey('budgets.id'))

    def __init__(self, description, amount, budget_id):
        self.description = description
        self.amount = amount
        self.budget_id = budget_id

    @classmethod
    def create_expense(cls, description, amount, budget_id):
        session = Session()
        expense = cls(description=description, amount=amount, budget_id=budget_id)
        session.add(expense)
        session.commit()
        session.close()
        return expense

    @classmethod
    def get_all_expenses(cls):
        session = Session()
        expenses = session.query(cls).all()
        session.close()
        return expenses
