from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

import os

load_dotenv()
app = Flask(__name__)

# Configurações do ambiente
if os.environ.get('FLASK_ENV') == 'production':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://seu_usuario:senha@db.sxvthokbekxptdcvymsc.supabase.co:5432/seu_banco'
else:
    host = os.environ.get('DB_HOST')
    db_name = os.environ.get('DB_NAME')
    username = os.environ.get('DB_USERNAME')
    password = os.environ.get('DB_PASSWORD')
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@{host}/{db_name}'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:54322/postgres'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

from app import views, models