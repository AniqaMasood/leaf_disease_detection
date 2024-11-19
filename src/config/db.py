from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # Import Base from models.py
from config.config import DB_USER,DB_PASSWORD,DB_NAME

# Load environment variables from .env file

# Database connection string (using psycopg2 for synchronous connection)
DATABASE_URL = (
    f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}'
)

# Create the SQLAlchemy engine (synchronous)
engine = create_engine(DATABASE_URL)

# Create a session local to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_db_session():
    """ Get a new database session. """
    session = SessionLocal()
    return session

# Function to create tables (with transaction handling)
def init_db():
    with engine.begin() as conn:
        conn.run_sync(Base.metadata.create_all)
