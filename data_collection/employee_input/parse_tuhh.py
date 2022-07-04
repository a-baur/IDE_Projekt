import json

people = ""

# got people from all institutes on the "Dekanat EIM" from
# https://www.tuhh.de/tuhh/dekanate/elektrotechnik-informatik-und-mathematik/forschung-und-institute.html

# all teaching people for "Informatik" from
# https://www.tuhh.de/tuhh/dekanate/elektrotechnik-informatik-und-mathematik/forschung-und-institute.html
people += """Matthias Mnich
Karl-Heinz Zimmermann
Antoine Mottet
Alexander Schläfer
Tobias Knopp
Sibylle Schupp
Volker Turau
Stefan Schulte
Nihat Ay
Riccardo Scandariato
Andreas Timm Giel
Görschwin Fey
Heiko Falk
Sibylle Fröschle
Christian Renner
Ulf Kulau
Christian Dietrich
Sohan Lal
"""

# from: https://mtec.et8.tuhh.de/staff.html
people += """Sven-Thomas Antoni
Lennart Holstein 
Finn Behrendt
Debayan Bhattacharya
Marcel Bengs
Aljoscha Diercks
Martin Fischer
Michael Freude
Stefan Gerlach
Sarah Grube
Sarah Latus
Robin Mieling
Maximilian Neidhardt
Omer Rajput
Katrin Rausch
Alexander Schlaefer
Johanna Sprenger
Carolin Stapper
"""

# from: https://www.tuhh.de/et6/team/profiles.html
people += """Andreas Timm-Giel
Koojana Kuladinithi
Janick Lokocz
Musab Ahmed Eltayeb Ahmed
Leonard Fisser
Konrad Fuger
Sebastian Lindner
Aliyu Makama
Daniel Plöger
Yevhenii Shudrenko
Daniel Stolpmann
Frank Laue
Thomas Müller
"""

# from: https://www.tuhh.de/ibi/people.html
people += """Tobias Knopp
Annemarie Tauche
Florian Sevecke
Tobias Knopp
Martin Hofmann
Florian Griese
Marija Boberg
Johannes Dora
Fynn Förger
Mirco Grosser
Niklas Hackelberg
Fabian Mohn
Lina Nawwas
Konrad Scheffler
Patryk Szwargulski
Florian Thieben
Christina Brandt
Matthias Gräser
"""

# from https://www.tuhh.de/algo/people.html
people += """Matthias Mnich
Laura Codazzi
David Fischer
Julian Golak
Matthias Kaul
Christian Ortlieb
Tobias Stamm
"""

# from https://www.tuhh.de/es/home/people.html
people += """Heiko Falk
Görschwin Fey
Mayer-Lindenberg
Karl-Heinz Zimmermann
Elke Nissen
Wolfgang Brandt
Stefan Just
Ahmad Al-Zoubi
Fin Bahnsen
Bernhard Berger
Wolfgang Brandt
Merve Cakir
Thilo Fischer
Shashank Jadhav
Paula Klimach
Gianluca Martino
Kateryna Muts
Nina Piontek
Swantje Plambeck
Afshin Poorkhanali
Eugen Romanenkov
Mehwish Saleemi
Lutz Schammer
Ana Karen Velazquez Sanchez
"""

# from https://www.tuhh.de/sts/institute/people.html
people += """Sibylle Schupp
Ulrike Hantschmann
Kai Bavendiek
Lars Beckers
Mathias Blumreiter
Hartmut Gau
Dmitry Ivanov
Timo Kamph
Anna Lainé
Sascha Lehmann
Ole Lübke
Rainer Marrone
Thomas Rahmlow
Antje Rogalla
Thomas Sidow
"""

# from https://www.ti5.tuhh.de/staff/
people += """Volker Turau
Marcus Venzke
Kristina Ahlborn
Manikku Badu
Ivonne Andrea Mantilla González
Florian Meyer
Peter Oppermann
Shashini Thamarasie Wanniarachchi
Amine Youssfi
"""

# from https://www.tuhh.de/ide/homepage/people.html
people += """Stefan Schulte
Ulrike Schneider
Dominik Schallmoser
Michael Peter Sober
Avik Banerjee
"""

# from https://www.dsf.tuhh.de/index.php/team/
people += """Nihat Ay
Sandra Krüger
Manfred Eppe
Michael Perezowsky
Carlotta Langer
Jesse van Oostrum
Frank Röder
Csongor-Huba Várady
"""

# from https://www.tuhh.de/softsec/institute.html
people += """Riccardo Scandariato
Ina Weigl
Abdullah Saei
Nicolas Diaz Ferreyra
Catherine Tony
Quang Cuong Bui
Simon Malte Schneider
Torge Hinrichs
"""

# from https://www3.tuhh.de/e-exk3/People/
people += """Ulf Kulau
"""

# from https://www3.tuhh.de/osg/People/
people += """Christian Dietrich
Yannick Loeck
"""

# go through names and sort out duplicates
names = []
for name in people.splitlines():
    if name not in names:
        names.append(name)

open_alex_id = 'https://openalex.org/I884043246'
institution_name = 'Hamburg University of Technology'

output = {
    'institution_name': institution_name,
    'open_alex_id': open_alex_id,
    'names': names}

with open('tuhh.json', 'w', encoding='utf-8') as file:
    json.dump(output, file, ensure_ascii=False, indent=4)
