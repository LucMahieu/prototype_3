import streamlit as st
questions = ['Wat is psychotherapie?', 'Wat zijn biologische therapieën?', 'Wat is psychodynamische therapie?', 'Wat is gedragstherapie?', 'Wat is "exposure" in de context van gedragstherapie?', 'Wat is cognitieve therapie?', 'Wat is cognitieve herstructurering?', 'Wat is cognitieve-gedragstherapie (CBT)?', 'Wat is client-centered therapie?', 'Wat zijn psychotrope medicijnen?', 'Wat zijn antianxiety drugs?', 'Wat zijn antidepressiva?', 'Wat zijn antipsychotica?', 'Wat is electroconvulsive therapie (ECT)?', 'Wat is het placebo-effect?', 'Wat is reflectief luisteren?', 'Wat is de systeembenadering?', 'Wat houdt hersenchirurgie als behandeling voor stoornissen in?', 'Wat zijn alternatieve biologische behandelingen voor psychologische stoornissen?', 'Wat is transcraniële magnetische stimulatie (TMS)?', 'Wat is diepe hersenstimulatie (DBS)?', 'Wat zijn de meest typische medicijnen voor bipolaire stoornis?']
answers = ['Psychotherapie is een formele psychologische behandeling die gericht is op het aanpakken van geestelijke gezondheidsproblemen. Dit kan bijvoorbeeld gesprekstherapie of cognitieve gedragstherapie omvatten.', 'Biologische therapieën zijn behandelingen voor psychische stoornissen die zijn gebaseerd op medische benaderingen van ziekten en aandoeningen. Een voorbeeld hiervan kan medicatie of elektroconvulsietherapie zijn.', 'Psychodynamische therapie is een therapie gebaseerd op Freudiaanse theorie, gericht op het begrijpen van onderliggende behoeften, verdedigingsmechanismen en drijfveren. Het kan bijvoorbeeld helpen bij het onbewuste conflict van een patiënt aan het licht te brengen.', 'Gedragstherapie is een behandeling gericht op het afleren van gedragingen door klassieke en operante conditionering. Een voorbeeld hiervan kan zijn het trainen van een kind om ongewenst gedrag te stoppen door middel van beloning en straf.', 'Exposure is een techniek in gedragstherapie waarbij herhaalde blootstelling aan een angstwekkende prikkel of situatie plaatsvindt. Het wordt vaak gebruikt om fobieën en angststoornissen te behandelen.', 'Cognitieve therapie is een behandeling die zich richt op het veranderen van vervormde gedachten die maladaptieve gedragingen en emoties produceren. Het wordt vaak gebruikt om depressie en angststoornissen te behandelen.', 'Cognitieve herstructurering is een therapeutische aanpak gericht op het helpen van cliënten bij het herkennen en veranderen van maladaptieve denkpatronen. Dit kan bijvoorbeeld helpen bij het aanpakken van negatieve zelfpraat.', 'Cognitieve-gedragstherapie is een therapie die technieken uit de cognitieve en gedragstherapie integreert om foutief denken te corrigeren en maladaptief gedrag te veranderen. Het wordt vaak gezien als een van de meest effectieve vormen van psychotherapie.', 'Client-centered therapie is een empathische benadering van therapie die zelfbegrip en persoonlijke groei aanmoedigt. Het is ontwikkeld door Carl Rogers en legt de nadruk op de ervaringen en gevoelens van de cliënt.', 'Psychotrope medicijnen zijn geneesmiddelen die mentale processen beïnvloeden en symptomen van psychologische stoornissen verlichten. Voorbeelden zijn antidepressiva en antipsychotica.', 'Antianxiety drugs zijn psychotrope medicijnen die worden gebruikt voor de behandeling van angst. Een voorbeeld is benzodiazepine, dat kalmerend werkt.', 'Antidepressiva zijn psychotrope medicijnen die worden gebruikt voor de behandeling van depressie. Ze werken door de balans van bepaalde chemische stoffen in de hersenen te herstellen, zoals serotonine.', 'Antipsychotica zijn psychotrope medicijnen die worden gebruikt voor de behandeling van schizofrenie en andere stoornissen met psychosen. Ze kunnen hallucinaties, waanideeën en andere symptomen verminderen.', 'Electroconvulsive therapie (ECT) is een behandeling waarbij een elektrische stroom door de hersenen wordt gestuurd om een \u200b\u200bepileptische aanval op te wekken. Het wordt soms gebruikt bij ernstige gevallen van depressie die niet reageren op andere behandelingen.', 'Het placebo-effect is de verbetering in gezondheid na behandeling met een placebo, een middel zonder actieve component voor de aandoening die wordt behandeld. Dit effect laat zien hoe krachtig de verwachtingen en overtuigingen van een persoon kunnen zijn in de genezing.', 'Reflectief luisteren is een techniek die gebruikt wordt in humanistische behandelmethoden, waarbij de therapeut luistert naar de cliënt en vervolgens de zorgen van de cliënt herhaalt om de cliënt te helpen zijn of haar gevoelens te verduidelijken.', 'Volgens de systeembenadering is een individu een deel van een grotere context en elke verandering in het gedrag van een individu zal het hele systeem beïnvloeden. Bijvoorbeeld, een alcoholist die stopt met drinken kan andere gezinsleden beginnen te bekritiseren wanneer zij drinken, wat de gezinsdynamiek kan veranderen.', 'Hersenchirurgie wordt soms gebruikt bij de behandeling van stoornissen, maar het betreft kleine hersengebieden en wordt meestal alleen als laatste redmiddel gebruikt.', 'Alternatieve biologische behandelingen voor psychologische stoornissen proberen de hersenactiviteit te veranderen om symptomen te beheersen. Voorbeelden hiervan zijn elektroconvulsieve therapie (ECT), transcraniële magnetische stimulatie (TMS) en diepe hersenstimulatie (DBS).', 'Bij TMS wordt een krachtige elektrische stroom door een spoel geleid, waardoor een magnetisch veld ontstaat dat ongeveer 40.000 keer sterker is dan het aardmagnetisch veld. Dit magnetisch veld induceert een elektrische stroom in het hersengebied direct onder de spoel, waardoor de neuronale functie in dat gebied wordt onderbroken.', 'DBS is een techniek waarbij elektroden chirurgisch worden geïmplanteerd in de hersenen. Mild elektriciteit wordt dan gebruikt om de hersenen te stimuleren op een optimale frequentie en intensiteit, vergelijkbaar met een pacemaker die het hart stimuleert. DBS wordt voornamelijk gebruikt om ernstige depressie te behandelen.', 'Stemmingsstabilisatoren, vooral lithium, en atypische antipsychotica zijn de meest effectieve behandelingen voor bipolaire stoornis. Ze beheersen manische symptomen beter dan depressieve symptomen.']


