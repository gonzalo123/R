import random
from functools import wraps

from flask import Flask, jsonify, request

app = Flask(__name__)

VALID_TOKEN = "api-secret-token"


def token_required(valid_token=VALID_TOKEN):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            auth_header = request.headers.get('Authorization')
            if auth_header and auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]

            if not token or token != valid_token:
                return jsonify({'message': 'Not valid token'}), 401

            return f(*args, **kwargs)

        return decorated

    return decorator


def generate_phone_number():
    area_code = random.randint(200, 999)
    prefix = random.randint(100, 999)
    line = random.randint(1000, 9999)
    return f"+1 {area_code}-{prefix}-{line}"


@app.get('/data')
@token_required(valid_token=VALID_TOKEN)
def get_data():
    return jsonify([
        {"phone": generate_phone_number(), "name": "Juan Pérez", "email": "juan@example.com"},
        {"phone": generate_phone_number(), "name": "María García", "email": "maria@example.com"},
        {"phone": generate_phone_number(), "name": "Carlos López", "email": "carlos@example.com"},
        {"phone": generate_phone_number(), "name": "Ana Martínez", "email": "ana@example.com"},
        {"phone": generate_phone_number(), "name": "Pablo Sánchez", "email": "pablo@example.com"},
        {"phone": generate_phone_number(), "name": "Laura Rodríguez", "email": "laura@example.com"},
        {"phone": generate_phone_number(), "name": "Diego Fernández", "email": "diego@example.com"},
        {"phone": generate_phone_number(), "name": "Carmen Gómez", "email": "carmen@example.com"},
        {"phone": generate_phone_number(), "name": "Javier Díaz", "email": "javier@example.com"},
        {"phone": generate_phone_number(), "name": "Sofía Ruiz", "email": "sofia@example.com"},
        {"phone": generate_phone_number(), "name": "Miguel Álvarez", "email": "miguel@example.com"},
        {"phone": generate_phone_number(), "name": "Lucía Jiménez", "email": "lucia@example.com"},
        {"phone": generate_phone_number(), "name": "Alejandro Moreno", "email": "alejandro@example.com"},
        {"phone": generate_phone_number(), "name": "Elena Muñoz", "email": "elena@example.com"},
        {"phone": generate_phone_number(), "name": "David Alonso", "email": "david@example.com"},
        {"phone": generate_phone_number(), "name": "Natalia Torres", "email": "natalia@example.com"},
        {"phone": generate_phone_number(), "name": "Roberto Gutiérrez", "email": "roberto@example.com"},
        {"phone": generate_phone_number(), "name": "Cristina Navarro", "email": "cristina@example.com"},
        {"phone": generate_phone_number(), "name": "Antonio Ramos", "email": "antonio@example.com"},
        {"phone": generate_phone_number(), "name": "Isabel Ortega", "email": "isabel@example.com"}
    ])
