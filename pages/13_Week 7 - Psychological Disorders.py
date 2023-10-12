import streamlit as st
questions = ['Wat is psychopathologie?', 'Wat betekent etiologie in de context van psychologie?', 'Wat is het Research Domain Criteria (RDoC) model?', "Wat houdt een 'assessment' in binnen de psychologie?", 'Wat is het diathese-stress model?', 'Wat is het family systems model?', 'Wat is het socioculturele model?', 'Wat is de cognitief-gedragsmatige benadering?', 'Wat zijn angststoornissen?', 'Wat is gegeneraliseerde angststoornis (GAD)?', 'Wat is agorafobie?', 'Wat is een ernstige depressieve stoornis?', 'Wat is aanhoudende depressieve stoornis?', 'Wat is aangeleerde hulpeloosheid?', 'Wat is bipolaire I-stoornis?', 'Wat is bipolaire II-stoornis?', 'Wat is schizofrenie?', 'Wat zijn delusies?', 'Wat zijn hallucinaties?', 'Wat is gedesorganiseerde spraak?', 'Wat is gedesorganiseerd gedrag?', 'Wat zijn negatieve symptomen?', 'Wat is een obsessief-compulsieve stoornis (OCD)?', 'Wat is anorexia nervosa?', 'Wat is bulimia nervosa?', 'Wat is een binge-eating disorder?']
answers = ['Psychopathologie verwijst naar ziektes of stoornissen van de geest, ook wel psychologische stoornissen genoemd. Dit kan variëren van depressie en angststoornissen tot schizofrenie en bipolaire stoornis.', 'Etiologie in de psychologie heeft betrekking op de factoren die bijdragen aan de ontwikkeling van een stoornis. Dit kan genetische predisposities, omgevingsinvloeden of traumatische gebeurtenissen omvatten.', 'Het RDoC is een methode die basisaspecten van functioneren definieert en deze overweegt op meerdere niveaus van analyse, van genen tot hersensystemen tot gedrag. Het wordt vaak gebruikt in onderzoek naar psychische aandoeningen.', "Een 'assessment' in de psychologie is een onderzoek naar de cognitieve, gedragsmatige of emotionele functies van een persoon om mogelijke psychologische stoornissen te diagnosticeren. Dit kan gesprekken, tests of observaties omvatten.", 'Het diathese-stress model is een diagnosemodel dat stelt dat een stoornis kan ontstaan wanneer een onderliggende kwetsbaarheid gekoppeld wordt aan een uitlokkende gebeurtenis. Bijvoorbeeld een persoon met een genetische kwetsbaarheid voor depressie die een zware levensgebeurtenis doormaakt.', 'Het family systems model is een diagnosemodel dat problemen binnen een individu ziet als een indicatie van problemen binnen de familie. Het is gebaseerd op de gedachte dat familiesystemen een grote invloed hebben op het welzijn van de individuele leden.', 'Het socioculturele model is een diagnosemodel dat psychopathologie ziet als het resultaat van de interactie tussen individuen en hun culturen. Hierbij wordt rekening gehouden met culturele normen, waarden en verwachtingen.', 'De cognitief-gedragsmatige benadering is een diagnosemodel dat psychopathologie ziet als het resultaat van aangeleerde, onaangepaste gedachten en overtuigingen. Cognitieve gedragstherapie is een veelgebruikte behandelmethode binnen dit model.', 'Angststoornissen zijn psychologische aandoeningen die gekenmerkt worden door overmatige angst en vrees, zelfs als er geen echt gevaar aanwezig is. Een voorbeeld hiervan is paniekstoornis, waarbij iemand terugkerende en onverwachte paniekaanvallen heeft.', 'Gegeneraliseerde angststoornis is een constante staat van angst die niet gekoppeld is aan een specifiek object of gebeurtenis. Mensen met GAD maken zich vaak overmatig zorgen over alledaagse dingen.', 'Agorafobie is een angststoornis waarbij men bang is voor situaties waaruit ontsnappen moeilijk of onmogelijk kan zijn. Mensen met agorafobie vermijden vaak plaatsen zoals winkelcentra of openbare vervoermiddelen.', 'Ernstige depressieve stoornis is een aandoening die gekenmerkt wordt door ernstige negatieve stemmingen of een gebrek aan interesse in normaal gesproken plezierige activiteiten. Dit wordt ook wel klinische depressie genoemd.', 'Aanhoudende depressieve stoornis is een vorm van depressie die minder ernstig is dan een ernstige depressieve stoornis, maar langer duurt. Deze aandoening wordt ook wel dysthymie genoemd.', 'Aangeleerde hulpeloosheid is een cognitief model van depressie waarbij mensen zich niet in staat voelen om gebeurtenissen in hun leven te beïnvloeden. Dit kan leiden tot gevoelens van machteloosheid en hopeloosheid.', 'Bipolaire I-stoornis is een aandoening die gekenmerkt wordt door extreem verhoogde stemmingen tijdens manische episodes en vaak ook door depressieve episodes. Tijdens een manische episode kan iemand zich bijvoorbeeld ongewoon energiek, vrolijk of prikkelbaar voelen.', 'Bipolaire II-stoornis is een aandoening die gekenmerkt wordt door afwisselende periodes van extreem depressieve en mild verhoogde stemmingen. Het belangrijkste verschil met bipolaire I-stoornis is dat de manische episodes niet zo extreem zijn.', 'Schizofrenie is een psychische stoornis die gekenmerkt wordt door veranderingen in gedachten, waarnemingen of bewustzijn, wat resulteert in psychose. Het kan bijvoorbeeld leiden tot hallucinaties of delusies.', 'Delusies zijn valse overtuigingen gebaseerd op verkeerde interpretaties van de realiteit. Bijvoorbeeld, iemand kan geloven dat ze constant in de gaten worden gehouden, ondanks dat er geen bewijs voor is.', 'Hallucinaties zijn valse zintuiglijke waarnemingen die worden ervaren zonder een externe bron. Iemand kan bijvoorbeeld stemmen horen die er niet zijn.', 'Gedesorganiseerde spraak betreft incoherente spraakpatronen die vaak wisselen van onderwerp en vreemde of ongepaste dingen uiten. Een persoon kan bijvoorbeeld beginnen over het weer en abrupt overschakelen naar een heel ander onderwerp.', 'Gedesorganiseerd gedrag omvat vreemd of ongebruikelijk gedrag, zoals vreemde bewegingen van ledematen, bizarre spraak of ongepast zelfzorg, zoals niet goed aankleden of zichzelf niet wassen.', 'Negatieve symptomen zijn kenmerken van schizofrenie die worden gekenmerkt door tekorten in functioneren, zoals apathie, gebrek aan emotie, en vertraagde spraak en beweging. Iemand kan bijvoorbeeld moeite hebben om motivatie te vinden voor dagelijkse activiteiten.', 'Een obsessief-compulsieve stoornis (OCD) is een stoornis die gekenmerkt wordt door frequente opdringerige gedachten en dwangmatige handelingen. Bijvoorbeeld, iemand kan het gevoel hebben dat ze hun handen voortdurend moeten wassen, zelfs als ze weten dat ze niet vuil zijn.', 'Anorexia nervosa is een eetstoornis gekenmerkt door een excessieve angst om dik te worden en dus het beperken van energie-inname om een significant laag lichaamsgewicht te bereiken. Een persoon kan bijvoorbeeld zelfs bij ernstig ondergewicht nog steeds het gevoel hebben dat ze moeten afvallen.', 'Bulimia nervosa is een eetstoornis die zich kenmerkt door een cyclus van diëten, eetaanvallen, en zuiveren (zelf-opgewekt braken). Het is een ernstige psychische aandoening die zowel fysieke als psychologische schade kan veroorzaken.', 'Een binge-eating disorder is een eetstoornis die wordt gekenmerkt door eetaanvallen die ernstige stress veroorzaken. Het verschilt van bulimia nervosa in die zin dat er geen zuiveringsgedrag plaatsvindt na de eetaanvallen.']

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