def change_card_index(index):
    # Select first element and re-insert at index
    st.session_state.questions.insert(index, st.session_state.questions[0])
    st.session_state.answers.insert(index, st.session_state.answers[0])

    # Delete the first duplicate card
    del st.session_state.questions[0]
    del st.session_state.answers[0]

    return


def evaluate_graduation(current_card):
    if current_card in st.session_state.easy_count:
        st.session_state.easy_count[current_card] += 1
    else:
        st.session_state.easy_count[current_card] = 1

    # Delete card if graduated
    if st.session_state.easy_count[current_card] >= 2:
        del st.session_state.questions[0]
        del st.session_state.answers[0]
    else:
        change_card_index(20)

    return


def reset_easy_count(current_card):
    st.session_state.easy_count[current_card] = 0


# -------------------------SESSION STATES----------------------------- #

if 'easy_count' not in st.session_state:
    st.session_state.easy_count = {}

if 'questions' not in st.session_state:
    st.session_state.questions = None

if 'answers' not in st.session_state:
    st.session_state.answers = None

if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False

if 'previous_page_name' not in st.session_state:
    st.session_state.previous_page_name = None

if 'current_page_name' not in st.session_state:
    st.session_state.current_page_name = __file__

# -------------------------------MAIN---------------------------------- #


def initialise_new_page():
    st.session_state.questions = questions.copy()
    st.session_state.answers = answers.copy()
    st.session_state.easy_count = {}
    return


# Read and store current file name
st.session_state.current_page_name = __file__

# Check if a new page is opened
if st.session_state.current_page_name != st.session_state.previous_page_name:
    # Change lists in session state with current week lists
    initialise_new_page()
    st.session_state.previous_page_name = st.session_state.current_page_name


card_progress = st.progress(0)
main_container = st.container()

with main_container:
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Easy', use_container_width=True):
            # Count executive times the user found current card easy
            evaluate_graduation(st.session_state.questions[0])
            st.session_state.show_answer = False

    with col2:
        if st.button('Medium', use_container_width=True):
            st.session_state.show_answer = False
            reset_easy_count(st.session_state.questions[0])
            change_card_index(5)

    with col3:
        if st.button('Hard', use_container_width=True):
            st.session_state.show_answer = False
            reset_easy_count(st.session_state.questions[0])
            change_card_index(2)


if st.button('Show Answer', use_container_width=True):
    st.session_state.show_answer = not st.session_state.show_answer

if len(st.session_state.questions) == 0:
    st.session_state.questions = questions.copy()
    st.session_state.answers = answers.copy()
    st.session_state.easy_count = {}

st.subheader(st.session_state.questions[0])
if st.session_state.show_answer:
    st.write(st.session_state.answers[0])

card_progress.progress(int(sum(st.session_state.easy_count.values()) / (2 * len(questions)) * 100))