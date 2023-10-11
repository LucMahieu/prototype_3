import streamlit as st
questions = ['Wat is het begrip bewustzijn?', 'Wat is change blindness?', 'Wat is endogene aandacht?', 'Wat is exogene aandacht?', 'Wat is priming?', 'Wat is subliminale perceptie?', 'Wat is meditatie?', 'Wat is hypnose?', 'Wat zijn circadiane ritmes?', 'Wat is REM-slaap?', 'Wat zijn dromen?', 'Wat is de activatie-synthese hypothese?', 'Wat is slapeloosheid?', 'Wat is obstructieve slaapapneu?', 'Wat is narcolepsie?']
answers = ['Bewustzijn verwijst naar iemands moment-tot-moment subjectieve ervaring van de wereld. Het omvat alles waar je je op een bepaald moment bewust van bent.', 'Change blindness is het onvermogen om grote veranderingen in je omgeving op te merken. Het gebeurt bijvoorbeeld wanneer je niet merkt dat een vriend een nieuwe bril draagt.', 'Endogene aandacht is de vrijwillige richting van onze aandacht, zoals wanneer je je concentreert op het lezen van een boek.', 'Exogene aandacht is de aandacht die onvrijwillig wordt geleid door een stimulus, zoals wanneer een plotselinge harde knal je aandacht trekt.', 'Priming is een versnelling van de reactie op een stimulus door recente ervaring met die stimulus of een gerelateerde stimulus. Bijvoorbeeld, na het zien van het woord "geel", ben je sneller geneigd om "banaan" te herkennen.', 'Subliminale perceptie is de verwerking van informatie door zintuiglijke systemen zonder bewuste waarneming. Bijvoorbeeld, je zou een bericht kunnen verwerken van een reclame die te snel flitst om bewust waar te nemen.', 'Meditatie is een mentale procedure die de aandacht richt op een extern object, een intern evenement, of een gevoel van bewustzijn. Het wordt vaak gebruikt voor ontspanning en stressvermindering.', 'Hypnose is een sociale interactie waarbij een persoon, reagerend op suggesties, veranderingen ervaart in geheugen, perceptie en/of vrijwillige actie. Het wordt soms gebruikt in therapeutische situaties.', "Circadiane ritmes zijn biologische patronen die zich op regelmatige tijdstippen voordoen, afhankelijk van het tijdstip van de dag. Bijvoorbeeld, het slaap-waakritme dat ons helpt om 's nachts te slapen en overdag wakker te zijn.", 'REM-slaap is een slaapfase gekenmerkt door snelle oogbewegingen, verlamming van de motorische systemen en dromen. Het is in deze fase dat de meest levendige dromen vaak optreden.', 'Dromen zijn producten van een veranderde bewustzijnstoestand waarin beelden en fantasieën worden verward met de realiteit. Een droom kan ervaren worden als een werkelijke gebeurtenis, hoewel deze slechts in de geest plaatsvindt.', 'De activatie-synthese hypothese stelt dat de hersenen proberen om willekeurige hersenactiviteit die tijdens de slaap optreedt, te interpreteren door deze te combineren met opgeslagen herinneringen. Hierdoor ontstaan dromen.', 'Insomnie is een slaapstoornis gekenmerkt door een onvermogen om te slapen, wat significante problemen veroorzaakt in het dagelijks leven. Het kan bijvoorbeeld leiden tot vermoeidheid overdag en verminderde concentratie.', 'Obstructieve slaapapneu is een stoornis waarbij mensen tijdens het slapen stoppen met ademen omdat hun keel sluit, wat resulteert in frequent ontwaken tijdens de nacht. Dit kan leiden tot ernstige vermoeidheid overdag en andere gezondheidsproblemen.', 'Narcolepsie is een slaapstoornis waarbij mensen overdag overmatige slaperigheid ervaren, soms zelfs slap worden en ineenzakken. Het is alsof de REM-slaap op ongepaste tijden optreedt.']

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