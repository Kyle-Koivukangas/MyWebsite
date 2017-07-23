from passlib.handlers.sha2_crypt import sha512_crypt
from datetime import datetime

from mywebsite.data.account import Account
from mywebsite.data.dbsession import DbSessionFactory


class AccountService:

    @staticmethod
    def get_accounts():
        session = DbSessionFactory.create_session()

        #accounts = session.query(Account).filter(Account.email).all()
        accounts = session.query(Account).all()
        return accounts

    @staticmethod
    def create_account(email: str, password: str, superuser: bool=False ):
        session = DbSessionFactory.create_session()

        account = Account()
        account.email = email.lower().strip()
        account.password_hash = AccountService.hash_text(password)
        account.is_super_user = superuser

        session.add(account)
    
        session.commit()
        return account

    @classmethod
    def find_account_by_email(cls, email):
        if not email or not email.strip():
            return None
        email = email.lower().strip()

        session = DbSessionFactory.create_session()

        account = session.query(Account).filter(Account.email == email).first()
        return account        

    @staticmethod
    def hash_text(text):
        hashed_text = sha512_crypt.encrypt(text, rounds=150_000)
        return hashed_text