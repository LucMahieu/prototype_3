import streamlit as st

solid_list_questions = ['Wat is psychologische wetenschap?', 'Wat is het centrale zenuwstelsel (CNS)?', 'Wat is het perifere zenuwstelsel (PNS)?', 'Wat zijn neuronen en hoe werken ze?', 'Wat zijn dendrieten van een neuron?', 'Wat is de functie van het cellichaam in een neuron?', 'Wat is de functie van een axon in een neuron?', 'Wat zijn terminale knoppen in een neuron?', 'Wat is een synaps?', 'Wat betekent genexpressie?', 'Wat zijn chromosomen?', 'Wat zijn genen?', 'Wat is een dominant gen?', 'Wat is een recessief gen?', 'Wat is een genotype?', 'Wat is een fenotype?', 'Wat zijn monozygote tweelingen?', 'Wat zijn dizygote tweelingen?', 'Wat is erfelijkheid (heredity)?', 'Wat is heritability?', 'Wat is epigenetica?', 'Wat is een polypeptide?', 'Wat zijn eiwitten en wat doen ze?', 'Wat is selective breeding?', 'Wat zijn polygenetische genen?', 'Wat is een zygote?', 'Wat is genetische variatie?', 'Wat is celdeling?', 'Wat zijn mutaties?', 'Wat is Behavioral genetics?', 'Wat zijn Adoption studies?', 'Wat is de betekenis van variation in genetica?', 'Wat is het MAOA-gen?', 'Wat zijn genetic modifications?', 'Wat is optogenetics?']
solid_list_answers = ['Psychologische wetenschap is de studie van geest, hersenen en gedrag door middel van onderzoek. Het omvat verschillende subvelden, waaronder neuropsychologie, ontwikkelingspsychologie en sociale psychologie.', 'Het centrale zenuwstelsel (CNS) bestaat uit de hersenen en het ruggenmerg. Het dient als het centrale punt voor het ontvangen en verzenden van signalen naar andere delen van het lichaam.', 'Het perifere zenuwstelsel (PNS) omvat alle zenuwcellen in het lichaam die niet deel uitmaken van het centrale zenuwstelsel. Het PNS bevat het somatische en autonome zenuwstelsel, dat signalen doorgeeft tussen het CNS en de rest van het lichaam.', 'Neuronen zijn de basiseenheden van het zenuwstelsel. Ze ontvangen, integreren en geven informatie door. Door elektrische impulsen en chemische signalen communiceren ze met andere neuronen en vormen ze neurale netwerken.', 'Dendrieten zijn takachtige uitlopers van een neuron die informatie van andere neuronen detecteren. Ze fungeren als antennes, het verzamelen van informatie van andere neuronen en het doorgeven aan de cellichaam.', 'Het cellichaam in een neuron is de plaats waar informatie van duizenden andere neuronen wordt verzameld en geïntegreerd. Het is de centrale hub van een neuron en essentieel voor het coördineren van de celactiviteit.', 'Een axon is een lang, smal deel van een neuron waardoor informatie van het cellichaam naar de eindknoppen wordt geleid. Het fungeert als een informatiesnelweg, met signalen die snel langs de lengte reizen.', 'Terminale knoppen zijn kleine knobbeltjes aan de uiteinden van axonen die chemische signalen van het neuron naar de synaps vrijgeven. Ze zijn essentieel voor de communicatie tussen neuronen.', "Een synaps is de ruimte tussen het eind van een verzendende neuron en de dendrieten van een ontvangende neuron, waar chemische communicatie plaatsvindt tussen de neuronen. Het is als een brug waarover signalen worden overgedragen tussen neuronen.", "Genexpressie verwijst naar of een specifiek gen aan of uit is. Bijvoorbeeld, als het gen voor blauwe ogen wordt 'aangezet', zal het individu blauwe ogen hebben.", 'Chromosomen zijn structuren in de cel die bestaan uit DNA, waarvan segmenten individuele genen vormen. Bij mensen bestaat elke cel gewoonlijk uit 23 paar chromosomen.', 'Genen zijn de eenheden van erfelijkheid die helpen bij het bepalen van de kenmerken van een organisme. Ze zijn als blauwdrukken die bepalen hoe een organisme zich zal ontwikkelen en functioneren.', 'Een dominant gen is een gen dat tot uiting komt in het nageslacht wanneer het aanwezig is. Bijvoorbeeld, het gen voor bruine ogen is dominant over het gen voor blauwe ogen.', 'Een recessief gen is een gen dat alleen tot uiting komt als het gepaard gaat met een soortgelijk gen van de andere ouder. Bijvoorbeeld, het gen voor blauwe ogen is recessief, dus beide ouders moeten dit gen doorgeven voor een kind om blauwe ogen te hebben.', 'Een genotype is de genetische samenstelling van een organisme, bepaald op het moment van de conceptie. Het is als de unieke genetische code die een organisme maakt tot wat het is.', 'Een fenotype zijn de waarneembare fysieke kenmerken van een organisme, die het resultaat zijn van zowel genetische als omgevingsinvloeden. Fenotype = genotype + omgeving. Het zijn de kenmerken die we kunnen zien, zoals haarkleur, oogkleur maar ook tatoeages. Oogkleur is bijvoorbeeld voor vrijwel 100% bepaald door het genotype en vrijwel 0% omgeving.', 'Monozygote tweelingen, ook wel identieke tweelingen genoemd, zijn tweelingbroers of -zussen die ontstaan uit één zygoot die in twee splitst, en delen dus dezelfde genen.', 'Dizygote tweelingen, ook wel twee-eiige tweeling genoemd, zijn tweelingbroers of -zussen die ontstaan uit twee afzonderlijk bevruchte eieren en hebben evenveel erfelijke verschillen in DNA als normale broers of zussen.', 'Erfelijkheid is de overdracht van kenmerken van ouders op nakomelingen via genen. Bijvoorbeeld, de kleur van je ogen is een erfelijke eigenschap.', 'Erfelijkheid is een statistische schatting van de mate waarin variatie in een eigenschap binnen een populatie te wijten is aan genetica. Bijvoorbeeld, als de erfelijkheid van lengte 0.6 is, betekent dit dat 60% van de variatie in lengte binnen een populatie te wijten is aan genetische verschillen.', 'Epigenetica is de studie van hoe de omgeving genetische expressie verandert op een manier die mogelijk kan worden doorgegeven aan nakomelingen. Zo kunnen bijvoorbeeld stressvolle gebeurtenissen in het leven van een ouder epigenetische veranderingen veroorzaken die van invloed zijn op de gezondheid van hun kinderen.', 'Een polypeptide is een soort bouwsteen die door een gen wordt aangemaakt om eiwitten te vormen. Bijvoorbeeld, insuline is een polypeptide dat een belangrijke rol speelt in de regulering van het bloedsuikergehalte.', 'Eiwitten zijn chemische stoffen die de structuur en functies van een cel bepalen. Ze zijn enorm divers, met duizenden soorten die elk een specifieke taak uitvoeren, afhankelijk van de behoeften van de omgeving. Hemoglobine, bijvoorbeeld, is een eiwit dat zuurstof in onze bloedbaan transporteert.', 'Selective breeding, ontwikkeld door Mendel, is een techniek waarbij specifieke eigenschappen van planten worden geselecteerd en gekruist om gewenste eigenschappen te bevorderen. Dit leidde tot de ontdekking van dominante en recessieve genen die de kenmerken van een organisme bepalen, zoals de kleur van bloemen bij erwtenplanten.', 'Polygenetische genen zijn een verzameling van genen die samen een bepaalde eigenschap beïnvloeden, zoals lengte of intelligentie. Ze verklaren de grote variatie in kenmerken zoals de huidskleur bij mensen, die niet kan worden toegeschreven aan een enkel dominant of recessief gen.', 'Een zygote is de bevruchte cel die resulteert uit de combinatie van een sperma- en een eicel tijdens de bevruchting. Het bevat 23 paar chromosomen, bijvoorbeeld, een menselijke zygote heeft 46 chromosomen in totaal.', 'Genetische variatie verwijst naar de unieke genetische samenstelling die ontstaat bij conceptie door de combinatie van chromosomen van de moeder en de vader. Dit resulteert in een mogelijkheid van 8 miljoen verschillende combinaties, wat de genetische diversiteit van de menselijke soort verklaart.', 'Celdeling is een tweestaps proces waarbij een cel eerst haar chromosomen dupliceert en vervolgens in twee nieuwe cellen splitst met dezelfde chromosoomstructuur. Dit is de basis van groei en ontwikkeling. Zo groeit een menselijk embryo van een enkele zygote tot miljoenen cellen door middel van celdeling.', 'Mutaties zijn fouten die optreden tijdens celdeling, wat tot veranderingen in het genetisch materiaal kan leiden. Hoewel de meeste mutaties neutraal zijn, kunnen sommige een evolutionair voordeel bieden als ze de overlevings- of voortplantingskansen van een organisme verbeteren. Bijvoorbeeld, een mutatie die resistentie tegen een ziekte veroorzaakt, kan zich door een populatie verspreiden omdat dragers van het gemuteerde gen meer kans hebben om te overleven en zich voort te planten.', 'Behavioral genetics is de studie naar hoe genen en omgeving interacties beïnvloeden in psychologische activiteiten. Het heeft belangrijke informatie verstrekt over de mate waarin biologie invloed heeft op de geest, hersenen en gedrag.', 'Adoption studies vergelijken de gelijkenissen tussen biologische verwanten en adoptieve verwanten. Niet-biologische geadopteerde broers en zussen kunnen vergelijkbare thuissituaties hebben, maar ze hebben verschillende genen. Dus de aanname is dat overeenkomsten tussen niet-biologische geadopteerde broers en zussen meer te maken hebben met de omgeving dan met genen.', 'Bij genetica verwijst variation naar de mate van verschil binnen een groep mensen voor een bepaalde eigenschap. Bijvoorbeeld, om de erfelijkheid van lengte te kennen, moeten we weten hoeveel individuele Amerikaanse vrouwen variëren in die eigenschap. Zodra we de typische hoeveelheid variatie binnen de populatie kennen, kunnen we zien of mensen die gerelateerd zijn (zussen of een moeder en dochter) minder variatie tonen dan vrouwen die willekeurig zijn gekozen.', 'Het MAOA-gen reguleert het MAO-enzym, dat betrokken is bij de afbraak van een klasse neurotransmitters genaamd monoaminen. Dit omvat dopamine, serotonine, en noradrenaline. Mannelijke individuen met een lage MAOA-genvariant hebben een hogere kans op veroordeling voor gewelddadige misdaden als ze als kinderen zijn mishandeld.', 'Genetic modifications verwijzen naar technieken waarbij het expressieniveau van een bepaald gen wordt verhoogd of verlaagd, of een gen van de ene diersoort wordt ingebracht in het embryo van een andere. Bijvoorbeeld, de haarloze muis op de foto heeft twee *nu* genen ontvangen, die de "naakte" mutatie veroorzaken en ook het immuunsysteem beïnvloeden.', 'Optogenetics is een onderzoekstechniek die nauwkeurige controle biedt over wanneer een neuron vuurt, waardoor onderzoekers de causale relatie tussen neurale activiteit en gedrag beter kunnen begrijpen. Het combineert het gebruik van licht (optica) met genetische modificaties.']

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
    st.session_state.questions = solid_list_questions.copy()
    st.session_state.answers = solid_list_answers.copy()
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
    st.session_state.questions = solid_list_questions.copy()
    st.session_state.answers = solid_list_answers.copy()
    st.session_state.easy_count = {}

