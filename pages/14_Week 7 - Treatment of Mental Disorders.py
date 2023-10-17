import streamlit as st
questions = ['Wat is psychotherapie?', 'Wat zijn biologische therapieën?', 'Wat is psychodynamische therapie?', 'Wat is gedragstherapie?', 'Wat is "exposure" in de context van gedragstherapie?', 'Wat is cognitieve therapie?', 'Wat is cognitieve herstructurering?', 'Wat is cognitieve-gedragstherapie (CBT)?', 'Wat is client-centered therapie?', 'Wat zijn psychotrope medicijnen?', 'Wat zijn antianxiety drugs?', 'Wat zijn antidepressiva?', 'Wat zijn antipsychotica?', 'Wat is electroconvulsive therapie (ECT)?', 'Wat is het placebo-effect?', 'Wat is reflectief luisteren?', 'Wat is de systeembenadering?', 'Wat houdt hersenchirurgie als behandeling voor stoornissen in?', 'Wat zijn alternatieve biologische behandelingen voor psychologische stoornissen?', 'Wat is transcraniële magnetische stimulatie (TMS)?', 'Wat is diepe hersenstimulatie (DBS)?', 'Wat zijn de meest typische medicijnen voor bipolaire stoornis?', 'Wat is de algemene prognose voor antisociale persoonlijkheidsstoornis?']
answers = ['Psychotherapie is een formele psychologische behandeling die gericht is op het aanpakken van geestelijke gezondheidsproblemen. Dit kan bijvoorbeeld gesprekstherapie of cognitieve gedragstherapie omvatten.', 'Biologische therapieën zijn behandelingen voor psychische stoornissen die zijn gebaseerd op medische benaderingen van ziekten en aandoeningen. Een voorbeeld hiervan kan medicatie of elektroconvulsietherapie zijn.', 'Psychodynamische therapie is een therapie gebaseerd op Freudiaanse theorie, gericht op het begrijpen van onderliggende behoeften, verdedigingsmechanismen en drijfveren. Het kan bijvoorbeeld helpen bij het onbewuste conflict van een patiënt aan het licht te brengen.', 'Gedragstherapie is een behandeling gericht op het afleren van gedragingen door klassieke en operante conditionering. Een voorbeeld hiervan kan zijn het trainen van een kind om ongewenst gedrag te stoppen door middel van beloning en straf.', 'Exposure is een techniek in gedragstherapie waarbij herhaalde blootstelling aan een angstwekkende prikkel of situatie plaatsvindt. Het wordt vaak gebruikt om fobieën en angststoornissen te behandelen.', 'Cognitieve therapie is een behandeling die zich richt op het veranderen van vervormde gedachten die maladaptieve gedragingen en emoties produceren. Het wordt vaak gebruikt om depressie en angststoornissen te behandelen.', 'Cognitieve herstructurering is een therapeutische aanpak gericht op het helpen van cliënten bij het herkennen en veranderen van maladaptieve denkpatronen. Dit kan bijvoorbeeld helpen bij het aanpakken van negatieve zelfpraat.', 'Cognitieve-gedragstherapie is een therapie die technieken uit de cognitieve en gedragstherapie integreert om foutief denken te corrigeren en maladaptief gedrag te veranderen. Het wordt vaak gezien als een van de meest effectieve vormen van psychotherapie.', 'Client-centered therapie is een empathische benadering van therapie die zelfbegrip en persoonlijke groei aanmoedigt. Het is ontwikkeld door Carl Rogers en legt de nadruk op de ervaringen en gevoelens van de cliënt.', 'Psychotrope medicijnen zijn geneesmiddelen die mentale processen beïnvloeden en symptomen van psychologische stoornissen verlichten. Voorbeelden zijn antidepressiva en antipsychotica.', 'Antianxiety drugs zijn psychotrope medicijnen die worden gebruikt voor de behandeling van angst. Een voorbeeld is benzodiazepine, dat kalmerend werkt.', 'Antidepressiva zijn psychotrope medicijnen die worden gebruikt voor de behandeling van depressie. Ze werken door de balans van bepaalde chemische stoffen in de hersenen te herstellen, zoals serotonine.', 'Antipsychotica zijn psychotrope medicijnen die worden gebruikt voor de behandeling van schizofrenie en andere stoornissen met psychosen. Ze kunnen hallucinaties, waanideeën en andere symptomen verminderen.', 'Electroconvulsive therapie (ECT) is een behandeling waarbij een elektrische stroom door de hersenen wordt gestuurd om een \u200b\u200bepileptische aanval op te wekken. Het wordt soms gebruikt bij ernstige gevallen van depressie die niet reageren op andere behandelingen.', 'Het placebo-effect is de verbetering in gezondheid na behandeling met een placebo, een middel zonder actieve component voor de aandoening die wordt behandeld. Dit effect laat zien hoe krachtig de verwachtingen en overtuigingen van een persoon kunnen zijn in de genezing.', 'Reflectief luisteren is een techniek die gebruikt wordt in humanistische behandelmethoden, waarbij de therapeut luistert naar de cliënt en vervolgens de zorgen van de cliënt herhaalt om de cliënt te helpen zijn of haar gevoelens te verduidelijken.', 'Volgens de systeembenadering is een individu een deel van een grotere context en elke verandering in het gedrag van een individu zal het hele systeem beïnvloeden. Bijvoorbeeld, een alcoholist die stopt met drinken kan andere gezinsleden beginnen te bekritiseren wanneer zij drinken, wat de gezinsdynamiek kan veranderen.', 'Hersenchirurgie wordt soms gebruikt bij de behandeling van stoornissen, maar het betreft kleine hersengebieden en wordt meestal alleen als laatste redmiddel gebruikt.', 'Alternatieve biologische behandelingen voor psychologische stoornissen proberen de hersenactiviteit te veranderen om symptomen te beheersen. Voorbeelden hiervan zijn elektroconvulsieve therapie (ECT), transcraniële magnetische stimulatie (TMS) en diepe hersenstimulatie (DBS).', 'Bij TMS wordt een krachtige elektrische stroom door een spoel geleid, waardoor een magnetisch veld ontstaat dat ongeveer 40.000 keer sterker is dan het aardmagnetisch veld. Dit magnetisch veld induceert een elektrische stroom in het hersengebied direct onder de spoel, waardoor de neuronale functie in dat gebied wordt onderbroken.', 'DBS is een techniek waarbij elektroden chirurgisch worden geïmplanteerd in de hersenen. Mild elektriciteit wordt dan gebruikt om de hersenen te stimuleren op een optimale frequentie en intensiteit, vergelijkbaar met een pacemaker die het hart stimuleert. DBS wordt voornamelijk gebruikt om ernstige depressie te behandelen.', 'Stemmingsstabilisatoren, vooral lithium, en atypische antipsychotica zijn de meest effectieve behandelingen voor bipolaire stoornis. Ze beheersen manische symptomen beter dan depressieve symptomen.', 'Er zijn weinig therapieën die werken voor mensen met antisociale persoonlijkheidsstoornis, maar de meeste mensen met deze stoornis vertonen een vermindering van antisociaal gedrag na ongeveer 40 jaar.']

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