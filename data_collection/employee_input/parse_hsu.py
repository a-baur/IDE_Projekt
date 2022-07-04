import json

# from https://www.hsu-hh.de/ti/team
people = """Bernd Klauer
Hans-Christoph Zeidler
Corina Flegel
Marcel Eckert
Dominik Meyer
Alexander Klemd
Christina Sander
Uwe Daube
Dennis Fliemann
Detlef Thomsen
"""

# go through names and sort out duplicates
names = []
for name in people.splitlines():
    if name not in names:
        names.append(name)

open_alex_id = 'https://openalex.org/I190134885'
institution_name = 'Helmut Schmidt University'

output = {
    'institution_name': institution_name,
    'open_alex_id': open_alex_id,
    'names': names}

with open('hsu.json', 'w', encoding='utf-8') as file:
    json.dump(output, file, ensure_ascii=False, indent=4)