import datetime
import uuid
import sqlalchemy.orm
from sqlalchemy import Column, String, Boolean, DateTime

from mywebsite.data.modelbase import SqlAlchemyBase


class Account(SqlAlchemyBase):
    __tablename__ = 'Account'

    id = Column(sqlalchemy.Integer, primary_key=True, default=lambda: str(uuid.uuid4()).replace('-', ''))
    email = Column(sqlalchemy.String, index=True, unique=True, nullable=False)
    password = Column(sqlalchemy.String, index=True, unique=True, nullable=False)
    created = Column(DateTime, default=datetime.datetime.now)
    email_confirmed = Column(Boolean, nullable=False, default=False)
    is_super_user = Column(Boolean, nullable=False, default=False)