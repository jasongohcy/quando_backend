from flask import Blueprint, request
from flask.json import jsonify
import os
from models.user import User
from models.payment import Payment
from quando_api.utils.braintree_helper import generate_client_token, transact
from quando_api.utils.jwt_helper import *
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)


payment_api_blueprint = Blueprint('payment_api',
                                  __name__,
                                  template_folder='templates')

@payment_api_blueprint.route('/token', methods=['GET'])
@jwt_required
def token():
    return generate_client_token()


@payment_api_blueprint.route('/new', methods=['POST'])
@jwt_required
def new():
    data = request.form
    subscription_amount = 100
    target_user = User.get_or_none( User.id == data['user_id'])
    payment_nonce = request.form['payment_method_nonce']
    payment_succeeded = False
    new_subscription = None

    if (target_user):
        transaction = transact( {
            "amount": subscription_amount,
            "payment_method_nonce": payment_nonce,
            "options": {
                "submit_for_settlement": True
            }
        } )
        
        print(transaction)
        if transaction:
            new_payment = Payment.create(
                amount=subscription_amount,
                payment_nonce=payment_nonce
            )

            new_subscription = Subscription.create(
                payment=new_payment.id,
                for_user=target_user.id
            )

            payment_succeeded = True
    
    return_data = None
    if new_subscription:
        return_data = new_subscription.as_dict()

    result = jsonify({
        'status' : payment_succeeded,
        'data' : return_data
    })

    return result