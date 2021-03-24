import os
import random, string
import logging
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_models_example import Base


def get_db_engine(db_uri: str):
    try:
        engine = create_engine(db_uri)
        # logging.info("Created database engine")
    except Exception as e:
        logging.error(f"DB error, please verify db uri. Err: {e}")
        raise e
    return engine


def create_all_tables(engine):
    Base.metadata.create_all(bind=engine)


def drop_all_tables(engine):
    Base.metadata.drop_all(bind=engine)


def configure_session_factory(engine):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal


def generate_pk(prefix=""):
    pk = "".join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        for _ in range(16)
    )
    parts = [] if not prefix else [prefix]
    parts.extend([datetime.now().strftime("%Y%m%d%H%M%S"), pk])
    pk = "_".join(parts)
    return pk[:31]
