from models.user import User
from models.contact import Contact
from flask import Blueprint, jsonify, request
from quando_api.utils.jwt_helper import *
import json

contact_api_blueprint = Blueprint('contact_api', __name__, template_folder='templates')

@contact_api_blueprint.route('/', methods=['POST'])
def create():
    req_data = request.get_json()
    email = req_data['email']
    text = req_data['text']

    contact = Contact(email=email, text=text)
    if contact.save():
        return jsonify({
            'message': 'Successfully submitted',
            'status': 'success',
        })
    else:
        errors = user.errors
        return jsonify({
            'status': 'failed',
            'message': errors
        })