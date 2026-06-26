# OWASP Vulnerable Webapp Lab

Bonusprojekt ITS, SoSe 2026, Hochschule Bochum.
Projekt 3: Vulnerable Webapp mit automatisiertem Exploit-Framework.

## Über das Projekt

Wir entwickeln einen Online-Shop mit mindestens 8 bewusst eingebauten Lücken
aus den OWASP Top 10. Dazu kommt ein Python-Exploit-Framework, das jede Lücke
automatisch ausnutzt und einen Report erzeugt.

## Team

| Name          | Matrikelnummer | Hauptthema                          |
|---------------|----------------|-------------------------------------|
| Elina Velecka | 18389748       | Auth & Exploit-Framework            |
| Lina Simrin   | 18395871       | Shop-Backend & SQLi-Lücken          |
| Njomza Zumeri | 18386523       | Forum/Reviews & XSS-Lücken          |

## Tech-Stack

- Python 3.11+, Flask, Flask-SQLAlchemy
- SQLite
- Jinja2-Templates, Bootstrap 5
- Docker / docker-compose
- Exploit-Framework: requests, BeautifulSoup, colorama, tabulate
- Tests: pytest

## Geplante Schwachstellen

| ID      | Schwachstelle               | OWASP 2021                | Geplanter Ort                 |
|---------|-----------------------------|---------------------------|-------------------------------|
| VULN-01 | SQL-Injection (Union-based) | A03 – Injection           | Produktsuche                  |
| VULN-02 | SQL-Injection (Blind)       | A03 – Injection           | Login-Endpunkt                |
| VULN-03 | Stored XSS                  | A03 – Injection           | Produkt-Bewertungen           |
| VULN-04 | Reflected XSS               | A03 – Injection           | Suchergebnis-Seite            |
| VULN-05 | Broken Authentication       | A07 – Auth Failures       | Session-Cookie / Login        |
| VULN-06 | IDOR                        | A01 – Broken Access Ctrl  | /orders/<id>                  |
| VULN-07 | Path Traversal              | A01 – Broken Access Ctrl  | Rechnungs-Download            |
| VULN-08 | Security Misconfiguration   | A05 – Misconfiguration    | Debug-Mode, /admin ungesch.   |
| VULN-09 | Sensitive Data Exposure     | A02 – Crypto Failures     | MD5-Passwörter (Bonus)        |
| VULN-10 | Insecure Deserialization    | A08 – Software Integrity  | Pickle-Cookie (Bonus)         |

Details zu jeder Lücke in `docs/02-vulnerabilities.md`.

## Setup

```bash
git clone https://github.com/linasimrin/owasp-vulnerable-webapp-lab.git
cd owasp-vulnerable-webapp-lab

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python -m app
```

App läuft unter `http://127.0.0.1:5000`.

## Exploit-Framework

```bash
python exploits/exploit_framework.py --target http://127.0.0.1:5000 --all
python exploits/exploit_framework.py --target http://127.0.0.1:5000 --module sqli_union
```

Reports landen in `exploits/reports/`.

## Projekt-Struktur

```
owasp-vulnerable-webapp-lab/
├── app/                # Flask-Anwendung
├── exploits/           # Exploit-Framework
├── docs/               # Doku
├── tests/              # Tests
├── presentation/       # Folien
├── docker-compose.yml
└── requirements.txt
```

## Dokumentation

- `docs/01-architektur.md` — Architektur, Datenmodell
- `docs/02-vulnerabilities.md` — Schwachstellen im Detail
- `docs/03-exploit-framework.md` — Aufbau des Frameworks
- `docs/04-defense.md` — sichere Varianten
- `docs/05-team-rollen.md` — Aufgabenverteilung
