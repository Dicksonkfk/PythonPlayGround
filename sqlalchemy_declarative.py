from sqlalchemy import Column, Integer, Float, String, Identity, VARCHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DebtorList(Base):
    __tablename__ = "debtorList"
    ic = Column(Integer, primary_key = True)
    id = Column(Integer, Identity(start=1, cycle = True) )
    name = Column(String(length = 50), nullable = False)
    corporate =  Column(String(length = 150), nullable = False)
    debts = Column(Float, nullable = False)
    contactNo = Column(VARCHAR(length = 20), nullable = True)

engine = create_engine("sqlite://sqlalchemy_example.db")

Base.metadata.create_all(engine)
