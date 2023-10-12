import streamlit as st
questions = ['Wat is sensatie in psychologische termen?', 'Wat betekent perceptie in de psychologie?', 'Wat is bottom-up verwerking?', 'Wat is top-down verwerking?', 'Wat is transductie in de context van sensatie en perceptie?', 'Wat is de absolute drempel in psychologie?', 'Wat is de verschil drempel in psychologie?', 'Wat is de signaaldetectietheorie (SDT)?', 'Wat is sensorische adaptatie?', 'Wat is de functie van het netvlies?', 'Wat zijn staafjes in het oog?', 'Wat zijn kegeltjes in het oog?', 'Wat is de fovea in het oog?', 'Wat is objectconstantheid?', 'Wat zijn binoculaire diepteaanwijzingen?', 'Wat zijn monoculaire diepteaanwijzingen?', 'Wat is binoculaire dispariteit?', 'Wat is convergentie in de context van diepteperceptie?', 'Wat is bewegingsparallax?', 'Wat is auditie?', 'Wat is een geluidsgolf?', 'Wat is het trommelvlies?', 'Wat is het vestibulaire gevoel?']
answers = ['Sensatie is de detectie van fysieke prikkels en de overdracht van deze informatie naar de hersenen. Het is de eerste stap in het proces van waarneming, zoals het voelen van warmte of het horen van een geluid.', 'Perceptie is het verwerken, organiseren en interpreteren van sensorische signalen in de hersenen. Het is hoe we betekenis geven aan onze zintuiglijke ervaring, zoals het erkennen van een liedje dat we horen.', 'Bottom-up verwerking is de perceptie die gebaseerd is op de fysieke kenmerken van de stimulus. Bijvoorbeeld, als we een onbekend object zien, vormen we een beeld van wat het is door de individuele kenmerken te analyseren.', 'Top-down verwerking is de interpretatie van sensorische informatie op basis van kennis, verwachtingen en eerdere ervaringen. Bijvoorbeeld, als we een woord in een onbekende taal zien, proberen we de betekenis ervan te begrijpen op basis van de context.', 'Transductie is het proces waarbij sensorische stimuli worden omgezet in neurale signalen die de hersenen kunnen interpreteren. Bijvoorbeeld, ogen zetten lichtstralen om in elektrische signalen die de hersenen als beelden interpreteren.', 'De absolute drempel is de minimale intensiteit van stimulatie die nodig is om een sensatie de helft van de tijd te detecteren. Bijvoorbeeld, het zachtste geluid dat je kunt horen of het zwakste licht dat je kunt zien.', 'De verschil drempel is de minimale hoeveelheid verandering die nodig is om een verschil tussen twee stimuli te detecteren. Bijvoorbeeld, het minimale volumeverschil dat nodig is om te merken dat een liedje luider of zachter is geworden.', 'De signaaldetectietheorie is een theorie van waarneming gebaseerd op het idee dat de detectie van een stimulus een oordeel vereist - het is geen alles-of-niets proces. Bijvoorbeeld, het beslissen of een vage schaduw een kat is of gewoon een struik, vereist een oordeel op basis van de beschikbare informatie.', 'Sensorische adaptatie is het verminderen van gevoeligheid voor een constant niveau van stimulatie. Bijvoorbeeld, we merken na een tijdje niet meer de klok tikken, omdat onze zintuigen zich hebben aangepast.', 'Het netvlies is het dunne oppervlak aan de binnenkant van het oog waar licht wordt omgezet in neurale signalen door sensorische receptoren.', 'Staafjes zijn cellen in het netvlies die reageren op lage lichtniveaus en resulteren in zwart-wit perceptie, bijvoorbeeld bij nachtzicht.', 'Kegeltjes zijn cellen in het netvlies die reageren op hogere lichtniveaus en resulteren in kleurwaarneming, bijvoorbeeld bij het zien van een regenboog.', 'De fovea is het centrum van het netvlies waar de kegeltjes dicht op elkaar zijn gepakt. Dit gebied zorgt voor het scherpste zicht.', 'Objectconstantheid is het correct waarnemen van objecten als constant in hun vorm, grootte, kleur en lichtintensiteit, ondanks ruwe sensorische data die de perceptie zouden kunnen misleiden. Bijvoorbeeld, een deur lijkt nog steeds rechthoekig aan te zien, zelfs als hij open is en we hem vanuit een hoek bekijken.', 'Binoculaire diepteaanwijzingen zijn visuele aanwijzingen vanuit beide ogen die de illusie van diepte veroorzaken. Elk oog ziet een iets ander beeld en die twee beelden worden samen gefuseerd tot één beeld.', 'Monoculaire diepteaanwijzingen zijn aanwijzingen voor diepte perceptie die beschikbaar zijn voor elk oog afzonderlijk. Bijvoorbeeld, de grootte van objecten in het gezichtsveld kan ons helpen inschatten hoe ver weg ze zijn.', 'Binoculaire dispariteit is een diepteaanwijzing waarbij elk oog door de afstand tussen de twee ogen een iets ander retinaal beeld ontvangt. Dit helpt ons om een driedimensionaal beeld van de wereld te vormen.', 'Convergentie is een aanwijzing voor binoculaire diepteperceptie. Wanneer een persoon een nabijgelegen object bekijkt, draaien de oogspieren de ogen naar binnen.', 'Bewegingsparallax is een monoculaire diepteaanwijzing die wordt waargenomen bij beweging ten opzichte van objecten. Dichterbij gelegen objecten lijken sneller te bewegen dan verder weg gelegen objecten.', 'Auditie is het horen of de perceptie van geluid. Dit is een van onze vijf zintuigen, waarmee we geluidsgolven kunnen waarnemen.', 'Een geluidsgolf is een patroon van veranderingen in luchtdruk gedurende een bepaalde periode. Deze veranderingen in luchtdruk produceren onze perceptie van geluid.', 'Het trommelvlies is een dunne membraan die het begin van het middenoor markeert. Geluidsgolven zorgen ervoor dat het vibreert, wat het begin is van het proces van geluidsdetectie.', 'Het vestibulaire gevoel is de perceptie van evenwicht die wordt bepaald door receptoren in het binnenoor. Het speelt een cruciale rol in het vermogen om rechtop te blijven en je fysieke oriëntatie in de ruimte te behouden.']

