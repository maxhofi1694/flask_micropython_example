from temphum_db import db
from datetime import datetime
# die datei beschreibt in welcher struktur die daten in der datenbank gespeichert sind

class sensordata(db.Model):
    id = db.Column(db.Integer, primary_key=True) # es gibt eine spalte id welche eine normale zahl (integer) ist und als hauptordnungszahl dient
    temp = db.Column(db.Float) # es gibt die temperatur als float zahl
    hum = db.Column(db.Float) # gleichfalls die feuchte
    reading_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # und es gibt eine datumszeile. dieser eintrag muss immer gemacht werden. da der esp kein datum mitliefert wird als default wert immer die momentane utc zeit vom server genommen

    def __repr__(self):
        return f"sensordata('{self.id}', '{self.temp}, '{self.hum},  '{self.reading_time}')" # das ist eine funktion wie daten nach print befehlen in der console dargestellt werden
