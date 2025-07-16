---
title: Datenmodell
parent: Technical Docs
nav_order: 3
---

[Kaan Baskaya]  
{: .label }

{: .no_toc }

# Datenmodell

Unsere Webapp zielt darauf ab, Freundschaften zwischen Studierenden durch persönlichkeitsbasiertes Matching zu fördern.  
Key Features sind: Registrierung, Login, Speicherung von Personality Results, Swipen anderer User, Matches bei gegenseitigem Interesse und direkte Nachrichten zwischen Matches.

Die Datenbankstruktur umfasst folgende Tabellen: `user`, `university`, `personality_result`, `swipe`, `match` und `message`.

Im Folgenden sind die zugehörigen Attribute, Typen und Einschränkungen aufgelistet.

---

## Tabelle: User

<details open markdown="block">
<summary>- User/</summary>
<pre>
"user_id"         INTEGER PRIMARY KEY,
"uni_id"          INTEGER,
"name"            TEXT NOT NULL,
"email"           TEXT UNIQUE NOT NULL,
"password"        TEXT NOT NULL,
"birth_date"      DATE NOT NULL,
"created_at"      DATE DEFAULT CURRENT_DATE,
"profile_picture" BLOB NOT NULL,
"description"     TEXT NOT NULL DEFAULT '',
FOREIGN KEY ("uni_id") REFERENCES university("uni_id")
</pre>
</details>

---

## Tabelle: University

<details open markdown="block">
<summary>- University/</summary>
<pre>
"uni_id"      INTEGER PRIMARY KEY,
"name"        TEXT NOT NULL,
"short_name"  TEXT,
"location"    TEXT
</pre>
</details>

---

## Tabelle: Personality_Result

<details open markdown="block">
<summary>- Personality_Result/</summary>
<pre>
"result_id"     INTEGER PRIMARY KEY,
"user_id"       INTEGER UNIQUE,
"vec_ei"        FLOAT,
"vec_sn"        FLOAT,
"vec_tf"        FLOAT,
"vec_jp"        FLOAT,
"mbti_type"     TEXT,
"completed_at"  DATE,
FOREIGN KEY ("user_id") REFERENCES user("user_id")
</pre>
</details>

---

## Tabelle: Swipe

<details open markdown="block">
<summary>- Swipe/</summary>
<pre>
"swipe_id"      INTEGER PRIMARY KEY,
"swiper_id"     INTEGER,
"swiped_id"     INTEGER,
"swipe_type"    TEXT,
"swiped_at"     DATE,
FOREIGN KEY ("swiper_id") REFERENCES user("user_id"),
FOREIGN KEY ("swiped_id") REFERENCES user("user_id")
</pre>
</details>

---

## Tabelle: Match

<details open markdown="block">
<summary>- Match/</summary>
<pre>
"match_id"      INTEGER PRIMARY KEY,
"user1_id"      INTEGER,
"user2_id"      INTEGER,
"compatibility" FLOAT,
"status"        TEXT,
"matched_at"    DATE,
FOREIGN KEY ("user1_id") REFERENCES user("user_id"),
FOREIGN KEY ("user2_id") REFERENCES user("user_id")
</pre>
</details>

---

## Tabelle: Message

<details open markdown="block">
<summary>- Message/</summary>
<pre>
"id"         INTEGER PRIMARY KEY,
"match_id"   INTEGER NOT NULL,
"sender_id"  INTEGER NOT NULL,
"text"       TEXT NOT NULL,
"timestamp"  DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY ("match_id") REFERENCES match("match_id"),
FOREIGN KEY ("sender_id") REFERENCES user("user_id")
</pre>
</details>

---

## Constraints und Beziehungen

Die Datenbank stellt durch `NOT NULL`, `UNIQUE` und `FOREIGN KEY` Constraints sicher, dass Datensätze vollständig, eindeutig und korrekt verknüpft sind.  
Zusätzlich existieren Beziehungen zwischen `User` ↔ `University`, `User` ↔ `PersonalityResult`, sowie untereinander in `Swipe` und `Match`.  
Das Modell basiert auf SQLAlchemy und unterstützt die funktionalen Anforderungen der App vollständig.