st.subheader(st.session_state.questions[0])
if st.session_state.show_answer:
    st.write(st.session_state.answers[0])

card_progress.progress(int(sum(st.session_state.easy_count.values()) / (2 * len(solid_list_questions)) * 100))


## Answer input field
def process_answer(input_text):
    with st.spinner('Evaluating your answer...'):
        score, feedback = evaluate_answer(input_text, st.session_state.questions[0], st.session_state.answers[0])
    # Store the score and feedback in the session state to access them after the input disappears
    st.session_state.submitted = True
    st.session_state.score = score
    st.session_state.feedback = feedback

# Send to openai for validation
from openai import OpenAI
client = OpenAI()
def evaluate_answer(answer, question, gold_answer):
    prompt = f"Question: {question}\nCorrect Answer: {gold_answer}\nUser Answer: {answer}\nIs the user's answer correct?"
    role_prompt = "I want you to act as a professor that marks the exam of a student. " \
                    "Your goal is to quantify the correctness of the answer given as a percentage, like X%. Give this percentage as the first return token, add a delimiter between this and the rest of the input using ;; " \
                    "You are critical and don't let students pass easily. You also identify what parts the student didn't get correct, if applicable and give feedback on how to improve." \
                    "Give your feedback in dutch."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": role_prompt},
            {"role": "user", "content": prompt}
        ],
        max_tokens=120
    )
    print(response)

    score = response.choices[0].message.content.split(";;")[0]
    feedback = response.choices[0].message.content.split(";;")[1]

    return score, feedback

