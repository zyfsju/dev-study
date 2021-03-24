from sqlalchemy.orm import Session, load_only
from sqlalchemy.orm import class_mapper
from sqlalchemy import func, and_


def get_report_by_id(db: Session, report_id: str):
    row = db.query(Report).get(report_id)
    return row
