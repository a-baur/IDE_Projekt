import json

# from https://www2.informatik.uni-hamburg.de/fiona/pers.php?order=name&ltype=liste&lang=de&group=
name_table = """
A
Fares Abawi 	WTM 	F-214 	+49 40 42883-2378 	>>> 	>>>
Ashad Achgarnush 	WISTS 	C-216 	+49 40 42883-2015 	>>> 	
Daniel Ahlers 	TAMS 	F-324 	+49 40 42883-2356 	>>> 	>>>
Kyra Ahrens 	WTM 	F-212 	+49 40 42883-2520 	>>> 	>>>
Dr. Philipp Allgeuer 	WTM 	F-209 	+49 40 42883-2517 	>>> 	
Jakob Andersen 	MAST 	D-215 	+49 40 42883-2305 	>>> 	>>>
Johanna Ansohn Mcdougall 	SVS 	F-629 	+49 40 42883-2287 	>>> 	>>>
Saba Anwar 	LT 	F-415 	+49 40 42883-2418 	>>> 	>>>
Dr. Oscar Javier Ariza Nunez 	HCI 	F-106 	+49 40 42883-2542 	>>> 	>>>
Anne Awizen 	DBIS, DOS, WISTS 	F-532a 	+49 40 42883-2420 	>>> 	>>>
Abinew Ali Ayele 	LT 	F-403 	+49 40 42883-2320 	>>> 	>>>

B
Fynn Bachmann 	ITMC 	C-115 	+49 40 42883-2229 	>>> 	
Christian Bähnisch 	HITeC 	R-015 	+49 40 42883-2610 	>>> 	
Debayan Banerjee 	LT 	F-409 	+49 40 42883-2363 	>>> 	>>>
Dr. Timo Baumann 	LT 	F-404 	+49 40 42883-2321 	>>> 	>>>
Prof. Dr. Jan Baumbach 	CSB 	N-9 	+49 40 42883-7313 	>>> 	>>>
Dennis Becker 	WTM 	F-213 	+49 40 42883-2521 	>>> 	>>>
Andreas Beckert 	WVP 	RRZ-305 	+49 40 42838-4690 	>>> 	
Andreas Beckert 	WVP 	RRZ-305 	+49 40 42838-4690 	>>> 	>>>
Louis Bellmann 	AMD 	ZBH-201 	+49 40 42838 7356 	>>> 	>>>
Prof. Dr. Petra Berenbrink 	ART 	G-221 	+49 40 42883-2174 	>>> 	>>>
Ole Berg 	AMD 	ZBH-201 	+49 40 42838-7358 	>>> 	>>>
Marc Bestmann 	TAMS 	F-313 	+49 40 42883-2398 	>>> 	>>>
Eugen Betke 	WR 	DRKZ-408 	+49 40 460094-422 	>>> 	>>>
Prof. Dr. Chris Biemann 	LT 	F-429 	+49 40 42883-2386 	>>> 	>>>
Felix Biermeier 	ART 	G-222 	+49 40 42883-2183 	>>> 	>>>
Volodymyr Biryuk 	MAST 	D-215 	+49 40 42883-2314 	>>> 	>>>
Laura Bisby 	CSB 	N-9 	+49 40 42883-7635 	>>> 	>>>
Prof. Dr. Eva Bittner 	WISTS 	C-209 	+49 40 42883-2409 	>>> 	>>>
Prof. Dr. Tilo Böhmann 	ITMC 	C-110 	+49 40 42883-2299 	>>> 	>>>
Wolf-Guido Bolick 	AMD 	ZBH-206 	+49 40 42838-7571 	>>> 	>>>
Leif Bonorden 	SWK 	D-228 	+49 40 42883-2036 	>>> 	>>>
Marten Borchers 	WISTS 	C-216 	+49 40 42883-2015 	>>> 	
Michael Borchers 	HCI 	F-120a 	+49 40 42883-2559 	>>> 	>>>
Heiko Tobias Bornholdt 	NET 	F-622 	+49 40 42883-2332 	>>> 	>>>
Abir Bouraffa 	MAST 	D-206 	+49 40 42883-N.N. 	>>> 	
Julia Bräker 	ITMC 	C-117 	+49 40 42883-2514 	>>> 	>>>
Dr. Kai Brüssau 	IWI 	VMP5 1038 	+49 40 42838-6290 	>>> 	
Thomas Bünnemann 	RZ 	D-109 	+49 40 42883-2278 	>>> 	>>>
Christian Burkert 	SVS 	F-607 	+49 40 42883-2406 	>>> 	>>>
Fabian Burmeister 	ITMC 	C-218 	+49 40 42883-2593 	>>> 	>>>

C
Dr. Hugo Cesar Carneiro 	WTM 	F-228b 	+49 40 42883-2531 	>>> 	>>>
Anna Cavasin 	AMD 	ZBH-304 	+49 40 42838-7324 	>>> 	>>>
Wenkai Chen 	TAMS 	F-425 	+49 40 42883-2716 	>>> 	
Prof. Dr. Zhaopeng Chen 	TAMS 	F-425 	+49 40 42883-2716 		>>>
Yan Chen-Zhang 	MAST 	N.N. 	+49 40 42883-N.N. 	>>> 	>>>
Lin Cong 	TAMS 	F-327 	+49 40 42883-2043 	>>> 	>>>
Izabel Cvetkovic 	WISTS 	C-219 	+49 40 42883-2543 	>>> 	>>>

D
Henrique da Costa Siqueira 	WTM 	F-228a 	+49 40 42883-2530 	>>> 	>>>
Christoph Damerius 	TEA 	G-226 	+49 40 42883-2238 	>>> 	>>>
Alexandra Dannenberg 	ITMC 	C-112 	+49 40 42883-2225 	>>> 	>>>
Danilo de Oliveira 	SP 	F-125 	+49 40 42883-2549 	>>> 	>>>
Dr.-Ing. Daniel Demmler 	SVS 	F-609 	+49 40 42883-2568 	>>> 	>>>
Konrad Diedrich 	AMD 	ZBH-302 	+49 40 4238-7380 	>>> 	>>>
Marina Ɖimber 	FB-Management 	A-202 	+49 40 42883-2204 	>>> 	
Kerstin Diop-Nickel 	CV 	R-107 	+49 40 42883-2582 	>>> 	>>>
Uschi Dolfus 	AMD 	ZBH-202 	+49 40 42838-7360 	>>> 	>>>
Prof. Dr. Leonie Dreschler-Fischer 	SAV 	R-111 	+49 40 42883-2452 	>>> 	>>>

E
Prof. Dr. Janick Edinger 	DOS 	F-532c 	+49 40 42883-2426 	>>> 	>>>
Emanuel Ehmki 	AMD 	ZBH-308 	+49 40 42838-7572 	>>> 	>>>
Dr. Christiane Ehrt 	AMD 	ZBH-209 	+49 40 42883-7359 	>>> 	
Dr. Christiane Ehrt 	AMD 	ZBH-209 	+49 40 42838-7359 	>>> 	>>>
Doğanalp Ergenç 	NET 	F-627 	+49 40 42883-2353 	>>> 	>>>

F
Rainer Faehrrolfes 	AMD 	ZBH-304 	+49 40 42838-7361 	>>> 	>>>
Huajian Fang 	SP, WTM 	F-117 	+49 40 42883-2714 	>>> 	>>>
Dr. Fariba Fazli 	MAST 	D-207 	+49 40 42883-2197 	>>> 	
Prof. Dr.-Ing. Hannes Federrath 	SVS 	F-632 	+49 40 42883-2358 	>>> 	>>>
Amit Fenn 	CSB 	N-9 	+49 40 42883-N.N. 	>>> 	>>>
Laura Fichtner 					
Niklas Fiedler 	TAMS 	F-327 	+49 40 42883-2043 	>>> 	>>>
Prof. Dr. Mathias Fischer 	NET 	F-613 	+49 40 42883-2112 	>>> 	>>>
Tim Fischer 	LT 	F-413 	+49 40 42883-N.N. 	>>> 	
Florian Flachsenberg 	AMD 	ZBH 	+49 40 42838-N.N. 	>>> 	>>>
Dr. Farnaz Fotrousi 	MAST 	D-209 	+49 40 42883-2310 	>>> 	>>>
Wiebke Frauen 	HITeC 	R-020 	+49 40 42883-2612 	>>> 	
Jann Philipp Freiwald 	HCI 	F-130 	+49 40 42883-2553 	>>> 	>>>
Prof. Dr. Simone Frintrop 	CV 	R-105 	+49 40 42883-2589 	>>> 	>>>
Dr. Di Fu 	WTM 	F-217 	+49 40 42883-2318 	>>> 	>>>
Anna Fuchs 	WR 	DKRZ 109 	+49 40 460094-417 	>>> 	>>>

G
Jenny Gabel 	HCI 	N.N. 	+49 40 42883-N.N. 	>>> 	
Connor Gäde 	WTM 	F-225 	+49 40 42883-2524 	>>> 	
Larissa Gebken 	WISTS 	C-217 	+49 40 42883-2144 	>>> 	>>>
Sebastian Gerdes 	SWK 	D-228 	+49 40 42883-2372 	>>> 	>>>
Melanie Geringhoff 	AMD 	ZBH-208 	+49 40 42838-7350 	>>> 	>>>
Prof. Dr.-Ing. Timo Gerkmann 	SP 	F-126 	+49 40 42883-2438 	>>> 	>>>
Daniel Glake 	DBIS 	F-528 	+49 40 42883-2334 	>>> 	>>>
Dr. Johannes Göbel 	Studienbüro 	a-309 	+49 40 42883-2404 	>>> 	>>>
Michael Görner 	TAMS 	F-315 	+49 40 42883-2432 	>>> 	>>>
Joel Graef 	AMD 	ZBH-204 	+49 40 42838-7354 	>>> 	>>>
Michael Größler 	AMD 	ZBH-304 	+49 40 42838-7324 	>>> 	>>>
Jasper Güldenstein 	Hamburg BitBots 	F-015 	+49 40 42883-2547 	>>> 	>>>
Torben Gutermuth 	AMD 	ZBH-202 	+49 40 42838-7361 	>>> 	>>>

H
Lena Hackl 	CSB 	N-9 	+49 40 42883-N.N. 	>>> 	>>>
Christine Häusser 	Bibliothek 	A-104 	+49 40 42883-2216 	>>> 	>>>
Dr. Muhammad Burhan Hafez 	WTM 	F-216 	+49 40 42883-2535 	>>> 	>>>
Tim Christopher Hahn 	ART 	G-226 	+49 40 42883-2186 	>>> 	>>>
Björn Hanssen 	Studienbüro 	A-309 	+49 40 42883-2219 	>>> 	>>>
Tobias Harren 	AMD 	ZBH 	+49 40 42838-73XX 	>>> 	>>>
Judith Hartfill 	HCI 	F-108 	+49 40 42883-2148 	>>> 	>>>
Michael Hartung 	CSB 	N-9 	+49 40 42883-N.N: 	>>> 	>>>
Hans Ole Hatzel 	LT 	F-417 	+49 40 42883-2366 	>>> 	>>>
Christopher Haubeck 	VSYS 	F-508 	+49 40 42883-2327 	>>> 	
Michael Haustermann 	ART 	G-230 	+49 40 42883-2236 	>>> 	>>>
Leonard Heilig 	IWI 	VMP5 3061 	+49 40 42838-5519 	>>> 	>>>
Dr. Norman Hendrich 	TAMS 	F-314 	+49 40 42883-2399 	>>> 	>>>
Julia Hertel 	HCI 	F-106 	+49 40 42883-2542 	>>> 	>>>
Rainer Herzog 	HITeC 	R-125 	+49 40 42883-2172 	>>> 	>>>
Marvin Heuer 	ITMC 	C-118 	+49 40 42883-2231 	>>> 	
Marc Heydorn 	Schulsupport 	R-005 	+49 40 42883-2602 	>>> 	
Andreas Heymann 	RZ 	D-130 	+49 40 42883-2293 	>>> 	>>>
Sophia Hönig 	AMD 	ZBH 	+49 40 42838-73XX 	>>> 	>>>
Bettina Horlach 	ITG, ITMC 	C-216 	+49 40 42883-2015 	>>> 	>>>
Hamed Hosseinpour 	ART 	G-222 	+49 40 42883-2184 	>>> 	>>>
Dr. Lothar Hotz 	Technologie Transfer, KOGS, HITeC 	R-021 	+49 40 42883-2605 	>>> 	>>>
Katrin Howind 	Bibliothek 	A-101 	+49 40 42883-2214 	>>> 	
Yihong Hu 	TAMS 	F-308 	+49 40 42883-2430 	>>> 	
Junbo Huang 	SEMS 	F-434 	+49 40 42883-2391 	>>> 	

I
Dr. Bahar Ilgen 	LT 	F-403 	+49 40 42883-2320 	>>> 	

J
Dr. Abhik Jana 	LT 	F-403 	+49 40 42883-2320 	>>> 	>>>
Karla Janssen 	FB-Büro 	A-207 	+49 40 42883-2401 	>>> 	
Dieter Jessen 	CV, SP 	F-120 	+49 40 42883-2584 	>>> 	>>>
Longquan Jiang 	SEMS 	F-434 	+49 40 42883-2391 	>>> 	
Dirk Johannßen 	LT 	F-412 	+49 40 42883-2365 	>>> 	>>>
Yannick Jonetzko 	TAMS 	F-324 	+49 40 42883-2356 	>>> 	>>>
Nidhi Joshi 	HCI 	N.N. 	+49 40 42883-N.N. 	>>> 	
German Alberto Junca Bernal 	TAMS 	F-333 	+49 40 42883-2373 	>>> 	

K
Shyukryan Karaosmanoglu 	HCI 	F-106 	+49 40 42883-2542 	>>> 	>>>
André Kelm 	CV 	R-117 	+49 40 42883-2577 	>>> 	
Dr. Matthias Kerzel 	WTM 	F-211 	+49 40 42883-2519 	>>> 	>>>
Felix Kiehn 	DBIS 	F-522 	+49 40 42883-2343 	>>> 	>>>
Philipp Kisters 	DOS 	F-510 	+49 40 42883-2339 	>>> 	>>>
Marc Klegin 	RZ 	D-109 	+49 40 42883-2278 	>>> 	>>>
Josefine Klimpel 	Bibliothek 	A-101 	+49 40 42883-2214 	>>> 	
Prof. Dr. Peter Kling 	TEA 	G-229 	+49 40 42883-2407 	>>> 	>>>
Ronald Kock 	Serviceteam 	P 	+49 40 42883-2315 	>>> 	
Prof. Dr. Michael Köhler-Bußmeier 	ART 	G-230 	+49 40 42883-2408 	>>> 	>>>
Katrin Köster 	LT, ART 	F-428, G-218 	+49 40 42883-2181 	>>> 	>>>
Kevin Köster 	SVS 	F-633 	+49 40 42883-2042 	>>> 	>>>
Katja Kösters 	WTM 	F-205 	+49 40 42883-2433 	>>> 	>>>
Ogeigha Koroyin 	Schulsupport 	R-017 	+49 40 42883-2613 	>>> 	
Mostafa Mohamed Kotb Said 	WTM 	F-207 	+49 40 42883-2497 	>>> 	
Angelie Kraft 	SEMS 	F-434 	+49 40 42883-2391 	>>> 	
Anja Kroscky 	Studienbüro 	A-305 	+49 40 42883-2211 	>>> 	>>>
Lucie Kruse 	HCI 	F-135a 	+49 40 42883-2585 	>>> 	>>>
Emir Kučević 	ITMC 	C-117 	+49 40 42883-N.N. 	>>> 	
Babett Kühne 	ITMC 	C-115 	+49 40 42883-2229 	>>> 	>>>
Gerrit Küstermann 	WISTS 	C-202 	+49 40 42883-2121 	>>> 	>>>
Bjoern Kulas 	HITeC 	R-026 	+49 40 42883-2618 	>>> 	
Anne Kunstmann 	SVS 	F-633 	+49 40 42883-2008 	>>> 	
Christian Kurtz 	ITMC 	C-116 	+49 40 42883-2230 	>>> 	>>>

L
Egor Lakomkin 	WTM 	F-225 	+49 40 42883-2318 	>>> 	>>>
Prof. Dr. Winfried Lamersdorf 	VSYS 	F-507 	+49 40 42883-2421 	>>> 	>>>
Dr. Mikko Lauri 	CV 	R-104 	+49 40 42883-2571 	>>> 	>>>
Navin Laxminarayanan Raj Prabhu 	SP 	F-124 	+49 40 42883-2538 	>>> 	>>>
Bunlong Lay 	SP 	F-125 	+49 40 42883-2545 	>>> 	>>>
Dr. Jae Hee Lee 	WTM 	F-228a 	+49 40 42883-2530 	>>> 	>>>
Anna Leffler 	Studienbüro 	A-306 	+49 40 42883-2213 	>>> 	>>>
Jean-Marie Lemercier 	SP 	F-124 	+49 40 42883-2538 	>>> 	>>>
Dr. Hermann Lenhart 	WR 	DKRZ 105 	+49 40 460094-130 	>>> 	>>>
Jörn Leukert 	Bibliothek 	A-101 	+49 40 42883-2214 	>>> 	
Tom Lewandowski 	ITMC 	C-117 	+49 40 42883-2708 	>>> 	>>>
Mengdi Li 	WTM 	F-226 	+49 40 42883-2393 	>>> 	>>>
Shuang Li 	TAMS 	F-330 	+49 40 42883-2504 	>>> 	>>>
Hongzhuo Liang 	TAMS 	F-331 	+49 40 42883-2440 	>>> 	>>>
Jens Lindemann 	SVS 	F-633 	+49 40 42883-2347 	>>> 	>>>
Melvyn Linke 	HITeC 	R-015 	+49 40 42883-2610 	>>> 	
Chit Tong Lio 	CSB 	N-9 	+49 40 42883-N.N. 	>>> 	>>>
Shang-Ching Liu 	TAMS 	F-425 	+49 40 42883-2716 	>>> 	
Prof. Dr. Chu Kiong Loo 	WTM 	F-207 	+49 40 42883-2497 	>>> 	>>>
Zakaria Louadi 	CSB 	N-9 	+49 40 42883-N.N. 	>>> 	>>>
Wenhao Lu 	WTM 	F-229 	+49 40 42883-2532 	>>> 	
Prof. Dr. Thomas Ludwig 	WR 	DKRZ 119 	+49 40 460094-200 	>>> 	>>>
Clara Marie Lüders 	MAST 	D-213 	+49 40 42883-2597 	>>> 	>>>
Antje Lünstedt 	HCI 	F-111 	+49 40 42883-2544 	>>> 	>>>
Jianzhi Lyu 	TAMS 	F-426 	+49 40 42883-2382 	>>> 	>>>

M
Prof. Dr. Walid Maalej 	MAST, FB-Leitung 	D-204 	+49 40 42883-2073 	>>> 	>>>
Dr. Andreas Mäder 	TAMS 	F-317 	+49 40 42883-2502 	>>> 	>>>
Dr. Sven Magg 	HITeC 	F-210 	+49 40 42883-2518 	>>> 	>>>
Dr. Karen Manalastas-Cantos 	CSB 	N-9 	+49 40 42883-N.N. 	>>> 	>>>
Georgiana Mania 	WR 	DKRZ-109 	+49 40 460094-145 	>>> 	>>>
Natalia Mannov 	MAST 	D-208 	+49 40 42883-2704 	>>> 	>>>
Nathalie Martin 	HCI 	F-108 	+49 40 42883-2148 	>>> 	
Matthias Marx 	SVS 	F-633 	+49 40 42883-2344 	>>> 	>>>
Celeste Mason 	HCI 	F-130 	+49 40 42883-2553 	>>> 	>>>
Julian Matschinske 	CSB 	N-9 	+49 40 42883-N.N. 	>>> 	>>>
Lucas Memmert 	WISTS 	C-219 	+49 40 42883-2543 	>>> 	
Prof. Dr.-Ing. Wolfgang Menzel 	NATS 	R-121 	+49 40 42883-2435 	>>> 	>>>
Christian Meyenburg 	AMD 	ZBH-201 	+49 40 42838-7353 	>>> 	>>>
Dr. Marcel Meyer 	WVP 	RRZ-305b 	+49 40 42838-9323 	>>> 	>>>
Benjamin Milde 	LT 	F-430 	+49 40 42883-2387 	>>> 	>>>
Kameswar Rao Modali 	WVP 	RRZ-305 	+49 40 42838-7374 	>>> 	
Kameswar Rao Modali 	WVP 	RRZ-305 	+49 40 42838-7364 	>>> 	>>>
Cedric Möller 	SEMS 	F-408 	+49 40 42883-2362 	>>> 	
Dr. Daniel Moldt 	ART 	G-213 	+49 40 42883-2247 	>>> 	>>>
Lloyd Montgomery 	MAST 	D-214 	+49 40 42883-2687 	>>> 	>>>
Annette Morawski 	FB-Management, FB-Referentin 	A-204 	+49 40 42883-2202 	>>> 	
Fariba Mostajeran Gourtani 	HCI 	F-130 	+49 40 42883-2553 	>>> 	>>>
David Mosteller 	ART, RZ 	D-131, G-230 	+49 40 42883-2093, +49 40 42883-2236 	>>> 	>>>
Tobias Müller 	SVS 	F-607 	+49 40 42883-2379 	>>> 	>>>

N
Max Neuendorf 	NET 	F-627 	+49 40 42883-2353 	>>> 	>>>
Prof. Ph.D. Bernd Neumann 	KOGS 	R-124 	+49 40 42883-2451 		>>>
Wiebke Noeske 	TAMS 	F-308 	+49 40 42883-2509 	>>> 	>>>
Volker Nötzold 	DBIS, VSYS 	F-512 	+49 40 42883-2330 	>>> 	>>>
Prof. Dr. Markus Nüttgens 	HARCIS 	MBA60 	+49 40 42838 2792 	>>> 	>>>

O
Margrit Obernesser 	Bibliothek 	A-104 	+49 40 42883-2216 	>>> 	>>>
Prof. Dr. Horst Oberquelle 	ASI 	C-121 	+49 40 42883-2429 	>>> 	>>>
Ozan Özdemir 	WTM 	F-225 	+49 40 42883-2446 	>>> 	>>>
Prof. Dr.-Ing. Stephan Olbrich 	WVP 	RRZ-308 	+49 40 42838-5766 	>>> 	>>>
Dr. Gabriel Orsini 	VSYS 	F-505 	+49 40 42883-2140 	>>> 	>>>
Thomas Otto 	ZBH 	ZBH N.N. 	+49 40 42883-N.N. 	>>> 	>>>
Mhaned Oubounyt 	CSB 	N-9 	+49 40 42883-N.N. 	>>> 	>>>

P
Prof. Dr.-Ing. Bernd Page 	MBS 	D-021 	+49 40 42883-2508 	>>> 	>>>
Dr. Fabian Panse 	DBIS 	F-513 	+49 40 42883-2089 	>>> 	>>>
Janis-Marie Paul 	ITMC 	C-116 	+49 40 42883-2232 	>>> 	>>>
Tal Peer 	SP 	F-117 	+49 40 42883-2713 	>>> 	>>>
Theresa Pekarek-Rosin 	WTM 	F-215 	+49 40 42883-2394 	>>> 	
Patrick Penner 	AMD 	ZBH-204 	+49 40 42838 7357 	>>> 	>>>
Dr.-Ing. Annika Peters 	WTM 	F-214 	+49 40 42883-2522 	>>> 	>>>
Silke Peters 	Studienbüro 	A-302 	+49 40 42883-2212 	>>> 	>>>
Tom Petersen 	SVS 	F-608 	+49 40 42883-2309 	>>> 	>>>
Fynn Petersen-Frey 	LT 	F-407 	+49 40 42883-2381 	>>> 	>>>
Yen Pham 	MAST 	D-213 	+49 40 42883-2306 	>>> 	
Jonathan Pletzer-Zelgert 	AMD 	ZBH-304 	+49 40 42838-7352 	>>> 	>>>
Dimitri Popov 	RZ 	D-134 	+49 40 42883-2294 	>>> 	>>>
Martin Poppinga 	DBIS, AMD 	F-515 	+49 40 42883-2326 	>>> 	>>>
Wolf Dietmar Posdorfer 	base.camp 	F-511 	+49 40 42883-2331 	>>> 	>>>
Mathis Poser 	WISTS 	C-204 	+49 40 42883-2151 	>>> 	>>>
Tim Puhlfürß 	MAST 	D-212 	+49 40 42883-2467 	>>> 	

Q
Leyuan Qu 	WTM 	F-227 	+49 40 42883-2441 	>>> 	>>>

R
Jun-Patrick Raabe 	ITG 	C-207 	+49 40 42883-2357 	>>> 	>>>
Paula Rachow 	SWK 	D-232 	+49 40 42883-2525 	>>> 	>>>
Prof. Dr. Matthias Rarey 	AMD 	ZBH-205 	+49 40 42838-7351 	>>> 	>>>
Dr.-Ing. Malin Rau 	ART 	G-220 	+49 40 42883-N.N. 	>>> 	
Dr. Marc Rautenhaus 	WVP 	RRZ-306 	+49 40 42838-7339 	>>> 	>>>
Bernd Rehling 	FB Informatik 	D-218 	+49 40 42883-2701 	>>> 	
Steffen Remus 	LT 	F-413 	+49 40 42883-2369 	>>> 	>>>
Anja Richter 	HITeC 	R-026 	+49 40 42883-2618 	>>> 	
Julius Richter 	SP 	F-127 	+49 40 42883-2539 	>>> 	>>>
Prof. Dr.-Ing. Matthias Riebisch 	SWK 	D-226 	+49 40 42883-2427 	>>> 	>>>
Stephanie von Riegen 	HITeC 	R-019 	+49 40 42883-2606 	>>> 	
Sebastian Reiner Rings 	HCI 	F-135a 	+49 40 42883-2285 	>>> 	>>>
Prof. Dr. Norbert Ritter 	DBIS 	F-516 	+49 40 42883-2419 	>>> 	>>>
Kevin Röbert 	NET 	F-6222 	+49 40 42883-2329 	>>> 	
Jan Henrik Röwekamp 	ART 	G-230 	+49 40 42883-2236 	>>> 	>>>
Prof. Dr. Arno Rolf 	ASI 	C-121 	+49 40 42883-2428 	>>> 	>>>
Tim Rolff 	CV, HCI 	R-116 	+49 40 42883-2579 	>>> 	>>>
Catharina Rudschies 	FB Informatik 	G-114 	+49 40 42883-2034 	>>> 	>>>
Philipp Ruppel 	TAMS 	F-306 	+49 40 42883-2512 	>>> 	>>>

S
Noha Sarhan 	CV 	R-109 	+49 40 42883-2591 	>>> 	>>>
Dagmar Schacht 	Studienbüro 	A-304 	+49 40 42883-2201 	>>> 	>>>
Tim Scharfenberg 	FB-Management 	A-201 	+49 40 42883-2203 	>>> 	
Andreas Schiek 	Serviceteam 	P 	+49 40 42883-2315 	>>> 	
Prof. Dr. Ingrid Schirmer 	ITG 	C-207 	+49 40 42883-2472 	>>> 	>>>
Mareike Schmidt 	DBIS 	F-522 	+49 40 42883-2343 	>>> 	>>>
Robert Schmidt 	AMD 	ZBH-302 	+49 40 42838-7319 	>>> 	>>>
Dennis Schmitz 	ART 	G-230 	+49 40 42883-2236 	>>> 	
Florian Schneider 	ART, TEA 	G-226 	+49 40 42883-2186 	>>> 	>>>
Prof. Dr. Ingrid Schneider 	FB Informatik 	G-126 	+49 40 42883-2109 	>>> 	>>>
Dr. Katrin Schöning-Stierand 	AMD 	ZBH-301 	+49 40 42838-7372 	>>> 	>>>
Bernd Schütz 	TAMS 	F-322 	+49 40 42883-2503 	>>> 	>>>
Stephanie Schulte Hemming 	SWK, SP 	D-227 	+49 40 42883-2312 	>>> 	>>>
Angela Schwabl-Möhlmann 	ITG 	D-225 	+49 40 42883-2316 	>>> 	>>>
August See 	NET 	N.N. 	+49 40 42883-N.N. 	>>> 	>>>
Dr. Martin Semmann 	ITMC 	C-109 	+49 40 42883-2465 	>>> 	>>>
Nurefsan Sertbas Bülbül 	NET 	F-626 	+49 40 42883-2352 	>>> 	>>>
Özge Sevgili Ergüven 	LT 	F-430 	+49 40 42883-2387 	>>> 	>>>
Sehrish Shafeeq 	NET 	F-627 	+49 40 42883-2353 	>>> 	>>>
Jochen Sieg 	AMD 	ZBH-206 	+49 40 42838-7355 	>>> 	>>>
Prof. Dr. Judith Simon 					
Britta Skulima 	NET, SVS 	F-605 	+49 40 42883-2510 	>>> 	>>>
Kai Sommer 	AMD 	ZBH 	+49 40 42838-N.N. 	>>> 	>>>
Julian Späth 	CSB 	N-9 	+49 40 42883-N.N. 	>>> 	>>>
Jannek Squar 	WR 	DKRZ 108 	+49 40 460094-420 	>>> 	>>>
Dr. Christoph Stanik 	MAST 	D-212 	+49 40 42883-2105 	>>> 	>>>
Prof. Dr. Frank Steinicke 	HCI 	F-113, A-208 	+49 40 42883-2439, +49 40 42883-2402 	>>> 	>>>
Prof. Dr.-Ing. H.-Siegfried Stiehl 	BV 	R-115 	+49 40 42883-2453 	>>> 	>>>
Joshua Stock 	SVS 	F-609 	+49 40 42883-2562 	>>> 	>>>
Erik Strahl 	WTM 	F-232 	+49 40 42883-2536 	>>> 	>>>
Xiaowen Sun 	WTM 	F-227 	+49 40 42883-2441 	>>> 	
Alexander Sutherland 	WTM 	F-228b 	+49 40 42883-2531 	>>> 	>>>

T
Dr. Haisen Ta 	TAMS 	F-425 	+49 40 42883-2716 		
Eylem Tas 	WISTS 	C-213 	+49 40 42883-2415 	>>> 	
Dr. Navid Tavanapour 	WISTS 	C-205 	+49 40 42883-2154 	>>> 	>>>
Kristina Tesch 	SP 	F-125 	+49 40 42883-2545 	>>> 	>>>
Jöran Tesse 	ITG 	C-213 	+49 40 42883-2415 	>>> 	>>>
Tatjana Tetsis 	TAMS 	F-311 	+49 40 42883-2430 	>>> 	>>>
Dr. Daniel Thewes 	WR 	DKRZ-109 	+49 40 460094-N.N. 	>>> 	>>>
Dr. Suzanne Tolmeijer 	WISTS 	C-220 	+49 40 42883-2121 	>>> 	
Dr. Olga Tsoy 	CSB 	N-9 	+49 40 42883-N.N. 	>>> 	>>>
Yuyang Tu 	TAMS 	F-425 	+49 40 42883-2361, +49 40 42883-2716 	>>> 	>>>

U
Chikaodi Gloria Uba 	ITMC 	C-115 	+49 40 42883-2229 	>>> 	
Prof. Dr. Ricardo Usbeck 	SEMS 	F-411 	+49 40 42883-2360 	>>> 	>>>

V
Prof. Dr. Rüdiger Valk 	ART 	G-207 	+49 40 42883-2412 	>>> 	>>>
Dr.-Ing. André van Hoorn 	SWK 	D-233 	+49 40 42883-2367 	>>> 	
Carina Volkmer 	MAST 	D-203 	+49 40 42883-2187 	>>> 	
Prof. Dr. Stefan Voß 	IWI 	VMP5 3064 	+49 40 42838-3062 	>>> 	>>>

W
Jingwen Wang 	LT 	F-435 	+49 40 42883-2392 	>>> 	
Xintong Wang 	LT 	F-405 	+49 40 42883-2322 	>>> 	>>>
Florens Wasserfall 	TAMS 	F-316 	+49 40 42883-2501, +49 40 42883-2102 	>>> 	>>>
Dr. Cornelius Weber 	WTM 	F-233 	+49 40 42883-2537 	>>> 	>>>
Tom Weber 	SWK 	D-231 	+49 40 42883-2153 	>>> 	>>>
Juliane Wegner 	Studienbüro 	A-308 	+49 40 42883-2208 	>>> 	>>>
Simon Welker 	SP 	F-124 	+49 40 42883-2538 	>>> 	
Felix Welter 	NET 	F-614 	+49 40 42883-2560 	>>> 	
Prof. Dr. Stefan Wermter 	WTM 	F-230 	+49 40 42883-2434 	>>> 	>>>
Jens Wettlaufer 	SVS, NET 	F-626 	+49 40 42883-2352 	>>> 	>>>
Pascal Wichmann 	SVS 	F-633 	+49 40 42883-2042 	>>> 	>>>
Marion Wiese 	SWK 	D-232 	+49 40 42883-2135 	>>> 	>>>
Christina Wiethof 	WISTS 	C-204 	+49 40 42883-2152 	>>> 	>>>
Florian Wilkens 	NET 	F-627 	+49 40 42883-2353 	>>> 	>>>
Christian Wilms 	CV 	R-108 	+49 40 42883-2573 	>>> 	>>>
Tatjana Wingarz 	NET 	F-616 	+49 40 42883-2348 	>>> 	>>>
Prof. Dr. Bernd E. Wolfinger 	TKRN 	F-617 	+49 40 42883-2424 	>>> 	>>>
Benjamin Wollmer 	DBIS 	F-515 	+49 40 42883-2326 	>>> 	>>>

Y
Dr. Ehsan Yaghoubi 	CV 	R-103 	+49 40 42883-2570 	>>> 	
Xi Yan 	SEMS 	F-434 	+49 40 42883-2391 	>>> 	
Dr. Seid Muhie Yimam 	LT, HCDS 	F-415 	+49 40 42883-2418 	>>> 	>>>

Z
Mohammad Ali Zamani 	WTM 	F-225 	+49 40 42883-2446 	>>> 	>>>
Prof. Dr. Jianwei Zhang 	TAMS 	F-330a 	+49 40 42883-2431 	>>> 	>>>
Jingxin Zhang 	HCI 	F-108 	+49 40 42883-2048 	>>> 	>>>
Xufeng Zhao 	WTM 	F-229 	+49 40 42883-2532 	>>> 	
Reinhard Zierke 	RZ 	D-132 	+49 40 42883-2295 	>>> 	>>>
Aleksandar Zivkovic 	RZ 	D-135 	+49 40 42883-2297 	>>> 	>>>
"""
open_alex_id = 'https://openalex.org/I159176309'
institution_name = 'Universität Hamburg'

# parse names out of table string
names = []
for line in name_table.splitlines():
    tab_split = line.split('\t')
    # filter empty lines or headlines ('A', 'B', ..)
    if len(tab_split) < 2:
        continue
    # remove titles
    name = tab_split[0]
    name = name.replace('Prof. Dr. ', '')
    name = name.replace('Dr. ', '')
    name = name.replace('H.-', '')
    name = name.replace('Prof. ', '')
    name = name.replace('Prof. Ph.D. ', '')
    name = name.replace('Prof. H.-', '')
    name = name.replace('Dr.-Ing. ', '')
    name = name.replace('Prof. Dr.-Ing. ', '')
    names.append(name)

output = {
    'institution_name': institution_name,
    'open_alex_id': open_alex_id,
    'names': names}

with open('uhh.json', 'w', encoding='utf-8') as file:
    json.dump(output, file, ensure_ascii=False, indent=4)

