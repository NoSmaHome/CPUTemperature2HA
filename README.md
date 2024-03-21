# CPUTemperature2HA

Voraussetzungen

Homeassistant Installation

aktive ssh-Verbindung auf euren externen Server (extern meint hier, nicht der localhost von Homeassistant)

Grundlegendes Verständnis in der IT (optional)

Vorgehen

Wie lese ich die CPU-Temperatur von einem Raspberry überhaupt aus?

Wie sorge ich dafür, dass diese automatisch ausgelesen wird und an Homeassistant übermittelt wird?

Wie richte ich einen Service ein, damit die Übertragung auch nach einem Neustart noch funktioniert?

1. Wie lese ich die CPU-Temperatur von einem Raspberry aus?

Das grundsätzliche Auslesen der CPU-Temperatur ist nicht sonderlich schwer und kann mit einem Command direkt umgesetzt werden.

vcgencmd measure_temp

Du erhältst als Ausgabe hier temp=54.9'C

Bis hierhin erstmal ganz Simpel, oder?

2. Wie sorge ich dafür, dass die Temperatur automatisch ausgelesen und an Homeassistant übermittelt wird?

Hierzu ist - wer hätte es gedacht - ein Script notwendig.

Da das Script auf Python-Basis läuft, müssen wir hier erstmal die notwendigen Voraussetzungen erfüllen und python3-pip installieren. Das geht wie folgt:

sudo apt update
sudo apt install python3-pip

Nach der Installation können wir nun schon unser Script schreiben. Ich habe dies im Verzeichnis /home/USER/scripts abgelegt. (USER musst du hier durch deinen Systembenutzer ersetzen)

mkdir -p /home/USER/Scripts
nano /home/USER/Scripts/cpu_temperatur_publisher.py

Hier kannst du nun gerne mein bereits geschriebenes Script verwenden

WICHTIG: Passe hier unbedingt HOMEASSISTANTIP und ACCESS-TOKEN an. Den Part "friendly_name" kannst du anpassen, um dort einen eigenen Namen für die Entität festzulegen.

Deine Homeassistant IP kennst du bestimmt, den Access Token erhälst du wie folgt:

Klicke in Homeassistant unten rechts auf deinen Benutzer (ich habe hier einen extra Benutzer erstellt, der nur die lokale Anmeldung unterstützt (musst du aber nicht))

Scrolle ganz nach unten und klicke auf "Langlebigen Access-Token erstellen"

Füge den Token ins Script ein (Der Part mit "Bearer " muss stehen bleiben, das ist ein Teil der Authentifizierung)

Speichere nun das Script mit STRG + O und schließe es mit STRG + X

testen unseres scripts

Zum Testen unseres Scripts kannst du nun einfach folgendes in die Konsole eingeben:

python3 /home/USER/scripts/cpu_temperatur_publisher.py

Wenn du hier eine Fehlermeldung erhältst, kann es sein, dass dein Script noch nicht ausführbar ist. Das holen wir schnell mit folgendem Befehl nach:

sudo chmod +x /home/USER/scripts/cpu_temperatur_publisher.py

Das Script läuft jetzt bereits und übermittelt die Temperatur an Homeassistant. Du kannst diese einsehen, indem du auf "Einstellungen → Geräte & Dienste → Entitäten" klickst und nach deiner Entität suchst (friendly_name aus dem Script)

Du hast es bis hierhin geschafft? Super! Das "Problem" ist nur, dass sobald du dein Terminal schließt oder den Raspberry neu startest, das Script abbricht und keine Werte mehr übermittelt. Wie lösen wir das?

Service einrichten, damit das Script automatisch läuft und startet

Wir müssen hier also einen systemd Service anlegen. Dazu müssen wir diesen erstmal schreiben. Das kannst du z.B. so machen:

sudo nano /etc/systemd/system/cpu_temperature_publisher.service

WICHTIG: Passe hier bitte unbedingt die zwei Platzhalter "SYSTEMBENUTZER" auf deinen Systembenutzernamen an, sonst funktioniert es nicht.

Du kannst du nun wieder Speichern mit STRG + O und schließen mit STRG + X

Damit hast du deinen eigenen systemd Service geschrieben. Dieser muss nun nur noch einmalig gestartet und aktiviert werden. Nutze dafür folgende Befehle:

sudo systemctl daemon-reload
sudo systemctl start cpu_temperature_publisher.service
sudo systemctl enable cpu_temperature_publisher.service

Um zu schauen, dass du alles richtig gemacht hast, kannst du dir den Status deines Services angucken. Dazu dient der Befehl

sudo systemctl status cpu_temperature_publisher.service

Du siehst in Grün die wichtigsten Punkte

enabled = Aktiviert - Der Service startet nach einem Neustart automatisch mit.

active (running) = Service läuft aktuell

Weitergehend solltest du unter CGroup auch dein eigenes Script sehen, auf welches der Service zugreift.
