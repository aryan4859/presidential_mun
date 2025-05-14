#utils/decorators.py
from functools import wraps
from flask import request, jsonify
from utils.helpers import decode_auth_token 

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header[7:]  

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            user_id = decode_auth_token(token)
            if isinstance(user_id, str):  
                raise Exception(user_id)
        except Exception as e:
            return jsonify({'message': str(e)}), 403
        
        return f(user_id, *args, **kwargs)
    
    return decorated_function
