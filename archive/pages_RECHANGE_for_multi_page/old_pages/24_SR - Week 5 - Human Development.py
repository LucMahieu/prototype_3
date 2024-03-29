import streamlit as st
questions = ['Wat is de betekenis van ontwikkelingspsychologie?', 'Wat is synaptische snoei?', 'Wat zijn teratogenen?', 'Wat is de dynamische systeemtheorie?', 'Wat is de habituatietechniek?', 'Wat is infantiele amnesie?', 'Wat is hechting?', 'Wat is assimilatie?', 'Wat is accommodatie in de context van cognitieve ontwikkeling?', "Wat is de sensorimotorische fase in Piaget's theorie van cognitieve ontwikkeling?", 'Wat betekent objectpermanentie?', "Wat is de preoperationele fase in Piaget's theorie van cognitieve ontwikkeling?", "Wat is de concreet-operationele fase in Piaget's theorie van cognitieve ontwikkeling?", "Wat is de formeel-operationele fase in Piaget's theorie van cognitieve ontwikkeling?", 'Wat houdt de ‘theory of mind’ in?', 'Wat is het preconventionele niveau in de theorie van morele ontwikkeling?', 'Wat is het conventionele niveau van morele ontwikkeling?', 'Wat is het postconventionele niveau van morele ontwikkeling?', 'Wat is inequity aversion?', 'Wat is een zygote?', 'Wat is een embryo?', 'Wat is een foetus?', 'Wat zijn Fetal Alcohol Spectrum Disorders (FASDs)?', 'Wat zijn babyreflexen?', 'Wat is de grijpreflex?', 'Wat is de zoekreflex?', 'Wat is de zuigreflex?', 'Wat is de zuigreflex bij pasgeborenen?', 'Wat is visuele scherpte bij pasgeborenen?', 'Wat is de preferential-looking techniek?', 'Wat is de Memory-Retention Test?', 'Wat is imprinting bij vogels?', 'Wat waren de bevindingen van Harlow?', 'Wat is de vreemde-situatietest?', 'Wat zijn de kritieken op Piagets theorie?', 'Wat is de relatie tussen de theory of mind en prosociaal gedrag?']
answers = ['Ontwikkelingspsychologie is de studie van veranderingen in fysiologie, cognitie, emotie en sociaal gedrag gedurende het leven. Het omvat onderwerpen zoals kinderontwikkeling, adolescentie en volwassenheid.', 'Synaptische snoei is een fysiologisch proces dat gebruikte synaptische verbindingen behoudt en ongebruikte verbindingen elimineert. Dit is essentieel voor de ontwikkeling en rijping van de hersenen in de kindertijd en adolescentie.', 'Teratogenen zijn stoffen of factoren die schade kunnen toebrengen aan het embryo of de foetus. Voorbeelden zijn bepaalde medicijnen, infecties, straling en drugs.', 'De dynamische systeemtheorie stelt dat ontwikkeling een zelforganiserend proces is waarbij nieuwe gedragingen ontstaan door consistente interacties tussen een individu en hun culturele en omgevingscontexten. Denk bijvoorbeeld aan een baby die leert lopen: de spierontwikkeling, motivatie van de baby, aanmoediging van ouders, en de fysieke omgeving (zoals de vloer) werken allemaal samen waardoor het kind de vaardigheid van lopen verwerft.', "De habituatietechniek onderzoekt hoe baby's dingen, zoals gezichten, onderscheiden door gebruik te maken van hun kijktijd. Als baby's herhaaldelijk naar voorwerpen van dezelfde categorie kijken, raken ze er gewend aan en kijken ze korter. Als je ze daarna een nieuw voorwerp uit een andere categorie toont, kijken ze langer, wat aangeeft dat ze het verschil waarnemen.", 'Infantiele amnesie is de onmogelijkheid om gebeurtenissen uit de vroege kindertijd te herinneren. Dit fenomeen verklaart waarom de meeste mensen geen herinneringen hebben van vóór de leeftijd van 3 à 4 jaar.', 'Hechting is een sterke, emotionele en blijvende verbinding tussen mensen die in de loop van tijd en omstandigheden standhoudt, zoals de band tussen een ouder en een kind. Hechting motiveert kinderen en verzorgers bijvoorbeeld om dicht bij elkaar te blijven, wat de veiligheid van de kinderen vergroot die ze nodig hebben om te overleven. ', "Assimilatie is het proces waarbij nieuwe informatie wordt opgenomen in bestaande schema's. Bijvoorbeeld, een kind dat een hond als 'huisdier' kent, kan een kat ook als 'huisdier' classificeren.", "Accommodatie is het proces waarbij een nieuw schema wordt gecreëerd of een bestaand schema aanzienlijk wordt aangepast om nieuwe informatie op te nemen die anders niet zou passen. Bijvoorbeeld, een kind kan zijn begrip van 'hond' aanpassen om ook honden van verschillende rassen en groottes te omvatten.", "In de sensorimotorische fase (0-2 jaar) van Piaget leren kinderen door directe interactie met hun omgeving, ontwikkelen ze het besef dat objecten blijven bestaan ook als ze niet zichtbaar zijn (objectpermanentie) en beginnen ze gedrag na te bootsen dat ze eerder hebben waargenomen, zoals een boze voetstap van hun vader.", "Objectpermanentie is het besef bij kinderen dat dingen blijven bestaan, zelfs als ze uit het zicht zijn. Zonder dit besef denkt een kind bijvoorbeeld dat een speelgoed dat onder een deken is verstopt, verdwenen is.", "In Piaget's preoperationele fase (tweede fase) denken kinderen voornamelijk op een intuïtieve en oppervlakkige manier, zoals geloven dat een langer glas automatisch meer vloeistof bevat dan een kort, breed glas. Ze zijn ook egocentrisch, wat betekent dat ze moeite hebben om dingen vanuit een ander perspectief te zien dan dat van zichzelf.", "De concreet-operationele fase is Piagets derde fase van cognitieve ontwikkeling, waarin kinderen beginnen na te denken over en logische operaties te begrijpen, en zich niet laten misleiden door verschijningen. Ze begrijpen bijvoorbeeld dat een glas water, wanneer dit in een ander glas wordt gegoten, dezelfde hoeveelheid water blijft. Ze kunnen dit echter alleen toepassen op concrete situaties. Zo begrijpen ze dat 4+1 en 6+1 een oneven getal opleveren, maar nog niet dat elk even getal + 1 een oneven getal oplevert.", "De formeel-operationele fase is Piaget's laatste fase van cognitieve ontwikkeling, waarin individuen abstract kunnen denken en hypotheses kunnen formuleren en testen door middel van deductieve logica. Dit stelt hen in staat om problemen te begrijpen en op te lossen die een abstract denkniveau vereisen.", "'Theory of mind' is het vermogen om te begrijpen dat andere mensen mentale toestanden hebben die hun gedrag beïnvloeden. Bijvoorbeeld, het begrijpen dat een vriend boos zou kunnen zijn omdat hij een slechte dag heeft gehad, zelfs als de situatie voor jou niet boosmakend lijkt.", "Het preconventionele niveau is het initiële stadium van morele ontwikkeling, waar moraliteit wordt bepaald door eigenbelang en de uitkomsten van gebeurtenissen. Bijvoorbeeld, in een situatie waar een man's vrouw ernstig ziek is, zou iemand op dit niveau redeneren: 'Hij moet het medicijn stelen om zijn vrouw te redden, want dan zal hij zich gelukkig voelen.'", "Het conventionele niveau is de tussenstap in de morele ontwikkeling waarbij moraliteit wordt bepaald door het naleven van maatschappelijke regels en het zoeken van goedkeuring van anderen. Iemand zou vanuit deze fase zeggen 'Hij moet het medicijn niet stelen. Je hoort niet te stelen, dus iedereen zal denken dat hij een slecht persoon is.'", "Het postconventionele niveau is de laatste fase van de morele ontwikkeling waarbij moraliteit wordt bepaald door abstracte principes en de waarde van alle leven. Een persoon op dit niveau zou bijvoorbeeld zeggen 'Soms moeten mensen de wet breken als de wet onjuist is. In deze situatie is het fout om te stelen, maar het is nog erger dat er zoveel geld wordt gevraagd voor een medicijn dat iemand zijn leven kan redden.'", 'Inequity aversion is een voorkeur voor het vermijden van oneerlijkheid in beslissingen over de verdeling van middelen. Dit is geïllustreerd in een experiment waarbij kinderen snoep verdeelden: ze kozen er vaak voor om zichzelf en een ander kind elk één snoepje te geven, maar waren terughoudend om het andere kind een extra snoepje te geven zonder er zelf ook een te krijgen.', 'Een zygote is de eerste cel van een nieuw leven, gecreëerd op het moment van bevruchting wanneer een zaadcel een eicel bevrucht. Ongeveer 2 weken na de bevruchting nestelt de zygote zich stevig in de baarmoederwand om verder te ontwikkelen.', 'Een embryo is een zich ontwikkelend mens van ongeveer 2 weken tot 2 maanden oud. Tijdens deze fase beginnen organen en interne systemen te vormen. Deze fase is bijzonder kwetsbaar voor invloeden zoals gifstoffen, drugs en extreme stress.', 'Een foetus is een groeiend mens na 2 maanden van prenatale ontwikkeling. Alle organen zijn gevormd, het hart begint te kloppen en het lichaam blijft groeien en ontwikkelen tot het klaar is voor leven buiten de baarmoeder.', 'Fetal Alcohol Spectrum Disorders (FASDs) worden veroorzaakt door alcoholgebruik tijdens de zwangerschap. Symptomen van deze groep aandoeningen zijn onder andere laag geboortegewicht, afwijkingen aan gezicht en hoofd, onvoldoende hersengroei en bewijs van beperkingen zoals gedrags- of cognitieve problemen of een laag IQ.', "Babyreflexen zijn aangeboren vaardigheden die baby's helpen overleven, waaronder de grijpreflex, de zoekreflex en de zuigreflex.", 'De grijpreflex is een overlevingsmechanisme dat voortkomt uit onze primaire voorouders. Jonge apen grijpen hun moeders vast, wat nuttig is omdat de nakomelingen van plaats naar plaats gedragen moeten worden.', "De zoekreflex is de automatische draai- en zuigreactie van baby's wanneer een tepel of een vergelijkbaar object een gebied in de buurt van hun mond raakt.", "De zuigreflex is een instinctieve reactie van baby's om te zuigen wanneer iets hun mond raakt. Dit helpt hen te voeden en te overleven.", 'Dit betekent dat pasgeborenen, wanneer ze een object vinden, de zuigreflex vertonen. Dit is een vroeg teken van visuele scherpte bij pasgeborenen.', 'Visuele scherpte is het vermogen om verschillen te onderscheiden tussen vormen, patronen en kleuren. Bij pasgeborenen is deze vaardigheid nog onderontwikkeld, maar verbetert snel gedurende de eerste 6 maanden en bereikt volwassen niveaus rond hun eerste levensjaar.', 'De preferential-looking techniek is een onderzoeksmethode waarbij een baby twee dingen getoond wordt. Als de baby langer naar één ding kijkt, weten de onderzoekers dat de baby het verschil kan zien en één ding interessanter vindt.', "De Memory-Retention Test is een test waarbij baby's leren dat ze een mobiel kunnen bewegen door met hun voeten te trappen. Als ze na een pauze snel hun voeten trappen om de mobiel te bewegen, tonen ze aan dat ze zich herinneren dat ze de mobiel hebben bewogen tijdens de leerfase.", 'Imprinting is een gedrag bij sommige vogelsoorten waarbij kuikens zich sterk hechten aan een nabije volwassene, zelfs van een andere soort. Dit gedrag treedt op bij vogels zoals kippen, ganzen en eenden.', "Harlow's onderzoek toonde aan dat contactcomfort - het belang van fysieke aanraking en geruststelling - van groot belang is voor sociale ontwikkeling. Dit werd aangetoond in experimenten waarbij babymonkeys de voorkeur gaven aan een zachte, knuffelbare surrogaatmoeder boven een draadmoeder die melk kon geven.", 'De vreemde-situatietest is een laboratoriumprocedure waarbij het kind, de verzorger en een vriendelijke maar onbekende volwassene betrokken zijn bij een reeks semi-gestructureerde episodes. Het doel is om de kwaliteit van de gehechtheid van het kind aan de verzorger te beoordelen.', 'Een van de kritieken op Piagets theorie is dat kinderen meer weten dan we denken en dat de overgang tussen de stadia soepeler verloopt. Bovendien ontwikkelt formeel operationeel denken zich niet zomaar, het moet worden onderwezen.', 'De theory of mind verwijst naar het vermogen om de mentale toestanden van anderen te begrijpen en te voorspellen, terwijl prosociaal gedrag verwijst naar vrijwillig gedrag dat bedoeld is om anderen te helpen. Een goed ontwikkelde theory of mind kan leiden tot meer prosociaal gedrag omdat het individu beter in staat is om de behoeften en gevoelens van anderen te begrijpen.']


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