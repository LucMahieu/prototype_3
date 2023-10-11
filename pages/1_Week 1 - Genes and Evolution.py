import streamlit as st
questions = ['Wat is psychologische wetenschap?', 'Wat is het centrale zenuwstelsel (CNS)?', 'Wat is het perifere zenuwstelsel (PNS)?', 'Wat zijn neuronen en hoe werken ze?', 'Wat zijn dendrieten in een neuron?', 'Wat is de functie van het cellichaam in een neuron?', 'Wat is de functie van een axon in een neuron?', 'Wat zijn terminale knoppen in een neuron?', 'Wat is een synaps?', 'Wat betekent genexpressie?', 'Wat zijn chromosomen?', 'Wat zijn genen?', 'Wat is een dominant gen?', 'Wat is een recessief gen?', 'Wat is een genotype?', 'Wat is een fenotype?', 'Wat zijn monozygote tweelingen?', 'Wat zijn dizygote tweelingen?', 'Wat is erfelijkheid?', 'Wat is erfelijkheid?', 'Wat is epigenetica?']
answers = ['Psychologische wetenschap is de studie van geest, hersenen en gedrag door middel van onderzoek. Het omvat verschillende subvelden, waaronder neuropsychologie, ontwikkelingspsychologie en sociale psychologie.', 'Het centrale zenuwstelsel (CNS) bestaat uit de hersenen en het ruggenmerg. Het dient als het centrale punt voor het ontvangen en verzenden van signalen naar andere delen van het lichaam.', 'Het perifere zenuwstelsel (PNS) omvat alle zenuwcellen in het lichaam die niet deel uitmaken van het centrale zenuwstelsel. Het PNS bevat het somatische en autonome zenuwstelsel, dat signalen doorgeeft tussen het CNS en de rest van het lichaam.', 'Neuronen zijn de basiseenheden van het zenuwstelsel. Ze ontvangen, integreren en geven informatie door. Door elektrische impulsen en chemische signalen communiceren ze met andere neuronen en vormen ze neurale netwerken.', 'Dendrieten zijn takachtige uitlopers van een neuron die informatie van andere neuronen detecteren. Ze fungeren als antennes, het verzamelen van informatie van andere neuronen en het doorgeven aan de cellichaam.', 'Het cellichaam in een neuron is de plaats waar informatie van duizenden andere neuronen wordt verzameld en geïntegreerd. Het is de centrale hub van een neuron en essentieel voor het coördineren van de celactiviteit.', 'Een axon is een lange, smalle groei van een neuron waardoor informatie van het cellichaam naar de eindknoppen wordt geleid. Het fungeert als een informatiesnelweg, met signalen die snel langs de lengte reizen.', 'Terminale knoppen zijn kleine knobbeltjes aan de uiteinden van axonen die chemische signalen van het neuron naar de synaps vrijgeven. Ze zijn essentieel voor de communicatie tussen neuronen.', "Een synaps is de ruimte tussen het eind van een 'zenden' neuron en de dendrieten van een 'ontvangen' neuron, waar chemische communicatie plaatsvindt tussen de neuronen. Het is als een brug waarover signalen worden overgedragen tussen neuronen.", "Genexpressie verwijst naar of een specifiek gen aan of uit is. Bijvoorbeeld, als het gen voor blauwe ogen wordt 'aangezet', zal het individu blauwe ogen hebben.", 'Chromosomen zijn structuren in de cel die bestaan uit DNA, waarvan segmenten individuele genen vormen. Bij mensen bestaat elke cel gewoonlijk uit 23 paar chromosomen.', 'Genen zijn de eenheden van erfelijkheid die helpen bij het bepalen van de kenmerken van een organisme. Ze zijn als blauwdrukken die bepalen hoe een organisme zich zal ontwikkelen en functioneren.', 'Een dominant gen is een gen dat tot uiting komt in het nageslacht wanneer het aanwezig is. Bijvoorbeeld, het gen voor bruine ogen is dominant over het gen voor blauwe ogen.', 'Een recessief gen is een gen dat alleen tot uiting komt als het gepaard gaat met een soortgelijk gen van de andere ouder. Bijvoorbeeld, het gen voor blauwe ogen is recessief, dus beide ouders moeten dit gen doorgeven voor een kind om blauwe ogen te hebben.', 'Een genotype is de genetische samenstelling van een organisme, bepaald op het moment van de conceptie. Het is als de unieke genetische code die een organisme maakt tot wat het is.', 'Een fenotype zijn de waarneembare fysieke kenmerken van een organisme, die het resultaat zijn van zowel genetische als omgevingsinvloeden. Het zijn de kenmerken die we kunnen zien, zoals haarkleur, oogkleur en lengte.', 'Monozygote tweelingen, ook wel identieke tweelingen genoemd, zijn tweelingbroers of -zussen die ontstaan uit één zygoot die in twee splitst, en delen dus dezelfde genen.', 'Dizygote tweelingen, ook wel broederlijke tweelingen genoemd, zijn tweelingbroers of -zussen die ontstaan uit twee afzonderlijk bevruchte eieren en zijn genetisch gezien niet meer vergelijkbaar dan niet-tweelingbroers of -zussen.', 'Erfelijkheid is de overdracht van kenmerken van ouders op nakomelingen via genen. Bijvoorbeeld, de kleur van je ogen is een erfelijke eigenschap.', 'Erfelijkheid is een statistische schatting van de mate waarin variatie in een eigenschap binnen een populatie te wijten is aan genetica. Bijvoorbeeld, als de erfelijkheid van lengte 0.6 is, betekent dit dat 60% van de variatie in lengte binnen een populatie te wijten is aan genetische verschillen.', 'Epigenetica is de studie van hoe de omgeving genetische expressie verandert op een manier die mogelijk kan worden doorgegeven aan nakomelingen. Zo kunnen bijvoorbeeld stressvolle gebeurtenissen in het leven van een ouder epigenetische veranderingen veroorzaken die van invloed zijn op de gezondheid van hun kinderen.']

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