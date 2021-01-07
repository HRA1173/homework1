# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:28:36 2020

@author: User
"""

"""
Aufgabe3.1:

Schreiben Sie eine Funktion add_frac, die zwei Brüche addieren kann.
Dabei werden jeweils Zähler und Nenner als Input an die Funktion übergeben add_frac(Zaehler1,Nenner1,Zaehler2,Nenner2) und als Liste verwaltet.
Die Eingabe soll nicht über einen Konsolen/User-Input erfolgen. Als Input sind nur ganze Zahlen zulässig.
Die Ausgabe ist ein neuer Bruch - es werden also wiederum Zähler und Nenner ausgegeben.
Zusatzaufgabe: Kürzen Sie das Resultat. Dies gelingt am einfachsten, wenn Sie Zähler und Nenner des Resultats durch ihren größten gemeinsamen Teiler (ggT) dividieren.
"""

def add_frac(Zaehler1,Nenner1,Zaehler2,Nenner2):
    """
    Diese Funktion addiert zwei Brüche miteinander.
    Es dürfen nur Ganzzahlen eingegeben werden.
    Die Nenner dürfen nicht null sein.
    """
    
    #Überprüfung der Eingabe auf Ganzzahl     
    if type(Zaehler1) != int or type(Nenner1) != int or type(Zaehler2) != int or type(Nenner2) != int:
        print("Bitte geben Sie nur Ganzzahlen ein!")
    #Überprüfung der Nenner auf Nulldivision
    elif Nenner1 == 0 or Nenner2 == 0:
        print("Fehler bei der Eingabe. Nenner darf nicht Null sein!")
    #Bruchaddition
    else:
        Nenner3 = Nenner1*Nenner2
        Zaehler3 = Zaehler1*Nenner2+Zaehler2*Nenner1
        return Zaehler3 / Nenner3