# Define a function to display the score and feedback with color coding
def display_result():
    try:
        score = float(st.session_state.score.strip('%'))
    except ValueError:
        score = 0

    # Give rgba with 0.2 opacity
    if score > 75:
        # Green
        color = 'rgba(0, 128, 0, 0.2)'
    elif score > 49:
        # Orange
        color = 'rgba(255, 165, 0, 0.2)'
    else:
        # Red
        color = 'rgba(255, 0, 0, 0.2)'

    # Displaying score and feedback with formatting within the div
    result_html = f"""
    <div style='background-color: {color}; padding: 25px; border-radius: 5px;'>
        <h1 style='font-size: 40px; margin: 0;'>{st.session_state.score}</h1>
        <p style='font-size: 20px; font-style: italic; margin: 0;'>{st.session_state.feedback}</p>
    </div>
    """
    st.markdown(result_html, unsafe_allow_html=True)

# Initialize session state variables if they don't exist
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'answer' not in st.session_state:
    st.session_state.answer = ""

if 'score' not in st.session_state:
    st.session_state.score = ""
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""

# Text input field and submit button
if not st.session_state.submitted:
    answer = st.text_input("Jouw antwoord:", key='answer')
    st.button('Submit', on_click=process_answer, args=(answer,))
else:
    # Display the submitted text as solid text
    st.text("Jouw antwoord:")
    st.write(st.session_state.answer)

# After submission, display the result
if st.session_state.submitted:
    display_result()
