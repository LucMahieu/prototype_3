import streamlit as st

questions = ['Wat is geheugen?', 'Wat is amnesie?', 'Wat is retrograde amnesie?', 'Wat is anterograde amnesie?', 'Wat is priming?', 'Wat is impliciet geheugen?', 'Wat is expliciet geheugen?', 'Wat is procedureel geheugen?', 'Wat is episodisch geheugen?', 'Wat is semantisch geheugen?', 'Wat is encoding in het geheugen?', 'Wat zijn schemas in het geheugen?', 'Wat is chunking in het geheugen?', 'Wat zijn mnemonic technieken?', 'Wat is sensorisch geheugen?', 'Wat is werkgeheugen?', 'Wat is langdurige geheugen?', 'Wat is het seriële positie-effect?', 'Wat is consolidatie?', 'Wat is langdurige potentiatie (LTP)?', 'Wat zijn flashbulb-herinneringen?', 'Wat is herconsolidatie?', 'Wat is een ophaalaanwijzing (retrieval cue)?', 'Wat is het principe van coding specificity?', 'Wat is prospective memory?', 'Wat is retrieval-induced forgetting?', 'Wat is proactive interference?', 'Wat is retroactive interference?', 'Wat is blocking in het geheugen?', 'Wat is absentmindedness?', 'Wat is persistence in de context van het geheugen?', 'Wat is memory bias?', 'Wat is source misattribution?', 'Wat is source amnesia?', 'Wat is cryptomnesia?', 'Wat is suggestibility?', 'Wat zijn de soorten impliciete geheugen?', 'Wat is priming in de context van geheugen?', 'Wat is perceptuele priming?', 'Wat is conceptuele priming?', 'Wat is procedureel geheugen?', 'Wat is klassieke conditionering?', 'Wat is niet-associatief leren?', 'Wat zijn de soorten expliciet geheugen?', 'Wat zijn de stadia van het geheugen?', 'Wat is het Levels of Processing-model van geheugen?', 'Wat betekent onderhoudsherhaling in de context van geheugen?', 'Wat is elaboratieve herhaling in de context van geheugen?', 'Wat is de methode van loci of geheugenpaleis?', 'Wat is iconisch geheugen?', 'Wat is echoïsch geheugen?', 'Wat is geheugenspanne?', 'Wat is het Primacy effect?', 'Wat is het Recency effect?', "Wat betekent 'Replay' in de context van geheugen?", 'Wat is Retrieval practice?', 'Wat is Context-dependent memory?', 'Wat is State-dependent memory?', "Wat betekent 'Good retrieval cues'?", 'Wat is Context reinstatement?', 'Wat houdt het Encoding specificity principle in?', "Wat betekent 'savings' in de context van geheugen?", "Wat is het 'tip-of-the-tongue' fenomeen?", "Wat is 'infantiele amnesie'?", "Wat is een 'vals geheugen'?", "Wat zijn 'onderdrukte herinneringen'?"]
answers = ['Geheugen is het vermogen om informatie op te slaan en op te halen. Dit kun je zien als het vermogen van je hersenen om ervaringen en kennis te behouden en terug te roepen.', 'Amnesie is een tekort in het lange-termijngeheugen als gevolg van ziekte, hersenletsel of psychologisch trauma, waarbij het individu de mogelijkheid verliest om grote hoeveelheden informatie op te halen. Een voorbeeld hiervan is iemand die na een ongeluk zijn jeugdherinneringen niet meer kan herinneren.', 'Retrograde amnesie is een aandoening waarbij mensen eerdere herinneringen verliezen, zoals herinneringen aan gebeurtenissen, feiten, mensen of persoonlijke informatie. Dit betekent bijvoorbeeld dat iemand zijn trouwdag of de naam van een oude vriend kan vergeten.', "Anterograde amnesie is een aandoening waarbij mensen het vermogen verliezen om nieuwe herinneringen te vormen. Dit is bijvoorbeeld wat er gebeurt bij de hoofdpersoon in de film 'Finding Nemo', waarbij Dory voortdurend vergeet wat er net is gebeurd.", 'Priming is een proces waarbij de reactie op een prikkel wordt vergemakkelijkt door recente ervaring met die prikkel of een gerelateerde prikkel. Als je bijvoorbeeld het woord "geel" hoort, ben je sneller geneigd om "banaan" te zeggen dan wanneer je het woord "blauw" had gehoord.', 'Impliciet geheugen is het type geheugen dat tot uitdrukking komt door reacties, acties of reacties. Het is bijvoorbeeld het vermogen om te fietsen of te typen zonder bewust na te denken over hoe je het doet.', 'Expliciet geheugen is het type geheugen dat bewust wordt opgehaald. Dit betreft bijvoorbeeld het herinneren van feiten voor een examen of het terughalen van een specifieke gebeurtenis uit je verleden.', 'Procedureel geheugen is een type impliciet geheugen dat betrekking heeft op vaardigheden en gewoonten. Dit is bijvoorbeeld het vermogen om te fietsen, piano te spelen of je schoenen te strikken.', 'Episodisch geheugen betreft herinneringen aan persoonlijke ervaringen, geïdentificeerd door tijd en plaats. Denk bijvoorbeeld aan het herinneren van je eerste schooldag.', 'Semantisch geheugen is het geheugen voor feiten die losstaan van persoonlijke ervaringen. Zoals bijvoorbeeld het feit dat de aarde rond de zon draait.', 'Encoding is het proces waarbij de waarneming van een stimulus of gebeurtenis wordt omgezet in een herinnering. Dit kan bijvoorbeeld gebeuren door associatie of herhaling.', 'Schemas zijn cognitieve structuren in het langetermijngeheugen die helpen bij het waarnemen, organiseren en verwerken van informatie. Denk bijvoorbeeld aan je schema van hoe een hond eruit ziet.', 'Chunking is het organiseren van informatie in betekenisvolle eenheden om het geheugen te vergemakkelijken. Zoals wanneer je een telefoonnummer opbreekt in kleinere groepen cijfers.', "Mnemonics zijn leermiddelen of strategieën die het onthouden bevorderen door het gebruik van retrieval cues. Een bekend voorbeeld voor Nederlanders is het gebruik van 't kofschip om te bepalen of een werkwoord in de verleden tijd met een d of t eindigt.", 'Sensorisch geheugen is een geheugensysteem dat zeer kortstondig zintuiglijke informatie opslaat in bijna zijn oorspronkelijke zintuiglijke vorm. Bijvoorbeeld het beeld van een scène dat kort blijft hangen nadat je je ogen hebt gesloten.', 'Werkgeheugen is een beperkt capaciteit cognitief systeem dat tijdelijk informatie opslaat en manipuleert voor complexe taken. Dit wordt bijvoorbeeld gebruikt bij het oplossen van een wiskundig probleem.', 'Langdurig geheugen verwijst naar de relatief permanente opslag van informatie. Bijvoorbeeld, herinneringen aan je kindertijd of de kennis die je hebt opgedaan tijdens je studie.', 'Het seriële positie-effect is het vermogen om items van een lijst te herinneren op basis van hun presentatievolgorde, met beter geheugen voor items die vroeg of laat in de lijst worden gepresenteerd. Bijvoorbeeld, bij het onthouden van een boodschappenlijstje, onthouden mensen vaak het eerste en laatste item beter.', 'Consolidatie is het proces van stabilisatie van een geheugenspoor na het leren. Dit is de reden waarom het herhalen van informatie kort na het leren het makkelijker maakt om te onthouden.', 'Langdurige potentiatie is de versterking van een synaptische verbinding, waardoor de postsynaptische neuronen makkelijker geactiveerd kunnen worden. Het is een belangrijk mechanisme voor leren en geheugen.', 'Flashbulb-herinneringen zijn levendige episodische herinneringen aan de omstandigheden waarin mensen voor het eerst hoorden van een verrassende, belangrijke of emotioneel opwekkende gebeurtenis. Bijvoorbeeld, veel mensen herinneren zich precies waar ze waren en wat ze deden toen ze hoorden over de aanslagen op 11 september 2001.', 'Herconsolidatie is het proces waarbij herinneringen kwetsbaar worden voor verstoring wanneer ze worden opgeroepen, waardoor ze opnieuw moeten worden geconsolideerd. Dit verklaart waarom herinneringen kunnen veranderen of vervagen na verloop van tijd.', 'Een ophaalaanwijzing (retrieval cue) is elke stimulus die helpt bij het toegang krijgen tot informatie die is opgeslagen in het langdurige geheugen. Bijvoorbeeld, de geur van vers gebakken brood kan herinneringen oproepen aan je grootmoeders keuken.', 'Coding specificity stelt dat herinneringen sterk gekoppeld zijn aan de context waarin ze zijn gevormd. Bijvoorbeeld, als je studeert met een bepaalde achtergrondmuziek, kan diezelfde muziek later helpen bij het oproepen van de informatie.', 'Prospective memory verwijst naar het herinneren om iets te doen in de toekomst. Een voorbeeld is het onthouden om melk te kopen na het werk.', 'Dit is een fenomeen waarbij het ophalen van bepaalde items het latere ophalen van gerelateerde items kan belemmeren. Het is alsof de hersenen ruimte maken voor de opgehaalde informatie door het vergeten van gerelateerde informatie.', 'Proactive interference houdt in dat oude informatie het vermogen om nieuwe informatie te leren belemmert. Als je bijvoorbeeld probeert een nieuwe telefoonnummer te leren, kan je oude nummer het leren van het nieuwe nummer verstoren.', 'Retroactive interference betekent dat nieuwe informatie interfereert met het vermogen om oude informatie te herinneren. Bijvoorbeeld, als je een nieuw telefoonnummer leert, kan het moeilijker zijn om je oude nummer te herinneren.', 'Blocking verwijst naar de tijdelijke onmogelijkheid om iets te herinneren. Je weet dat je de informatie kent, maar je kunt er gewoon niet bij op dat moment.', 'Absentmindedness omvat aandachtstekorten en het vergeten om dingen te doen. Het kan zijn dat je vergeet de oven uit te zetten of waar je je sleutels hebt gelegd.', 'Persistence verwijst naar de ongewenste herinnering aan herinneringen die men liever zou vergeten. Dit komt vaak voor bij traumatische gebeurtenissen.', 'Memory bias is het veranderen van herinneringen in de loop van de tijd zodat ze overeenkomen met huidige overtuigingen of houdingen. Je herinnert je bijvoorbeeld een gebeurtenis uit je jeugd op een positievere manier omdat je nu gelukkiger bent.', 'Source misattribution verwijst naar het verkeerd herinneren van de tijd, plaats, persoon of omstandigheden die betrokken zijn bij een herinnering. Een voorbeeld hiervan is het verwarren van de locatie waar een gebeurtenis plaatsvond.', 'Source amnesia is een soort misattributie waarbij een persoon niet kan herinneren waar een herinnering vandaan komt. Zo kan iemand zich een feit of detail herinneren, maar niet meer waar ze deze informatie hebben opgepikt.', 'Cryptomnesia is een type van source misattribution waarbij een persoon gelooft dat een herinnerde gedachte origineel is, terwijl dat niet zo is. Dit kan gebeuren wanneer iemand bijvoorbeeld een idee presenteert als zijn eigen, terwijl hij het eigenlijk ergens anders heeft gehoord of gelezen.', 'Suggestibility is de neiging om misleidende informatie van externe bronnen in persoonlijke herinneringen op te nemen. Bijvoorbeeld, een getuige van een misdaad kan onbewust valse details in hun herinnering opnemen na het horen van de verklaringen van anderen.', 'Impliciete geheugen kan worden onderverdeeld in priming, procedureel geheugen, klassieke conditionering en niet-associatief leren. Deze vormen van geheugen werken veelal onbewust en hebben betrekking op zaken als vaardigheden, gewoonten en perceptuele herkenning.', 'Priming is een vorm van impliciet geheugen waarbij de reactie op een stimulus wordt vergemakkelijkt door recente ervaring met die stimulus of een gerelateerde stimulus. Het kan zowel perceptueel als conceptueel van aard zijn.', 'Perceptuele priming is een vorm van priming waarbij de reactie op dezelfde stimulus wordt vergemakkelijkt door recente blootstelling aan die stimulus. Dit is sterk afhankelijk van de hersengebieden die perceptuele verwerking ondersteunen.', "Conceptuele priming is een vorm van priming waarbij de reactie op een conceptueel gerelateerde stimulus wordt vergemakkelijkt. Bijvoorbeeld, het woord 'tafel' kan een reactie op het woord 'stoel' vergemakkelijken. Dit heeft veel te maken met hersengebieden die betrokken zijn bij conceptuele verwerking.", 'Procedureel geheugen is een vorm van impliciet geheugen dat betrekking heeft op vaardigheden en gewoonten, zoals het rijden van een auto of lezen. Het omvat geautomatiseerd gedrag en is zeer resistent tegen verval. Motorische vaardigheden en cognitieve vaardigheden vallen onder procedureel geheugen.', 'Klassieke conditionering is een vorm van impliciet geheugen waarbij een associatie wordt gemaakt tussen stimuli. Het is de basis voor veel leerprocessen, zoals het Pavloviaanse conditioneren waarbij een neutrale stimulus geassocieerd raakt met een stimulus die een reflexieve reactie oproept.', 'Niet-associatief leren is een vorm van impliciet geheugen waarbij gedrag verandert als gevolg van herhaalde blootstelling aan een stimulus. Dit omvat gewenning en sensitisatie, processen die belangrijk zijn voor adaptatie aan de omgeving.', 'Expliciet geheugen kan worden onderverdeeld in episodisch geheugen en semantisch geheugen. Dit zijn vormen van geheugen die we bewust kunnen oproepen en communiceren, zoals persoonlijke ervaringen of feitelijke kennis.', 'De stadia van het geheugen omvatten coderen, opslaan en ophalen. Dit zijn de belangrijkste stappen in het proces van het creëren en later herinneren van herinneringen.', 'Het Levels of Processing-model stelt dat de diepte van mentale verwerking invloed heeft op de waarschijnlijkheid van geheugencodering. Hoe dieper een item wordt gecodeerd en hoe meer betekenis het heeft, hoe beter het wordt onthouden. Bijvoorbeeld, het herhalen van een item kan het geheugen verbeteren, maar de manier waarop het item wordt herhaald, is ook belangrijk.', 'Onderhoudsherhaling verwijst naar het steeds opnieuw herhalen van een item, wat leidt tot oppervlakkige verwerking. Dit betekent dat de informatie op een basale manier wordt verwerkt, zoals alleen het onthouden van de vorm of het oppervlak van een object.', 'Elaboratieve herhaling is het op een betekenisvolle manier coderen van informatie, bijvoorbeeld door na te denken over het concept van het item of te beslissen of het op jezelf betrekking heeft. Het betekent dat we basale informatie uitbreiden door deze op een betekenisvolle manier te koppelen aan bestaande kennis, wat leidt tot diepe verwerking.', 'De methode van loci, ook bekend als het geheugenpaleis, is een strategie waarbij items die je wilt onthouden worden geassocieerd met fysieke locaties. Bijvoorbeeld, je zou de namen van je klasgenoten kunnen associëren met verschillende items in je slaapkamer om ze beter te onthouden.', 'Iconisch geheugen is een type visueel zintuiglijk geheugen waarbij je kort een beeld kunt visualiseren en enkele van de details kunt herinneren nadat je er kort naar hebt gekeken.', 'Echoïsch geheugen is een type auditief zintuiglijk geheugen waarmee je de laatste paar woorden die iemand heeft uitgesproken kunt herhalen, zelfs als je aan iets anders denkt.', 'Geheugenspanne verwijst naar de hoeveelheid informatie die het werkgeheugen kan bevatten. Onderzoek suggereert dat deze limiet ongeveer vier tot zeven items is.', 'Het Primacy effect verwijst naar het betere geheugen dat mensen hebben voor items die aan het begin van de lijst worden gepresenteerd. Bijvoorbeeld, bij het onthouden van een boodschappenlijstje, zijn de items aan het begin vaak beter te herinneren.', 'Het Recency effect verwijst naar het betere geheugen dat mensen hebben voor de meest recente items, degenen aan het einde van de lijst. Bijvoorbeeld, bij het leren van een lijst woorden, zullen de laatste woorden vaak beter onthouden worden.', "'Replay' verwijst naar het proces waarbij de neurale circuits die een herinnering vertegenwoordigen opnieuw vuren. Dit kan gebeuren tijdens slaap of bij bewuste herinnering gedurende de dag. Het helpt bij het versterken van de verbindingen tussen neuronen die de herinnering vertegenwoordigen.", 'Retrieval practice is een strategie waarbij informatie actief wordt opgeroepen door te proberen deze te herinneren. Onderzoek heeft aangetoond dat testen die retrieval practice omvatten, het geheugen beter versterken dan hetzelfde tijdsbestek besteden aan het herzien van reeds gelezen informatie.', 'Context-dependent memory houdt in dat we de fysieke context van een herinnering coderen samen met de informatie, en de context kan helpen bij het ophalen van de herinnering. Bijvoorbeeld, het leren van woordenlijsten op het land of onder water resulteerde in betere herinnering als de testomgeving overeenkwam met de leeromgeving.', 'State-dependent memory houdt in dat interne signalen, zoals stemming of de effecten van drugs of alcohol, de terugwinning van informatie uit het langetermijngeheugen kunnen beïnvloeden. Zo kan het zijn dat je je beter positieve herinneringen herinnert in een goede stemming en negatieve in een slechte stemming.', 'Goede retrieval cues zijn technieken om herinneringen op te roepen door de context of de gemoedstoestand waarin de oorspronkelijke leerervaring plaatsvond te herscheppen.', 'Context reinstatement betekent het herscheppen van de context waarin het oorspronkelijke leren plaatsvond. Dit kan aspecten omvatten zoals de kamer waar je in was, geuren of geluiden, en zelfs je stemming op dat moment.', 'Het Encoding specificity principle stelt dat elke stimulus die samen met een ervaring wordt gecodeerd, later een herinnering aan die ervaring kan triggeren. Een rijkere coderingscontext leidt tot een betere herinnering. Bijvoorbeeld, de geur van een bepaalde parfum kan een herinnering aan een bepaald persoon of gebeurtenis oproepen.', "'Savings' verwijst naar het idee dat zelfs als je je iets niet kunt herinneren, er sporen van het geheugen kunnen bestaan. Het verschil tussen de oorspronkelijke leerervaring en het opnieuw leren wordt 'savings' genoemd. Bijvoorbeeld, het opnieuw leren van Spaans of wiskunde van de middelbare school zou minder tijd en moeite kosten dan de eerste keer.", "Het 'tip-of-the-tongue' fenomeen is een vorm van blokkeren waarbij mensen grote frustratie ervaren terwijl ze proberen zich specifieke, enigszins obscure woorden te herinneren. Ondanks dat ze soms weten met welke letter het woord begint, hoeveel lettergrepen het heeft en mogelijk hoe het klinkt, kunnen ze het precieze woord niet in het werkgeheugen krijgen.", 'Infantiele amnesie verwijst naar het feit dat de meeste mensen zich geen specifieke episodische herinneringen kunnen herinneren van voor de leeftijd van 3 of 4. Dit wordt toegeschreven aan de vroege ontwikkeling van de prefrontale cortex en taalvaardigheden. Als je een specifieke herinnering hebt van rond deze leeftijd of eerder, is de herinnering waarschijnlijk afkomstig van een andere bron, zoals je ouders, broers of zussen, of een foto uit je kindertijd.', 'Een vals geheugen is een herinnering aan een gebeurtenis die niet heeft plaatsgevonden. Dit kan gebeuren wanneer mensen een gebeurtenis visualiseren en later deze mentale afbeelding verwarren met een echte herinnering. Dit is in wezen een probleem bij het monitoren van de bron van de afbeelding.', 'Onderdrukte herinneringen zijn herinneringen aan traumatische gebeurtenissen die bewust of onbewust uit het bewustzijn worden gehouden. Hoewel er veel debat is over de geldigheid van dergelijke herinneringen, geloven sommige mensen dat ze met de juiste therapie kunnen worden opgehaald.']


