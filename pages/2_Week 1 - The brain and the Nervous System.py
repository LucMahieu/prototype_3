import streamlit as st
questions = ['Wat is een actiepotentiaal?', 'Wat is de rustmembraanpotentiaal van een neuron?', 'Wat is de relatieve refractaire periode?', 'Wat houdt het alles-of-niets-principe in bij neurale activiteit?', ]
answers = ['Een actiepotentiaal is het elektrische signaal dat langs het axon gaat en uiteindelijk zorgt voor de afgifte van chemicaliën uit de terminale knoppen. Het is als een elektrische golf die langs het axon reist, waardoor naastgelegen ionkanalen openen en weer sluiten in een golvende reeks.','De rustmembraanpotentiaal verwijst naar de elektrische lading van een neuron wanneer het niet actief is, typisch -70 millivolt. Bijvoorbeeld, in een gepolariseerde toestand heeft het neuron meer negatieve ionen binnenin dan erbuiten, wat zorgt voor de elektrische energie die nodig is om het neuron te laten vuren.', 'De relatieve refractaire periode is een kort tijdsbestek na een actiepotentiaal waarin de membraanpotentiaal van een neuron hypergepolariseerd is, ofwel meer negatief, waardoor het moeilijker wordt om opnieuw te vuren. Dit betekent dat meer excitatoire input nodig zou zijn om een nieuw actiepotentiaal te triggeren.', 'Het alles-of-niets-principe stelt dat wanneer een neuron vuurt, het elke keer met dezelfde potentie vuurt; een neuron vuurt of niet, hoewel de vuurfrequentie kan variëren. Dus, ongeacht de sterkte van de stimulatie, zal de sterkte van het vuren elke keer hetzelfde zijn.']

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
if st.session_state.card_index < len(questions) - 1:
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