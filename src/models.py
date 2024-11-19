from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from config.config import TABLE_NAME
# Base class for models
Base = declarative_base()

# Disease model definition (table)
class Disease(Base):
    __tablename__ = TABLE_NAME  # Name of the table in the database

    DiseaseID = Column(Integer, primary_key=True, index=True)
    DiseaseName = Column(String, index=True)
    Symptoms = Column(String)
    Prevention = Column(String)
    Treatment = Column(String)
