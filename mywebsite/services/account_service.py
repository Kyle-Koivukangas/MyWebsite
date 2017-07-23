
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
    def create_account(email: str, password: str, superuser: bool):

        session = DbSessionFactory.create_session()

        account = Account(email=email, password=password, created=datetime.now(), email_confirmed=True, is_super_user=False, )
        
        session.add(account)
    
        session.commit()
        return account