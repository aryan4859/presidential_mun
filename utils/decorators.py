from functools import wraps
from flask import request, jsonify
from utils.helpers import decode_auth_token  # Ensure decode_auth_token is correctly imported

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get token from Authorization header (preferred method)
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header[7:]  # Remove 'Bearer ' part

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            # Decode the token and get the user ID
            user_id = decode_auth_token(token)
            if isinstance(user_id, str):  # Check if token decoding returned an error message
                raise Exception(user_id)
        except Exception as e:
            return jsonify({'message': str(e)}), 403
        
        # Pass the user_id to the route handler
        return f(user_id, *args, **kwargs)
    
    return decorated_function
