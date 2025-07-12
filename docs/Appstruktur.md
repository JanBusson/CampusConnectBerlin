---
title: Struktur der App
nav_order: 3
---

# Struktur der Anwendung
Um so strukturiert wie möglich zu arbeiten, haben wir unsere Datenstruktur, siehe im Folgendem, so aufgeteilt.

**Ordner Struktur app/**
- .github/workflows/
- dao/
- docs/
- documents/
- forms/
- instance/
- routes/
- services/
- templates/

**app/.github/workflows/**
- jekyll-gh-pages.yml

**app/dao/**
- match_dao.py
- personality_dao.py
- swipe_dao.py
- university_dao.py
- user_dao.py

**app/docs/**
- assets/images/
    - Datenmodell.jpg
- technical-docs
    - architecture.md
    - data-model.md
    - reference.md
- Arbeitsteilung.md
- Quellennutzung.md
- _config.yml
- index.md
- value-proposition.md

**app/documents/**
- WebApp_Idea_JAK.docx

**app/forms/**
- form_login.py
- form_matching.py
- form_register.py
- form_start.py
- form_welcome.py

**app/instance/**
- campusconnect_berlin.sqlite

**app/routes/**
- __init__.py
- profile_picture.py
- route_friend_suggestions.py
- route_login.py
- route_matching.py
- route_my_matches.py
- route_quiz.py
- route_quizresult.py
- route_register.py
- route_start.py
- route_welcome.py

**app/services/**
- match_service.py
- swipe_service.py
- user_service.py

**app/templates/**
- 404.html
- 500.html
- base.html
- friend_suggestions.html
- login.html
- matching.html
- my_matches.html
- quiz.html
- quiz_results.html
- register.html
- start.html
- welcome.html


- .gitignore
- LICENSE
- README.md
- app.py
- db.py
- insert_profiles.py
- insert_uni.py
- models.py
- requirements.txt


# Technologies und Dependencies

Unsere Webanwendung basiert auf einem Python-Backend mit Flask und verwendet Pakete für den Datenbankzugriff und Styling.


## Kern Technologien

### Flask
- Beschreibung: Das zentrale Framework für unsere Webanwendung. Es verwaltet das Routing, HTTP-Requests und die Templates.
- Version: `Flask==2.2.3` (siehe `requirements.txt`)


### Flask-SQLAlchemy
- Beschreibung: Object-Relational Mapper (ORM), um einfach mit der relationalen Datenbank zu arbeiten, ohne direkt SQL schreiben zu müssen.
- Version: `Flask-SQLAlchemy==3.0.5`

### bcrypt
- Beschreibung: Für sicheres Hashing von Passwörtern. Damit speichern wir keine Klartext-Passwörter in der Datenbank.
- Version: `bcrypt==4.0.1`

### Flask-Bootstrap
- Beschreibung: Integriert Bootstrap-Styles in die Flask-App, um ein responsives Frontend zu erstellen.
- Version: `Flask-Bootstrap==3.3.7.1`


## Dependencies
Die wichtigsten Abhängigkeiten:
- Flask: v2.2.3
- Flask-SQLAlchemy: v3.0.5
- bcrypt: v4.0.1
- Flask-Bootstrap: v3.3.7.1

Die exakten Versionen aller Pakete findet man in [`requirements.txt`](./requirements.txt).

## Local Development
So startet man das Projekt lokal:
1. Zuerst eine Virtuelle Umgebung erstellen 
   ```bash
   python -m venv venv
   source venv/bin/activate oder
   venv\Scripts\activate    
