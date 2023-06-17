import os
from flask import Flask
from sqlalchemy import text
from routes import tasks
from models import db
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(tasks)
app.debug = True

load_dotenv()
dbConnectionString = os.getenv("DB_CONNECTION_STRING")
app.config['SQLALCHEMY_DATABASE_URI'] = dbConnectionString

db.init_app(app)


def check_connection():
    with app.app_context():
        try:
            db.session.execute(text("SELECT 1"))
            print('Database connection successful')
        except Exception as e:
            print(f"Error connecting to the database: {str(e)}")
        finally:
            db.session.remove()


if __name__ == '__main__':
    check_connection()
    app.run()
