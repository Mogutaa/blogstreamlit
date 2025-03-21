import os
import bcrypt
from dotenv import load_dotenv
from streamlit_authenticator import Authenticate

load_dotenv()

def setup_auth():
    # Carregar credenciais do .env
    admin_user = os.getenv("ADMIN_USERNAME")
    admin_pass = os.getenv("ADMIN_PASSWORD").encode('utf-8')
    stored_hash = os.getenv("ADMIN_HASHED_PASSWORD").encode('utf-8')

    # Verificar se o hash da senha está correto
    if not bcrypt.checkpw(admin_pass, stored_hash):
        raise ValueError("Senha admin inválida ou hash corrompido")

    return Authenticate(
        credentials={
            'usernames': {
                admin_user: {
                    'email': os.getenv("ADMIN_EMAIL"),
                    'name': 'Administrador',
                    'password': stored_hash.decode('utf-8')
                }
            }
        },
        cookie_name='portfolio_auth',
        key=os.getenv("COOKIE_KEY"),
        cookie_expiry_days=30
    )
