from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PEP(Base):
    __tablename__ = "pep"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birth_date = Column(Date, nullable=True)
    added_date = Column(Date, nullable=True)
