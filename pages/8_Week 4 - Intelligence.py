import streamlit as st
questions = ['Wat is intelligentie?', 'Wat is de mentale leeftijd?', 'Wat is het intelligentiequotiënt (IQ)?', 'Wat is algemene intelligentie (g)?', 'Wat is vloeibare intelligentie?', 'Wat is gekristalliseerde intelligentie?', 'Wat is emotionele intelligentie (EI)?', 'Wat is taal?', 'Wat zijn morfemen?', 'Wat zijn fonemen?', 'Wat is afasie?', 'Wat is het gebied van Wernicke?', 'Wat is de theorie van linguïstische relativiteit?']
answers = ['Intelligentie is het vermogen om kennis te gebruiken om te redeneren, beslissingen te nemen, complexe ideeën te begrijpen, problemen op te lossen, snel te leren en zich aan te passen aan omgevingsuitdagingen. Het is een cruciale factor voor succes in vele aspecten van het leven.', 'Mentale leeftijd is een beoordeling van het intellectuele niveau van een kind in vergelijking met leeftijdsgenoten, bepaald door de testresultaten van het kind te vergelijken met het gemiddelde voor kinderen van dezelfde chronologische leeftijd. Zo kan een kind van 10 jaar met een mentale leeftijd van 13 jaar verder gevorderd zijn dan zijn of haar leeftijdsgenoten.', 'Het IQ is een maat voor intelligentie die wordt berekend door de geschatte mentale leeftijd van een kind te delen door de chronologische leeftijd van het kind en dit getal vervolgens met 100 te vermenigvuldigen. Een IQ van 100 wordt beschouwd als gemiddeld.', 'Algemene intelligentie (g) is de theorie dat er een enkele factor is die intelligentie onderliggend bepaalt. Het is een idee dat voor het eerst werd voorgesteld door de psycholoog Charles Spearman.', 'Vloeibare intelligentie weerspiegelt het vermogen om informatie te verwerken, relaties te begrijpen en logisch na te denken, vooral in nieuwe of complexe situaties. Het is cruciaal voor het oplossen van nieuwe problemen waarvoor weinig of geen eerdere kennis vereist is.', 'Gekristalliseerde intelligentie weerspiegelt zowel de kennis die is opgedaan door ervaring als het vermogen om die kennis te gebruiken. Het omvat vaardigheden en kennis die we in de loop van de tijd hebben opgedaan, zoals woordenschat en culturele informatie.', 'Emotionele intelligentie is een type sociale intelligentie dat het beheer, de herkenning en het begrip van emoties benadrukt, en het gebruik van deze emoties om denken en handelen te sturen. Het omvat vaardigheden zoals empathie, zelfbewustzijn en emotionele regulatie.', 'Taal is een communicatiesysteem dat geluiden en symbolen gebruikt volgens grammaticale regels. Het stelt ons in staat om complexe ideeën en emoties uit te drukken en te begrijpen, en speelt een cruciale rol in menselijke interactie.', 'Morfemen zijn de kleinste betekenisdragende eenheden van taal, inclusief voor- en achtervoegsels. Bijvoorbeeld, het woord "onbreekbaar" bestaat uit de morfemen "on-", "breek" en "-baar".', 'Fonemen zijn de basisklanken van spraak en vormen de fundamenten van taal. Bijvoorbeeld, het Engelse woord "cat" heeft drie fonemen: /k/, /æ/, en /t/.', 'Afasie is een taalstoornis die leidt tot tekorten in taalbegrip en -productie, vaak als gevolg van hersenbeschadiging, zoals een beroerte.', 'Het gebied van Wernicke is een gebied waar de temporale en pariëtale lobben van de linker hersenhelft samenkomen, gerelateerd aan spraakbegrip. Schade aan dit gebied kan leiden tot Wernicke-afasie, gekenmerkt door vloeiende maar zinloze spraak.', 'De theorie van linguïstische relativiteit stelt dat taal het denken bepaalt. Bijvoorbeeld, sprekers van talen met veel woorden voor sneeuw zouden meer gedetailleerde percepties van sneeuw hebben.']

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