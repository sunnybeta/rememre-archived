from typing import Any
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_timestamp(a,b, target: Any) -> None:
    ts = datetime.utcnow()
    target.created_at  = ts
    target.updated_at  = ts


def update_timestamp(a,b, target: Any) -> None:
    ts = datetime.utcnow()
    target.updated_at  = ts
