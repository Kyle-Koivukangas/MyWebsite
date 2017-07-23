import datetime
import uuid
import sqlalchemy.orm
from sqlalchemy import Column, String, Boolean, DateTime
import sqlalchemy

from mywebsite.data.modelbase import SqlAlchemyBase


class Account(SqlAlchemyBase):
    __tablename__ = 'Account'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()).replace('-', ''))
    email = Column(String, index=True, unique=True, nullable=False)
    password_hash = Column(String, index=True, unique=True, nullable=False)
    created = Column(DateTime, index=True, default=datetime.datetime.now)
    email_confirmed = Column(Boolean, nullable=False, default=False)
    is_super_user = Column(Boolean, nullable=False, default=False)