# -------------------------SESSION STATES----------------------------- #

if 'card_index' not in st.session_state:
    st.session_state.card_index = 0

if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False


# -------------------------BUTTON FUNCTIONS---------------------------- #


# -------------------------------MAIN---------------------------------- #

# Progress bar that progresses according to the card number
card_progress = st.progress(0)

main_container = st.container()
sub_container = st.container()

# Navigate to next question when button is pressed
if st.session_state.card_index < len(questions):
    # Two columns in which the flashcard navigation buttons are placed
    col1, col2 = sub_container.columns(2)
    with col1:
        if st.button("Show Answer", use_container_width=True):
            st.session_state.show_answer = True
        else:
            st.session_state.show_answer = False
    with col2:
        if st.button("Next question", use_container_width=True):
            st.session_state.card_index += 1
            st.session_state.show_answer = False

    if st.session_state.card_index < len(questions):
        st.subheader(questions[st.session_state.card_index])
        if st.session_state.show_answer is True:
            st.write(answers[st.session_state.card_index])
    else:
        st.subheader("Great work! Do you want to Loop through the material again?")
        st.button("Reset deck")

else:
    st.subheader("You finished all the questions for this lecture.")
    # st.balloons()
    if st.button("Reset deck"):
        st.session_state.card_index = 0
        st.session_state.show_answer = False
        st.experimental_rerun()

# Update the progress bar according to the card number
card_progress.progress(st.session_state.card_index / len(questions))