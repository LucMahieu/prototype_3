import streamlit as st
questions = ['Wat is een actiepotentiaal?', 'Wat is de rustmembraanpotentiaal?', 'Wat is de relatieve refractaire periode?', 'Wat is het alles-of-niets principe?', 'Wat is de absolute refractaire periode?', 'Wat is de myelineschede?', 'Wat zijn de knopen van Ranvier?', 'Wat zijn neurotransmitters?', 'Wat zijn receptoren in neuronen?', 'Wat is reuptake bij neurotransmitters?', 'Wat is het Broca-gebied in de hersenen?', 'Wat is elektro-encefalografie (EEG)?', 'Wat is positronemissietomografie (PET)?', 'Wat is magnetische resonantie beeldvorming (MRI)?', 'Wat is functionele magnetische resonantie beeldvorming (fMRI)?', 'Wat is transcraniële magnetische stimulatie (TMS)?', 'Wat is de cerebrale cortex?', 'Wat is het corpus callosum?', 'Wat zijn de occipitale lobben?', 'Wat zijn de pariëtale lobben?', 'Wat zijn de temporale lobben?', 'Wat zijn de frontale lobben?', 'Wat is de prefrontale cortex?', 'Wat is een "split brain"?', 'Wat is de insula in de hersenen?', 'Wat is de functie van de thalamus?', 'Wat is de hypothalamus en wat doet het?', 'Wat is de functie van de hippocampus?', 'Wat is de functie van de amygdala?', 'Wat zijn de basale ganglia?', 'Wat is de hersenstam en wat doet het?', 'Wat is de cerebellum en wat doet het?', 'Wat is het somatische zenuwstelsel (SNS)?', 'Wat is het autonome zenuwstelsel (ANS)?', 'Wat is het sympathische zenuwstelsel?', 'Wat is het parasympathische zenuwstelsel?', 'Wat is het endocriene systeem?', 'Wat zijn hormonen?', 'Wat is de hypofyse?', 'Wat zijn neurale netwerken?', 'Wat zijn sensorische neuronen?', 'Wat zijn somatosensore zenuwen?', 'Wat zijn motorneuronen?', 'Wat zijn interneuronen?', 'Wat zijn reflexen?', 'Wat zijn ionkanalen?', 'Wat zijn ionen?', 'Wat is een membraan in een neuron?', 'Wat is een gepolariseerd neuron?', 'Wat is ionenstroom in neuronen?', 'Wat is een natrium-kaliumpomp in neuronen?', 'Wat zijn excitatoire signalen in neuronen?', 'Wat zijn inhiberende signalen in neuronen?', 'Wat is het effect van excitatoire en inhiberende signalen in neuronen?', 'Wat is een actiepotentiaal in neuronen?', 'Wat is een presynaptische neuron?', 'Wat is een postsynaptische neuron?', 'Wat zijn de psychologische functies van de neurotransmitter Acetylcholine?', 'Wat zijn de psychologische functies van de neurotransmitter Norepinephrine?', 'Wat zijn de psychologische functies van de neurotransmitter Serotonine?', 'Wat zijn de psychologische functies van de neurotransmitter Dopamine?', 'Wat houdt de binding van een neurotransmitter in?', 'Wat is enzymdeactivatie?', 'Wat is autoreceptie?', 'Wat zijn agonisten?', 'Wat zijn antagonisten?', 'Wat is event-related potential (ERP)?', 'Wat is het voorbrein?', 'Wat is grijze stof?', 'Wat is witte stof?', 'Wat is de primaire somatosensorische cortex?', 'Wat is een somatosensorische homunculus?', 'Wat is de primaire auditieve cortex?', 'Wat is de primaire motorische cortex?', 'Wat is de nucleus accumbens?']
answers = ['Actiepotentiaal is het elektrische signaal dat langs het axon reist en de afgifte van chemicaliën uit de eindknoppen veroorzaakt. Het is de manier waarop informatie door het zenuwstelsel wordt verzonden.', "De rustmembraanpotentiaal is de elektrische lading van een neuron wanneer het niet actief is. Het is een soort 'stand-by' staat voor neuronen, klaar om geactiveerd te worden.", 'De relatieve refractaire periode is een korte periode na een actiepotentiaal waarin het neuron hypergepolariseerd is, waardoor het moeilijker wordt om opnieuw te vuren. Dit helpt de richting van de signaaloverdracht te behouden.', 'Het alles-of-niets principe stelt dat wanneer een neuron vuurt, het altijd met dezelfde potentie vuurt. Een neuron vuurt of vuurt niet, hoewel de frequentie van vuren kan variëren.', 'De absolute refractaire periode is een korte periode na een actiepotentiaal waarin het ionenkanaal niet opnieuw kan reageren. Dit voorkomt dat het neuron in snel opeenvolgende volgorde vuurt.', 'De myelineschede is een vetachtig materiaal, gemaakt door gliacellen, dat sommige axonen isoleert om een snellere beweging van elektrische impulsen langs het axon mogelijk te maken. Dit helpt snellere signaaloverdracht binnen het zenuwstelsel.', "De knopen van Ranvier zijn kleine openingen tussen segmenten van de myelineschede waar actiepotentialen plaatsvinden. Ze werken als 'oplaadstations' voor de actiepotentiaal om de signaalsterkte te behouden.", 'Neurotransmitters zijn chemische stoffen die signalen overdragen tussen neuronen. Voorbeelden zijn serotonine en dopamine, die respectievelijk betrokken zijn bij stemming en beloning.', 'Receptoren zijn gespecialiseerde eiwitmoleculen op de postsynaptische membraan van neuronen. Neurotransmitters binden aan deze moleculen nadat ze de synaps zijn overgestoken.', 'Reuptake is het proces waarbij een neurotransmitter wordt teruggenomen in de presynaptische terminalknoppen, waardoor de activiteit ervan stopt.', 'Het Broca-gebied is een klein deel van de linker frontale regio van de hersenen, cruciaal voor de productie van taal. Schade aan dit gebied kan leiden tot problemen met spreken en schrijven.', 'Elektro-encefalografie (EEG) is een techniek voor het meten van elektrische activiteit in de hersenen. Het wordt vaak gebruikt om abnormaliteiten zoals epilepsie te detecteren.', 'Positronemissietomografie (PET) is een beeldvormingstechniek die de metabolische activiteit beoordeelt door een radioactieve stof in de bloedbaan te injecteren. Het kan bijvoorbeeld worden gebruikt om tumoren te detecteren.', 'Magnetische resonantie beeldvorming (MRI) is een beeldvormingstechniek die een krachtig magnetisch veld gebruikt om hoogwaardige beelden van de hersenen te produceren.', 'Functionele magnetische resonantie beeldvorming (fMRI) is een beeldvormingstechniek die veranderingen in de activiteit van de werkende menselijke hersenen onderzoekt door veranderingen in de zuurstofniveaus van het bloed te meten.', "Transcraniële magnetische stimulatie (TMS) is het gebruik van sterke magneten om de normale hersenactiviteit kortstondig te onderbreken als een manier om hersenregio's te bestuderen. Het wordt bijvoorbeeld gebruikt bij onderzoek naar depressie.", 'De cerebrale cortex is de buitenste laag van het hersenweefsel die verantwoordelijk is voor alle gedachten, percepties en complexe gedragingen. Het is als het ware het "denkcentrum" van de hersenen.', 'Het corpus callosum is een brug van miljoenen axonen die de hersenhelften verbindt en informatie-uitwisseling tussen hen mogelijk maakt. Het speelt een cruciale rol in de communicatie tussen beide hersenhelften.', 'De occipitale lobben zijn gebieden in de cerebrale cortex aan de achterkant van de hersenen die belangrijk zijn voor het zicht. Schade aan deze gebieden kan bijvoorbeeld problemen met het zien veroorzaken.', 'De pariëtale lobben zijn gebieden in de cerebrale cortex die belangrijk zijn voor het gevoel van aanraking en aandacht voor de omgeving. Ze liggen voor de occipitale lobben en achter de frontale lobben.', 'De temporale lobben zijn gebieden in de cerebrale cortex die belangrijk zijn voor het verwerken van auditieve informatie, geheugen en de perceptie van objecten en gezichten. Ze liggen onder de pariëtale lobben en voor de occipitale lobben.', 'De frontale lobben zijn gebieden in de cerebrale cortex aan de voorkant van de hersenen die belangrijk zijn voor beweging en hogere psychologische processen geassocieerd met de prefrontale cortex.', 'De prefrontale cortex is het voorste deel van de frontale lobben, vooral prominent bij mensen. Deze is belangrijk voor aandacht, werkgeheugen, besluitvorming, passend sociaal gedrag en persoonlijkheid.', 'Een "split brain" is een toestand die optreedt wanneer het corpus callosum chirurgisch wordt doorgesneden, waardoor de twee hersenhelften niet direct informatie van elkaar ontvangen. Dit kan leiden tot unieke gedragsveranderingen en waarnemingen.', 'De insula is een deel van de hersenschors dat zich bevindt in een diepe groef en speelt een belangrijke rol bij smaak, pijn, waarneming van lichamelijke toestanden en empathie.', 'De thalamus fungeert als de poort naar de hersenen en ontvangt bijna alle binnenkomende sensorische informatie voordat deze de cortex bereikt.', 'De hypothalamus is een hersenstructuur die betrokken is bij de regulatie van lichaamsfuncties, zoals lichaamstemperatuur, lichaamsritmes, bloeddruk en bloedglucosespiegels, en beïnvloedt onze basis-gemotiveerde gedragingen.', 'De hippocampus is een hersenstructuur die geassocieerd is met het vormen van herinneringen.', 'De amygdala is een hersenstructuur die een cruciale rol speelt in het leren associëren van dingen met emotionele reacties en in het verwerken van emotionele informatie.', 'De basale ganglia zijn een systeem van subcorticale structuren die belangrijk zijn voor de planning en productie van bewegingen.', 'De hersenstam is een verlengstuk van het ruggenmerg en huisvest structuren die functies regelen die geassocieerd zijn met overleving, zoals hartslag, ademhaling, slikken, overgeven, plassen en orgasme.', 'Het cerebellum is een grote, ingewikkelde uitstulping aan de achterkant van de hersenstam en is essentieel voor gecoördineerde beweging en evenwicht.', 'Het somatische zenuwstelsel is een component van het perifere zenuwstelsel dat sensorische en motorische signalen tussen het centrale zenuwstelsel en de huid, spieren en gewrichten overbrengt. Het is bijvoorbeeld betrokken bij vrijwillige bewegingen zoals het optillen van een voorwerp.', 'Het autonome zenuwstelsel is een component van het perifere zenuwstelsel dat sensorische en motorische signalen tussen het centrale zenuwstelsel en de lichaamsklieren en interne organen overbrengt. Het regelt onbewuste functies zoals de hartslag en spijsvertering.', "sympathische zenuwstelsel is een onderdeel van het autonome zenuwstelsel dat het lichaam voorbereidt op actie. Het activeert 'fight-or-flight' reacties in respons op stress of dreiging.", "Het parasympathische zenuwstelsel is een onderdeel van het autonome zenuwstelsel dat het lichaam terugbrengt naar zijn rusttoestand. Het bevordert rust, spijsvertering en energie-opslag na een 'fight-or-flight' reactie.", 'Het endocriene systeem is een communicatiesysteem dat hormonen gebruikt om gedachten, gedragingen en acties te beïnvloeden. Het regelt bijvoorbeeld de stofwisseling, groei en ontwikkeling, en stemming.', 'Hormonen zijn chemische stoffen die door endocriene klieren worden vrijgegeven en via de bloedbaan naar doelweefsels reizen. Deze weefsels worden vervolgens beïnvloed door de hormonen. Insuline is een voorbeeld van een hormoon dat de bloedsuikerspiegel reguleert.', "De hypofyse is een klier aan de basis van de hypothalamus die hormonale signalen naar andere endocriene klieren stuurt en hun hormoonafgifte regelt. Het wordt vaak de 'meesterklier' genoemd omdat het veel lichaamsfuncties regelt via dit hormonale netwerk.", 'Neurale netwerken zijn circuits die ontstaan door selectieve communicatie tussen neuronen. Ze ontwikkelen zich door genetische invloed, rijping, ervaring en herhaaldelijk vuren. Een neuron kan communiceren met tienduizenden andere neuronen.', 'Sensorische neuronen detecteren informatie uit de fysieke wereld en geven die informatie door aan de hersenen. Een voorbeeld is wanneer je iets heets aanraakt of jezelf per ongeluk prikt met een scherp object, de signalen triggeren een bijna onmiddellijke reactie.', 'Somatosensore zenuwen zijn sensorische zenuwen die informatie van de huid en spieren leveren. Ze zijn verantwoordelijk voor sensaties die van binnen het lichaam worden ervaren.', 'Motorneuronen sturen spieren aan om te samentrekken of te ontspannen, waardoor beweging ontstaat. Bijvoorbeeld, bij het opheffen van een arm zijn motorneuronen betrokken.', 'Interneuronen werken als doorgeefstations die communicatie tussen sensorische en motorneuronen vergemakkelijken. Ze spelen een cruciale rol in de reflexen van ons lichaam.', 'Reflexen zijn onze automatische motorische reacties die optreden voordat we zelfs aan die reacties denken. Ze converteren sensatie in actie met slechts een handvol neuronen, zoals wanneer we onze hand snel wegtrekken na het aanraken van een heet voorwerp.', 'Ionkanalen zijn gespecialiseerde poriën die het passeren van ionen door de cel mogelijk maken wanneer de neuron signalen over de axon zendt. Elk kanaal is specifiek voor een bepaald type ion, bijvoorbeeld natriumkanalen laten alleen natriumionen door.', 'Ionen zijn elektrisch geladen moleculen, sommige negatief en sommige positief geladen. Twee soorten ionen die bijdragen aan de rustpotentiaal van een neuron zijn natriumionen en kaliumionen.', 'Het membraan is het buitenoppervlak van een neuron, een vettige barrière die niet oplost in de waterige omgeving binnen en buiten het neuron. Het is selectief permeabel, wat betekent dat sommige stoffen door het membraan kunnen bewegen, terwijl andere dat niet kunnen. Het membraan speelt een belangrijke rol in de communicatie tussen neuronen door de concentratie van elektrisch geladen moleculen te reguleren.', 'Een gepolariseerd neuron heeft in zijn rusttoestand een negatieve lading binnenin ten opzichte van buiten, wat de "rustpotentiaal" wordt genoemd. Deze lading ontstaat door een balans van verschillende ionen aan weerszijden van het celmembraan. Wanneer deze balans verandert en het neuron depolariseert, kan dit leiden tot het vuren van een actiepotentiaal.', 'Ionen passeren het neuronmembraan via de ionkanalen. De stroom van ionen door elk kanaal wordt gecontroleerd door een gating-mechanisme. Wanneer een gate open is, stromen ionen in en uit het neuron door het celmembraan. De selectieve permeabiliteit van het celmembraan beïnvloedt ook de ionenstroom.', 'De natrium-kaliumpomp is een mechanisme in het membraan dat bijdraagt aan de polarisatie. Deze pomp verhoogt de hoeveelheid kalium en vermindert de hoeveelheid natrium in het neuron, waardoor de rustpotentiaal van het membraan behouden blijft.', 'Excitatoire signalen zijn een van de twee soorten signalen die de dendrieten bereiken. Ze depolariseren het celmembraan, waardoor de polarisatie afneemt door de negatieve lading binnen de cel te verminderen ten opzichte van buiten de cel. Door depolarisatie verhogen deze signalen de kans dat het neuron zal vuren.', 'Inhiberende signalen zijn een van de twee soorten signalen die de dendrieten bereiken. Ze hyperpolariseren de cel door de negatieve lading binnen de cel te verhogen ten opzichte van buiten de cel. Door hyperpolarisatie verminderen deze signalen de kans dat het neuron zal vuren.', 'Excitatoire en inhiberende signalen worden gecombineerd binnen het neuron. Normaal gesproken wordt een neuron bestookt met duizenden excitatoire en inhiberende signalen en wordt het vuren ervan bepaald door het aantal en de frequentie van deze signalen. Als de som van excitatoire en inhiberende signalen leidt tot een positieve verandering in voltage die de vuurdrempel van het neuron overschrijdt, wordt een actiepotentiaal gegenereerd.', 'Het begint met een negatieve elektrische lading binnen het neuron ten opzichte van buiten. Wanneer het neuron vuurt, laat het meer positieve ionen binnen (depolarisatie), wat resulteert in een omkering van de polariteit. Het keert dan terug naar zijn licht negatieve rusttoestand. Dit gebeurt bij elk deel van de blootgestelde axon terwijl de actiepotentiaal zich voortbeweegt langs de axon.', 'Een presynaptische neuron is de neuron die het signaal verstuurt. In een communicatieproces tussen twee neuronen, is dit de zender.', 'Een postsynaptische neuron is de neuron die het signaal ontvangt. In een communicatieproces tussen twee neuronen, is dit de ontvanger.', 'Acetylcholine is betrokken bij motorische controle over spieren en speelt een rol bij leren, geheugen, slaap en dromen.', 'Norepinephrine, ook wel noradrenaline genoemd, is betrokken bij arousal, waakzaamheid en aandacht.', 'Serotonine reguleert emotionele toestanden en impulsiviteit en speelt een rol bij het dromen.', 'Dopamine is betrokken bij beloning en motivatie. Het is bijvoorbeeld essentieel in het plezier dat we ervaren tijdens het eten of sociale interactie.', 'De binding van een neurotransmitter vindt plaats nadat deze is vrijgegeven in de synaps en zich hecht, of bindt, aan receptoren op de dendrieten van de postsynaptische neuron. Deze binding kan ionkanalen doen openen of strakker sluiten, wat een excitatoir of inhibitoir signaal in de postsynaptische neuron produceert.', 'Enzymdeactivatie treedt op wanneer een enzym de neurotransmitter in de synaps vernietigt. Verschillende enzymen breken verschillende neurotransmitters af. Dit speelt een belangrijke rol in het beëindigen van de signaaloverdracht tussen neuronen.', 'Autoreceptie is een proces waarbij neurotransmitters binden aan receptoren op het presynaptische neuron. Autoreceptoren houden bij hoeveel neurotransmitters in de synaps zijn vrijgegeven. Wanneer een overmaat wordt gedetecteerd, geven de autoreceptoren een signaal aan het presynaptische neuron om te stoppen met het vrijgeven van de neurotransmitter.', 'Agonisten zijn geneesmiddelen en toxines die de werking van neurotransmitters versterken. Een agonist helpt de postsynaptische neuron om herhaaldelijk te reageren door de werking van de neurotransmitter te verhogen. Cafeïne is bijvoorbeeld een agonist die de werking van de neurotransmitter adenosine blokkeert.', 'Antagonisten zijn geneesmiddelen en toxines die de acties van neurotransmitters remmen. Een antagonist werkt tegen de neurotransmitter en vermindert de werking ervan. Een voorbeeld is naloxon, dat wordt gebruikt om de effecten van opioïden te blokkeren.', 'ERP is een methode om te meten hoe de hersenactiviteit verandert in reactie op een specifieke stimulus. Omdat deze methode onderzoekers in staat stelt om patronen te observeren die geassocieerd zijn met specifieke gebeurtenissen, wordt het event-related potential genoemd. ERPs geven informatie over de snelheid en timing van de hersenverwerking, maar het is moeilijk om te bepalen waar in de hersenen deze processen plaatsvinden.', 'Het voorbrein is het grootste deel van de menselijke hersenen. Het bestaat uit de hersenschors en onderliggende subcorticale gebieden en bestaat uit twee hemisferen.', 'Grijze stof is de buitenste laag van de hersenschors, die voornamelijk bestaat uit cellichamen, dendrieten en niet-gemyeliniseerde axonen van neuronen. Deze communiceren alleen met nabijgelegen neuronen.', 'Witte stof bevindt zich onder de grijze stof en bestaat voornamelijk uit axonen en de vette myelinescheden die hen omringen. Deze gemyeliniseerde axonen reizen tussen verschillende hersengebieden.', 'De primaire somatosensorische cortex is een strook aan de voorkant van de pariëtale kwab die langs de centrale fissuur loopt. Deze cortex groepeert nabijgelegen sensaties. Zo liggen bijvoorbeeld de sensaties van de vingers dicht bij de sensaties van de handpalm. Dit resulteert in de somatosensorische homunculus.', 'Een somatosensorische homunculus is een vervormde representatie van het hele lichaam (de term is Grieks voor "kleine man"). Het is vervormd omdat meer corticaal gebied is toegewijd aan gevoeligere delen van het lichaam, zoals het gezicht en de vingers.', 'De primaire auditieve cortex bevindt zich in de temporale lobben en is het hersengebied dat verantwoordelijk is voor het horen.', 'De primaire motorische cortex bevindt zich in het achterste deel van de frontale lobben en bevat neuronen die direct naar het ruggenmerg projecteren om de spieren van het lichaam te bewegen. De verantwoordelijkheden zijn verdeeld over het midden van het lichaam. Bijvoorbeeld, de linkerhersenhelft controleert de rechterarm, terwijl de rechterhersenhelft de linkerarm controleert.', 'De nucleus accumbens, gelegen in de basale ganglia, speelt een belangrijke rol in het ervaren van beloning en het motiveren van gedrag. Bijna elke plezierige ervaring (van het eten van voedsel dat je lekker vindt tot het kijken naar een persoon die je aantrekkelijk vindt) gaat gepaard met dopamine-activiteit in de nucleus accumbens die je het object of de persoon waar je ervaring mee hebt, doet verlangen. Hoe gewenster objecten zijn, hoe meer ze de basisbeloningscircuits in onze hersenen activeren.']

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

# Two columns in which the flashcard navigation buttons are placed
col1, col2, col3 = sub_container.columns(3)
with col1:
    if st.button("Previous question", use_container_width=True):
        if st.session_state.card_index == 0:  # Als het de eerste vraag is, ga naar de laatste
            st.session_state.card_index = len(questions) - 1
        else:
            st.session_state.card_index -= 1
        st.session_state.show_answer = False

with col2:
    if st.button("Show Answer", use_container_width=True):
        st.session_state.show_answer = True
    else:
        st.session_state.show_answer = False

with col3:
    if st.button("Next question", use_container_width=True):
        st.session_state.card_index = (st.session_state.card_index + 1) % len(questions)  # Modulo zorgt ervoor dat het een carrousel wordt
        st.session_state.show_answer = False

if st.session_state.card_index < len(questions):
    st.subheader(questions[st.session_state.card_index])
    if st.session_state.show_answer is True:
        st.write(answers[st.session_state.card_index])
else:
    st.subheader("Great work! Do you want to Loop through the material again?")
    st.button("Reset deck")

# Update the progress bar according to the card number
card_progress.progress(st.session_state.card_index / len(questions))
