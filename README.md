
# python_proj

Entwickel ein Python-Programm, dass auf Window-Server-2022 läuft und folgendes tut:

Version-1 Windows-Version, RAM, Anzahl der Prozessorkerne auslesen und in einer CSV-Datei ausgeben.

Version-2 wie Version 1, liest aber den auch HD-Speicher aller Festplatten und Netzlaufwerke aus (Maximale Speicherkapazität, aktuelle Speicherbelegung)

Version-3 wie Version-2, liest aber auch Infos aus der Windows-Registry (z. B. Office-Version) aus

Version-4 wie Version-3, läuft aber kontinuierlich im Hintergrund und liest die Daten 1 Mal pro Minute aus und fügt sie in der CSV-Datei als neuen Datensatz unten an. In der CSV wir außerdem Datum und Uhrzeit des Auslesezeitpunkts dokumentiert

Version-5 wie Version-4, ist aber konfigurierbar: Die Häufigkeit der regelmäßigen Datenerhebung kann eingestellt werden (von min. 1x pro Milli-Sekunde bis zu max. 1x pro Jahr) und die Art der erhobenen Daten kann einstellt werden (Also für Windows-Version, RAM, Prozessorkerne, HD-Speicher, Registry-Info, TIMEDATE ... jeweils "JA/NEIN" einstellen)

Version-6 wie Version-5, die Ausgabe kann aber auch in XML erfolgen
