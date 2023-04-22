from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import Base, DebtorList

engine = create_engine("sqlite:///sqlalchemy_example.db")

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

debtorList = session.query(DebtorList).all()
for debtor in debtorList:
    print(debtor.name)

debtor = session.query(DebtorList).first()
print("\n" + debtor.name)

badDebts = session.query(DebtorList).filter(DebtorList.debts >= 10000).one()
print("\n" + badDebts.debts + "\n")

000000000000000000000000000000000000000
