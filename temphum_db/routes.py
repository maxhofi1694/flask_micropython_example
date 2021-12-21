# diese datei definiert alle sub-urls = routes
from flask import Flask, render_template, request, jsonify # importiert helfer die gebaucht werded
from temphum_db import app, db # importiert teile der app/server
from temphum_db.models import  sensordata # importiert in welchem "model" = struktur die daten in der datenbank gespeichert sind
from sqlalchemy import desc, and_, not_ # importiert helfer um auf die datenbank zuzugreifen und alle daten zu sortieren



@app.route("/",methods=['GET']) # das definiert unsere hauptseite. GET bedeutet, dass sie dem nutzer der sie aufruft etwas gibt
def home():
    return render_template("home.html") # es soll einfach nur das html file "home.html" angezeigt werden

@app.route("/table",methods=['GET']) # das definiert die seite, wo die tabelle angezeigt wird
def table():
    all_data = sensordata.query.order_by(desc(sensordata.reading_time)).all() #  alle daten aus der datenbank werden geladen, geordnet nach der zeit 
    #print(all_data)
    return render_template("table.html",all_data=all_data) # die seit table.html soll dargestellt werden. dazu werden auch alle daten aus der datenbank angegeben



@app.route("/post_data", methods=['POST']) # das ist keine seite sondern wegen POST das interface wo der nutzer daten hinschicken kann
def post_data(): # sobald /post_data aufgerufen wird wird diese funktion ausgeführt
    print("Neue Daten!") 
    data = request.get_json() # von dem post request wird die json-payload genommen    

    newSensordata = sensordata()  # erstellt einen blankoeintrag für die datenbank
    if "temp" in data:  # schaut ob es den key temp überhaut in der json variable hat
            newSensordata.temp = data["temp"] # falls ja wird der wert in den blanko eintrag gespeichert
    if "hum" in data:  # schaut ob es den key hum überhaut in der json variable hat
        newSensordata.hum = data["hum"] # falls ja wird der wert in den blanko eintrag gespeichert
        db.session.add(newSensordata) # der befüllte blanko eintrag wird der datenbank hinzugefügt
        db.session.commit() # und das hinzufügen wird bestätigt
        print("Es hat %0.2f °C und %0.2f %% rel. Feuchte" % (data["temp"],data["hum"]))
        return jsonify({"message": "Json posted for normal sensor"}), 200 # an den nutzer soll ein json zurückgegeben werden, dass alles gklappt hat
    else: # falls hum/temp nicht im request waren
        return jsonify({"message": "ERROR: Temperatur und Feuchte fehlt"}), 401 # soll der nutzer eine entsprechende fehlermeldung bekommen


@app.route("/get_latest_status", methods=["GET"]) # methode om die letzten gesendeten werte abzufragen
def get_latest_status():
    currentSensor = sensordata.query.order_by(sensordata.id.desc()).first() # sucht in der datenbank alle daten raus, ordnet sie absteigend, und wählt dann den ersten = jüngste dateneintrag aus

    current_temp_hum = {
                          "time": currentSensor.reading_time.strftime('%X GMT %D '),
                          "temp": currentSensor.temp,
                          "hum":  currentSensor.hum } # das ist eine ein jsonformat das an denjenigen gegeben wird der die funktion aufgerufen hat
    return  jsonify(current_temp_hum) # hier wird es zurückgegeben