def change_card_index(index):
    # Select first element and re-insert at index
    st.session_state.questions.insert(index, st.session_state.questions[0])
    st.session_state.answers.insert(index, st.session_state.answers[0])

    # Delete the first duplicate card
    del st.session_state.questions[0]
    del st.session_state.answers[0]

    return


def evaluate_graduation(current_card):
    if current_card in st.session_state.easy_count:
        st.session_state.easy_count[current_card] += 1
    else:
        st.session_state.easy_count[current_card] = 1

    # Delete card if graduated
    if st.session_state.easy_count[current_card] >= 2:
        del st.session_state.questions[0]
        del st.session_state.answers[0]
    else:
        change_card_index(20)

    return


def reset_easy_count(current_card):
    st.session_state.easy_count[current_card] = 0


# -------------------------SESSION STATES----------------------------- #

if 'easy_count' not in st.session_state:
    st.session_state.easy_count = {}

if 'questions' not in st.session_state:
    st.session_state.questions = None

if 'answers' not in st.session_state:
    st.session_state.answers = None

if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False

if 'previous_page_name' not in st.session_state:
    st.session_state.previous_page_name = None

if 'current_page_name' not in st.session_state:
    st.session_state.current_page_name = __file__

# -------------------------------MAIN---------------------------------- #


