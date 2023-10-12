import streamlit as st
questions = ['Wat is cognitie?', 'Wat is denken in psychologische termen?', 'Wat zijn analoge representaties?', 'Wat zijn symbolische representaties?', 'Wat is een concept?', 'Wat is het prototype-model?', 'Wat is het exemplar-model?', 'Wat is een script in psychologische termen?', 'Wat zijn stereotypes?']
answers = ['Cognitie verwijst naar mentale activiteiten zoals denken en het begrijpen dat voortkomt uit denken. Het omvat processen zoals leren, geheugen, aandacht en probleemoplossing.', 'Denken is het mentaal manipuleren van kennisrepresentaties over de wereld. Het kan letterlijk worden gezien als het "praten met onszelf" in onze geest.', 'Analoge representaties zijn mentale representaties die enkele van de fysieke kenmerken van de objecten die ze representeren bezitten. Een mentaal beeld van een appel, waarbij je de vorm en kleur voorstelt, is een voorbeeld van een analoge representatie.', 'Symbolische representaties zijn abstracte mentale representaties die niet overeenkomen met de fysieke kenmerken van objecten of ideeën. Het woord "appel" dat een fysieke appel representeert, is een voorbeeld van een symbolische representatie.', 'Een concept is een categorie of klasse van gerelateerde items, waarbij mentale representaties van die items betrokken zijn. Het concept "fruit" bevat bijvoorbeeld items zoals appels, peren en bananen.', 'Het prototype-model is een theorie die stelt dat er binnen elke categorie een standaardvoorbeeld of prototype is dat de meest typische kenmerken van die categorie belichaamt. Bijvoorbeeld, voor de categorie "vogels" zou de roodborst een typisch prototype kunnen zijn.', 'Het exemplar-model is een model waarbij alle leden van een categorie voorbeelden (exemplaren) zijn en samen het concept vormen en de lidmaatschap van de categorie bepalen. In dit model zou elke individuele vogel die je hebt gezien bijdragen aan je begrip van de categorie "vogels".', "Een script is een schema dat gedrag en verwachtingen over tijd binnen een bepaalde situatie stuurt. Bijvoorbeeld, het script voor naar een restaurant gaan zou kunnen bevatten: een tafel zoeken, menu's ontvangen, eten bestellen, eten, betalen en vertrekken.", 'Stereotypes zijn cognitieve schema\'s die snelle en efficiënte informatie verwerking over mensen mogelijk maken op basis van hun lidmaatschap in bepaalde groepen. Bijvoorbeeld, het idee dat "alle Nederlanders houden van fietsen" is een stereotype.']

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