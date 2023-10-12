import streamlit as st
questions = ['Wat is de betekenis van ontwikkelingspsychologie?', 'Wat is synaptische snoei?', 'Wat zijn teratogenen?', 'Wat is de dynamische systeemtheorie?', 'Wat is de habituatietechniek?', 'Wat is infantiele amnesie?', 'Wat is hechting?', 'Wat is assimilatie?', 'Wat is accommodatie in de context van cognitieve ontwikkeling?', "Wat is de sensorimotorische fase in Piaget's theorie van cognitieve ontwikkeling?", 'Wat betekent objectpermanentie?', "Wat is de preoperationele fase in Piaget's theorie van cognitieve ontwikkeling?", "Wat is de concreet-operationele fase in Piaget's theorie van cognitieve ontwikkeling?", "Wat is de formeel-operationele fase in Piaget's theorie van cognitieve ontwikkeling?", 'Wat houdt de ‘theory of mind’ in?', 'Wat is het preconventionele niveau in de theorie van morele ontwikkeling?', 'Wat is het conventionele niveau van morele ontwikkeling?', 'Wat is het postconventionele niveau van morele ontwikkeling?', 'Wat is inequity aversion?']
answers = ['Ontwikkelingspsychologie is de studie van veranderingen in fysiologie, cognitie, emotie en sociaal gedrag gedurende het leven. Het omvat onderwerpen zoals kinderontwikkeling, adolescentie en volwassenheid.', 'Synaptische snoei is een fysiologisch proces dat gebruikte synaptische verbindingen behoudt en ongebruikte verbindingen elimineert. Dit is essentieel voor de ontwikkeling en rijping van de hersenen in de kindertijd en adolescentie.', 'Teratogenen zijn stoffen of factoren die schade kunnen toebrengen aan het embryo of de foetus. Voorbeelden zijn bepaalde medicijnen, infecties, straling en drugs.', 'De dynamische systeemtheorie stelt dat ontwikkeling een zelforganiserend proces is waarbij nieuwe gedragingen ontstaan door consistente interacties tussen een individu en hun culturele en omgevingscontexten. Denk bijvoorbeeld aan een baby die leert lopen: de spierontwikkeling, motivatie van de baby, aanmoediging van ouders, en de fysieke omgeving (zoals de vloer) werken allemaal samen waardoor het kind de vaardigheid van lopen verwerft.', "De habituatietechniek onderzoekt hoe baby's dingen, zoals gezichten, onderscheiden door gebruik te maken van hun kijktijd. Als baby's herhaaldelijk naar voorwerpen van dezelfde categorie kijken, raken ze er gewend aan en kijken ze korter. Als je ze daarna een nieuw voorwerp uit een andere categorie toont, kijken ze langer, wat aangeeft dat ze het verschil waarnemen.", 'Infantiele amnesie is de onmogelijkheid om gebeurtenissen uit de vroege kindertijd te herinneren. Dit fenomeen verklaart waarom de meeste mensen geen herinneringen hebben van vóór de leeftijd van 3 à 4 jaar.', 'Hechting is een sterke, emotionele en blijvende verbinding tussen mensen die in de loop van tijd en omstandigheden standhoudt, zoals de band tussen een ouder en een kind. Hechting motiveert kinderen en verzorgers bijvoorbeeld om dicht bij elkaar te blijven, wat de veiligheid van de kinderen vergroot die ze nodig hebben om te overleven. ', "Assimilatie is het proces waarbij nieuwe informatie wordt opgenomen in bestaande schema's. Bijvoorbeeld, een kind dat een hond als 'huisdier' kent, kan een kat ook als 'huisdier' classificeren.", "Accommodatie is het proces waarbij een nieuw schema wordt gecreëerd of een bestaand schema aanzienlijk wordt aangepast om nieuwe informatie op te nemen die anders niet zou passen. Bijvoorbeeld, een kind kan zijn begrip van 'hond' aanpassen om ook honden van verschillende rassen en groottes te omvatten.", "In de sensorimotorische fase (0-2 jaar) van Piaget leren kinderen door directe interactie met hun omgeving, ontwikkelen ze het besef dat objecten blijven bestaan ook als ze niet zichtbaar zijn (objectpermanentie) en beginnen ze gedrag na te bootsen dat ze eerder hebben waargenomen, zoals een boze voetstap van hun vader.", "Objectpermanentie is het besef bij kinderen dat dingen blijven bestaan, zelfs als ze uit het zicht zijn. Zonder dit besef denkt een kind bijvoorbeeld dat een speelgoed dat onder een deken is verstopt, verdwenen is.", "In Piaget's preoperationele fase (tweede fase) denken kinderen voornamelijk op een intuïtieve en oppervlakkige manier, zoals geloven dat een langer glas automatisch meer vloeistof bevat dan een kort, breed glas. Ze zijn ook egocentrisch, wat betekent dat ze moeite hebben om dingen vanuit een ander perspectief te zien dan dat van zichzelf.", "De concreet-operationele fase is Piagets derde fase van cognitieve ontwikkeling, waarin kinderen beginnen na te denken over en logische operaties te begrijpen, en zich niet laten misleiden door verschijningen. Ze begrijpen bijvoorbeeld dat een glas water, wanneer dit in een ander glas wordt gegoten, dezelfde hoeveelheid water blijft. Ze kunnen dit echter alleen toepassen op concrete situaties. Zo begrijpen ze dat 4+1 en 6+1 een oneven getal opleveren, maar nog niet dat elk even getal + 1 een oneven getal oplevert.", "De formeel-operationele fase is Piaget's laatste fase van cognitieve ontwikkeling, waarin individuen abstract kunnen denken en hypotheses kunnen formuleren en testen door middel van deductieve logica. Dit stelt hen in staat om problemen te begrijpen en op te lossen die een abstract denkniveau vereisen.", "'Theory of mind' is het vermogen om te begrijpen dat andere mensen mentale toestanden hebben die hun gedrag beïnvloeden. Bijvoorbeeld, het begrijpen dat een vriend boos zou kunnen zijn omdat hij een slechte dag heeft gehad, zelfs als de situatie voor jou niet boosmakend lijkt.", "Het preconventionele niveau is het initiële stadium van morele ontwikkeling, waar moraliteit wordt bepaald door eigenbelang en de uitkomsten van gebeurtenissen. Bijvoorbeeld, in een situatie waar een man's vrouw ernstig ziek is, zou iemand op dit niveau redeneren: 'Hij moet het medicijn stelen om zijn vrouw te redden, want dan zal hij zich gelukkig voelen.'", "Het conventionele niveau is de tussenstap in de morele ontwikkeling waarbij moraliteit wordt bepaald door het naleven van maatschappelijke regels en het zoeken van goedkeuring van anderen. Iemand zou vanuit deze fase zeggen 'Hij moet het medicijn niet stelen. Je hoort niet te stelen, dus iedereen zal denken dat hij een slecht persoon is.'", "Het postconventionele niveau is de laatste fase van de morele ontwikkeling waarbij moraliteit wordt bepaald door abstracte principes en de waarde van alle leven. Een persoon op dit niveau zou bijvoorbeeld zeggen 'Soms moeten mensen de wet breken als de wet onjuist is. In deze situatie is het fout om te stelen, maar het is nog erger dat er zoveel geld wordt gevraagd voor een medicijn dat iemand zijn leven kan redden.'", 'Inequity aversion is een voorkeur voor het vermijden van oneerlijkheid in beslissingen over de verdeling van middelen. Dit is geïllustreerd in een experiment waarbij kinderen snoep verdeelden: ze kozen er vaak voor om zichzelf en een ander kind elk één snoepje te geven, maar waren terughoudend om het andere kind een extra snoepje te geven zonder er zelf ook een te krijgen.']

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