from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import DebtorList, Base

engine = create_engine("sqlite:///sqlalchemy_example.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

Xantec = DebtorList(ic=124401981998, name="Mr Wong", corporate = "Xantec Solutions Sdn Bhd", debts = 100000.87, contactNo = 1234657890 )
FirstSM = DebtorList(ic=120249092012, name="Ms Kim", corporate = "First SM Sdn Bhd", debts = 88.10, contactNo = 1589645355 )
D_and_A_Chemicals = DebtorList(ic=56955422120, name="Miss Chan", corporate = "D_and_A_Chemicals Sdn Bhd", debts = 5000.87, contactNo = 12356895122 )

corporate = (Xantec, FirstSM, D_and_A_Chemicals)
session.add_all(corporate)