**Einfaches Beispiel für einen Flask-Server (Python) und ESP (Micropython)**


Das System besteht aus zwei Teilen:

1.  Dem ESP, welcher die die Temperatur und Feuchte an den Server schickt, sobald er angeschalten ist
2.  Dem Flask-Server, welcher:
- die Daten von dem ESP empfängt und in eine Datenbank speichert
- dem Nutzer eine Webseite zur Verfügung stellt:
  - die Hauptseite mit neuen Werten updated
  - auf einer Setie alle bisherigen Werte anzeigt


**Ordnerstruktur**

- TEMPHUM_DB: 
  - .vscode/: Einstellungen für VSCODE (IDE), das sollte alles autogeneriert sein
  - micropython/: boot.py + main.py für den ESP
  - temphum_db/: das Package für den Flask-Server
    - static/: alle statischen Dateien des Servers wie CSS, Fonts und Javascript
      - js/: scripts.js beinhaltet die Funktion die die Temperatur/Feuchte auf der Homepage alle 5s updated.

  - templates/: beinhaltet die html-Files
  - __init __.py: erzeugt das Python-Package
  - data.db: Die Datenbank. Wird erstellt, sobald der FLask-Server das erste mal läuft
  - models.py: beschreibt die Struktur der Daten in der Datenbank
  - routes.py: beschreibt die einzelnen "Seiten" die der Server besitzt und verarbeitet alle Daten
  - .gitignore: listet alle Files/Ordner auf, welche **nicht** in Git aufgenommen werden sollen
  - requirements.txt: listet alle packages auf, die der Flask-Server benötigt
  - run.py: startet den Server


**Funktionsweise**
- Server:
  - der Server stellt einen Endpunkt für Temperatur und Feuchtewerte bereit. Wenn Daten im richtigen Format an den Endpunkt geschickt werden, speichert der Server die Daten in einer Datenbank ab.
  - der Server stellt zwei Seiten bereit:
    - die Hauptseite, bei der die momentane Temperatur und Feuchte angezeigt wird
    - eine Seite, die die Tabelle aller bisherigen Temperaturen/Feuchtewerte anzeigt
  - für die Haupseite stellt der Sever noch ein Endpunkt bereit, bei dem er die aktuellsten Werte zurück gibt
- ESP:
  - der ESP liest die Temperatur und Feuchte ein (hier werden nur Dummywerte verwendet)
  - er formatiert diese Werte und schickt sie als POST-HTTP Request an den Server

![Overview](/overview.svg )


**Benutzung:**

*für Ubuntu oder RaspberryPi in einem Terminal*

1. clonen des Repository 
   
   `git clone `

2. Installieren des Python-Virtualenvironment (vereinfacht die Installation der benötigten Packages):
   
   `sudo apt install python3-venv` (installiert die bnötigten Packages)

3. Innerhalb des Ordners TEMPHUM_DB soll ein virtual environment mit dem name `env` erstellt werden:
   
   `python3 -m venv env`

4. Nun aktiviere das virtual environment:
   
   `source env/bin/activate`

   im Terminal muss nun `(env) user@computer:` stehen

5. Installieren aller benötigten packages (aus requirement.txt):
   
   `pip install -r requirements.txt`

6. Starten des Servers:
   
   `pfad/zum/ordner/temphum_db/env/bin/python pfad/zum/ordner/temphum_db/run.py`

   in dem Terminal wird dann angegeben auf welcher IP der Server läuft:

   `Running on http://192.168.178.69:8000/ (Press CTRL+C to quit)`

Sobald die Seite aufgerufen wird oder der ESP Daten schickt wird das in dem Terminal entsprechend angezeigt:

`192.168.178.69 - - [19/Dec/2021 17:10:44] "GET /get_latest_status HTTP/1.1" 200`

   