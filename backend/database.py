from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from backend.utils import log_config

# Set up logging
log_config.setup_logging()

# Create a logger for database.py
logger = log_config.get_logger(__name__)

load_dotenv()


def create_connection(db_name):
    """
    Create and return a database engine for the PostgreSQL database.

    Parameters:
    - db_name: Name of the database to connect to.

    Returns:
    - engine: SQLAlchemy database engine object.
    """
    try:
        logger.info("Inside create_connection method...")
        # Connect to the Postgres database
        connection_string = f"postgresql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:5432/{db_name}"
        engine = create_engine(connection_string)
        logger.info(f"Connected to {db_name} successfully!!")
        return engine

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise
