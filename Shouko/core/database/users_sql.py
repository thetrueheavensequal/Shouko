from sqlalchemy import Column, BigInteger, JSON
from core.database import BASE, SESSION


class Users(BASE):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    user_id = Column(BigInteger, primary_key=True)
    target_user = Column(JSON)

    def __init__(self, user_id, target_user=None):
        self.user_id = user_id
        self.target_user = target_user

    def __repr__(self):
        return "<User {} ({})>".format(self.target_user, self.user_id)


def num_users():
    try:
        return SESSION.query(Users).count()
    finally:
        SESSION.close()