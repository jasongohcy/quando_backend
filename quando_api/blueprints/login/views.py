from flask import Blueprint, request, jsonify, url_for
import os
from models.user import User
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime,timedelta

login_api_blueprint = Blueprint('login_api',
                                __name__,
                                template_folder='templates')

# login user
@login_api_blueprint.route('/create', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    time = request.json.get('time', None)
    
    errors = []
    if not username:
        errors.append("username")
    if not password:
        errors.append("password")
    if errors:
        return jsonify({"msg": {"Missing parameters":[error for error in errors]}}), 400

    user = User.get_or_none(User.username == username)
    if user and check_password_hash(user.password, password):
        user.last_login = time
        user.save()
        new_user_id = user.id
        expires = timedelta(days=365)
        access_token = create_access_token(new_user_id, expires_delta=expires)


        return jsonify({
            "access_token": access_token,
            "message": "Successfully signed in.",
            "status": "success",
            "user": {
                "id": user.id,
                "destination": user.going_to,
                "location": user.location,
                "profile_picture": user.profile_image_url,
                "username": user.username
            }
        }), 200
    else:
        return jsonify({"msg": "Bad login"}), 404


# google sign in
@login_api_blueprint.route("/callback", methods=["POST"])
def callback():
    import ast
    email = ast.literal_eval(request.json["body"])["profileObj"]["email"]
    # email = request.json["profileObj"]["email"]
    check_user = User.get_or_none(User.email == email)
    if check_user:
        expires = timedelta(days=365)
        access_token = create_access_token(check_user.id, expires_delta=expires)
        return jsonify({
            "access_token": access_token,
            "message": "Successfully signed in.",
            "status": "success",
            "user": {
                "id": check_user.id,
                "profile_picture": check_user.profile_image_url,
                "username": check_user.username
            }
        }), 200
    else:
        return jsonify({"msg": "Bad login"}), 404

# facebook sign in
@login_api_blueprint.route("/callback/facebook", methods=["POST"])
def callback_facebook():
    # breakpoint()
    email = request.json["email"]
    check_user = User.get_or_none(User.email == email)
    if check_user:
        expires = timedelta(days=365)
        access_token = create_access_token(check_user.id, expires_delta=expires)
        return jsonify({
            "access_token": access_token,
            "message": "Successfully signed in.",
            "status": "success",
            "user": {
                "id": check_user.id,
                "profile_picture": check_user.profile_image_url,
                "username": check_user.username
            }
        }), 200
    else:
        return jsonify({"msg": "Bad login"}), 404


@login_api_blueprint.route('/logout')
def logout():
    return jsonify ({
        'status' : True
    })