import streamlit as st
questions = ['Wat is de betekenis van ontwikkelingspsychologie?', 'Wat is synaptische snoei?', 'Wat zijn teratogenen?', 'Wat is de dynamische systeemtheorie?', 'Wat is de habituatietechniek?', 'Wat is infantiele amnesie?', 'Wat is hechting?', 'Wat is assimilatie?', 'Wat is accommodatie in de context van cognitieve ontwikkeling?', "Wat is de sensorimotorische fase in Piaget's theorie van cognitieve ontwikkeling?", 'Wat betekent objectpermanentie?', "Wat is de preoperationele fase in Piaget's theorie van cognitieve ontwikkeling?", "Wat is de concreet-operationele fase in Piaget's theorie van cognitieve ontwikkeling?", "Wat is de formeel-operationele fase in Piaget's theorie van cognitieve ontwikkeling?", 'Wat is de theorie van de geest?', 'Wat is het preconventionele niveau in de theorie van morele ontwikkeling?', 'Wat is het conventionele niveau van morele ontwikkeling?', 'Wat is het postconventionele niveau van morele ontwikkeling?', 'Wat is inequity aversion?', 'Wat is puberteit?']
answers = ['Ontwikkelingspsychologie is de studie van veranderingen in fysiologie, cognitie, emotie en sociaal gedrag gedurende het leven. Het omvat onderwerpen zoals kinderontwikkeling, adolescentie en volwassenheid.', 'Synaptische snoei is een fysiologisch proces dat gebruikte synaptische verbindingen behoudt en ongebruikte verbindingen elimineert. Dit is essentieel voor de ontwikkeling en rijping van de hersenen in de kindertijd en adolescentie.', 'Teratogenen zijn stoffen of factoren die schade kunnen toebrengen aan het embryo of de foetus. Voorbeelden zijn bepaalde medicijnen, infecties, straling en drugs.', 'De dynamische systeemtheorie stelt dat ontwikkeling een zelforganiserend proces is waarbij nieuwe gedragingen ontstaan door consistente interacties tussen een individu en hun culturele en omgevingscontexten.', "De habituatietechniek is een methode om te onderzoeken hoe baby's objecten, zoals gezichten, categoriseren. Het maakt gebruik van het principe dat baby's langer kijken naar objecten uit een nieuwe categorie nadat ze objecten uit één categorie hebben bekeken.", 'Infantiele amnesie is de onmogelijkheid om gebeurtenissen uit de vroege kindertijd te herinneren. Dit fenomeen verklaart waarom de meeste mensen geen herinneringen hebben van vóór de leeftijd van 3 à 4 jaar.', 'Hechting is een sterke, emotionele en blijvende verbinding tussen mensen die in de loop van tijd en omstandigheden standhoudt, zoals de band tussen een ouder en een kind.', "Assimilatie is het proces waarbij nieuwe informatie wordt opgenomen in bestaande schema's. Bijvoorbeeld, een kind dat een hond als 'huisdier' kent, kan een kat ook als 'huisdier' classificeren.", "Accommodatie is het proces waarbij een nieuw schema wordt gecreëerd of een bestaand schema aanzienlijk wordt aangepast om nieuwe informatie op te nemen die anders niet zou passen. Bijvoorbeeld, een kind kan zijn begrip van 'hond' aanpassen om ook honden van verschillende rassen en groottes te omvatten.", "De sensorimotorische fase is de eerste fase van Piaget's cognitieve ontwikkeling, waarin baby's informatie verwerven via hun zintuigen en motorische vaardigheden. Reflexieve reacties ontwikkelen zich tot meer doelgerichte acties door de ontwikkeling van schema's.", "Objectpermanentie is het begrip dat objecten blijven bestaan, zelfs wanneer ze niet zichtbaar zijn. Een klassiek voorbeeld is het 'kiekeboe'-spelletje dat volwassenen met baby's spelen.", "De preoperationele fase is Piaget's tweede fase van cognitieve ontwikkeling, waarin kinderen symbolisch over objecten denken, maar redeneren op basis van intuïtie en oppervlakkige verschijningen. Bijvoorbeeld, een kind kan denken dat een lang, dun glas meer vloeistof bevat dan een kort, breed glas.", "De concreet-operationele fase is Piaget's derde fase van cognitieve ontwikkeling, waarin kinderen beginnen na te denken over en logische operaties te begrijpen, en niet worden misleid door verschijningen. Zo zullen ze begrijpen dat een glas water dat in een ander glas wordt gegoten dezelfde hoeveelheid water blijft.", "De formeel-operationele fase is Piaget's laatste fase van cognitieve ontwikkeling, waarin individuen abstract kunnen denken en hypotheses kunnen formuleren en testen door middel van deductieve logica. Dit stelt hen in staat om problemen te begrijpen en op te lossen die een abstract denkniveau vereisen.", 'Theorie van de geest is het vermogen om te begrijpen dat andere mensen mentale toestanden hebben die hun gedrag beïnvloeden. Bijvoorbeeld, het begrijpen dat een vriend boos zou kunnen zijn omdat hij een slechte dag heeft gehad, zelfs als de situatie voor jou niet boosmakend lijkt.', 'Het preconventionele niveau is het initiële stadium van morele ontwikkeling, waar moraliteit wordt bepaald door eigenbelang en de uitkomsten van gebeurtenissen. Een kind op dit niveau zou bijvoorbeeld denken dat iets verkeerd is als het leidt tot straf.', 'Het conventionele niveau is de tussenstap in de morele ontwikkeling waarbij moraliteit wordt bepaald door het naleven van maatschappelijke regels en het zoeken van goedkeuring van anderen. Een kind op dit niveau zou bijvoorbeeld iets niet stelen omdat het tegen de regels is en ze niet in de problemen willen komen.', 'Het postconventionele niveau is de laatste fase van de morele ontwikkeling waarbij moraliteit wordt bepaald door abstracte principes en de waarde van alle leven. Een persoon op dit niveau zou bijvoorbeeld niet stelen omdat ze geloven dat het fundamenteel onrechtvaardig is.', 'Inequity aversion is een voorkeur voor het vermijden van oneerlijkheid in beslissingen over de verdeling van middelen. Bijvoorbeeld, iemand zou liever een gelijk bedrag aan geld tussen twee mensen verdelen dan één persoon meer te geven dan de andere.', 'Puberteit is het begin van de adolescentie, gekenmerkt door het begin van seksuele rijpheid en daarmee het vermogen om te reproduceren. Het omvat veranderingen zoals groei spurts en de ontwikkeling van secundaire geslachtskenmerken.']

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