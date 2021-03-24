from sqlalchemy.dialects.mysql import DOUBLE
from sqlalchemy.orm import relationship, Session, load_only
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, String, Integer, Float, JSON, DateTime, func
from sqlalchemy.sql.schema import CheckConstraint


Base = declarative_base()


project_names = ("test1", "test2")


class File(Base):
    __tablename__ = "file"

    file_id = Column(String(256), primary_key=True)
    file_path = Column(String(512))
    longitude = Column(JSON)  # array
    latitude = Column(JSON)  # array
    last_modified_at = Column(DateTime, default=func.current_timestamp())

    report_file_relations = relationship("ReportFileRelation", back_populates="file")


class ReportFileRelation(Base):
    __tablename__ = "report_file_relation"

    _id = Column(Integer, primary_key=True)
    file_id = Column(String(256), ForeignKey("file.file_id"))
    report_id = Column(String(128), ForeignKey("report.report_id"))
    per_file = Column(JSON)  # array

    file = relationship("File", back_populates="report_file_relations")
    report = relationship("Report", back_populates="report_file_relations")


class Report(Base):
    __tablename__ = "report"

    report_id = Column(String(128), primary_key=True)
    input_dir = Column(String(256))
    project_name = Column(String(128), nullable=False)
    result = Column(JSON)  # array
    last_modified_at = Column(DateTime, default=func.current_timestamp())

    report_file_relations = relationship("ReportFileRelation", back_populates="report")

    CheckConstraint(project_name.in_(project_names))
