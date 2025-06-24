from datetime import date

# Jan
def calculate_age(birth_date):
    today = date.today()

    # liefert das aktuelle Alter
    # erstmal die DIfferenz von aktuellem Jahr und Geburtsjahr, anschließend wird geschaut ob der User dieses Jahr "schon Geburtstag hatte"
    # ist das aktuelle Datum vor dem Geburtstag, so wird 1 abgezogen (weil True, das ergebnis des Vergleichs, als 1 interpretiert wird)
    # wenn der Geburtstag shcon war bleibt das Ergebnis gleich (weil der Vergleich False leifert, was in Python als 0 interpretiert wird)
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))