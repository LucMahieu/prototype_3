import streamlit as st
questions = ['Wat is persoonlijkheid?', 'Wat is een persoonlijkheidstrek?', 'Wat zijn temperamenten?', 'Wat is de vijffactorentheorie?', 'Wat zijn trait-benaderingen?', 'Wat is het Behavioral Approach System (BAS)?', 'Wat is het Behavioral Inhibition System (BIS)?', 'Wat is het Fight-Flight-Freeze System (FFFS)?', 'Wat zijn humanistische benaderingen in persoonlijkheidsstudies?', 'Wat is de locus of control?', 'Wat is wederkerig determinisme (reciprocal determinism)?', 'Wat is ‘Need of cognition’?', 'Wat is situationisme?', 'Wat is interactionisme?', 'Wat zijn idiografische benaderingen?', 'Wat zijn nomothetische benaderingen?', 'Wat zijn projective measures?', 'Wat is een self-schema?', 'Wat is zelfwaardering of self-esteem?', 'Wat is de Sociometer theory?', 'Wat is sociale vergelijking?', 'Wat is self-serving bias?']
answers = ['Persoonlijkheid verwijst naar de kenmerkende patronen van gedachten, emotionele reacties en gedragingen die stabiel zijn in de tijd en over verschillende situaties. Het is wat ons uniek maakt als individuen.', 'Een persoonlijkheidstrek is een stabiel patroon van denken, voelen en gedrag. Voorbeelden zijn eerlijkheid, optimisme of agressiviteit.', 'Temperamenten zijn biologisch gebaseerde neigingen om op specifieke manieren te handelen of te voelen. Een voorbeeld hiervan is een persoon die van nature uitbundig en energiek is.', 'De vijffactorentheorie stelt voor dat persoonlijkheid kan worden gedefinieerd door vijf factoren: openheid, nauwkeurigheid, extraversie, vriendelijkheid en neuroticisme. Dit wordt ook wel het Big Five-model genoemd.', 'Het elaboration likelihood model is een theorie die suggereert dat overtuigende berichten leiden tot veranderingen in attitudes via ofwel de centrale of perifere route. Dit hangt af van de mate waarin het individu nadenkt over de inhoud van de boodschap. Is de individu gemotiveerd en in de mogelijk om dit te doen, dan gaat het via de centrale route. Is een individu niet gemotiveerd of niet in de mogelijkheid, dan gaat het via de perifere route.', 'Het Behavioral Approach System (BAS) is een hersensysteem dat gedrag stimuleert in reactie op kansen voor beloningen of prikkels. Het is betrokken bij motivatie en het nastreven van aangename ervaringen. Dit is het ‘gaan’ centrum en is onderdeel van de Revised reinforcement sensitivity theory.', 'Het Behavioral Inhibition System (BIS) is een hersensysteem dat de omgeving in de gaten houdt voor potentiële bedreigingen en gedrag remt dat pijn of gevaar kan riskeren. Het is betrokken bij angst en vermijdend gedrag. Dit is het ‘slow down’ centrum en is onderdeel van de Revised reinforcement sensitivity theory.', 'Het Fight-Flight-Freeze System (FFFS) is een hersensysteem dat reageert op bedreigingen door defensief gedrag te initiëren: bevriezen, ontsnappen, of vechten. Het is een fundamenteel onderdeel van onze overlevingsreactie.', 'Humanistische benaderingen leggen de nadruk op zelfactualisatie en zelfbegrip om persoonlijkheid te bestuderen. Ze kijken naar hoe individuen hun volledig potentieel kunnen bereiken en begrijpen. Verschillen in persoonlijkheid kunnen verklaard worden door waar ze staan in de Maslow’s piramide: ‘the hierarchy of needs’. ', 'De locus of control verwijst naar de overtuigingen over de mate van controle die iemand heeft over de uitkomsten in zijn of haar leven. Bijvoorbeeld, iemand met een interne locus of control gelooft dat zij controle hebben over hun eigen leven.', 'Wederkerig determinisme is een theorie die stelt dat iemands gedragingen worden beïnvloed door drie factoren: de omgeving, verschillende persoonlijke factoren (zoals verwachtingen, eigenschappen, zelfvertrouwen) en het gedrag zelf. ', '‘Need of cognition’ is de neiging om complexe cognitieve activiteiten te ondernemen en ervan te genieten, zoals het oplossen van puzzels of kritisch denken.', 'Situationisme is de theorie dat situationele factoren, meer dan persoonlijkheidstrekken, gedrag bepalen. Dit betekent dat de omgeving waarin iemand zich bevindt, een grotere invloed kan hebben op hun gedrag dan hun persoonlijkheid.', 'Interactionisme is de theorie dat zowel situaties als persoonlijkheidstrekken gezamenlijk gedrag bepalen. Het stelt dat gedrag het resultaat is van de interactie tussen persoonlijke kenmerken en de omgeving.', 'Idiografische benaderingen richten zich op het begrijpen van de complexiteit van de individuele persoonlijkheid, waarbij ze meer kijken naar de unieke aspecten van een persoon dan naar algemene kenmerken. Hierbij zou de onderzoeker bijvoorbeeld tien mensen vragen om persoonlijkheidstrekken op te schrijven die ze bij zichzelf vinden passen. ', 'Nomothetische benaderingen richten zich op algemene persoonlijkheidskenmerken die over individuen heen kunnen worden gezien, zoals de neiging om extravert of introvert te zijn. Hierbij zou de onderzoeker mensen een vragenlijst geven met honderd persoonlijkheidstrekken waar ze zichzelf op kunnen scoren tussen de één en tien.', 'Projective measures zijn persoonlijkheidstests die reageren op dubbelzinnige prikkels, vaak gebruikt om onbewuste processen te beoordelen. Bijvoorbeeld de Rorschach-inktvlektest, waarbij individuen hun interpretaties van ongestructureerde inktvlekken geven.', 'Een self-schema is een cognitieve structuur die kennis, overtuigingen en herinneringen over jezelf organiseert. Het helpt bijvoorbeeld bij het snel verwerken van informatie die relevant is voor onszelf.', 'Self-esteem is een evaluatief aspect van zelfperceptie waarbij individuen zich waardevol of niet kunnen voelen. Het is nauw verbonden met hoe we ons voelen over onze prestaties en capaciteiten.', 'De sociometer theory stelt dat zelfvertrouwen dient als een sociometer: een interne meter die het niveau van sociale acceptatie of afwijzing monitort. Het helpt ons te bepalen hoe goed we passen in onze sociale omgeving en of we risico lopen op uitsluiting.', "Sociale vergelijking is het proces van het evalueren van je eigen vaardigheden, acties en overtuigingen door ze te contrasteren met die van anderen. Bijvoorbeeld, iemand kan zijn loopbaanvoortgang beoordelen door deze te vergelijken met collega's.", 'Self-serving bias is de neiging om successen toe te schrijven aan zichzelf en mislukkingen aan externe factoren. Bijvoorbeeld, als we slagen voor een test, kan het zijn omdat we slim zijn. Maar als we falen, is het misschien omdat de test te moeilijk was.']

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