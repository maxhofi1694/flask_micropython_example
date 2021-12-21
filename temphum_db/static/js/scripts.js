// Empty JS for your own code to be here

// eine funktion welche nach vollständigem laden der seite immer wieder ausgeführt wird
$(document).ready(function () {
    function update_status() {
        $.getJSON("/get_latest_status", // holt sich den letzten eintrag von python
            function (data) {
                // man schaut ob das element mit der id temp auf der seite des users vorhanden ist = man ist auf der homepage
                var element = document.getElementById('temp'); // check if it is on main page https://stackoverflow.com/questions/5629684/how-can-i-check-if-an-element-exists-in-the-visible-dom
                if (typeof (element) != 'undefined' && element != null) { // falls ja
                    document.getElementById("temp").innerHTML = data.temp + " °C"; // ersetze das element temp mit der aktuellen temperatur und °C
                    document.getElementById("hum").innerHTML = data.hum + " %"; // gleichfalls für die feuchte
                }

            }
        );
        setTimeout(arguments.callee, 5000); // warte nun 5s
    };

    update_status() // ruf die funktion immer wieder auf, sobald die seite geladen wurde
});


