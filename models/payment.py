import peewee as pw
from models.base_model import BaseModel
from models.user import User


class Payment(BaseModel):
    amount = pw.DecimalField()
    payment_nonce = pw.TextField()