from . import API
from ..data.admins import AdminToken, Admin
from shared.data import delete_model, add_model
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import UnsupportedAlgorithm


def _get_token(data):
    return AdminToken.query.get(data['token'])


@API.register('verify_token')
def verify_token(data):
    token_obj = _get_token(data)
    valid = True if token_obj else False
    return { 'valid': valid }


@API.register('create_user')
def create_user(data):
    response = { 'success': False }

    token_obj = _get_token(data)
    if not token_obj:
        response['error'] = 'Invalid token'
        return response

    username = data.get('username')
    pub_key_str = data.get('public_key')

    if not username or not pub_key_str:
        response['error'] = 'Incomplete data'
        return response

    if Admin.query.filter_by(name=username).first():
        response['error'] = 'Username already exists'
        return response

    try:
        serialization.load_pem_public_key(pub_key_str.encode())
    except (ValueError, UnsupportedAlgorithm):
        response['error'] = 'Invalid public key'
        return response

    user = Admin(username, token_obj.email, pub_key_str.encode())
    add_model(user)
    delete_model(token_obj)

    response['success'] = True
    return response
