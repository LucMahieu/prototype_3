import streamlit as st
questions = ['Wat is psychological science?', 'Wat is het centraal zenuwstelsel (CNS)?', 'Wat is het perifere zenuwstelsel (PNS)?', 'Wat zijn neuronen?', 'Wat zijn dendrieten?']
answers = ['Psychological science is de studie van geest, hersenen en gedrag door middel van onderzoek. Het richt zich op het begrijpen van hoe deze gebieden met elkaar samenhangen.', 'Het centraal zenuwstelsel bestaat uit de hersenen en het ruggenmerg. Dit systeem speelt een cruciale rol in het verwerken van informatie van het lichaam en het bepalen van reacties.', 'Het perifere zenuwstelsel bestaat uit alle zenuwcellen in het lichaam die geen deel uitmaken van het centrale zenuwstelsel. Het omvat het somatische en autonome zenuwstelsel.', 'Neuronen zijn de basiseenheden van het zenuwstelsel en zijn cellen die informatie ontvangen, integreren en verzenden. Ze werken via elektrische impulsen, communiceren met andere neuronen via chemische signalen en vormen neurale netwerken.', "Dendrieten zijn vertakte uitlopers van neuronen die informatie detecteren van andere neuronen. Ze functioneren als de 'antennes' van de neuronen, waarbij ze signalen opvangen en doorgeven aan het cellichaam."]

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
if st.session_state.card_index <= len(questions):
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

    st.subheader(questions[st.session_state.card_index])
    if st.session_state.show_answer is True:
        st.write(answers[st.session_state.card_index])
else:
    st.subheader("You finished all the questions for this lecture.")
    # st.balloons()
    if st.button("Reset deck"):
        st.session_state.card_index = 0
        st.session_state.show_answer = False
        st.experimental_rerun()
    card_progress.progress(1)

# Update the progress bar according to the card number
card_progress.progress(st.session_state.card_index / len(questions))