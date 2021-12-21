# initialisiert das package und sieht bei jedem server gleich aus
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cf70bb46d14588d7782df5c5717fd2fa' # random key welcher bei manachen webseiten gebraucht wird
db = SQLAlchemy(app)

from temphum_db import routes # hier müssen nochmal die verschiedenen sub-urls eingeladen werden