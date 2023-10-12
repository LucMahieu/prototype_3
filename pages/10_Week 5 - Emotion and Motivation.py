import streamlit as st
questions = ['Wat is een emotie?', 'Wat zijn primaire emoties?', 'Wat zijn secundaire emoties?', 'Wat houdt de James-Lange theorie in?', 'Wat houdt de Cannon-Bard theorie in?', 'Wat is de tweefactortheorie van emotie?', 'Wat zijn display rules?', 'Wat is ideal affect?', 'Wat is motivatie?', 'Wat is een behoefte?', 'Wat is de behoeftenhiërarchie volgens Maslow?', 'Wat is zelfactualisatie?', "Wat is een 'drive'?", 'Wat is homeostase?', 'Wat is de Yerkes-Dodson wet?', 'Wat zijn prikkels?', 'Wat is extrinsieke motivatie?', 'Wat is intrinsieke motivatie?', 'Wat is zelfeffectiviteit?', 'Wat is zelfregulatie?', 'Wat is de behoefte om te behoren?', 'Wat is de balanstheorie?', 'Wat is cognitieve dissonantie?', 'Wat is zelfbevestiging?', 'Wat zijn core values?']
answers = ['Een emotie is een onmiddellijke, specifieke negatieve of positieve reactie op omgevingsgebeurtenissen of interne gedachten. Bijvoorbeeld, blijdschap is een positieve reactie op een aangename gebeurtenis.', 'Primaire emoties zijn emoties die aangeboren, evolutionair adaptief en universeel zijn (gedeeld tussen culturen). Voorbeelden zijn woede, angst, vreugde en verdriet.', 'Secundaire emoties zijn mengsels van primaire emoties. Zo kan bijvoorbeeld schaamte worden gezien als een combinatie van angst en verdriet.', 'De James-Lange theorie stelt dat mensen specifieke patronen van lichamelijke reacties waarnemen en als gevolg van die waarneming emotie voelen.', 'De Cannon-Bard theorie stelt dat informatie over emotionele stimuli tegelijkertijd naar de cortex en het lichaam wordt gestuurd en resulteert in respectievelijk emotionele ervaring en lichamelijke reacties.', 'De tweefactortheorie stelt dat het label dat wordt toegepast op fysiologische opwinding resulteert in de ervaring van een emotie. Bijvoorbeeld, als je hart sneller klopt en iemand zegt dat je bang bent, dan zal je die opwinding waarschijnlijk als angst interpreteren.', 'Display rules zijn regels die we leren door socialisatie, die bepalen welke emoties geschikt zijn in bepaalde situaties. Bijvoorbeeld, in sommige culturen is het ongepast om verdriet in het openbaar te tonen.', 'Ideal affect verwijst naar de emotionele en affectieve toestanden die mensen willen ervaren of die culturen bijzonder waarderen. Bijvoorbeeld, sommige culturen waarderen kalmte meer dan opwinding.', 'Motivatie is een proces dat gedrag stimuleert, richt en onderhoudt met het oog op een doel. Het kan zijn dat je bijvoorbeeld studeert voor een examen om een goed cijfer te halen.', 'Een behoefte is een staat van biologische, sociale of psychologische tekortkoming. Bijvoorbeeld, honger is een biologische behoefte en behoefte aan sociale interactie is een sociale behoefte.', "Maslow's behoeftenhiërarchie stelt dat basisbehoeften voor overleving eerst moeten worden voldaan voordat mensen hogere behoeften kunnen bevredigen. Zoals, eerst moeten basisbehoeften zoals voedsel en onderdak worden voldaan voordat men kan streven naar zaken als zelfactualisatie.", 'Zelfactualisatie is een staat die wordt bereikt wanneer iemands persoonlijke dromen en aspiraties zijn gerealiseerd. Bijvoorbeeld, een kunstenaar kan zelfactualisatie bereiken door zijn/haar meesterwerk te creëren.', "Een 'drive' is een psychologische staat die, door opwinding te creëren, een organisme motiveert om een behoefte te bevredigen. Bijvoorbeeld, honger kan een 'drive' zijn om voedsel te zoeken.", 'Homeostase is de neiging van lichaamsfuncties om een evenwicht te behouden. Zoals, ons lichaam reguleert zijn interne temperatuur ongeacht de externe temperatuur.', 'De Yerkes-Dodson wet is het psychologische principe dat stelt dat de prestaties op uitdagende taken toenemen met opwinding tot een gematigd niveau. Daarna belemmert extra opwinding de prestaties. Bijvoorbeeld, een beetje stress kan nuttig zijn voor een examen, maar te veel stress kan de prestaties belemmeren.', 'Prikkels zijn externe objecten of externe doelen, in plaats van interne drives, die gedragingen motiveren. Zoals, een financiële beloning kan een prikkel zijn om hard te werken.', 'Extrinsieke motivatie is de drijfveer om een activiteit uit te voeren vanwege de externe doelen die met die activiteit zijn verbonden. Bijvoorbeeld, studeren voor een examen om een goed cijfer te halen.', 'Intrinsieke motivatie is de drijfveer om een activiteit uit te voeren vanwege de waarde of het plezier dat aan die activiteit wordt geassocieerd, niet vanwege een duidelijk extern doel. Bijvoorbeeld, het lezen van een boek omdat je geniet van het verhaal.', 'Zelfeffectiviteit is het geloof dat inspanningen om een doel te bereiken succesvol zullen zijn. Het is een belangrijk aspect van motivatie en zelfvertrouwen.', 'Zelfregulatie is het proces waarbij mensen hun gedrag sturen naar het bereiken van doelen. Zoals het volgen van een dieet of studieplanning om een bepaald doel te bereiken.', 'De behoefte om te behoren is de behoefte aan interpersoonlijke verbindingen, een fundamentele drijfveer die zich heeft ontwikkeld voor adaptieve doeleinden. Zoals het verlangen om deel uit te maken van een groep of gemeenschap.', 'De balanstheorie stelt dat mensen gemotiveerd zijn om harmonie in hun interpersoonlijke relaties te bereiken. Een triade is in balans als alle relaties in dezelfde richting gaan of als twee relaties negatief zijn en één positief.', 'Cognitieve dissonantie is het onaangename gevoel bij het besef van twee tegenstrijdige overtuigingen of een overtuiging die in conflict is met een gedrag. Bijvoorbeeld, het geloven in dierenrechten maar toch vlees eten.', 'Zelfbevestiging is de behoefte aan een gevoel van zelf dat coherent en stabiel is. Het kan worden bereikt door zelfreflectie en affirmaties die de eigen waarden en overtuigingen bevestigen.', 'Core values zijn sterk aangehouden overtuigingen over de blijvende principes die het meest belangrijk en betekenisvol zijn. Ze bevorderen emoties en acties wanneer ze worden opgeroepen of bedreigd. Een voorbeeld is eerlijkheid, die een individu kan motiveren om de waarheid te spreken, zelfs in moeilijke situaties.']

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