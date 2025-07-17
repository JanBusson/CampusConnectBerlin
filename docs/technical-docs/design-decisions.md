---
title: Design Decisions
parent: Technical Docs
nav_order: 5
---

{: .no_toc }
# Design Decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ TOC
{: toc }
</details>

## 1. Persönlichkeitsbasiertes Matching mit Vektor Distanz
by [Kaan]
### Problemstellung

Ziel unserer App ist es, Freundschaften zwischen Studierenden zu fördern. Ein einfaches Matching basierend auf gemeinsamen Interessen oder MBTI Typ Paarungen (INFP passt zu ENFJ) ist zu allgemein, da zwei Personen mit demselben Typ stark unterschiedliche Ausprägungen haben können.

### Entscheidung

Wir haben stattdessen ein vektorbasiertes Matching Modell entwickelt. Auf Basis des MBTI Tests (ursprünglich je 3 Fragen pro Achse) berechnen wir für jeden User vier Werte zwischen –3 und +3 für:

- Extraversion-Introversion (EI)  
- Sensing-Intuition (SN)  
- Thinking-Feeling (TF)  
- Judging-Perceiving (JP)  

Diese vierdimensionale Struktur erlaubt es, Persönlichkeitsprofile mathematisch als Vektoren zu sehen. Die Ähnlichkeit zweier User ergibt sich aus der euklidischen Distanz ihrer Vektoren:

Kompatibilität = 1 - (d / max_d)

Die maximale Distanz (`max_distance`) beträgt 12, da jede Achse eine maximale Abweichung von 6 haben kann. Das Ergebnis ist ein Score zwischen 0 (sehr unähnlich) und 1 (perfect Match).

### Vorteile

- Graduelle Differenzierung statt allgemeiner Typen
- Vergleichbarkeit aller Nutzer auch mit ähnlichen, aber nicht identischen Profilen
- Kompatibilität kann als Score, Ranking oder Threshold verwendet werden
- Grundlage für Analysen (Machine Learning)

---

## 2. Trennung von Datenzugriff, Logik und Struktur: DAO, Service Layer & SQLAlchemy
by [Kaan]
### Problemstellung

Bei wachsender Codebasis mit mehreren Datenbankzugriffen, Matchings, Nachrichtenlogik und User Interactions wäre es unübersichtlich, alles in den Flask Routen zu behandeln.

### Entscheidung

Wir haben uns für ein strukturiertes Architekturmodell mit folgenden Komponenten entschieden:

- SQLAlchemy als ORM zur Modellierung der Datenbanktabellen
- DAO Klassen (z. B. `match_dao`, `user_dao`) zur Trennung von Datenbankzugriff und Logik
- Service Layer (z. B. `MatchService`) zur Berechnung der Kompatibilität und möglicher Zusatzlogik

### Vorteile

- Jede Klasse hat eine klar definierte Verantwortung  
- Code ist besser lesbar, testbar und erweiterbar  
- DAO Methoden wie `get_all_for_uid()` oder `save_message()` können überall verwendet werden  
- Neue Services (z. B. `ChatService`) können einfach ergänzt werden

---

## 3. Persönlichkeitsbasiertes Matching mit 16 Personalities
by [Ailin]
### Problemstellung

Aktuelle Applikationen für Freundschaften und das Kennenlernen von neuen Menschen basiert hauptsächlich auf Interessen. Da, viele User nicht die Erfahrungen sammeln, die sie sich eigentlich gewünscht haben, haben wir einen anderen Ansatz zum matching implementiert. Die User sollen anhand ihrer Persönlichkeitstypen gematched werden, weil dadurch die Einschätzung welcher Art von Person es sich handelt, präziser wird.  

### Entscheidung
Die Ermittlung des Persönlichkeitstypen basiert anhand des 16Personalities Tests, beziehungsweise Myers-Briggs-Type-Indicator Tests. Da, die Webseite https://www.16personalities.com/free-personality-test bereits ein solches Quiz kostenlos anbietet, haben wir uns daran gerichtet. Genauso wie auf der Webseite gibt es für jede Frage eine Skala zum Antworten von -3 bis 3. Dies haben wir übernommen, da der Gedanke, dass der User sehr weit sich für eine Richtung entscheiden kann (-3 bzw 3 auf der Skala) oder im Gegenteil neutral (0 auf der Skala) antworten kann. 

Wie bereits erklärt gibt es 4 Dimensionen, die den Persönlichkeitstypen definieren. Um zu berechnen welcher Parameter in einer Dimension dominiert wurde wie gefolgt berechnet:
Beispiel für die Dimension E/I:
5 Fragen für jeweils eine Dimension
1. Antwort: 1
2. Antwort: 2
3. Antwort: 3
4. Antwort:-2
5. Antwort: 0

Summe = 4 -> Da, die Summe postiv ist, ist das Ergebnis **E**xtraversion

### Vorteile

- Persönlichkeitstest um Menschen besser einzuschätzen
- Anderer Ansatz als herkömmliche Anwendungen - potenziell mehr Erfolg beim Matchen


