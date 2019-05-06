from models.base_model import BaseModel
from models.user import User
import peewee as pw
from app import app

class Contact(BaseModel):
    email = pw.CharField()
    text = pw.CharField()

