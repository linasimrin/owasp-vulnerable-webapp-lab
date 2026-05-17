# Schwachstellen

Diese Datei dokumentiert alle bewusst eingebauten Sicherheitslücken im Projekt.
Pro Lücke: ID, OWASP-Mapping, Beschreibung, Payload, sichere Variante.

Status-Legende: `[ ]` geplant — `[x]` umgesetzt — `[demo]` mit Exploit-Modul

## VULN-01 — SQL-Injection (Union-based)

**OWASP 2021:** A03 – Injection
**Datei:** `app/routes/shop.py` (Produktsuche)
**Status:** `[ ]`

### Beschreibung
TBD

### Payload
```
TBD
```

### Sichere Variante
TBD

---

## VULN-02 — SQL-Injection (Blind)

**OWASP 2021:** A03 – Injection
**Datei:** `app/routes/auth.py` (Login)
**Status:** `[ ]`

### Beschreibung
TBD

### Payload
TBD

### Sichere Variante
TBD

---

## VULN-03 — Stored XSS

**OWASP 2021:** A03 – Injection
**Datei:** `app/routes/shop.py` (Produkt-Bewertungen)
**Status:** `[ ]`

### Beschreibung
TBD

### Payload
TBD

### Sichere Variante
TBD

---

## VULN-04 — Reflected XSS

**OWASP 2021:** A03 – Injection
**Datei:** `app/routes/shop.py` (Suchergebnis)
**Status:** `[ ]`

### Beschreibung
TBD

### Payload
TBD

### Sichere Variante
TBD

---

## VULN-05 — Broken Authentication

**OWASP 2021:** A07 – Identification and Authentication Failures
**Datei:** `app/routes/auth.py` (Session-Cookie / Login)
**Status:** `[ ]`

### Beschreibung
TBD

### Payload
TBD

### Sichere Variante
TBD

---

## VULN-06 — IDOR (Insecure Direct Object Reference)

**OWASP 2021:** A01 – Broken Access Control
**Datei:** `app/routes/orders.py` (`/orders/<id>`)
**Status:** `[ ]`

### Beschreibung
TBD

### Payload
TBD

### Sichere Variante
TBD

---

## VULN-07 — Path Traversal

**OWASP 2021:** A01 – Broken Access Control
**Datei:** `app/routes/orders.py` (Rechnungs-Download)
**Status:** `[ ]`

### Beschreibung
TBD

### Payload
TBD

### Sichere Variante
TBD

---

## VULN-08 — Security Misconfiguration

**OWASP 2021:** A05 – Security Misconfiguration
**Datei:** `app/__init__.py`, `app/routes/admin.py`
**Status:** `[ ]`

### Beschreibung
TBD

### Payload
TBD

### Sichere Variante
TBD

---

## VULN-09 — Sensitive Data Exposure (Bonus)

**OWASP 2021:** A02 – Cryptographic Failures
**Datei:** `app/models.py`, `app/routes/auth.py`
**Status:** `[ ]`

### Beschreibung
TBD 123
### Payload
TBD

### Sichere Variante
TBD