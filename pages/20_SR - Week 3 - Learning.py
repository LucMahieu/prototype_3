import streamlit as st

solid_list_questions = ['Wat betekent leren?', 'Wat is non-associatief leren?', 'Wat is associatief leren?', 'Wat is sociaal leren?', 'Wat is habituatie?', 'Wat is sensibilisatie?', 'Wat is Pavloviaanse conditionering (klassieke conditionering)?', 'Wat is een ongeconditioneerde respons?', 'Wat is een ongeconditioneerde stimulus?', 'Wat is een geconditioneerde stimulus?', 'Wat is een geconditioneerde reactie?', 'Wat is acquisitie in de context van conditionering?', 'Wat is extinctie in de context van conditionering?', 'Wat is spontane herstel in de context van conditionering?', 'Wat is het Rescorla-Wagner model?', 'Wat is stimulus generalisatie?', 'Wat is stimulusdiscriminatie?', 'Wat is operante conditionering (instrumentele conditionering)?', 'Wat is de wet van effect?', 'Wat is behaviorisme?', 'Wat is een versterker?', 'Wat is positieve versterking?', 'Wat is negatieve versterking?', 'Wat is straf?', 'Wat is positieve straf?', 'Wat is negatieve straf?', 'Wat is shaping in de context van operant conditionering?', 'Wat is temporal discounting?', 'Wat is continue versterking?', 'Wat is gedeeltelijke versterking?', 'Wat is het effect van uitdoving bij gedeeltelijke versterking?', 'Wat is equipotentialiteit?', 'Wat is een fobie?', 'Wat is fear conditioning?', 'Wat betekent modeling in de context van gedrag?', 'Wat is vicarious learning?', 'Wat is instructed learning?', 'Wat is Dishabituation?', "Wat betekent het als een reactie 'Extinguished' is?", "Wat is een 'Prediction error'?", "Wat is een 'Positive prediction error'?", "Wat is een 'Negative prediction error'?", "Wat is 'Second-order conditioning'?", "Wat zijn 'Succesive approximations'?", "Wat zijn 'Primary reinforcers'?", 'Wat zijn secundaire versterkers?', "Wat zijn de meest voorkomende beloningsschema's?", 'Wat is een Fixed-Ratio (FR) beloningsschema?', 'Wat is een Variable-Ratio (VR) beloningsschema?', 'Wat is een Fixed-Interval (FI) beloningsschema?', 'Wat is een Variable-Interval (VI) beloningsschema?']
solid_list_answers = ['Leren is een relatief blijvende verandering in gedrag als gevolg van ervaring. Bijvoorbeeld, een kind leert om een vork te gebruiken door het te proberen en te oefenen.', 'Non-associatief leren is het reageren na herhaalde blootstelling aan een enkele stimulus of gebeurtenis. Een voorbeeld is schrikken van een plotseling geluid, maar na herhaalde blootstelling minder schrikken.', 'Associatief leren is het verbinden van twee stimuli of gebeurtenissen die samen voorkomen. Zoals het aanleren dat een stoplicht op rood staat betekent dat je moet stoppen.', 'Sociaal leren is het aanleren of veranderen van gedrag na verbale instructie of blootstelling aan een ander individu dat het gedrag uitvoert. Bijvoorbeeld, een kind leert hoe een vork te gebruiken door zijn ouders te observeren.', 'Habituatie is een afname in gedragsrespons na herhaalde blootstelling aan een stimulus. Zoals het minder schrikken van een plotseling geluid na herhaalde blootstelling.', 'Sensibilisatie is een toename in gedragsrespons na blootstelling aan een stimulus. Zoals het meer alert reageren op een geluid na een schrikreactie.', "Pavloviaanse conditionering houdt in dat een oorspronkelijk neutrale stimulus, zoals een bel, een respons kan opwekken na herhaaldelijk gepaard te zijn met een stimulus die een natuurlijke respons opwekt, zoals voedsel dat kwijlen veroorzaakt bij honden. In Pavlov's beroemde experiment leerden honden te kwijlen bij het horen van een bel alleen, omdat ze het geluid gingen associëren met het krijgen van eten.", 'Een ongeconditioneerde respons is een reactie die niet hoeft te worden geleerd, zoals een reflex. Bijvoorbeeld, de knie-reflexreactie bij een tik op de knieschijf.', 'Een ongeconditioneerde stimulus (US) is een stimulus die een reactie uitlokt, zoals een reflex, zonder enige voorafgaande leerervaring. Een voorbeeld kan zijn het schrikken van een plotseling, luid geluid.', 'Een geconditioneerde stimulus (CS) is een stimulus die een reactie uitlokt alleen nadat er leren heeft plaatsgevonden. Een voorbeeld is een bel die geassocieerd wordt met voedsel en daardoor speekselvloed veroorzaakt bij een hond.', 'Een geconditioneerde reactie (CR) is een reactie op een geconditioneerde stimulus; het is een reactie die is aangeleerd. Bijvoorbeeld, het speekselvloed bij een hond wanneer de bel gaat, na training.', 'Acquisitie is de geleidelijke vorming van een associatie tussen de geconditioneerde en ongeconditioneerde stimuli. Dit is het leerproces waarbij een organisme leert dat een geconditioneerde stimulus voorspelt dat een ongeconditioneerde stimulus zal volgen.', "Extinctie is een proces waarbij de geconditioneerde reactie wordt verzwakt wanneer de geconditioneerde stimulus wordt herhaald zonder de ongeconditioneerde stimulus. Het is het 'ontleren' van de associatie, zoals wanneer de bel wordt gerinkeld zonder voedsel, de hond stopt met kwijlen.", 'Spontane herstel is wanneer een eerder uitgedoofde geconditioneerde reactie opnieuw opduikt na de presentatie van de geconditioneerde stimulus. Bijvoorbeeld, na een periode van geen bel en voedsel, zal het rinkelen van de bel weer speekselvloed veroorzaken bij de hond.', 'Het Rescorla-Wagner model beschrijft hoe associaties tussen stimuli versterkt of verzwakt worden op basis van verwachtingen. Wanneer een geconditioneerde stimulus (zoals een bel) niet langer de verwachte ongeconditioneerde stimulus (zoals voedsel) voorspelt, verzwakt de associatie tussen de twee. Aan de andere kant, als de voorspelling consistent uitkomt, wordt de associatie versterkt.', 'Stimulus generalisatie is een vorm van leren waarbij stimuli die vergelijkbaar maar niet identiek zijn aan de geconditioneerde stimulus de geconditioneerde reactie veroorzaken. Bijvoorbeeld, een hond die getraind is om te kwijlen bij het geluid van een specifieke bel, kan ook kwijlen bij het geluid van een vergelijkbare bel.', "Stimulusdiscriminatie is het onderscheid dat wordt gemaakt tussen twee vergelijkbare stimuli wanneer slechts één van hen consequent wordt geassocieerd met de ongeconditioneerde stimulus. Dit komt veel voor in klassieke conditionering, zoals bij Pavlov's hondenexperiment.", 'Operante conditionering is een leerproces waarbij de gevolgen van een actie de waarschijnlijkheid bepalen dat deze in de toekomst wordt uitgevoerd. Een voorbeeld is een kind dat leert zijn speelgoed op te ruimen om te voorkomen dat hij straf krijgt.', "De wet van effect, geformuleerd door Thorndike, stelt dat elk gedrag dat leidt tot een 'bevredigende toestand' waarschijnlijk weer zal optreden, en elk gedrag dat leidt tot een 'vervelende toestand' minder waarschijnlijk weer zal optreden.", 'Behaviorisme is een psychologische benadering die de nadruk legt op omgevingsinvloeden op waarneembaar gedrag. Het kijkt niet naar interne processen zoals denken of voelen, maar alleen naar gedrag dat kan worden waargenomen en gemeten.', 'Een versterker is een stimulus die een reactie volgt en de kans vergroot dat de reactie wordt herhaald. Een voorbeeld is een beloning die een kind krijgt nadat hij zijn huiswerk heeft gemaakt.', 'Positieve versterking is het toedienen van een stimulus om de kans op herhaling van een gedrag te vergroten. Bijvoorbeeld, het geven van een snoepje aan een kind na het opruimen van zijn speelgoed.', 'Negatieve versterking is het wegnemen van een onaangename stimulus om de kans op herhaling van een gedrag te vergroten. Een voorbeeld is het stoppen van een vervelend geluid als een kind zijn kamer opruimt.', 'Straf is een stimulus die een gedrag volgt en de kans verkleint dat het gedrag wordt herhaald. Een voorbeeld is een ouder die een kind berispt voor het vertonen van slecht gedrag.', 'Positieve straf is het toedienen van een stimulus om de kans op herhaling van een gedrag te verminderen. Een voorbeeld is een kind straffen door extra klusjes toe te wijzen na ongepast gedrag.', 'Negatieve straf is het wegnemen van een stimulus om de kans op herhaling van een gedrag te verminderen. Een voorbeeld is het afnemen van speeltijd als een kind zich misdraagt.', 'Shaping is een proces waarbij gedragingen die steeds meer op het gewenste gedrag lijken, worden versterkt. Bijvoorbeeld, bij het trainen van een hond, zou je eerst belonen voor simpelweg naar je toe komen, dan voor het zitten, enzovoort.', 'Temporal discounting is de neiging om de subjectieve waarde van een beloning te verminderen als deze na een vertraging wordt gegeven. Dit zou kunnen verklaren waarom sommige mensen liever een kleinere onmiddellijke beloning kiezen boven een grotere toekomstige beloning.', 'Continue versterking is een type leren waarbij gedrag elke keer dat het optreedt, wordt versterkt. Bijvoorbeeld, elke keer dat een hond op commando zit, krijgt hij een traktatie.', 'Gedeeltelijke versterking is een type leren waarbij gedrag intermitterend wordt versterkt. Dit kan bijvoorbeeld gebeuren wanneer een hond niet elke keer een traktatie krijgt als hij op commando zit, maar slechts af en toe.', 'Het effect van uitdoving bij gedeeltelijke versterking is dat gedrag langer aanhoudt onder gedeeltelijke versterking dan onder continue versterking. Dit komt omdat het organisme gewend is geraakt aan onregelmatige beloningen.', 'Equipotentialiteit is het principe dat elk geconditioneerd stimulus gekoppeld aan elk ongeconditioneerd stimulus zou moeten resulteren in leren. Dit betekent dat in theorie elke stimulus gekoppeld kan worden aan een respons.', 'Een fobie is een verworven angst die buiten proportie is ten opzichte van de echte dreiging van een object of situatie. Bijvoorbeeld, arachnofobie is een intense en irrationele angst voor spinnen.', 'Fear conditioning is een vorm van klassieke conditionering waarbij neutrale stimuli worden omgezet in dreigende stimuli. Een voorbeeld kan zijn het leren bang te zijn voor de toon van een bel omdat deze eerder gepaard ging met een onaangename gebeurtenis.', 'Modeling is het imiteren van waargenomen gedrag. Bijvoorbeeld, een kind kan leren hoe te reageren in een sociale situatie door het gedrag van zijn ouders te observeren.', 'Vicarious learning is het leren van de gevolgen van een actie door te kijken naar anderen die beloond of bestraft worden voor het uitvoeren van die actie. Bijvoorbeeld, een kind kan leren niet te liegen nadat het ziet dat zijn broer gestraft wordt voor liegen.', 'Instructed learning is het leren van associaties en gedragingen door middel van verbale communicatie. Bijvoorbeeld, een instructeur kan iemand leren hoe een auto te besturen door hen te vertellen hoe het te doen.', 'Dishabituation is een toename van een reactie door een verandering in iets vertrouwds.', "Een reactie is 'Extinguished' wanneer de geconditioneerde stimulus de ongeconditioneerde stimulus niet langer voorspelt. Dit betekent dat de geleerde reactie verdwijnt als de stimulus niet langer gepaard gaat met de verwachte uitkomst.", "Een 'Prediction error' is het verschil tussen de verwachte en de werkelijke uitkomst volgens leertheoretici. Dit is een belangrijk concept in het leren, omdat het bepaalt hoe sterk een associatie is.", "Een 'Positive prediction error' treedt op wanneer na het verschijnen van een stimulus iets verrassends gebeurt. Dit kan de aanwezigheid zijn van een onverwachte gebeurtenis of een sterkere versie van de verwachte stimulus dan verwacht. Deze voorspellingsfout versterkt de associatie tussen de geconditioneerde en de ongeconditioneerde stimulus.", "Een 'Negative prediction error' treedt op wanneer een verwachte gebeurtenis niet gebeurt. De afwezigheid van de gebeurtenis leidt tot een negatieve voorspellingsfout, die de associatie tussen de geconditioneerde en de ongeconditioneerde stimulus verzwakt.", "'Second-order conditioning' vindt plaats wanneer een geconditioneerde stimulus wordt gekoppeld aan een nieuwe stimulus. Deze nieuwe stimulus leidt dan tot een geconditioneerde reactie.", '\'Succesive approximations\' zijn belangrijk in vorming. Het versterken van opeenvolgende benaderingen leidt uiteindelijk tot het gewenste gedrag. Dit is vergelijkbaar met het kinderspel "warm-koud", waarbij aanwijzingen gegeven worden om een verborgen object te vinden.', "'Primary reinforcers' zijn stimuli die noodzakelijk zijn voor overleving, zoals voedsel of water. Ze voldoen aan biologische behoeften en versterken daarom gedrag dat leidt tot het verkrijgen ervan. Dit is evolutionair gezien zinvol, want dieren die gedrag vertonen dat wordt versterkt door voedsel of water, hebben een grotere kans om te overleven en hun genen door te geven.", 'Secundaire versterkers zijn stimuli die dienen als versterkers maar geen biologische behoeften bevredigen. Ze worden gevormd door klassieke conditionering, zoals geld dat we associëren met beloningen zoals voedsel, veiligheid en macht.', "De meest voorkomende beloningsschema's zijn vast interval, variabel interval, vast ratio en variabel ratio. Dit zijn schema's die de basis van beloning combineren met de regelmaat van beloning.", 'Een Fixed-Ratio (FR) schema is wanneer een beloning wordt gegeven na een vast aantal reacties. Bijvoorbeeld, een werknemer die betaald wordt per geproduceerd item, of een stempelkaart bij een café waar je een gratis koffie krijgt na elke tien aankopen.', 'Een Variable-Ratio (VR) schema is wanneer een beloning wordt gegeven na een onvoorspelbaar aantal reacties. Het gemiddelde aantal reacties dat nodig is voor een beloning is constant, maar het exacte aantal reacties kan variëren. Een voorbeeld hiervan is een gokautomaat in een casino, waar je soms na een paar keer trekken wint, en andere keren pas na vele pogingen.', 'Een Fixed-Interval (FI) schema is wanneer een beloning wordt gegeven na een vast tijdsinterval, ongeacht het aantal reacties in die tijd. Een voorbeeld hiervan is een werknemer die elke maand een salaris ontvangt, of een huisdier dat elke dag op vaste tijden wordt gevoed.', 'Een Variable-Interval (VI) schema is wanneer een beloning wordt gegeven na een onvoorspelbaar tijdsinterval. Het gemiddelde tijdsinterval tussen de beloningen is constant, maar het exacte tijdsinterval kan variëren. Een voorbeeld hiervan zou kunnen zijn het ontvangen van e-mails, waarbij de tijd tussen de berichten varieert.']


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