from collections.abc import Generator

from sqlalchemy import create_engine, text
from sqlalchemy.orm import (
    Session,
    declarative_base,
    sessionmaker,
)

from src.utils.config import Config


def get_database_url() -> str:
    """Builds the SQLAlchemy database connection URL.

    Retrieves the database configuration from the application
    settings and constructs a MySQL connection string compatible
    with SQLAlchemy.

    Raises:
        TypeError: If the configuration returned by Config().config()
            is not a dictionary.

    Returns:
        str: SQLAlchemy database connection URL.
    """
    db_config = Config().config("fixr")

    if not isinstance(db_config, dict):
        raise TypeError(
            "Config().config('fixr') must return a dict, "
            f"got {type(db_config).__name__!r} instead."
        )

    return (
        f"mysql+mysqlconnector://"
        f"{db_config['user']}:{db_config['password']}"
        f"@{db_config['host']}:{db_config['port']}"
        f"/{db_config['database']}?charset=utf8"
    )


engine = create_engine(
    get_database_url(),
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """Provides a database session for a request lifecycle.

    Creates a new SQLAlchemy session, yields it to the caller,
    and ensures the session is properly closed after use.

    Yields:
        Session: Active SQLAlchemy database session.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def check_database_connection(db: Session) -> bool:
    """Checks whether the database connection is available.

    Args:
        db: Active SQLAlchemy database session.

    Returns:
        bool: True if the database is reachable, otherwise False.
    """
    try:
        db.execute(text("SELECT 1"))
        return True
    except Exception:
        return False