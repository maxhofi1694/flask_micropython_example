# startet den gesamten webserver, welcher im package temphum_db zusammengefasst ist

from temphum_db import app, db # importiert die notwendigen sachen aus dem package
from sqlalchemy_utils import database_exists # helfer funktion zum schauen ob es eine datenbank gibt


if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # legt fest wie die datenbank heißt, und /// gibt an, dass sie in dem package-ordner liegen soll
    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']): # schaut ob es die datenbank gibt
        db.create_all() #wenn nicht wird sie erstellt
    app.run(host="0.0.0.0", port=8000, debug=True) # startet den webserver auf der ip des computers mit dem port 8000
  