def initialise_new_page():
    st.session_state.questions = questions.copy()
    st.session_state.answers = answers.copy()
    st.session_state.easy_count = {}
    return


# Read and store current file name
st.session_state.current_page_name = __file__

# Check if a new page is opened
if st.session_state.current_page_name != st.session_state.previous_page_name:
    # Change lists in session state with current week lists
    initialise_new_page()
    st.session_state.previous_page_name = st.session_state.current_page_name


card_progress = st.progress(0)
main_container = st.container()

with main_container:
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Easy', use_container_width=True):
            # Count executive times the user found current card easy
            evaluate_graduation(st.session_state.questions[0])
            st.session_state.show_answer = False

    with col2:
        if st.button('Medium', use_container_width=True):
            st.session_state.show_answer = False
            reset_easy_count(st.session_state.questions[0])
            change_card_index(5)

    with col3:
        if st.button('Hard', use_container_width=True):
            st.session_state.show_answer = False
            reset_easy_count(st.session_state.questions[0])
            change_card_index(2)


if st.button('Show Answer', use_container_width=True):
    st.session_state.show_answer = not st.session_state.show_answer

if len(st.session_state.questions) == 0:
    st.session_state.questions = questions.copy()
    st.session_state.answers = answers.copy()
    st.session_state.easy_count = {}

st.subheader(st.session_state.questions[0])
if st.session_state.show_answer:
    st.write(st.session_state.answers[0])

card_progress.progress(int(sum(st.session_state.easy_count.values()) / (2 * len(questions)) * 100))