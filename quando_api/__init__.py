from app import app
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##
from quando_api.blueprints.users.views import users_api_blueprint
from quando_api.blueprints.login.views import login_api_blueprint
from quando_api.blueprints.payment.views import payment_api_blueprint
from quando_api.blueprints.sessions.views import sessions_api_blueprint


app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users')
app.register_blueprint(login_api_blueprint, url_prefix='/api/v1/login')
app.register_blueprint(payment_api_blueprint, url_prefix='/api/v1/payment')
app.register_blueprint(sessions_api_blueprint, url_prefix='/api/v1/sessions')




