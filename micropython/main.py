import urequests as requests # lib für http requests (=datenübertragung internet)
import ujson # lib für die verarbeitung von json files
import uos, machine, time, urandom # weitere helfer libs


def post_data_to_server():  # funktion die daten an einen server posten
    #rand = random.randint(0,10)
    temp = 20 + urandom.getrandbits(3) # temperatur + zufällige abweichung
    hum = 50 + urandom.getrandbits(5) # feuchte + zufällige abweichung
    post_data = ujson.dumps({ 'temp': temp, 'hum': hum}) # ein eine json variable wird erzeugt
    request_url = 'http://192.168.178.69:8000/post_data' # die ip/url für den request wird festgelegt
    try: # es soll versucht werden den post-request zu machen:
      res = requests.post(request_url, headers = {'content-type': 'application/json'}, data = post_data) # der eigentliche request
      result_txt = ujson.loads(res.text) # konvertiert die json antowrt des servers zu einem python obj
      print(result_txt['message']) # gibt die antwort in der shell aus
      
    except: # falls ein fehler bei dem request auftritt gebe eine rückmeldung
        print("could not post: ",post_data)
        res = -1
    return res
    
while True:  # diese schleife wird nach boot.py bis sie abgebrochen wird durchgeführt
    post_data_to_server() #daten werden an server geschickt
    time.sleep(5) # der esp wartet 5 sekunden
    
    