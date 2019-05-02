import braintree
import os

MERCHANT_ID = os.getenv('BT_MERCHANT_ID')
PUBLIC_KEY = os.getenv('BT_PUBLIC_KEY')
PRIVATE_KEY = os.getenv('BT_PRIVATE_KEY')

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id= MERCHANT_ID,
        public_key= PUBLIC_KEY,
        private_key= PRIVATE_KEY
    )
)

def generate_client_token():
    return gateway.client_token.generate()

def transact(options):
    return gateway.transaction.sale(options)

def find_transaction(id):
    return gateway.transaction.find(id)