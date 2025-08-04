# import json
# from datetime import datetime
# import os

# def store_case(case_data):
#     filename = f"cases/case_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
#     os.makedirs("cases", exist_ok=True)

#     with open(filename, "w") as f:
#         json.dump(case_data, f, indent=4)

# db.py
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database URL
DATABASE_URL = "sqlite:///./cases.db"

# Setup SQLAlchemy engine and session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()

# Define the Case model
class LegalCase(Base):
    __tablename__ = "legal_cases"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    crime = Column(String, nullable=False)
    location = Column(String, nullable=False)
    punishment = Column(String, nullable=False)
    date = Column(String, nullable=True)
    full_report = Column(Text, nullable=False)

# Create the table (run once)
Base.metadata.create_all(bind=engine)

# Function to store a case
def store_case(case_data):
    session = SessionLocal()

    # Get data from the response structure
    name = case_data["extracted_data"].get("name", "Unknown")
    crime = case_data["extracted_data"].get("crime", "Unknown")
    location = case_data["extracted_data"].get("location", "Unknown")
    date = case_data["extracted_data"].get("date", "N/A")
    punishment = case_data["legal_research"].get("recommended_punishment", "N/A")
    full_report = case_data["generated_report"]

    # Create a new case record
    new_case = LegalCase(
        name=name,
        crime=crime,
        location=location,
        punishment=punishment,
        date=date,
        full_report=full_report
    )

    # Add and commit to DB
    session.add(new_case)
    session.commit()
    session.close()
