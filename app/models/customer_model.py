from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash


@dataclass
class CustomerModel(db.Model):
    id: int
    name: str
    last_name: str
    email: str
    cep: str
    street: str
    neighborhood: str
    state: str
    phone: str

    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    cep = Column(String(12), nullable=False)
    street = Column(String(256), nullable=False)
    neighborhood = Column(String(256), nullable=False)
    state = Column(String(256), nullable=False)
    phone = Column(String(15), nullable=False)
    password_hash = Column(String(255), nullable=False)

    @property
    def password(self):
        raise AttributeError('Password is not acessible.')

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)
        return self.password_hash

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
