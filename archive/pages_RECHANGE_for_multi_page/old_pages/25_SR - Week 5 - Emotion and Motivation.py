import streamlit as st
questions = ['Wat is een emotie?', 'Wat zijn primaire emoties?', 'Wat zijn secundaire emoties?', 'Wat houdt de James-Lange theorie in?', 'Wat houdt de Cannon-Bard theorie in?', 'Wat is de Schachter-Singer theory (tweefactortheorie van emotie)?', 'Wat zijn display rules?', 'Wat is ideal affect?', 'Wat is motivatie?', 'Wat is een behoefte?', 'Wat is de behoeftenhiërarchie volgens Maslow?', 'Wat is zelfactualisatie?', "Wat is een 'drive'?", 'Wat is homeostase?', 'Wat is de Yerkes-Dodson wet?', 'Wat zijn prikkels (incentives)?', 'Wat is extrinsieke motivatie?', 'Wat is intrinsieke motivatie?', 'Wat is zelfeffectiviteit?', 'Wat is zelfregulatie?', 'Wat is de behoefte om te behoren?', 'Wat is de balanstheorie?', 'Wat is cognitieve dissonantie?', 'Wat is zelfbevestiging?', 'Wat zijn core values?', 'Wat zijn stemmingen?', 'Wat is het circumplex model van emoties?', 'Wat is arousal?', 'Welke systemen zijn betrokken bij emotie?', 'Wat is de functie van de insula?', 'Wat is de functie van de amygdala?', 'Wat is het snelle pad naar de amygdala?', 'Wat is het trage pad naar de amygdala?', 'Wat is de rol van de amygdala in het geheugen?', 'Wat is een polygraaf en hoe wordt het gebruikt?', 'Wat is de gezichtsuitdrukking hypothese?', 'Wat is misattributie van opwinding?', 'Wat zijn ontwrichtende emoties?', 'Wat is het negatieve-feedbackmodel van homeostase?', 'Wat zijn gewoontes?', 'Wat betekent het om gratificatie uit te stellen?', "Wat betekent het om 'hot cognitions' om te zetten naar 'cold cognitions'?", 'Wat is rationaliseren?']
answers = ['Een emotie is een onmiddellijke, specifieke negatieve of positieve reactie op omgevingsgebeurtenissen of interne gedachten. Bijvoorbeeld, blijdschap is een positieve reactie op een aangename gebeurtenis.', 'Primaire emoties zijn emoties die aangeboren, evolutionair adaptief en universeel zijn (gedeeld tussen culturen). Voorbeelden zijn woede, angst, vreugde en verdriet.', 'Secundaire emoties zijn mengsels van primaire emoties. Zo kan bijvoorbeeld schaamte worden gezien als een combinatie van angst en verdriet.', "De James-Lange theorie stelt dat mensen specifieke patronen van lichamelijke reacties waarnemen en als gevolg van die waarneming emotie voelen. 'Ik ben bang, want ik beef. '", "De Cannon-Bard theorie stelt dat informatie over emotionele stimuli tegelijkertijd naar de cortex en het lichaam wordt gestuurd en resulteert in een emotionele ervaring (arousal) en lichamelijke reacties. 'Ik ben bang, en ik beef.'", 'De tweefactortheorie stelt dat het label dat wordt toegepast op fysiologische opwinding resulteert in de ervaring van een emotie. Bijvoorbeeld, als je hart sneller klopt en iemand zegt dat je bang bent, dan zal je die opwinding waarschijnlijk als angst interpreteren.', 'Display rules zijn regels die we leren door socialisatie, die bepalen welke emoties geschikt zijn in bepaalde situaties. Bijvoorbeeld, in sommige culturen is het ongepast om verdriet in het openbaar te tonen.', 'Ideal affect verwijst naar de emotionele en affectieve toestanden die mensen willen ervaren of die culturen bijzonder waarderen. Bijvoorbeeld, sommige culturen waarderen kalmte meer dan opwinding.', 'Motivatie is een proces dat gedrag stimuleert, richt en onderhoudt met het oog op een doel. Het kan zijn dat je bijvoorbeeld studeert voor een examen om een goed cijfer te halen.', 'Een behoefte is een staat van biologische, sociale of psychologische tekortkoming. Bijvoorbeeld, honger is een biologische behoefte en behoefte aan sociale interactie is een sociale behoefte.', "Maslow's behoeftenhiërarchie stelt dat basisbehoeften voor overleving eerst moeten worden voldaan voordat mensen hogere behoeften kunnen bevredigen. Zoals, eerst moeten basisbehoeften zoals voedsel en onderdak worden voldaan voordat men kan streven naar zaken als zelfactualisatie.", 'Zelfactualisatie is een staat die wordt bereikt wanneer iemands persoonlijke dromen en aspiraties zijn gerealiseerd. Bijvoorbeeld, een kunstenaar kan zelfactualisatie bereiken door zijn/haar meesterwerk te creëren.', "Een 'drive' is een psychologische staat die, door opwinding te creëren, een organisme motiveert om een behoefte te bevredigen. Bijvoorbeeld, honger kan een 'drive' zijn om voedsel te zoeken.", "Homeostase zorgt ervoor dat lichaamsfuncties in evenwicht blijven. Zo regelt ons lichaam de interne temperatuur door te laten beven bij kou en te laten zweten als het te warm is.", 'De Yerkes-Dodson wet is het psychologische principe dat stelt dat de prestaties op uitdagende taken toenemen met opwinding tot een gematigd niveau. Daarna belemmert extra opwinding de prestaties. Bijvoorbeeld, een beetje stress kan nuttig zijn voor een examen, maar te veel stress kan de prestaties belemmeren.', 'Prikkels (incentives) zijn externe objecten of externe doelen, in plaats van interne drives, die gedragingen motiveren. Zoals, een financiële beloning een prikkel kan zijn om hard te werken.', 'Extrinsieke motivatie is de drijfveer om een activiteit uit te voeren vanwege de externe doelen die met die activiteit zijn verbonden. Bijvoorbeeld, studeren voor een examen om een goed cijfer te halen.', 'Intrinsieke motivatie is de drijfveer om een activiteit uit te voeren vanwege de waarde of het plezier dat aan die activiteit wordt geassocieerd, niet vanwege een duidelijk extern doel. Bijvoorbeeld, het lezen van een boek omdat je geniet van het verhaal.', 'Zelfeffectiviteit is het geloof dat inspanningen om een doel te bereiken succesvol zullen zijn. Het is een belangrijk aspect van motivatie en zelfvertrouwen.', 'Zelfregulatie is het proces waarbij mensen hun gedrag sturen naar het bereiken van doelen. Zoals het volgen van een dieet of studieplanning om een bepaald doel te bereiken.', 'De behoefte om te behoren is de behoefte aan interpersoonlijke verbindingen, een fundamentele drijfveer die zich heeft ontwikkeld voor adaptieve doeleinden. Zoals het verlangen om deel uit te maken van een groep of gemeenschap.', 'De balanstheorie stelt dat mensen gemotiveerd zijn om harmonie in hun interpersoonlijke relaties te bereiken. Een triade is in balans als alle mensen elkaar mogen of allemaal niet mogen, of wanneer twee mensen de derde niet mogen. Een disbalans is er als twee vrienden het niet eens zijn over de derde persoon.', 'Cognitieve dissonantie is het onaangename gevoel bij het besef van twee tegenstrijdige overtuigingen of een overtuiging die in conflict is met een gedrag. Bijvoorbeeld, het geloven in dierenrechten maar toch vlees eten.', 'Zelfbevestiging is de behoefte aan een gevoel van zelf dat coherent en stabiel is. Het kan worden bereikt door zelfreflectie en affirmaties die de eigen waarden en overtuigingen bevestigen.', 'Core values zijn sterk aangehouden overtuigingen over de blijvende principes die het meest belangrijk en betekenisvol zijn. Ze bevorderen emoties en acties wanneer ze worden opgeroepen of bedreigd. Een voorbeeld is eerlijkheid, die een individu kan motiveren om de waarheid te spreken, zelfs in moeilijke situaties.', 'Stemmingen zijn diffuse, langdurige emotionele toestanden die geen identificeerbare trigger hebben of een specifieke gedrags- of fysiologische reactie. Ze kleuren subtiel gedachten en gedrag, zonder directe verandering in wat er gebeurt. Mensen in een goede of slechte stemming weten vaak niet waarom ze zich zo voelen.', 'Het circumplex model plot emoties op twee continuüms: valentie, of hoe negatief of positief ze zijn, en arousal, of hoe activerend ze zijn. Bijvoorbeeld, het verliezen van een dollar zou negatieve valentie en lichte arousal kunnen veroorzaken, terwijl het winnen van de loterij positieve valentie en hoge arousal zou veroorzaken.', 'Arousal is een term die gebruikt wordt om fysiologische activatie te beschrijven, zoals verhoogde hersenactiviteit, of verhoogde autonome reacties zoals een versnelde hartslag, verhoogd zweten of spierspanning.', "Veel hersenstructuren buiten het limbisch systeem zijn betrokken bij emotie. Belangrijke structuren in het limbisch systeem voor emotie zijn de insula en de amygdala, maar ook verschillende regio's van de prefrontale cortex zijn belangrijk voor het genereren van emoties.", 'De insula ontvangt en integreert somatosensorische signalen van het hele lichaam en is betrokken bij het subjectieve bewustzijn van lichamelijke toestanden. Het speelt een belangrijke rol in de ervaring van emoties, zoals afschuw en angst.', 'De amygdala verwerkt de emotionele betekenis van stimuli en genereert onmiddellijke emotionele en gedragsreacties. Het is de hersenstructuur die het belangrijkst is voor emotioneel leren, zoals het ontwikkelen van geconditioneerde angstreacties.', 'Het snelle pad is een systeem dat sensorische informatie bijna onmiddellijk verwerkt. Langs dit pad reist sensorische informatie snel door de thalamus direct naar de amygdala voor prioritaire verwerking.', 'Het trage pad leidt tot meer doordachte en grondige evaluaties. Langs dit pad reist sensorische informatie van de thalamus naar de cortex, waar de informatie grondiger wordt onderzocht voordat het naar de amygdala wordt gestuurd. Het snelle systeem bereidt dieren voor om te reageren op een dreiging in het geval dat het trage pad de dreiging bevestigt.', 'De amygdala speelt een rol in het opslaan van emotionele gebeurtenissen in het geheugen. Het verhoogt de activiteit bij emotionele gebeurtenissen, wat de lange termijn geheugen verbetert, vooral voor angstige gebeurtenissen. Het helpt ons schadelijke situaties te herinneren en mogelijk te vermijden.', 'Een polygraaf is een elektronisch apparaat dat de fysiologische reactie van het lichaam op vragen meet, zoals ademhalings- en hartslag. Het wordt vaak gebruikt in criminele onderzoeken en bij sollicitaties waarbij geheime documenten betrokken zijn als een soort leugendetector, hoewel het geen onderscheid kan maken in de verhoogde fysiologische opwinding.', 'De gezichtsuitdrukking hypothese stelt dat verschillende gezichtsuitdrukkingen kunnen leiden tot verschillende emoties. Een voorbeeld is het lezen van een stripverhaal met een pen boven de lip (wat een frons veroorzaakt) of tussen de tanden (wat een glimlach veroorzaakt), wat invloed heeft op hoe grappig je de strip vindt.', 'Misattributie van opwinding vindt plaats wanneer mensen de bron van hun opwinding verkeerd identificeren. Een voorbeeld is een studie waarbij mannen die over een smalle enge brug liepen meer aantrekking toonden voor een vrouwelijke onderzoeker op de brug dan mannen die over een veiligere brug liepen.', 'Ontwrichtende emoties zijn negatieve gevoelens zoals nervositeit of positieve gevoelens zoals afgeleid worden door uit te kijken naar een spannende aankomende gebeurtenis, die onze acties kunnen verstoren.', 'Het negatieve-feedbackmodel van homeostase is het proces waarbij ons lichaam een bepaalde temperatuur handhaaft. Als we te warm of te koud zijn, start onze hersenen (voornamelijk de hypothalamus) reacties zoals zweten om af te koelen of rillen om op te warmen. Dit blijft doorgaan tot de gewenste temperatuur is bereikt.', 'Gewoonten zijn gedragingen die na verloop van tijd een dominante reactie worden als ze consistent een bepaalde drang verminderen. De kans dat een gedrag zal optreden is te wijten aan drang en gewoonte.', 'Het uitstellen van gratificatie is een kenmerk van zelfregulatie waarbij onmiddellijke beloningen worden uitgesteld in de zoektocht naar langetermijndoelen. Een voorbeeld hiervan is studenten die thuis blijven studeren in plaats van uit te gaan met vrienden om toegelaten te worden tot een graduate school.', "Het omzetten van 'hot cognitions' naar 'cold cognitions' is een strategie waarbij je een gewenst object mentaal verandert in iets ongewensts, waarbij je de focus verlegt van de belonende, plezierige aspecten van objecten naar hun conceptuele of symbolische betekenissen. Bijvoorbeeld, kinderen stelden zich in een studie een verleidelijke pretzel voor als een bruine stam of marshmallows als wolken.", 'Rationaliseren is een manier om dissonantie te verminderen door een conflict weg te redeneren. Rationalisaties zijn geen waarheden, maar mythen die we onszelf vertellen om dissonantie te verminderen. Bijvoorbeeld, rokers kunnen geloven dat roken gevaarlijk is, maar rationaliseren het conflict tussen die overtuiging en het roken door zichzelf ervan te overtuigen dat roken niet zo gevaarlijk is als het wordt voorgesteld.']


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