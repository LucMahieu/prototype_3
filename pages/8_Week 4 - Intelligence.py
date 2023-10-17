import streamlit as st
questions = ['Wat is intelligentie?', 'Wat is de mentale leeftijd?', 'Wat is het intelligentiequotiënt (IQ)?', 'Wat is algemene intelligentie (g)?', 'Wat is vloeibare intelligentie?', 'Wat is gekristalliseerde intelligentie?', 'Wat is emotionele intelligentie (EI)?', 'Wat is taal?', 'Wat zijn morfemen?', 'Wat zijn fonemen?', 'Wat is afasie (aphasia)?', 'Wat is het gebied van Wernicke?', 'Wat is de theorie van linguïstische relativiteit?', 'Wat houdt de psychometrische benadering van intelligentiemeting in?', 'Wat zijn prestatiestests?', 'Wat zijn aanlegtests?', 'Wat is de triarchische theorie van intelligentie?', 'Wat is analytische intelligentie?', 'Wat is creatieve intelligentie?', 'Wat is praktische intelligentie?', 'Wat is de correlatie tussen reactietijd en algemene intelligentie?', 'Wat betekent een negatieve zwakke correlatie in de context van taakdiscriminatie en algemene intelligentie?', 'Wat betekent een negatieve zwakke correlatie van 0,5 in de context van werkgeheugencapaciteit en algemene intelligentie?', 'Wat is de correlatie tussen executive control en algemene intelligentie?', 'Wat is het Flynn-effect in de context van een taak waarbij letters aan de linkerkant worden gepresenteerd en een toon aangeeft dat men naar rechts of beide kanten moet kijken?']
answers = ['Intelligentie is het vermogen om kennis te gebruiken om te redeneren, beslissingen te nemen, complexe ideeën te begrijpen, problemen op te lossen, snel te leren en zich aan te passen aan omgevingsuitdagingen. Het is een cruciale factor voor succes in vele aspecten van het leven.', 'Mentale leeftijd is een beoordeling van het intellectuele niveau van een kind in vergelijking met leeftijdsgenoten, bepaald door de testresultaten van het kind te vergelijken met het gemiddelde voor kinderen van dezelfde chronologische leeftijd. Zo kan een kind van 10 jaar met een mentale leeftijd van 13 jaar verder gevorderd zijn dan zijn of haar leeftijdsgenoten.', 'Het IQ is een maat voor intelligentie die wordt berekend door de geschatte mentale leeftijd van een kind te delen door de chronologische leeftijd van het kind en dit getal vervolgens met 100 te vermenigvuldigen. Een IQ van 100 wordt beschouwd als gemiddeld.', 'Algemene intelligentie (g) is de theorie dat er een enkele factor is die intelligentie onderliggend bepaalt. Het is een idee dat voor het eerst werd voorgesteld door de psycholoog Charles Spearman.', 'Vloeibare intelligentie weerspiegelt het vermogen om informatie te verwerken, relaties te begrijpen en logisch na te denken, vooral in nieuwe of complexe situaties. Het is cruciaal voor het oplossen van nieuwe problemen waarvoor weinig of geen eerdere kennis vereist is.', 'Gekristalliseerde intelligentie weerspiegelt zowel de kennis die is opgedaan door ervaring als het vermogen om die kennis te gebruiken. Het omvat vaardigheden en kennis die we in de loop van de tijd hebben opgedaan, zoals woordenschat en culturele informatie.', 'Emotionele intelligentie is een type sociale intelligentie dat het beheer, de herkenning en het begrip van emoties benadrukt, en het gebruik van deze emoties om denken en handelen te sturen. Het omvat vaardigheden zoals empathie, zelfbewustzijn en emotionele regulatie.', 'Taal is een communicatiesysteem dat geluiden en symbolen gebruikt volgens grammaticale regels. Het stelt ons in staat om complexe ideeën en emoties uit te drukken en te begrijpen, en speelt een cruciale rol in menselijke interactie.', 'Morfemen zijn de kleinste betekenisdragende eenheden van taal, inclusief voor- en achtervoegsels. Bijvoorbeeld, het woord "onbreekbaar" bestaat uit de morfemen "on-", "breek" en "-baar".', 'Fonemen zijn de basisklanken van spraak en vormen de fundamenten van taal. Bijvoorbeeld, het Engelse woord "cat" heeft drie fonemen: /k/, /æ/, en /t/.', 'Afasie (aphasia) is een taalstoornis die leidt tot tekorten in taalbegrip en -productie, vaak als gevolg van hersenbeschadiging, zoals een beroerte.', 'Het gebied van Wernicke is een gebied waar de temporale en pariëtale lobben van de linker hersenhelft samenkomen, gerelateerd aan spraakbegrip. Schade aan dit gebied kan leiden tot Wernicke-afasie, gekenmerkt door vloeiende maar zinloze spraak.', 'De theorie van linguïstische relativiteit stelt dat taal het denken bepaalt. Bijvoorbeeld, sprekers van talen met veel woorden voor sneeuw zouden meer gedetailleerde percepties van sneeuw hebben.', 'De psychometrische benadering probeert intelligentie te begrijpen door de patroon van resultaten op intelligentietests te bestuderen. Het richt zich op hoe mensen presteren op gestandaardiseerde tests die mentale vaardigheden beoordelen, zoals wat mensen weten en hoe ze problemen oplossen. Een voorbeeld hiervan zijn de prestatiestests en aanlegtests.', 'Prestatiestests zijn ontworpen om de huidige niveaus van vaardigheid en kennis van mensen te beoordelen. Deze tests worden vaak gebruikt in het onderwijs om te bepalen wat een student heeft geleerd.', 'Aanlegtests proberen te voorspellen welke taken en mogelijk zelfs welke banen mensen in de toekomst goed zullen kunnen uitvoeren. De resultaten van deze tests kunnen een grote invloed hebben op iemands leven.', 'De triarchische theorie van intelligentie suggereert dat er drie soorten intelligentie zijn: analytisch, creatief en praktisch. Ondanks enige kritiek, biedt deze theorie een intuïtief begrip van intelligentie door de verschillende manieren waarop we problemen oplossen te benadrukken.', 'Analytische intelligentie is vergelijkbaar met wat gemeten wordt door psychometrische tests. Het gaat om goede probleemoplossende vaardigheden, het voltooien van analogieën, het oplossen van puzzels en andere academische uitdagingen.', 'Creatieve intelligentie houdt in dat je inzicht kunt krijgen en nieuwe problemen kunt oplossen - op nieuwe en interessante manieren kunt denken. Dit kan bijvoorbeeld betekenen dat je een unieke oplossing bedenkt voor een complex probleem.', 'Praktische intelligentie verwijst naar het omgaan met alledaagse taken, zoals weten of een parkeerplaats groot genoeg is voor je voertuig, een goede beoordelaar van mensen zijn, een effectieve leider zijn enzovoort.', 'Hoewel het een onderwerp van onderzoek is, wordt vaak gedacht dat er een correlatie bestaat tussen reactietijd en algemene intelligentie. Met andere woorden, mensen met een hogere algemene intelligentie zouden over het algemeen snellere reactietijden kunnen hebben.', 'Een negatieve zwakke correlatie betekent dat hoe sneller de reactietijd bij een discriminatietaak, hoe hoger de intelligentiescore, maar de samenhang is zwak.', 'Een negatieve zwakke correlatie van 0,5 betekent dat hoe meer tijd iemand nodig heeft, hoe lager de intelligentiescore. De correlatie is echter zwak, wat impliceert dat er ook andere factoren zijn die de intelligentie beïnvloeden.', 'De correlatie tussen executive control en algemene intelligentie is dat hoe meer items iemand kan herhalen bij het presenteren van lange zinnen of veel items, hoe hoger de intelligentiescore. Dit suggereert dat executive control een rol kan spelen bij het meten van intelligentie.', 'Het Flynn-effect verwijst naar het fenomeen waarbij mensen die er niet in slagen te schakelen tussen taken, zoals het kijken naar verschillende kanten wanneer een toon wordt afgespeeld, lager scoren op intelligentietests. Dit suggereert dat mentale flexibiliteit een component van intelligentie kan zijn.']

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

# Two columns in which the flashcard navigation buttons are placed
col1, col2, col3 = sub_container.columns(3)
with col1:
    if st.button("Previous question", use_container_width=True):
        if st.session_state.card_index == 0:  # Als het de eerste vraag is, ga naar de laatste
            st.session_state.card_index = len(questions) - 1
        else:
            st.session_state.card_index -= 1
        st.session_state.show_answer = False

with col2:
    if st.button("Show Answer", use_container_width=True):
        st.session_state.show_answer = True
    else:
        st.session_state.show_answer = False

with col3:
    if st.button("Next question", use_container_width=True):
        st.session_state.card_index = (st.session_state.card_index + 1) % len(questions)  # Modulo zorgt ervoor dat het een carrousel wordt
        st.session_state.show_answer = False

if st.session_state.card_index < len(questions):
    st.subheader(questions[st.session_state.card_index])
    if st.session_state.show_answer is True:
        st.write(answers[st.session_state.card_index])
else:
    st.subheader("Great work! Do you want to Loop through the material again?")
    st.button("Reset deck")

# Update the progress bar according to the card number
card_progress.progress(st.session_state.card_index / len(questions))
