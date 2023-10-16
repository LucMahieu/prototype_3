import streamlit as st
questions = ['Wat is cognitie?', 'Wat is denken in psychologische termen?', 'Wat zijn analoge representaties?', 'Wat zijn symbolische representaties?', 'Wat is een concept?', 'Wat is het prototype-model?', 'Wat is het exemplar-model?', 'Wat is een script in psychologische termen?', 'Wat zijn stereotypes?', 'Wat is bevestigingsbias?', 'Wat is hindsight bias?', 'Wat is verliesaversie?', 'Wat is het endowment effect?', 'Wat is het appraisal tendency framework?', "Wat betekent 'overcoming obstacles to solutions'?", "Wat betekent 'use an algorithm'?", "Wat betekent 'working backward'?", "Wat is de strategie 'working backward' bij het overwinnen van obstakels?", 'Wat betekent het om een probleemoplossende strategie over te dragen?', "Wat zijn 'maximizing' en 'satisficing' in besluitvorming?", 'Wat zijn de vocale akkoorden?', 'Wat is de orale holte?', 'Hoe worden geluiden geproduceerd?', "Wat is Broca's afasie?", 'Wat is Receptieve afasie/Wernicke’s afasie?', 'Wat is gezamenlijke aandacht?', 'Wat is overgeneralisatie in taalontwikkeling?', 'Wat is Universele grammatica?']
answers = ['Cognitie verwijst naar mentale activiteiten zoals denken en het begrijpen dat voortkomt uit denken. Het omvat processen zoals leren, geheugen, aandacht en probleemoplossing.', 'Denken is het mentaal manipuleren van kennisrepresentaties over de wereld. Het kan letterlijk worden gezien als het "praten met onszelf" in onze geest.', 'Analoge representaties zijn mentale representaties die enkele van de fysieke kenmerken van de objecten die ze representeren bezitten. Een mentaal beeld van een appel, waarbij je de vorm en kleur voorstelt, is een voorbeeld van een analoge representatie.', 'Symbolische representaties zijn abstracte mentale representaties die niet overeenkomen met de fysieke kenmerken van objecten of ideeën. Het woord "appel" dat een fysieke appel representeert, is een voorbeeld van een symbolische representatie.', 'Een concept is een categorie of klasse van gerelateerde items, waarbij mentale representaties van die items betrokken zijn. Het concept "fruit" bevat bijvoorbeeld items zoals appels, peren en bananen.', 'Het prototype-model is een theorie die stelt dat er binnen elke categorie een standaardvoorbeeld of prototype is dat de meest typische kenmerken van die categorie belichaamt. Bijvoorbeeld, voor de categorie "vogels" zou de roodborst een typisch prototype kunnen zijn.', 'Het exemplar-model is een model waarbij alle leden van een categorie voorbeelden (exemplaren) zijn en samen het concept vormen en de lidmaatschap van de categorie bepalen. In dit model zou elke individuele vogel die je hebt gezien bijdragen aan je begrip van de categorie "vogels".', "Een script is een schema dat gedrag en verwachtingen over tijd binnen een bepaalde situatie stuurt. Bijvoorbeeld, het script voor naar een restaurant gaan zou kunnen bevatten: een tafel zoeken, menu's ontvangen, eten bestellen, eten, betalen en vertrekken.", 'Stereotypes zijn cognitieve schema\'s die snelle en efficiënte informatie verwerking over mensen mogelijk maken op basis van hun lidmaatschap in bepaalde groepen. Bijvoorbeeld, het idee dat "alle Nederlanders houden van fietsen" is een stereotype.', 'Bevestigingsbias is de neiging om alleen te focussen op informatie die overeenkomt met onze bestaande overtuigingen. Bijvoorbeeld, als iemand gelooft dat katten onvriendelijk zijn, kunnen ze neigen om alleen gevallen waarin katten agressief of afstandelijk zijn op te merken en te onthouden.', 'Hindsight bias is een fout in redenering waarbij mensen, na een gebeurtenis, verklaringen creëren die suggereren dat ze de uitkomst vooraf hadden kunnen voorspellen. Een voorbeeld hiervan is mensen die beweerden te hebben geweten dat Donald Trump Clinton zou verslaan, wijzend op Clintons eerdere nederlagen.', 'Verliesaversie is de neiging van mensen om verliezen zwaarder te wegen dan winsten bij het nemen van beslissingen. Bijvoorbeeld, mensen zijn over het algemeen meer bezorgd over de kosten van iets dan over de voordelen ervan.', 'Het endowment effect is de neiging om dingen die we bezitten meer te waarderen dan wat we ervoor zouden betalen. Het idee is dat het bezitten van iets het in onze geest met extra waarde bekleedt. Bijvoorbeeld, de prijs die mensen vragen om een object te verkopen dat ze bezitten, is vaak hoger dan wat ze bereid zouden zijn te betalen om hetzelfde object te kopen.', 'Het appraisal tendency framework stelt dat stemmingen neigingen oproepen, zoals de wens om naar iets toe te bewegen of ervan weg te bewegen. Deze stemming-gerelateerde neigingen beïnvloeden hoe we ongerelateerde informatie en keuzes beoordelen. Bijvoorbeeld, positieve stemmingen maken mensen optimistischer over hun kansen om de loterij te winnen.', "'Overcoming obstacles to solutions' verwijst naar verschillende strategieën om problemen aan te pakken en op te lossen, zoals het formuleren van subdoelen, herstructurering, het gebruik van een algoritme, achteruit werken, het gebruik van een analogie of wachten op een plotseling inzicht.", "'Use an algorithm' verwijst naar het gebruik van een set regels of instructies die, indien correct gevolgd, altijd tot het juiste antwoord leiden. Bijvoorbeeld, om het oppervlak van een rechthoek te vinden, kun je de lengte vermenigvuldigen met de breedte - dit is een algoritme omdat het altijd werkt.", "'Working backward' is een probleemoplossende strategie waarbij je begint bij het gewenste eindresultaat en dan stappen terugneemt om te bepalen welke acties nodig zijn om dat resultaat te bereiken. Het is vooral nuttig bij complexe problemen waarbij de oplossing duidelijk is, maar de stappen om er te komen dat niet zijn.", "'Working backward' is een strategie waarbij je, als de juiste stappen voor het oplossen van een probleem niet duidelijk zijn, van het doel naar de beginsituatie werkt om een oplossing te vinden. Bijvoorbeeld bij het waterlelie probleem, waarbij je van het einddoel (het meer vol waterlelies) terugwerkt naar de startsituatie (één waterlelie).", 'Het overdragen van een probleemoplossende strategie betekent het gebruik van een strategie die in één context werkt om een probleem op te lossen dat structureel vergelijkbaar is. Dit vereist aandacht voor de structuur van elk probleem en kan verbeterd worden door het oplossen van meerdere vergelijkbare problemen.', "'Maximizing' is het streven naar de perfecte keuze uit een reeks opties, terwijl 'satisficing' het zoeken naar een 'goed genoeg' keuze is die voldoet aan minimale eisen.", 'De vocale akkoorden zijn plooien van slijmvliesmembranen die deel uitmaken van het strottenhoofd, een orgaan in de nek, vaak de stemkast genoemd.', 'De orale holte is het deel van de mond achter de tanden en boven de tong.', 'Mensen spreken door lucht door de vocale akkoorden te dwingen. De lucht gaat van de vocale akkoorden naar de orale holte. Daar veranderen kaak-, lip- en tongbewegingen de vorm van de mond en de stroom van de lucht, waardoor de geluiden die door de vocale akkoorden worden geproduceerd, veranderen.', "Broca's afasie is een aandoening veroorzaakt door een laesie in de linker frontale kwab, waardoor het vermogen om te spreken wordt onderbroken. Hoewel deze individuen over het algemeen begrijpen wat er tegen hen wordt gezegd en ze hun lippen en tongen kunnen bewegen, kunnen ze geen woorden vormen of samenstellen tot een zin.", "Receptieve afasie, ook bekend als Wernicke's afasie, ontstaat wanneer het Wernicke-gebied is beschadigd. Patiënten hebben dan moeite met het begrijpen van de betekenis van woorden. Ze zijn vaak zeer verbaal, maar wat ze zeggen volgt niet de grammaticaregels of heeft geen zin.", 'Gezamenlijke aandacht is een vroege interactie met verzorgers die de basis legt voor de taalverwerving van kinderen. Als bijvoorbeeld de verzorger naar het speelgoed kijkt en een nieuwe naam zegt, zoals "dax", zal het kind de naam "dax" aan het speelgoed toewijzen.', 'Overgeneralisatie treedt op wanneer kinderen nieuwe grammaticaregels die ze leren overtoepassen. Bijvoorbeeld, als ze leren dat het toevoegen van "-ed" een werkwoord in de verleden tijd zet, voegen ze "-ed" toe aan elk werkwoord, inclusief onregelmatige werkwoorden die die regel niet volgen. Dus ze kunnen zeggen "runned" of "holded" hoewel ze op jongere leeftijd misschien "ran" of "held" zeiden.', 'Universele grammatica is een theorie die stelt dat de structuur van een taal inherent is aan het menselijk brein. Het idee is dat alle mensen geboren worden met een aangeboren vermogen om taal te leren en te gebruiken, ongeacht de specifieke taal die ze leren.']

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