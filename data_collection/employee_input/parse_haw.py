import json

# from https://www.haw-hamburg.de/hochschule/technik-und-informatik/departments/informatik/unser-department/beschaeftigte/
name_table = """Christian Ahlf
Department Informatik
T +49 40 428 75-8103
christian.ahlf@haw-hamburg.de

Jakob Andersen
Wissenschaftlicher Mitarbeiter
Department Informatik
Berliner Tor 7
20099 Hamburg
jakob.andersen@haw-hamburg.de

Behnisch Awis
Department Informatik
behnisch.awis@haw-hamburg.de
Prof. Dr.

Reinhard Baran
Department Informatik
Berliner Tor 7, Raum 7.83b
20099 Hamburg
T +49 40 428 75-8015
reinhard.baran@haw-hamburg.de
Prof. Dr.

Martin Becke
Department Informatik
martin.becke@haw-hamburg.de

Ilona Blanck
Department Informatik
ilona.blanck@haw-hamburg.de

Holger Brackelmann
Department Informatik
holger.brackelmann@haw-hamburg.de

Michael Brodersen
Department Informatik
Berliner Tor 7, Raum 11.86
20099 Hamburg
T +49 40 428 75-8395
michael.brodersen@haw-hamburg.de

Jessica Broscheit
Department Informatik
jessica.broscheit@haw-hamburg.de

Arne Busch
Department Informatik
arne.busch@haw-hamburg.de
Prof. Dr.

Bettina Buth
Department Informatik
Berliner Tor 7, Raum 11.80a
20099 Hamburg
T +49 40 428 75-8150
bettina.buth@haw-hamburg.de
Prof. Dr.

Thomas Clemen
Department Informatik
Berliner Tor 7, Raum 11.83
20099 Hamburg
T +49 40 428 75-8411
thomas.clemen@haw-hamburg.de
Prof. Dr.

Zhen Dai
Professorin für System und Software Engineering
Department Informatik
Berliner Tor 7, Raum 7.86b
20099 Hamburg
T +49 40 428 75-8541
zhenru.dai@haw-hamburg.de

Tobias De Gasperis
Department Informatik
Berliner Tor 7, Raum 7.02
20099 Hamburg
T +49 40 428 75-8145
tobias.degasperis@haw-hamburg.de

Uwe Doleschel
Department Informatik
uwe.doleschel@haw-hamburg.de
Dr.

Susanne Draheim
Department Informatik
susanne.draheim@haw-hamburg.de
Prof. Dr.

Friedrich Esser
Department Informatik
friedrich.esser@haw-hamburg.de
Prof. Dr.

Wolfgang Fohl
Department Informatik
wolfgang.fohl@haw-hamburg.de

Timo Häckel
Department Informatik
Prof. Dr.-Ing.

Lars Hamann
Department Informatik
lars.hamann@haw-hamburg.de
Dr.

Frank Heitmann
Department Informatik
frank.heitmann@haw-hamburg.de

Torge Hinrichs
Department Informatik
Berliner Tor 7, Raum 11.80a
20099 Hamburg
T +49 40 428 75-8151
torge.hinrichs@haw-hamburg.de
Prof. Dr.

Martin Hübner
Department Informatik
Berliner Tor 7, Raum 11.80b
20099 Hamburg
T +49 40 428 75-8402
martin.huebner@haw-hamburg.de
Prof. Dr.

Philipp Jenke
Professor für Softwareentwicklung
Department Informatik
Berliner Tor 7, Raum 11.92
20099 Hamburg
T +49 40 428 75-8431
philipp.jenke@haw-hamburg.de

André Jeworutzki
Department Informatik
Prof. Dr.

Bernd Kahlbrandt
emeritiert
Department Informatik
bernd.kahlbrandt@haw-hamburg.de
Prof. Dr.

Christoph Klauck
Department Informatik
T +49 40 428 75-8412
christoph.klauck@haw-hamburg.de

Holger Klindtworth
Department Informatik
holger.klindtworth@haw-hamburg.de

Sven Koch
Department Informatik
sven.koch@haw-hamburg.de
Prof. Dr.-Ing.

Bert-Uwe Köhler
Department Informatik
bert-uwe.koehler@haw-hamburg.de
Prof. Dr.

Michael Köhler-Bußmeier
Theoretische Informatik
Department Informatik
michael.koehler-bussmeier@haw-hamburg.de
Prof. Dr.

Franz Korf
Department Informatik
Berliner Tor 7, Raum 11.92
20099 Hamburg
T +49 40 428 75-8420
franz.korf@haw-hamburg.de
Prof. Dr.

Klaus-Peter Kossakowski
Professor für IT-Sicherheit
Department Informatik
Berliner Tor 7, Raum 10.81a
20099 Hamburg
T +49 40 428 75-8157
klaus-peter.kossakowski@haw-hamburg.de
Prof. Dr.

Thomas Lehmann
Department Informatik
Berliner Tor 7, Raum 7.80
20099 Hamburg
T +49 40 428 75-8335
thomas.lehmann@haw-hamburg.de
Dr. rer. nat.

Ulfia Lenfers
Department Informatik
Dr.

Ji-Young Lim
Department Informatik
ji-young.lim@haw-hamburg.de
Prof. Dr.

Christian Lins
Department Informatik
christian.lins@haw-hamburg.de

Tim Luecke
Department Informatik
tim.luecke@haw-hamburg.de

Philip McClenaghan
Department Informatik
philip.mcclenaghan@haw-hamburg.de
Prof. Dr.

Andreas Meisel
Department Informatik
andreas.meisel@haw-hamburg.de

Eike Meyer
Department Informatik
eike.meyer@haw-hamburg.de
Prof. Dr.

Michael Neitzke
Department Informatik
michael.neitzke@haw-hamburg.de

Malte Nogalski
Department Informatik
Malte.Nogalski@haw-hamburg.de

Hans Nordeck
Department Informatik
hans.nordeck@haw-hamburg.de

Florian Ocker
Department Informatik
florian.ocker@haw-hamburg.de
Prof. Dr.

Julia Padberg
Department Informatik
Berliner Tor 7
20099 Hamburg
T +49 40 428 75-8412
julia.padberg@haw-hamburg.de
Prof. Dr.

Stephan Pareigis
Professor für Angewandte Mathematik und Technische Informatik
Department Informatik
Berliner Tor 7, Raum 12.07
20099 Hamburg
T +49 40 428 75-8400
stephan.pareigis@haw-hamburg.de

Peter Radzuweit
AI-Labor
Department Informatik
Berliner Tor 7, Raum 11.03
20099 Hamburg
T +49 40 428 75-8433
peter.radzuweit@haw-hamburg.de

Daniel Riege
Department Informatik
daniel.riege@haw-hamburg.de
Prof. Dr.

Stefan Sarstedt
Professor für Software-Engineering und Softwarearchitektur
Department Informatik
Berliner Tor 7, Raum 10.85
20099 Hamburg
T +49 40 428 75-8434
stefan.sarstedt@haw-hamburg.de
Prof. Dr.

Michael Schäfers
Department Informatik
Berliner Tor 7, Raum 7.80
20099 Hamburg
T +49 40 428 75-8155
michael.schaefers@haw-hamburg.de

Knut Schmahl
Department Informatik
knut.schmahl@haw-hamburg.de
Prof. Dr.

Thomas Schmidt
Rechnernetze & Internettechnologien / Informatik
Department Informatik
T +49 40 428 75-8452
Prof. Dr.

Axel Schmolitzky
Department Informatik
Berliner Tor 7, Raum 11.87
20099 Hamburg
T +49 40 428 75-8124
axel.schmolitzky@haw-hamburg.de
Prof. Dr.

Martin Schultz
Wirtschaftsinformatik
Department Informatik
Berliner Tor 7
20099 Hamburg
T +49 40 428 75-8538
martin.schultz@haw-hamburg.de
Prof. Dr.

Bernd Schwarz
Department Informatik
bernd.schwarz@haw-hamburg.de

Stefan Stanjek
Department Informatik
stefan.stanjek@haw-hamburg.de
Prof. Dr.

Ulrike Steffens
Department Informatik
Berliner Tor 7, Raum 10.83
20099 Hamburg
T +49 40 428 75-8184
ulrike.steffens@haw-hamburg.de
Prof. Dr.

Peer Stelldinger
Professor für Theoretische Informatik, Bildverarbeitung und Maschinelles Lernen
Department Informatik
Berliner Tor 7, Raum 10.81
20099 Hamburg
peer.stelldinger@haw-hamburg.de
Prof. Dr.

Jan Sudeikat
Department Informatik
jan.sudeikat@haw-hamburg.de
Prof. Dr.

Tim Tiedemann
Professor für Intelligente Sensorik
Department Informatik
Berliner Tor 7, Raum 7.80
20099 Hamburg
T +49 40 428 75-8155
tim.tiedemann@haw-hamburg.de
Prof. Dr.

Marina Tropmann-Frick
Professorin für Data Science
Department Informatik
Berliner Tor 7, Raum 10.88
20099 Hamburg
marina.tropmann-frick@haw-hamburg.de
Prof. Dr.

Kai von Luck
Department Informatik
kai.vonluck@haw-hamburg.de
Prof. Dr.

Jens von Pilgrim
Department Informatik
jenshenning.vonpilgrim@haw-hamburg.de

Beate Waltrup
Department Informatik
beate.waltrup@haw-hamburg.de
Prof. Dr.

Birgit Wendholt
Department Informatik
Berliner Tor 7, Raum 10.84
20099 Hamburg
T +49 40 428 75-8060
birgit.wendholt@haw-hamburg.de

Fredrik Winkler
Department Informatik
fredrik.winkler@haw-hamburg.de
Prof. Dr.

Olaf Zukunft
Department Informatik
Berliner Tor 7, Raum 11.83
20099 Hamburg
T +49 40 428 75-8432
olaf.zukunft@haw-hamburg.de
"""
open_alex_id = 'https://openalex.org/I70451448'
institution_name = 'Hamburg University of Applied Sciences'

# parse names out of table string
names = []
for paragraph in name_table.split('\n\n'):
    paragraph_line_split = paragraph.split('\n')
    name = paragraph_line_split[0]
    names.append(name)

output = {
    'institution_name': institution_name,
    'open_alex_id': open_alex_id,
    'names': names}

with open('haw.json', 'w', encoding='utf-8') as file:
    json.dump(output, file, ensure_ascii=False, indent=4)



