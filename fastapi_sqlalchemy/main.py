from fastapi import Depends, FastAPI, HTTPException, Request, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse, JSONResponse
from sqlalchemy.orm import Session
from collections import defaultdict
from azure_ad_auth_example import AuthError, requires_auth
from typing import Optional
import os

# import schemas
from sqlalchemy_session_example import (
    get_db_engine,
    create_all_tables,
    # drop_all_tables,
    configure_session_factory,
)
from sqlalchemy_utils_example import get_report_by_id
import os


# from database import SessionLocal, engine

parts = [os.getenv(x) for x in ["DB_USER", "DB_PWD", "DB_HOST", "DB_PORT", "DB_NAME"]]
db_uri = f"mysql+pymysql://{parts[0]}:{parts[1]}@{parts[2]}:{parts[3]}/{parts[4]}"
engine = get_db_engine(db_uri)
create_all_tables(engine)
# drop_all_tables(engine)
SessionLocal = configure_session_factory(engine)


app = FastAPI(root_path=os.getenv("ROOT_PATH", ""))


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.exception_handler(AuthError)
async def auth_exception_handler(request: Request, exc: AuthError):
    return JSONResponse(status_code=exc.status_code, content=exc.error)


@app.get("/reports/{report_id}", response_class=ORJSONResponse)
@requires_auth
def read_result_aggr(
    report_id: str,
    request: Request,
    X_Api_Key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    # return crud.get_result_aggr(report_id=report_id, db=db)
    report = get_report_by_id(db, report_id)
    return report
