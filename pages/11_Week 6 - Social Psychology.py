import streamlit as st
questions = ['Wat is het outgroup homogeneity effect?', 'Wat houdt de sociale identiteitstheorie in?', 'Wat betekent ingroup favoritism?', 'Wat is groepspolarisatie?', 'Wat wordt bedoeld met groupthink?', 'Wat is sociale facilitatie?', 'Wat is sociaal loafing?', 'Wat is deïndividuatie?', 'Wat betekent conformiteit?', 'Wat is normatieve invloed?', 'Wat is informatieve invloed?', 'Wat zijn sociale normen?', 'Wat is gehoorzaamheid?', 'Wat is agressie?', 'Wat zijn prosociale gedragingen?', 'Wat is altruïsme?', 'Wat is inclusieve fitness?', 'Wat is het bystander intervention effect?', 'Wat zijn attitudes?', 'Wat is het mere exposure effect?', 'Wat zijn expliciete attitudes?', 'Wat zijn impliciete attitudes?', 'Wat is persuasie?', 'Wat is het elaboration likelihood model?', 'Wat is compliance?', 'Wat betekent nonverbaal gedrag?', 'Wat zijn attributies?', 'Wat zijn persoonlijke attributies?', 'Wat zijn situationele attributies?', 'Wat is de fundamentele attributiefout?', 'Wat is de actor/observer discrepancy?', 'Wat is vooroordeel?', 'Wat betekent discriminatie?', 'Wat is modern racisme?', 'Wat is stereotype dreiging?']
answers = ['Het outgroup homogeneity effect is de perceptie dat leden van een outgroup minder gevarieerd zijn dan leden van een ingroup. Dit kan leiden tot stereotypering en vooroordelen.', 'De sociale identiteitstheorie houdt in dat ingroups bestaan uit individuen die zichzelf zien als leden van dezelfde sociale categorie en trots halen uit hun groepslidmaatschap. Dit kan bijvoorbeeld betrekking hebben op nationaliteit, religie of een sportteam.', 'Ingroup favoritism is de neiging om positiever te oordelen over en privileges te verlenen aan leden van je eigen groep boven leden van een outgroup. Het kan leiden tot discriminatie en ongelijke behandeling.', 'Groepspolarisatie is de versterking van de heersende attitudes binnen een groep door discussie binnen die groep. Dit kan ertoe leiden dat een groep een extremer standpunt inneemt dan de individuele leden aanvankelijk hadden.', 'Groupthink is een fenomeen waarbij een groep suboptimale beslissingen neemt om de harmonie en samenhang binnen de groep te behouden. Het is vaak een probleem in situaties waar groepsdruk en conformiteit sterk zijn.', 'Sociale facilitatie is de verbetering van prestaties in aanwezigheid van anderen. Dit kan bijvoorbeeld gebeuren tijdens een sportwedstrijd of een openbaar spreekbeurt.', 'Sociaal loafing is de neiging om minder inspanning te leveren wanneer je in een groep werkt in vergelijking met alleen werken. Dit kan het groepsproductiviteit negatief beïnvloeden.', 'Deïndividuatie is een toestand van verminderd zelfbewustzijn en verzwakte naleving van persoonlijke normen wanneer men in een groep is. Het kan bijvoorbeeld leiden tot roekeloos gedrag tijdens rellen of online trollen.', 'Conformiteit is het aanpassen van je gedrag en meningen om overeen te stemmen met die van anderen of met de verwachtingen van anderen. Bijvoorbeeld, je kunt je kledingstijl aanpassen om beter te passen bij je vrienden.', 'Normatieve invloed betekent dat je je gedrag aanpast om in een groep te passen. Bijvoorbeeld, je kunt vlees eten op een barbecue om niet anders te lijken, ook al ben je vegetariër.', 'Informatieve invloed is het aanpassen van je gedrag omdat je gelooft dat het gedrag van anderen de correcte manier van reageren weerspiegelt. Bijvoorbeeld, in een nieuw restaurant volg je misschien de lokale klanten om te bepalen hoe je moet bestellen.', 'Sociale normen zijn de verwachte gedragsnormen die ons gedrag beïnvloeden. Bijvoorbeeld, het is een sociale norm om je hand op te steken als je een vraag wilt stellen in een klaslokaal.', 'Gehoorzaamheid is het opvolgen van de bevelen van een autoriteitsfiguur. Bijvoorbeeld, een soldaat die orders opvolgt van zijn commandant.', 'Agressie is gedrag dat bedoeld is om een ander individu te schaden. Bijvoorbeeld, iemand fysiek aanvallen is een vorm van agressie.', 'Prosociale gedragingen zijn acties die gunstig zijn voor anderen. Bijvoorbeeld, een oudere dame helpen haar boodschappen naar haar auto te dragen is een prosociaal gedrag.', 'Altruïsme is het bieden van hulp zonder enige openlijke beloning te verwachten. Bijvoorbeeld, een vreemdeling helpen die gevallen is zonder te verwachten dat ze je terugbetalen.', 'Inclusieve fitness is een concept dat zich richt op het adaptieve voordeel van het overdragen van genen via kin selectie. Het gaat dus niet alleen om individuele overleving, maar ook om het helpen van verwanten die dezelfde genen delen.', 'Het bystander intervention effect verwijst naar de reductie in hulpvaardig gedrag wanneer andere mensen aanwezig zijn. Dit kan bijvoorbeeld optreden in noodsituaties waarbij de aanwezigheid van een menigte de waarschijnlijkheid van hulp verminderd.', 'Attitudes zijn evaluaties van objecten, gebeurtenissen of ideeën. Ze beïnvloeden hoe we reageren op de wereld om ons heen, bijvoorbeeld het hebben van een positieve houding ten opzichte van recycling kan leiden tot milieuvriendelijk gedrag.', 'Het mere exposure effect is de toename in sympathie voor een stimulus na herhaalde blootstelling eraan. Bijvoorbeeld, als je een liedje steeds opnieuw hoort, is de kans groter dat je het leuk gaat vinden.', 'Expliciete attitudes zijn attitudes die een individu bewust kan rapporteren. Bijvoorbeeld, je kan bewust zeggen dat je een voorkeur hebt voor katten boven honden.', 'Impliciete attitudes zijn attitudes die onbewust invloed hebben op iemands gevoelens en gedrag. Ze zijn vaak moeilijker te herkennen en kunnen bijvoorbeeld leiden tot onbewuste vooroordelen.', 'Persuasie is de bewuste poging om een attitude te veranderen door middel van berichtcommunicatie. Een voorbeeld hiervan is reclame, die probeert consumentenattitudes te veranderen om producten te verkopen.', 'Het elaboration likelihood model is een theorie die suggereert dat overtuigende berichten leiden tot veranderingen in attitudes via ofwel de centrale of perifere route. Dit hangt af van de mate waarin het individu nadenkt over de inhoud van de boodschap.', 'Compliance verwijst naar de neiging om toe te geven aan de verzoeken van anderen. Het is bijvoorbeeld de reden waarom we vaak "ja" zeggen als iemand ons om een gunst vraagt.', 'Nonverbaal gedrag omvat communicatieve handelingen of gebaren, zoals gezichtsuitdrukkingen en bewegingen. Wanneer we bijvoorbeeld glimlachen, uit dat nonverbaal onze blijdschap.', 'Attributies zijn verklaringen die we geven voor de oorzaken van acties of gebeurtenissen. Zo kunnen we bijvoorbeeld zeggen dat iemand te laat kwam omdat hij/zij vastzat in het verkeer.', 'Persoonlijke attributies zijn interne kenmerken, zoals karaktereigenschappen of inspanningen, die worden gebruikt om iemands gedrag te verklaren. Bijvoorbeeld, als we zeggen dat iemand goed presteert omdat hij/zij hard werkt.', 'Situationele attributies verwijzen naar externe gebeurtenissen, zoals geluk of het weer, om iemands gedrag te verklaren. Bijvoorbeeld, het toeschrijven van iemands slechte humeur aan slecht weer.', 'De fundamentele attributiefout is de neiging om het gedrag van anderen toe te schrijven aan interne factoren, terwijl de invloed van situationele factoren wordt onderschat. Bijvoorbeeld, iemand als lui bestempelen omdat hij/zij een deadline heeft gemist zonder rekening te houden met mogelijke externe factoren.', 'De actor/observer discrepancy is de neiging om de eigen acties toe te schrijven aan situationele factoren, terwijl we de acties van anderen toeschrijven aan persoonlijke kenmerken. Bijvoorbeeld, als we te laat zijn, wijten we dat aan het verkeer, maar als iemand anders te laat is, zien we dat als onverantwoordelijk.', 'Vooroordeel verwijst naar negatieve overtuigingen, meningen en gevoelens die geassocieerd worden met een stereotype. Bijvoorbeeld, het idee dat alle mensen van een bepaalde nationaliteit lui zijn, is een vooroordeel.', 'Discriminatie is de ongelijke behandeling van mensen op basis van hun lidmaatschap van een bepaalde groep. Een voorbeeld is het niet aannemen van een gekwalificeerde kandidaat voor een baan, puur vanwege hun etnische achtergrond.', 'Modern racisme is een subtiele vorm van vooroordelen die hand in hand gaan met de afwijzing van openlijk racistische overtuigingen. Dit kan bijvoorbeeld blijken wanneer iemand zegt dat hij geen racist is, maar toch stereotypen over een bepaalde etnische groep gelooft.', 'Stereotype dreiging is de angst om beoordeeld te worden op basis van een negatief stereotype over de groep waartoe men behoort. Bijvoorbeeld, een vrouw die zich zorgen maakt dat haar prestaties in een wiskundetest zullen bevestigen dat vrouwen slecht zijn in wiskunde.']

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