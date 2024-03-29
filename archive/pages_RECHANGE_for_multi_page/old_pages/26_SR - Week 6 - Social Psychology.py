import streamlit as st
questions = ['Wat is het outgroup homogeneity effect?', 'Wat houdt de sociale identiteitstheorie in?', 'Wat betekent ingroup favoritism?', 'Wat is groepspolarisatie?', 'Wat wordt bedoeld met groupthink?', 'Wat is sociale facilitatie?', 'Wat is sociaal loafing?', 'Wat is deïndividuatie?', 'Wat betekent conformiteit?', 'Wat is normatieve invloed?', 'Wat is informatieve invloed?', 'Wat zijn sociale normen?', 'Wat is gehoorzaamheid?', 'Wat is agressie?', 'Wat zijn prosociale gedragingen?', 'Wat is altruïsme?', 'Wat is inclusieve fitness?', 'Wat is het bystander intervention effect?', 'Wat zijn attitudes?', 'Wat is het mere exposure effect?', 'Wat zijn expliciete attitudes?', 'Wat zijn impliciete attitudes?', 'Wat is persuasie?', 'Wat is het elaboration likelihood model?', 'Wat is compliance?', 'Wat betekent nonverbaal gedrag?', 'Wat zijn attributies?', 'Wat zijn persoonlijke attributies?', 'Wat zijn situationele attributies?', 'Wat is de fundamentele attributiefout?', 'Wat is de actor/observer discrepancy?', 'Wat is vooroordeel?', 'Wat betekent discriminatie?', 'Wat is modern racisme?', 'Wat is stereotype dreiging?', 'Wat stelt de social brain hypothese voor?', 'Wat betekent reciprociteit?', 'Wat is de betekenis van transiviteit in sociale relaties?', 'Wat is het risky-shift effect?', 'Wat betekent het om geïndividualiseerd te zijn?', 'Wat zijn de vier soorten groepsinvloed?', 'Wat zijn enkele soorten groepsdynamiek?']
answers = ['Het outgroup homogeneity effect is de perceptie dat leden van een outgroup minder gevarieerd zijn dan leden van een ingroup. Dit kan leiden tot stereotypering en vooroordelen.', 'De sociale identiteitstheorie houdt in dat ingroups bestaan uit individuen die zichzelf zien als leden van dezelfde sociale categorie en trots halen uit hun groepslidmaatschap. Dit kan bijvoorbeeld betrekking hebben op nationaliteit, religie of een sportteam.', 'Ingroup favoritism is de neiging om positiever te oordelen over en privileges te verlenen aan leden van je eigen groep boven leden van een outgroup. Het kan leiden tot discriminatie en ongelijke behandeling.', 'Groepspolarisatie is de versterking van de heersende attitudes binnen een groep door discussie binnen die groep. Dit kan ertoe leiden dat een groep een extremer standpunt inneemt dan de individuele leden aanvankelijk hadden.', 'Groupthink is een fenomeen waarbij een groep suboptimale beslissingen neemt om de harmonie en samenhang binnen de groep te behouden. Het is vaak een probleem in situaties waar groepsdruk en conformiteit sterk zijn.', 'Sociale facilitatie is de verbetering van prestaties in aanwezigheid van anderen. Dit kan bijvoorbeeld gebeuren tijdens een sportwedstrijd of een openbaar spreekbeurt.', 'Sociaal loafing is de neiging om minder inspanning te leveren wanneer je in een groep werkt in vergelijking met alleen werken. Dit kan het groepsproductiviteit negatief beïnvloeden.', 'Deïndividuatie is een toestand van verminderd zelfbewustzijn en verzwakte naleving van persoonlijke normen wanneer men in een groep is. Het kan bijvoorbeeld leiden tot roekeloos gedrag tijdens rellen of online trollen.', 'Conformiteit is het aanpassen van je gedrag en meningen om overeen te stemmen met die van anderen of met de verwachtingen van anderen. Bijvoorbeeld, je kunt je kledingstijl aanpassen om beter te passen bij je vrienden.', 'Normatieve invloed betekent dat je je gedrag aanpast om in een groep te passen. Bijvoorbeeld, je kunt vlees eten op een barbecue om niet anders te lijken, ook al ben je vegetariër.', 'Informatieve invloed is het aanpassen van je gedrag omdat je gelooft dat het gedrag van anderen de correcte manier van reageren weerspiegelt. Bijvoorbeeld, in een nieuw restaurant volg je misschien de lokale klanten om te bepalen hoe je moet bestellen.', 'Sociale normen zijn de verwachte gedragsnormen die ons gedrag beïnvloeden. Bijvoorbeeld, het is een sociale norm om je hand op te steken als je een vraag wilt stellen in een klaslokaal.', 'Gehoorzaamheid is het opvolgen van de bevelen van een autoriteitsfiguur. Bijvoorbeeld, een soldaat die orders opvolgt van zijn commandant.', 'Agressie is gedrag dat bedoeld is om een ander individu te schaden. Bijvoorbeeld, iemand fysiek aanvallen is een vorm van agressie.', 'Prosociale gedragingen zijn acties die gunstig zijn voor anderen. Bijvoorbeeld, een oudere dame helpen haar boodschappen naar haar auto te dragen is een prosociaal gedrag.', 'Altruïsme is het bieden van hulp zonder enige openlijke beloning te verwachten. Bijvoorbeeld, een vreemdeling helpen die gevallen is zonder te verwachten dat ze je terugbetalen.', 'Inclusieve fitness richt zich op het adaptieve voordeel van genenoverdracht via kin selectie. Het draait niet enkel om persoonlijke overleving, maar ook om het ondersteunen van verwanten met gedeelde genen. Mieren voeden bijvoorbeeld de koningin en beschermen de eitjes, ondanks dat ze zichzelf niet voortplanten, waardoor hun genetisch materiaal indirect wordt doorgegeven.', 'Het bystander intervention effect verwijst naar de vermindering in hulpvaardig gedrag wanneer andere mensen aanwezig zijn. Dit kan bijvoorbeeld optreden in noodsituaties waarbij de aanwezigheid van een menigte de waarschijnlijkheid van hulp verminderd.', 'Attitudes zijn evaluaties van objecten, gebeurtenissen of ideeën. Ze beïnvloeden hoe we reageren op de wereld om ons heen, bijvoorbeeld het hebben van een positieve houding ten opzichte van recycling kan leiden tot milieuvriendelijk gedrag.', 'Het mere exposure effect is de toename in sympathie voor een stimulus na herhaalde blootstelling eraan. Bijvoorbeeld, als je een liedje steeds opnieuw hoort, is de kans groter dat je het leuk gaat vinden.', 'Expliciete attitudes zijn attitudes die een individu bewust kan rapporteren. Bijvoorbeeld, je kan bewust zeggen dat je een voorkeur hebt voor katten boven honden.', 'Impliciete attitudes zijn attitudes die onbewust invloed hebben op iemands gevoelens en gedrag. Ze zijn vaak moeilijker te herkennen en kunnen bijvoorbeeld leiden tot onbewuste vooroordelen.', 'Persuasie is een bewuste poging om iemands houding te veranderen via berichten. Dit kan op een centrale of perifere manier gebeuren. Bij de centrale aanpak verandert de houding door de inhoud van het bericht, zoals "je zou dit moeten geloven omdat...". Bij de perifere aanpak beïnvloedt het enkele feit dat een bericht bestaat de houding, zoals posters in een school die stemgedrag beïnvloeden.', 'Het elaboration likelihood model is een theorie die suggereert dat overtuigende berichten leiden tot veranderingen in attitudes via ofwel de centrale of perifere route. Dit hangt af van de mate waarin het individu nadenkt over de inhoud van de boodschap. Is de individu gemotiveerd en in de mogelijk om dit te doen, dan gaat het via de centrale route. Is een individu niet gemotiveerd of niet in de mogelijkheid, dan gaat het via de perifere route. ', 'Compliance verwijst naar de neiging om toe te geven aan de verzoeken van anderen. Het is bijvoorbeeld de reden waarom we vaak "ja" zeggen als iemand ons om een gunst vraagt.', 'Nonverbaal gedrag omvat communicatieve handelingen of gebaren, zoals gezichtsuitdrukkingen en bewegingen. Wanneer we bijvoorbeeld glimlachen, uit dat nonverbaal onze blijdschap.', 'Attributies zijn verklaringen die we geven voor de oorzaken van acties of gebeurtenissen. Zo kunnen we bijvoorbeeld zeggen dat iemand te laat kwam omdat hij/zij vastzat in het verkeer.', 'Persoonlijke attributies zijn interne kenmerken, zoals karaktereigenschappen of inspanningen, die worden gebruikt om iemands gedrag te verklaren. Bijvoorbeeld, als we zeggen dat iemand goed presteert omdat hij/zij hard werkt.', 'Situationele attributies verwijzen naar externe gebeurtenissen, zoals geluk of het weer, om iemands gedrag te verklaren. Bijvoorbeeld, het toeschrijven van iemands slechte humeur aan slecht weer.', 'De fundamentele attributiefout is de neiging om het gedrag van anderen toe te schrijven aan interne factoren, terwijl de invloed van situationele factoren wordt onderschat. Bijvoorbeeld, iemand als lui bestempelen omdat hij/zij een deadline heeft gemist zonder rekening te houden met mogelijke externe factoren.', 'De actor/observer discrepancy is de neiging om de eigen acties toe te schrijven aan situationele factoren, terwijl we de acties van anderen toeschrijven aan persoonlijke kenmerken. Bijvoorbeeld, als we te laat zijn, wijten we dat aan het verkeer, maar als iemand anders te laat is, zien we dat als onverantwoordelijk.', 'Vooroordeel verwijst naar negatieve overtuigingen, meningen en gevoelens die geassocieerd worden met een stereotype. Bijvoorbeeld, het idee dat alle mensen van een bepaalde nationaliteit lui zijn, is een vooroordeel.', 'Discriminatie is de ongelijke behandeling van mensen op basis van hun lidmaatschap van een bepaalde groep. Een voorbeeld is het niet aannemen van een gekwalificeerde kandidaat voor een baan, puur vanwege hun etnische achtergrond.', 'Modern racisme is een subtiele vorm van vooroordelen die hand in hand gaan met de afwijzing van openlijk racistische overtuigingen. Dit kan bijvoorbeeld blijken wanneer iemand zegt dat hij geen racist is, maar toch stereotypen over een bepaalde etnische groep gelooft.', 'Stereotype dreiging is de angst om beoordeeld te worden op basis van een negatief stereotype over de groep waartoe men behoort. Bijvoorbeeld, een vrouw die zich zorgen maakt dat haar prestaties in een wiskundetest zullen bevestigen dat vrouwen slecht zijn in wiskunde.', 'De social brain hypothese stelt dat primaten grote prefrontale cortexes hebben omdat ze leven in dynamische en complexe sociale groepen die in de loop van de tijd veranderen. Dit suggereert dat sociale interactie een belangrijke rol speelt in de evolutionaire ontwikkeling van de hersenen.', 'Reciprociteit impliceert dat als je iemand helpt, die persoon geneigd zal zijn om jou ook te helpen. Hetzelfde geldt als je iemand schade berokkent. Dit is een fundamenteel principe in sociale interacties en relaties.', 'Transitiviteit in sociale relaties betekent dat mensen over het algemeen dezelfde meningen delen als hun vrienden, inclusief het leuk vinden of niet leuk vinden van dezelfde mensen. Dit fenomeen versterkt sociale banden en groepscohesie.', 'Het risky-shift effect verwijst naar het fenomeen waarbij groepen vaak riskantere beslissingen nemen dan individuen. Dit kan verklaren waarom bijvoorbeeld bedrijfsbesturen relatief riskante investeringen kunnen doen die geen van de leden individueel zou hebben ondernomen.', 'Geïndividualiseerd zijn betekent dat we rondlopen met een gevoel van onszelf als individuen die verantwoordelijk zijn voor onze eigen acties. Het benadrukt het belang van persoonlijke autonomie en verantwoordelijkheid in menselijk gedrag.', 'De vier soorten groepsinvloed zijn groepsdynamiek, conformiteit, naleving en gehoorzaamheid. Deze concepten beschrijven de verschillende manieren waarop het gedrag van individuen kan worden beïnvloed door hun interactie met een groep.', 'Enkele soorten groepsdynamiek zijn het effect van loutere aanwezigheid, sociaal luieren en deïndividuatie. Deze verschijnselen beschrijven hoe de aanwezigheid en interactie binnen een groep het gedrag van individuen kan beïnvloeden.']


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