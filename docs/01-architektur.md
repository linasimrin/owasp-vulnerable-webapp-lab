# Architektur

## Übersicht

Die Anwendung ist ein bewusst verwundbarer Online-Shop, der mit Python und Flask
gebaut wird. Ziel ist eine realistische Webanwendung, in die wir gezielt
Sicherheitslücken aus den OWASP Top 10 einbauen, um sie anschließend mit einem
eigenen Exploit-Framework auszunutzen.

## Komponenten

- **Web-Frontend** (Jinja2 + Bootstrap): Produktliste, Produktdetail mit
  Bewertungen, Warenkorb, Login/Registrierung, Bestellverlauf, Rechnungs-Download.
- **Backend** (Flask): Routes, Business-Logik, Session-Verwaltung.
- **Datenbank** (SQLite): User, Produkte, Bestellungen, Bewertungen.
- **Exploit-Framework** (Python, separat von der App): CLI-Tool, das jede
  Schwachstelle in der laufenden App automatisch ausnutzt und einen Report
  generiert.

## Datenmodell (Entwurf)

| Tabelle    | Felder                                                    |
|------------|-----------------------------------------------------------|
| `users`    | id, username, password_hash, email, is_admin, created_at  |
| `products` | id, name, description, price, stock, image_path           |
| `reviews`  | id, product_id, user_id, content, rating, created_at      |
| `orders`   | id, user_id, total, status, created_at                    |
| `order_items` | id, order_id, product_id, quantity, unit_price         |
| `invoices` | id, order_id, file_path, created_at                       |

## Request-Flow (Beispiel: Produktsuche)

1. Browser sendet `GET /search?q=...`
2. Flask-Route `shop.search` nimmt den Parameter entgegen
3. SQL-Abfrage wird gegen `products` ausgeführt
4. Ergebnis wird in `templates/search.html` gerendert und zurückgegeben

In diesem Flow stecken später zwei Lücken:
- VULN-01 (SQLi Union-based) im Query-Building
- VULN-04 (Reflected XSS) im Template-Rendering

## Projekt-Struktur

```
app/
├── __init__.py        # Flask-App-Factory
├── models.py          # SQLAlchemy-Modelle
├── routes/
│   ├── auth.py        # Login, Register, Logout
│   ├── shop.py        # Produkte, Suche, Warenkorb
│   ├── orders.py      # Bestellungen, Rechnungs-Download
│   └── admin.py       # Admin-Bereich (bewusst ungeschützt)
├── templates/         # Jinja2-Templates
├── static/            # CSS, JS, Bilder
└── uploads/           # Datei-Uploads (Path-Traversal-Ziel)
```

## Isolation

Die gesamte Anwendung läuft in einem Docker-Container. So ist sichergestellt,
dass die Schwachstellen weder das Host-System noch das lokale Netzwerk
gefährden können. Konfiguration in `docker-compose.yml`.