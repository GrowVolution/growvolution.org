## 🗂️ Projekt Struktur

```bash
growvolution.org/
├── website/                # Package der Flask-App
    ├── data/               # Flask SQLAlchemy Daten der Seite
    ├── logic/              # Strukturierte Logik der Routes
    ├── routing/            # Routing der Seite (übergibt Handling an 'logic/')
    ├── socket/             # Flask SocketIO Package
        ├── events/         # Eventhandling
        ├── messages/       # Gezielt Nachrichten an aktive Clients senden
    ├── static/
        ├── css/            # Eigene Styles
        ├── js/             # Frontend Logik
        ├── img/            # Bilder
    ├── subsites/           # Subsites der Seite (für subdomains)
        ├── learning/       # Lernplattform (in Planung)
            ├── ...         # Aufbau ähnlich wie website/
        ├── people/         # Für Interna (Verein, ...)
            ├── ...         # wie website/
        ├── banking/        # Banking-System (in Planung)
            ├── ...         # wie website/
    ├── templates/          # HTML Templates (Jinja2)
    ├── utils/              # Tools der App
    ├── ...
├── setup.*                 # Nur zur Einrichtung des Projekts
├── requirements.txt        # Abhängigkeiten
├── PICTURES.md             # Auf der Seite verwendete Bilder (CC0)
├── main.py                 # 'python main.py' -> Startet die App
├── ...                             
```

Schau dich gern ein wenig um, ich bin sehr bemüht es übersichtlich und tragfähig für den weiteren Ausbau zu halten.
Wenn du Fragen oder Feedback hast, bin ich immer offen dafür! ✌🏼
