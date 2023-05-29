from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from common.variables import SERVER_DATABASE

Base = declarative_base()


class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    initiator = relationship('Contacts', backref='initiator')
    recipient = relationship('Contacts', backref='recipient')

    def __init__(self, username):
        self.name = username
        self.id = None

    def __repr__(self):
        return f'User {self.id} : {self.name}'


class LoginHistory(Base):
    __tablename__ = 'LoginHistory'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_time = Column(DateTime)
    ip = Column(String)
    port = Column(String)

    def __init__(self, name, date, ip, port):
        self.id = None
        self.name = name
        self.date_time = date
        self.ip = ip
        self.port = port

    def __repr__(self):
        return f'{self.date_time} - {self.name} port:{self.port} id:{self.id}'


class Contacts(Base):
    __tablename__ = 'Contacts'
    id = Column(Integer, primary_key=True)
    from_user_id = Column(Integer, ForeignKey('Users.id'))
    to_user_id = Column(Integer, ForeignKey('Users.id'))
    status = Column(String, default='Sent')

    def __init__(self, id, from_user_id, to_user_id, status):
        self.id = id
        self.from_user_id = from_user_id
        self.to_user_id = to_user_id
        self.status = status

    def __repr__(self):
        return f'{self.from_user_id} - {self.to_user_id} status : {self.status}'


class ServerStorage:
    def __init__(self):
        self.database_engine = create_engine(SERVER_DATABASE, echo=True, pool_recycle=7200)
        Base.metadata.create_all(self.database_engine)


db = ServerStorage()
