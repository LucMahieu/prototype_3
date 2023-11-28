import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def openai_call(system_message, user_message="", model='gpt-4', temp=0.0):
    message = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]
    response = openai.ChatCompletion.create(
        model=model,
        temperature=temp,
        messages=message
    )

    return response['choices'][0]['message']['content']


def strip_empty_lines(text):
    return "\n".join(line.strip() for line in text.splitlines() if line.strip())


def batch_generator(data, batch_size):
    """
    Genereer batches van de ingevoerde data.

    :param data: dictionary met termen en definities
    :param batch_size: de gewenste grootte van elke batch
    :return: een generator die dictionaries uitstuurt van grootte batch_size
    """
    # Zorg ervoor dat data een dictionary is en batch_size een positief getal.
    assert isinstance(data, dict) and batch_size > 0, "Ongeldige input"

    # Tijdelijke opslag voor de huidige batch.
    current_batch = {}

    # Loop door elk item in de data.
    for term, definition in data.items():
        # Voeg het item toe aan de huidige batch.
        current_batch[term] = definition

        # Als de huidige batch de gewenste grootte heeft bereikt,
        # geef deze dan terug en reset de huidige batch.
        if len(current_batch) == batch_size:
            yield current_batch
            current_batch = {}

    # Als er items over zijn in de huidige batch na het eindigen van de loop, geef deze dan ook terug.
    if current_batch:

        yield current_batch


def glossary_to_dict(glossary):
    glossary_dict = {}
    glossary_lines = glossary.splitlines()
    for i, line in enumerate(glossary_lines):
        line = line.strip()  # Verwijder whitespace aan het begin en eind van de lijn
        if i % 2 == 0:
            key = line
        else:
            glossary_dict[key] = line
    return glossary_dict


def flashcard_generator(dict, batch_size):
    flashcards = ""
    i = 1
    for batch in batch_generator(dict, batch_size):
        print(f"GENERATING BATCH {i}")
        i += 1
        # print(f"Dit is een batch: {batch}")
        system_message = """
Taakbeschrijving:
Gegeven is een dictionary met een begrip als key en de definitie als value. Creëer vragen en antwoorden voor elk item in de dictionary met behulp van een flashkaartformaat waarbij je eerst de vraag op de voorkant van de flashcard schrijft, gevolgd door twee puntkomma's (;;) en dan het antwoord op de vraag op de achterkant van de flashcard.

% BEGIN VOORBEELD %
Input:
{'neurotransmitters': 'Chemical substances that transmit signals from one neuron to another.', 'receptors': 'In neurons, specialized protein molecules on the postsynaptic membrane; neurotransmitters bind to these molecules after passing across the synapse.', 'reuptake': 'The process whereby a neurotransmitter is taken back into the presynaptic terminal buttons, thereby stopping its activity.'}

Output:
Wat zijn neurotransmitters?;;Chemische stoffen die signalen overbrengen van het ene neuron naar het andere.
Wat zijn receptoren in de context van neuronen?;;Gespecialiseerde eiwitmoleculen op het postsynaptische membraan waar neurotransmitters aan binden nadat ze de synaps zijn gepasseerd.
Wat betekent heropname (reuptake) in de context van neurotransmitters?;;Het proces waarbij een neurotransmitter wordt teruggenomen in de presynaptische terminale knoppen, waardoor zijn activiteit stopt.
% EINDE VOORBEELD %
"""

        user_message = f"""
Input:
{batch}

Output:

"""

        response = openai_call(system_message, user_message, model='gpt-4', temp=0.7)

        # Ensure the new response is added on a new line
        if not response.endswith("\n"):
            response += "\n"
        flashcards += response
        # print(f"Dit is een response: {response}")

    return flashcards


def flashcard_generator_2(dict, batch_size):
    flashcards = ""
    i = 1
    for batch in batch_generator(dict, batch_size):
        print(f"GENERATING BATCH {i}")
        i += 1

        system_message = """
Taakbeschrijving:
Gegeven is een dictionary met een begrip als key en de definitie als value. Creëer vragen en antwoorden voor elk item in de dictionary met behulp van een flashkaartformaat waarbij je eerst de vraag op de voorkant van de flashcard schrijft, gevolgd door twee puntkomma's (;;) en dan het antwoord op de vraag op de achterkant van de flashcard. Geef in het antwoord een beknopte uitleg van maximaal twee zinnen lang, die gebaseerd is op de gegeven definitie en geef, indien mogelijk, een duidelijk voorbeeld of aanvullende informatie om het concept te verhelderen.

%BEGIN VOORBEELD%
Input:
{'neurotransmitters': 'Chemical substances that transmit signals from one neuron to another.', 'receptors': 'In neurons, specialized protein molecules on the postsynaptic membrane; neurotransmitters bind to these molecules after passing across the synapse.', 'reuptake': 'The process whereby a neurotransmitter is taken back into the presynaptic terminal buttons, thereby stopping its activity.'}

Output:
Wat zijn neurotransmitters?;;Neurotransmitters zijn chemische stoffen die signalen overdragen tussen neuronen. Een voorbeeld is dopamine, dat betrokken is bij beloning en motivatie.
Wat zijn receptoren in neuronen?;;Receptoren zijn eiwitmoleculen op neuronen waar neurotransmitters aan binden om signalen over te dragen. Ze werken als sloten die alleen door specifieke neurotransmitter-"sleutels" kunnen worden geopend.
Wat is reuptake bij neurotransmitters?;;Reuptake is het proces waarbij neurotransmitters worden teruggenomen in de neuronen die ze hebben vrijgegeven, waardoor hun activiteit in de synaps stopt.
%EINDE VOORBEELD%

"""

        user_message = f"""
Input:
{batch}

Output:

"""

        response = openai_call(system_message, user_message, model='gpt-4', temp=0.7)
        print(f"BATCH RESPONSE: {response}")
        cleaned_response = strip_empty_lines(response)

        # Ensure the new response is added on a new line
        if not cleaned_response.endswith("\n"):
            cleaned_response += "\n"
        flashcards += cleaned_response

    return flashcards


def format_flashcards(raw_text):
    # Initialiseren van de lists.
    questions = []
    answers = []

    # Opsplitsen van de raw_text string in afzonderlijke flashcards.
    flashcards = raw_text.strip().split("\n")

    # Itereren over elke flashcard.
    for card in flashcards:
        # Splitsen van de flashcard in vraag en antwoord met behulp van ";;".
        question, answer = card.split(";;")

        # Toevoegen van vraag en antwoord aan hun respectieve lijsten.
        questions.append(question.strip())
        answers.append(answer.strip())

    return questions, answers


week_1_1 = """psychological science
The study, through research, of mind, brain, and behavior.
central nervous system (CNS)
The brain and the spinal cord.
peripheral nervous system (PNS)
All nerve cells in the body that are not part of the central nervous system. The peripheral nervous system includes the somatic and autonomic nervous systems.
neurons
The basic units of the nervous system; cells that receive, integrate, and transmit information. They operate through electrical impulses, communicate with other neurons through chemical signals, and form neural networks.
dendrites
Branchlike extensions of the neuron that detect information from other neurons.
cell body
The site in the neuron where information from thousands of other neurons is collected and integrated.
axon
A long, narrow outgrowth of a neuron by which information is conducted from the cell body to the terminal buttons.
terminal buttons
At the ends of axons, small nodules that release chemical signals from the neuron into the synapse.
synapse
The gap between the terminal buttons of a “sending” neuron and the dendrites of a “receiving” neuron, where chemical communication occurs between the neurons.
gene expression
Whether a particular gene is turned on or off.
chromosomes
Structures within the cell body that are made up of DNA, segments of which comprise individual genes.
genes
The units of heredity that help determine an organism’s characteristics.
dominant gene
A gene that is expressed in the offspring whenever it is present.
recessive gene
A gene that is expressed only when it is matched with a similar gene from the other parent.
genotype
The genetic constitution of an organism, determined at the moment of conception.
phenotype
Observable physical characteristics, which result from both genetic and environmental influences.
monozygotic twins
Also called identical twins; twin siblings that result from one zygote splitting in two and that therefore share the same genes.
dizygotic twins
Also called fraternal twins; twin siblings that result from two separately fertilized eggs and therefore are no more similar genetically than nontwin siblings.
heredity
Transmission of characteristics from parents to offspring through genes.
heritability
A statistical estimate of the extent to which variation in a trait within a population is due to genetics.
epigenetics
The study of how the environment changes genetic expression in a way that might be passed along to offspring.
"""
week_1_2 = """action potential
The electrical signal that passes along the axon and subsequently causes the release of chemicals from the terminal buttons.
resting membrane potential
The electrical charge of a neuron when it is not active.
relative refractory period
The brief period of time following action potential when a neuron’s membrane potential is more negative, or hyperpolarized, making it harder to fire again.
all-or-none principle
The principle that when a neuron fires, it fires with the same potency each time; a neuron either fires or not, although the frequency of firing can vary.
absolute refractory period
The brief period of time following an action potential when the ion channel is unable to respond again.
myelin sheath
A fatty material, made up of glial cells, that insulates some axons to allow for faster movement of electrical impulses along the axon.
nodes of Ranvier
Small gaps of exposed axon between the segments of myelin sheath, where action potentials take place.
neurotransmitters
Chemical substances that transmit signals from one neuron to another.
receptors
In neurons, specialized protein molecules on the postsynaptic membrane; neurotransmitters bind to these molecules after passing across the synapse.
reuptake
The process whereby a neurotransmitter is taken back into the presynaptic terminal buttons, thereby stopping its activity.
Broca’s area
A small portion of the left frontal region of the brain, crucial for the production of language.
electroencephalography (EEG)
A technique for measuring electrical activity in the brain.
positron emission tomography (PET)
A method of brain imaging that assesses metabolic activity by using a radioactive substance injected into the bloodstream.
magnetic resonance imaging (MRI)
A method of brain imaging that uses a powerful magnetic field to produce high-quality images of the brain.
functional magnetic resonance imaging (fMRI)
An imaging technique used to examine changes in the activity of the working human brain by measuring changes in the blood’s oxygen levels.
transcranial magnetic stimulation (TMS)
The use of strong magnets to briefly interrupt normal brain activity as a way to study brain regions.
cerebral cortex
The outer layer of brain tissue, which forms the convoluted surface of the brain; the site of all thoughts, perceptions, and complex behaviors.
corpus callosum
A massive bridge of millions of axons that connects the hemispheres of the brain and allows information to flow between them.
occipital lobes
Regions of the cerebral cortex—at the back of the brain—important for vision.
parietal lobes
Regions of the cerebral cortex—in front of the occipital lobes and behind the frontal lobes—important for the sense of touch and for attention to the environment.
temporal lobes
Regions of the cerebral cortex—below the parietal lobes and in front of the occipital lobes—important for processing auditory information, for memory, and for object and face perception.
frontal lobes
Regions of the cerebral cortex—at the front of the brain—important for movement and higher-level psychological processes associated with the prefrontal cortex.
prefrontal cortex
The frontmost portion of the frontal lobes, especially prominent in humans; important for attention, working memory, decision making, appropriate social behavior, and personality.
split brain
A condition that occurs when the corpus callosum is surgically cut and the two hemispheres of the brain do not receive information directly from each other.
insula
The part of the cerebral cortex lying inside the lateral fissure; important for taste, pain, perception of bodily states, and empathy.
thalamus
The gateway to the brain; it receives almost all incoming sensory information before that information reaches the cortex.
hypothalamus
A brain structure that is involved in the regulation of bodily functions, including body temperature, body rhythms, blood pressure, and blood glucose levels; it also influences our basic motivated behaviors.
hippocampus
A brain structure that is associated with the formation of memories.
amygdala
A brain structure that serves a vital role in learning to associate things with emotional responses and in processing emotional information.
basal ganglia
A system of subcortical structures that are important for the planning and production of movement.
brain stem
An extension of the spinal cord; it houses structures that control functions associated with survival, such as heart rate, breathing, swallowing, vomiting, urination, and orgasm.
cerebellum
A large, convoluted protuberance at the back of the brain stem; it is essential for coordinated movement and balance.
somatic nervous system (SNS)
A component of the peripheral nervous system; it transmits sensory signals and motor signals between the central nervous system and the skin, muscles, and joints.
autonomic nervous system (ANS)
A component of the peripheral nervous system; it transmits sensory signals and motor signals between the central nervous system and the body’s glands and internal organs.
sympathetic division
A division of the autonomic nervous system; it prepares the body for action.
parasympathetic division
A division of the autonomic nervous system; it returns the body to its resting state.
endocrine system
A communication system that uses hormones to influence thoughts, behaviors, and actions.
hormones
Chemical substances, released from endocrine glands, that travel through the bloodstream to targeted tissues; the tissues are subsequently influenced by the hormones.
pituitary gland
A gland located at the base of the hypothalamus; it sends hormonal signals to other endocrine glands, controlling their release of hormones.
"""
week_2_1 = """consciousness
One’s moment-to-moment subjective experience of the world.
change blindness
A failure to notice large changes in one’s environment.

endogenous attention
Attention that is directed voluntarily.
exogenous attention
Attention that is directed involuntarily by a stimulus.

priming
A facilitation in the response to a stimulus due to recent experience with that stimulus or a related stimulus.
subliminal perception
The processing of information by sensory systems without conscious awareness.

meditation
A mental procedure that focuses attention on an external object, an internal event, or a sense of awareness.

hypnosis
A social interaction during which a person, responding to suggestions, experiences changes in memory, perception, and/or voluntary action.

circadian rhythms
Biological patterns that occur at regular intervals as a function of time of day.
REM sleep
The stage of sleep marked by rapid eye movements, paralysis of motor systems, and dreaming.

dreams
Products of an altered state of consciousness in which images and fantasies are confused with reality.
activation-synthesis hypothesis
A hypothesis of dreaming proposing that the brain tries to make sense of random brain activity that occurs during sleep by synthesizing the activity with stored memories.

insomnia
A disorder characterized by an inability to sleep that causes significant problems in daily living.
obstructive sleep apnea
A disorder in which people, while asleep, stop breathing because their throat closes; the condition results in frequent awakenings during the night.
narcolepsy
A sleep disorder in which people experience excessive sleepiness during normal waking hours, sometimes going limp and collapsing.
"""
week_2_2 = """sensation
The detection of physical stimuli and the transmission of this information to the brain.
perception
The processing, organization, and interpretation of sensory signals in the brain.
bottom-up processing
Perception based on the physical features of the stimulus.
top-down processing
The interpretation of sensory information based on knowledge, expectations, and past experiences.
transduction
The process by which sensory stimuli are converted to neural signals the brain can interpret.

absolute threshold
The minimum intensity of stimulation necessary to detect a sensation half the time.
difference threshold
The minimum amount of change required to detect a difference between two stimuli.
signal detection theory (SDT)
A theory of perception based on the idea that the detection of a stimulus requires a judgment—it is not an all-or-nothing process.
sensory adaptation
A decrease in sensitivity to a constant level of stimulation.

retina
The thin inner surface of the back of the eyeball, which contains the sensory receptors that transduce light into neural signals.
rods
Retinal cells that respond to low levels of light and result in black-and-white perception.
cones
Retinal cells that respond to higher levels of light and result in color perception.
fovea
The center of the retina, where cones are densely packed.

object constancy
Correctly perceiving objects as constant in their shape, size, color, and lightness, despite raw sensory data that could mislead perception.

binocular depth cues
Cues of depth perception that arise from the fact that people have two eyes.
monocular depth cues
Cues of depth perception that are available to each eye alone.
binocular disparity
A depth cue; because of the distance between the two eyes, each eye receives a slightly different retinal image.
convergence
A cue of binocular depth perception; when a person views a nearby object, the eye muscles turn the eyes inward.
motion parallax
A monocular depth cue observed when moving relative to objects, in which the objects that are closer appear to move faster than the objects that are farther away.

audition
Hearing; the sense of sound perception.
sound wave
A pattern of changes in air pressure during a period of time; it produces the perception of a sound.
eardrum
A thin membrane that marks the beginning of the middle ear; sound waves cause it to vibrate.
vestibular sense
Perception of balance determined by receptors in the inner ear.
"""
week_3_1 = """learning
A relatively enduring change in behavior resulting from experience.

nonassociative learning
Responding after repeated exposure to a single stimulus or event.
associative learning
Linking two stimuli or events that occur together.
social learning
Acquiring or changing a behavior after verbal instruction or exposure to another individual performing that behavior.

habituation
A decrease in behavioral response after repeated exposure to a stimulus.
sensitization
An increase in behavioral response after exposure to a stimulus.

Pavlovian conditioning (classical conditioning)
A type of associative learning in which a neutral stimulus comes to elicit a response when it is associated with a stimulus that already produces that response.
unconditioned response (UR)
A response that does not have to be learned, such as a reflex.
unconditioned stimulus (US)
A stimulus that elicits a response, such as a reflex, without any prior learning.
conditioned stimulus (CS)
A stimulus that elicits a response only after learning has taken place.
conditioned response (CR)
A response to a conditioned stimulus; a response that has been learned.

acquisition
The gradual formation of an association between the conditioned and unconditioned stimuli.
extinction
A process in which the conditioned response is weakened when the conditioned stimulus is repeated without the unconditioned stimulus.
spontaneous recovery
When a previously extinguished conditioned response reemerges after the presentation of the conditioned stimulus.

Rescorla-Wagner model
A cognitive model of classical conditioning; it holds that learning is determined by the extent to which an unconditioned stimulus is unexpected or surprising.

stimulus generalization
Learning that occurs when stimuli that are similar but not identical to the conditioned stimulus produce the conditioned response.
stimulus discrimination
A differentiation between two similar stimuli when only one of them is consistently associated with the unconditioned stimulus.

operant conditioning (instrumental conditioning)
A learning process in which the consequences of an action determine the likelihood that it will be performed in the future.
law of effect
Thorndike’s general theory of learning: Any behavior that leads to a “satisfying state of affairs” is likely to occur again, and any behavior that leads to an “annoying state of affairs” is less likely to occur again.
behaviorism
A psychological approach that emphasizes environmental influences on observable behaviors.

reinforcer
A stimulus that follows a response and increases the likelihood that the response will be repeated.
positive reinforcement
The administration of a stimulus to increase the probability of a behavior’s recurrence.
negative reinforcement
The removal of an unpleasant stimulus to increase the probability of a behavior’s recurrence.
punishment
A stimulus that follows a behavior and decreases the likelihood that the behavior will be repeated.
positive punishment
The administration of a stimulus to decrease the probability of a behavior’s recurrence.
negative punishment
The removal of a stimulus to decrease the probability of a behavior’s recurrence.

shaping
A process of operant conditioning; it involves reinforcing behaviors that are increasingly similar to the desired behavior.

temporal discounting
The tendency to discount the subjective value of a reward when it is given after a delay.

continuous reinforcement
A type of learning in which behavior is reinforced each time it occurs.
partial reinforcement
A type of learning in which behavior is reinforced intermittently.
partial-reinforcement extinction effect
The greater persistence of behavior under partial reinforcement than under continuous reinforcement.

equipotentiality
The principle that any conditioned stimulus paired with any unconditioned stimulus should result in learning.

phobia
An acquired fear that is out of proportion to the real threat of an object or a situation.
fear conditioning
A type of classical conditioning that turns neutral stimuli into threatening stimuli.

modeling
The imitation of observed behavior.
vicarious learning
Learning the consequences of an action by watching others being rewarded or punished for performing the action.
instructed learning
Learning associations and behaviors through verbal communication.
"""
week_3_2 = """memory
The ability to store and retrieve information.

amnesia
A deficit in long-term memory resulting from disease, brain injury, or psychological trauma where the individual loses the ability to retrieve vast quantities of information.
retrograde amnesia
A condition in which people lose past memories, such as memories for events, facts, people, or personal information.
anterograde amnesia
A condition in which people lose the ability to form new memories.

priming
A facilitation in the response to a stimulus due to recent experience with that stimulus or a related stimulus.
implicit memory
Memory that is expressed through responses, actions, or reactions.
explicit memory
Memory that is consciously retrieved.

procedural memory
A type of implicit memory that involves skills and habits.

episodic memory
Memory for one’s past experiences identified by time and place.
semantic memory
Memory for facts independent of personal experience.

encoding
The process by which the perception of a stimulus or event gets transformed into a memory.

schemas
Cognitive structures in long-term memory that help perceive, organize, and process information.

chunking
Organizing information into meaningful units to facilitate memory.
mnemonics
Learning aids or strategies that enhance recall through the use of retrieval cues.

sensory memory
A memory system that very briefly stores sensory information in close to its original sensory form.

working memory
A limited-capacity cognitive system that temporarily stores and manipulates information for complex tasks.

long-term memory
The relatively permanent storage of information.
serial position effect
The ability to recall items from a list depends on the order of presentation, with better memory for items presented early or late in the list.

consolidation
The process of stabilizing a memory trace after learning.
long-term potentiation (LTP)
Strengthening of a synaptic connection, making the postsynaptic neurons more easily activated.

flashbulb memories
Vivid episodic memories for the circumstances in which people first learned of a surprising, consequential, or emotionally arousing event.

reconsolidation
Memories can become vulnerable to disruption when they are recalled, requiring them to be consolidated again.

retrieval cue
Any stimulus that helps access information stored in long-term memory.
encoding specificity principle
The idea that a cue can effectively remind us of an experience if it was part of the original encoding of the experience.

prospective memory
Remembering to do something at some future time.

retrieval-induced forgetting
A phenomenon where recalling some items can impair subsequent recall of related items.

proactive interference
Old information interferes with the ability to learn new information.
retroactive interference
New information interferes with the ability to recall old information.
blocking
The temporary inability to remember something.
absentmindedness
Lapses of attention and forgetting to do things.

persistence
The unwanted recollection of memories that one would prefer to forget.

memory bias
The changing of memories over time so that they conform to current beliefs or attitudes.

source misattribution
Misremembering the time, place, person, or circumstances involved with a memory.
source amnesia
A type of misattribution where the person can’t recall where a memory comes from.
cryptomnesia
A type of source misattribution where a person believes a recalled thought is original when it is not.

suggestibility
The tendency to incorporate misleading information from external sources into personal recollections.
"""
week_4_1 = """cognition
The mental activity that includes thinking and the understandings that result from thinking.

thinking
The mental manipulation of representations of knowledge about the world.
analogical representations
Mental representations that possess some of the physical characteristics of objects they represent.
symbolic representations
Abstract mental representations that do not correspond to the physical features of objects or ideas.

concept
A category or class of related items; it involves mental representations of those items.
prototype model
A theory positing that within each category, there is a best example or prototype that embodies the most typical features of the category.
exemplar model
A conceptualization model where all members of a category are examples (exemplars) and collectively they form the concept and determine category membership.

script
A schema that directs behavior and expectations over time within a certain situation.
stereotypes
Cognitive schemas that facilitate quick, efficient information processing about people based on their membership in certain groups.
"""
week_4_2 = """intelligence
The ability to use knowledge to reason, make decisions, comprehend complex ideas, solve problems, learn quickly, and adapt to environmental challenges.
mental age
An assessment of a child’s intellectual standing relative to same-age peers, determined by comparing the child's test score with the average score for children of each chronological age.
intelligence quotient (IQ)
An index of intelligence calculated by dividing a child’s estimated mental age by the child’s chronological age and then multiplying this number by 100.

general intelligence (g)
The theory that a single factor underlies intelligence.
fluid intelligence
Intelligence reflecting the ability to process information, understand relationships, and think logically, especially in novel or complex situations.
crystallized intelligence
Intelligence reflecting both the knowledge gained through experience and the ability to use that knowledge.
emotional intelligence (EI)
A type of social intelligence emphasizing the management, recognition, and understanding of emotions, and utilizing them to guide thought and action.

language
A communication system using sounds and symbols adhering to grammatical rules.
morphemes
The smallest units of language that carry meaning, including suffixes and prefixes.
phonemes
The basic sounds of speech, serving as the fundamental building blocks of language.
aphasia
A language disorder resulting in deficits in language comprehension and production.
Wernicke’s area
An area where the temporal and parietal lobes of the left hemisphere meet, related to speech comprehension.
linguistic relativity theory
The proposition that language dictates thought.
"""
week_5_1 = """developmental psychology
The study of changes across the life span in physiology, cognition, emotion, and social behavior.
synaptic pruning
A physiological process that preserves utilized synaptic connections and eliminates unused ones.
teratogens
Agents that cause harm to the embryo or fetus.

dynamic systems theory
The view that development is a self-organizing process, where new behaviors emerge through consistent interactions between an individual and their cultural and environmental contexts.

habituation technique
A method to explore how infants categorize objects, such as faces, leveraging the principle that after observing objects from one category, infants will gaze longer at objects from a new category.
infantile amnesia
The inability to recall events from early childhood.

attachment
A strong, emotional, and enduring connection between people that persists over time and circumstances.

assimilation
The process wherein new information is incorporated into existing schemes.
accommodation
The process wherein a new scheme is created or an existing one is significantly altered to incorporate new information that would not fit otherwise.
sensorimotor stage
Piaget’s first stage of cognitive development, wherein infants acquire information through their senses and motor skills, and reflexive responses develop into more deliberate actions through the development of schemes.
object permanence
Understanding that objects continue to exist even when they are not visible.
preoperational stage
Piaget’s second stage of cognitive development, wherein children think symbolically about objects but reason based on intuition and superficial appearance.
concrete operational stage
Piaget’s third stage of cognitive development, wherein children begin to think about and understand logical operations, not being deceived by appearances.
formal operational stage
Piaget’s final stage of cognitive development, wherein individuals can think abstractly and formulate and test hypotheses through deductive logic.

theory of mind
The ability to understand that other people possess mental states that influence their behavior.

preconventional level
The initial stage of moral development, where morality is determined by self-interest and event outcomes.
conventional level
The intermediate stage of moral development, where morality is determined by adherence to societal rules and seeking approval from others.
postconventional level
The final stage of moral development, where morality is dictated by abstract principles and the value of all life.
inequity aversion
A preference for avoiding unfairness in resource distribution decisions.

puberty
The onset of adolescence, signified by the commencement of sexual maturity and, consequently, the ability to reproduce.
"""
week_5_2 = """emotion
An immediate, specific negative or positive response to environmental events or internal thoughts.

primary emotions
Emotions that are innate, evolutionarily adaptive, and universal (shared across cultures).

secondary emotions
Blends of primary emotions.

James-Lange theory
A theory of emotion stating that people perceive specific patterns of bodily responses and as a result of that perception feel emotion.

Cannon-Bard theory
A theory of emotion stating that information about emotional stimuli is sent simultaneously to the cortex and the body and results in emotional experience and bodily reactions, respectively.

two-factor theory
A theory of emotion stating that the label applied to physiological arousal results in the experience of an emotion.

display rules
Rules learned through socialization that dictate which emotions are suitable in given situations.

ideal affect
Emotional and affective states that people want to feel or that cultures especially value.

motivation
A process that energizes, guides, and maintains behavior toward a goal.

need
A state of biological, social, or psychological deficiency.

need hierarchy
Maslow’s arrangement of needs, in which basic survival needs must be met before people can satisfy higher needs.

self-actualization
A state that is achieved when one’s personal dreams and aspirations have been attained.

drive
A psychological state that, by creating arousal, motivates an organism to satisfy a need.

homeostasis
The tendency for bodily functions to maintain equilibrium.

Yerkes-Dodson law
The psychological principle that performance on challenging tasks increases with arousal up to a moderate level. After that, additional arousal impairs performance.

incentives
External objects or external goals, rather than internal drives, that motivate behaviors.

extrinsic motivation
Motivation to perform an activity because of the external goals toward which that activity is directed.

intrinsic motivation
Motivation to perform an activity because of the value or pleasure associated with that activity, rather than for an apparent external goal or purpose.

self-efficacy
The belief that efforts toward a goal will result in success.

self-regulation
The process by which people direct their behavior toward the attainment of goals.

need to belong
The need for interpersonal attachments, a fundamental motive that has evolved for adaptive purposes.

balance theory
The idea that people are motivated to achieve harmony in their interpersonal relationships. A triad is balanced when the relationships are all the same direction or if two relationships are negative and one is positive.

cognitive dissonance
The unpleasant feeling of being aware of holding two conflicting beliefs or a belief that conflicts with a behavior.

self-affirmation
A need for a sense of self that is coherent and stable.

core values
Strongly held beliefs about the enduring principles that are most important and meaningful. Values promote emotions and actions when they are aroused or threatened.
"""
week_6_1 = """outgroup homogeneity effect
The perception of outgroup members as less varied than ingroup members.

social identity theory
The concept that ingroups comprise individuals who perceive themselves as members of the same social category and derive pride from this group membership.

ingroup favoritism
A propensity to positively evaluate and privilege ingroup members over outgroup members.

group polarization
The enhancement of a group's prevailing attitudes through discussion within the group.

groupthink
A phenomenon wherein a group makes suboptimal decisions in a bid to maintain group harmony and coherence.

social facilitation
The improvement of performance when in the presence of others.

social loafing
The tendency to exert less effort when working in a group compared to working alone.

deindividuation
A state of diminished self-awareness and attenuated adherence to personal standards when in a group.

conformity
Adjusting one's behaviors and opinions to align with those of others or with others' expectations.

normative influence
Conforming to fit into a group.

informational influence
Conforming based on the belief that others’ behavior represents the correct way to respond.

social norms
Anticipated standards of conduct that influence behavior.

obedience
Complying with the directives of an authority figure.

aggression
Behavior intending to harm another individual.

prosocial behaviors
Actions that are beneficial to others.

altruism
Offering needed help without expecting any overt reward.

inclusive fitness
A concept that focuses on the adaptive benefit of transmitting genes through kin selection.

bystander intervention effect
The reduction in helping behavior observed when others are present.

attitudes
Evaluations of objects, events, or ideas.

mere exposure effect
The increase in liking for a stimulus following repeated exposure to it.

explicit attitudes
Attitudes that an individual can consciously report.

implicit attitudes
Attitudes that unconsciously impact one’s feelings and behavior.

persuasion
The conscious effort to alter an attitude through message communication.

elaboration likelihood model
A theory suggesting that persuasive messages result in attitude changes via either the central or peripheral route.

compliance
A tendency to accede to the requests of others.

nonverbal behavior
Communicative actions or gestures, such as facial expressions, gestures, and movements.

attributions
Explanations for the causes of actions or events.

personal attributions
Explanations that refer to internal characteristics, such as traits, moods, abilities, or efforts, to describe someone’s behavior.

situational attributions
Explanations that refer to external events, such as luck, accidents, the weather, or others’ actions, to describe someone’s behavior.

fundamental attribution error
The bias toward attributing others’ behaviors to internal factors while underestimating situational influences.

actor/observer discrepancy
The tendency to attribute one’s own actions to situational factors while attributing others’ actions to personal characteristics.

prejudice
Negative beliefs, opinions, and feelings associated with a stereotype.

discrimination
Unequal treatment of individuals because of their group membership.

modern racism
Subtle forms of prejudice that coexist with a rejection of overtly racist beliefs.

stereotype threat
A self-confirming apprehension that one will be evaluated based on a negative stereotype.
"""
week_6_2 = """personality
Characteristic patterns of thoughts, emotional responses, and behaviors that are stable over time and across situations.

personality trait
A stable pattern of thought, emotion, and behavior.

temperaments
Biologically grounded tendencies to act or feel in specific ways.

five-factor theory
A theory proposing that personality can be defined by five factors: openness, conscientiousness, extraversion, agreeableness, and neuroticism.

trait approaches
Approaches focusing on how individuals differ in personality dispositions.

behavioral approach system (BAS)
A brain system that drives behavior in response to opportunities for rewards or incentives.

behavioral inhibition system (BIS)
A brain system that monitors the environment for potential threats and inhibits behavior that may risk pain or danger.

fight-flight-freeze system (FFFS)
A brain system that reacts to threat by initiating defensive behaviors: freeze, escape, or fight.

humanistic approaches
Approaches that emphasize self-actualization and self-understanding to explore personality.

locus of control
Beliefs regarding the amount of control one has over outcomes in life.

reciprocal determinism
A theory positing that personality expression can be explained by the interaction of environment, personal factors, and behavior.

need for cognition
A tendency to engage in and enjoy complex cognitive activities.

situationism
The theory that situational factors, more than personality traits, determine behavior.

interactionism
The theory that both situations and personality traits jointly determine behavior.

idiographic approaches
Approaches focusing on understanding the complexity of the individual personality.

nomothetic approaches
Approaches focusing on general personality characteristics across individuals.

projective measures
Personality tests that involve responding to ambiguous stimuli, often used to assess unconscious processes.

self-schema
A cognitive structure that organizes knowledge, beliefs, and memories about oneself.

self-esteem
An evaluative aspect of the self-perception in which individuals may feel worthwhile or not.

sociometer
An internal gauge that monitors levels of social acceptance or rejection.

social comparison
The practice of evaluating one's own abilities, actions, and beliefs by contrasting them with others’.

self-serving bias
The tendency to attribute successes to oneself and failures to external factors.
"""
week_7_1 = """psychopathology
Sickness or disorder of the mind; psychological disorder.

etiology
Factors that contribute to the development of a disorder.

Research Domain Criteria (RDoC)
A method that defines basic aspects of functioning and considers them across multiple levels of analysis, from genes to brain systems to behavior.

assessment
In psychology, examination of a person’s cognitive, behavioral, or emotional functioning to diagnose possible psychological disorders.

diathesis-stress model
A diagnostic model proposing that a disorder may develop when an underlying vulnerability is coupled with a precipitating event.

family systems model
A diagnostic model that considers problems within an individual as indicating problems within the family.

sociocultural model
A diagnostic model that views psychopathology as the result of the interaction between individuals and their cultures.

cognitive-behavioral approach
A diagnostic model that views psychopathology as the result of learned, maladaptive thoughts and beliefs.

anxiety disorders
Psychological disorders characterized by excessive fear and anxiety in the absence of true danger.

generalized anxiety disorder (GAD)
A diffuse state of constant anxiety not associated with any specific object or event.

agoraphobia
An anxiety disorder marked by fear of being in situations in which escape may be difficult or impossible.

major depressive disorder
A disorder characterized by severe negative moods or a lack of interest in normally pleasurable activities.

persistent depressive disorder
A form of depression that is not severe enough to be diagnosed as major depressive disorder but lasts longer.

learned helplessness
A cognitive model of depression in which people feel unable to control events in their lives.

bipolar I disorder
A disorder characterized by extremely elevated moods during manic episodes and, frequently, depressive episodes as well.

bipolar II disorder
A disorder characterized by alternating periods of extremely depressed and mildly elevated moods.

schizophrenia
A psychological disorder characterized by alterations in thoughts, in perceptions, or in consciousness, resulting in psychosis.

delusions
False beliefs based on incorrect inferences about reality.

hallucinations
False sensory perceptions that are experienced without an external source.

disorganized speech
Incoherent speech patterns that involve frequently changing topics and saying strange or inappropriate things.

disorganized behavior
Acting in strange or unusual ways, including strange movement of limbs, bizarre speech, and inappropriate self-care, such as failing to dress properly or bathe.

negative symptoms
Symptoms of schizophrenia that are marked by deficits in functioning, such as apathy, lack of emotion, and slowed speech and movement.

obsessive-compulsive disorder (OCD)
A disorder characterized by frequent intrusive thoughts and compulsive actions.

anorexia nervosa
An eating disorder characterized by excessive fear of becoming fat and therefore restricting energy intake to obtain a significantly low body weight.

bulimia nervosa
An eating disorder characterized by the alternation of dieting, binge eating, and purging (self-induced vomiting).

binge-eating disorder
An eating disorder characterized by binge eating that causes significant distress.
"""
week_7_2 = """psychotherapy
Formal psychological treatment aimed at addressing mental health issues.

biological therapies
Treatments for psychological disorders grounded in medical approaches to disease and illness.

psychodynamic therapy
Therapy based on Freudian theory, aimed at understanding underlying needs, defenses, and motives.

behavior therapy
Treatment focused on unlearning behaviors through classical and operant conditioning.

exposure
A behavioral therapy technique involving repeated exposure to an anxiety-inducing stimulus or situation.

cognitive therapy
Treatment focusing on modifying distorted thoughts that produce maladaptive behaviors and emotions.

cognitive restructuring
A therapy approach aiming to help clients recognize and alter maladaptive thought patterns.

cognitive-behavioral therapy (CBT)
A therapy that integrates techniques from cognitive and behavior therapy to correct faulty thinking and change maladaptive behaviors.

client-centered therapy
An empathetic approach to therapy that encourages self-understanding and personal growth.

psychotropic medications
Drugs that affect mental processes and alleviate symptoms of psychological disorders.

antianxiety drugs
Psychotropic medications used for treating anxiety.

antidepressants
Psychotropic medications used for treating depression.

antipsychotics
Psychotropic medications used for treating schizophrenia and other psychosis-involved disorders.

electroconvulsive therapy (ECT)
A treatment involving the administration of an electrical current to the brain to induce a seizure, used in some severe depression cases.

placebo effect
Improvement in health following treatment with a placebo, having no active component for the condition being treated.
"""

week_1_1_extra = """Wat is polypeptide?

Een gen bevat de specifieke instructie om polypeptide te maken. Dit zijn de bouwstenen van eiwitten. 

Wat zijn eiwitten en wat doen ze?

Eiwitten zijn basischemicaliën die de structuur van een cel vormen en de activiteiten aansturen. Er zijn duizenden type eiwitten, en elk type draagt een specifieke taak. De omgeving bepaalt welke eiwitten gemaakt worden en wanneer dit gebeurd. 

Wat is selective breeding?

Een experimentele techniek ontwikkeld door Mendel. Hij kruis-plantte volledig paarse en volledig witte bloemen. This second generation revealed a different pattern: Of the hundreds of pea plants, about 75 percent had purple flowers and 25 percent had white flowers. This 3:1 ratio repeated itself in additional studies. It also held true for other characteristics, such as pod shape. From this pattern, Mendel deduced that the plants contained separate units, now referred to as genes, that existed in different versions (e.g., white and purple). In determining an offspring’s features, some of these versions would be dominant and others would be recessive.

Polygenetic genes

When a population displays a range of variability for a certain characteristic, such as height or intelligence, the characteristic is *polygenic*. In other words, the trait is influenced by many genes (as well as by environment). Consider human skin color. There are not just three or four separate skin colors. There is a spectrum of colors. The huge range of skin tones among Americans alone (phenotype) shows that human skin color is not the end product of a single dominant/recessive gene pairing (genotype). Instead, the variety shows the effects of multiple genes.

Zygote

After one sperm and one egg combine during fertilization, the resulting fertilized cell, known as a zygote, contains 23 pairs of chromosomes. 

Genetic variation 

Half of each pair of chromosomes comes from the mother, and the other half comes from the father. From any two parents, 8 million combinations of the 23 chromosomes are possible. The net outcome is that a unique genotype is created at conception, accounting for the genetic variation of the human species.

Cell division

The zygote grows through cell division. This process has two stages: First the chromosomes duplicate. Then the cell divides into two new cells with an identical chromosome structure. Cell division is the basis of the life cycle and is responsible for growth and development. 

Mutations 

Errors sometimes occur during cell division, leading to mutations. Most mutations are benign and have little influence on the organism. The evolutionary significance of such a change is complex. If a mutation produces an ability or a behavior that proves advantageous to the organism, that mutation may spread through the population because those who carry the gene are more likely to survive and reproduce. 

Behavioral genetic

The study of how genes and environment interact to influence psychological activity is known as behavioral genetics. Behavioral genetics has provided important information about the extent to which biology influences mind, brain, and behavior.

Adoption studies

Adoption studies **compare the similarities between biological relatives and adoptive relatives. Nonbiological adopted siblings may share similar home environments, but they have different genes. Therefore, the assumption is that similarities among nonbiological adopted siblings have more to do with environment than with genes.

Variation

The heritability for a trait depends on the variation: the measure of the overall difference among a group of people for that particular trait.To know the heritability of height, we need to know how much individual American women vary in that trait. Once we know the typical amount of variation within the population, we can see whether people who are related (sisters or a mother and daughter) show less variation than women chosen at random.

MAOA-gene 

The gene that controls MAO is called MAOA and comes in two forms, one of which leads to higher levels of MAO and the other to lower levels. The MAO enzyme is involved in the degradation of a class of neurotransmitters called monoamines, which includes dopamine, serotonin, and norepinephrine. By influencing the level of MAO enzyme, the MAOA gene regulates the impact of these neurotransmitters in the brain. Males who had the low-MAOA gene were much more likely to have been convicted of violent crimes than others if they had been maltreated as children. The effects of maltreatment had less of an effect for those with the high-MAOA gene.

Genetic modifications

Researchers can employ various gene manipulation techniques to enhance or reduce the expression of a particular gene or even to insert a gene from one animal species into the embryo of another. The are researchers can then compare the genetically modified animal with an unmodified one to test theories about the affected gene’s function. The two white mice and three brown mice in this photo are genetically normal. The sixth mouse is hairless because it has been genetically modified. Specifically, this mouse has received two *nu* genes, which cause the “nude” mutation. These genes also affect the immune system, so the mouse is a good laboratory subject for studies related to immune function.

Optogenetics

This research technique provides precise control over when a neuron fires. That control enables researchers to better understand the causal relationship between neural firing and behavior. Optogenetics combines the use of light (optics) with gene alterations."""
week_1_2_extra = """Neural networks 

Each neuron communicates with tens of thousands of other neurons. Neurons do not communicate randomly or arbitrarily, however. They communicate selectively with other neurons to form circuits, or neural networks. These networks develop through genetic influence, maturation and experience, and repeated firing.

Sensory neurons

Sensory neurons **detect information from the physical world and pass that information along to the brain. To get a sense of how fast that process can work, think of the last time you touched something hot or accidentally pricked yourself with a sharp object, such as a tack. Those signals triggered your body’s nearly instantaneous response and sensory experience of the impact. 

Somatosensory nerves 

The sensory nerves that provide information from the skin and muscles are called somatosensory nerves. **(This term comes from the Greek for “body sense.” It means sensations experienced from within the body.) 

Motor neurons

Motor neurons direct muscles to contract or relax, thereby producing movement.

Interneurons

Interneurons act as relay stations facilitating communication between sensory and motor neurons.

Reflexes
Reflexes are our automatic motor responses. They occur before we even think about those responses. For each reflex action, a handful of neurons simply convert sensation into action.

Ion channels

These specialized pores allow ions **to pass in and out of the cell when the neuron transmits signals down the axon. Each channel matches a specific type of ion: Sodium channels allow sodium ions but not potassium ions to pass through the membrane, and potassium channels allow passage of potassium ions but not sodium ions

Ions 

Ions are electrically charged molecules, some charged negatively and some charged positively. Two types of ions that contribute to a neuron’s resting membrane potential are sodium ions and potassium ions.

Membrane

The outer surface of a neuron is a membrane, a fatty barrier that does not dissolve in the watery environment inside and outside the neuron. The membrane is selectively permeable. In other words, some substances move in or out of the membrane, and some do not. Located on the membrane are ion channels. By controlling the movement of ions, the membrane plays an important role in communication between neurons: It regulates the concentration of electrically charged molecules that are the basis of the neuron’s electrical activity.

Polarized neuron

When a neuron has more negative ions inside than outside, the neuron is described as being polarized. The polarized state of the resting neuron creates the electrical energy necessary to power the firing of the neuron. This is also referred to as the resting membrane potential 

Ion flow 

Ions pass through the neuron membrane at the ion channels. The flow of ions through each channel is controlled by a gating mechanism. When a gate is open, ions flow in and out of the neuron through the cell membrane. A closed gate prevents their passage. Ion flow is also affected by the cell membrane’s selective permeability. That is, much like a bouncer at an exclusive nightclub, the membrane allows some types of ions to cross more easily than others.

Sodium-potassium pump

Another mechanism in the membrane that contributes to polarization is the sodium-potassium pump. This pump increases potassium and decreases sodium inside the neuron, thus helping maintain the resting membrane potential.

Excitatory signals 

One of the two types of signals that arrive at the dendrites. Excitatory signals depolarize the cell membrane (i.e., decrease polarization by decreasing the negative charge inside the cell relative to outside the cell). Through depolarization, these signals increase the likelihood that the neuron will fire.

Inhibitory signals 

One of the two types of signals that arrive at the dendrites. Inhibitory signals hyperpolarize the cell (i.e., increase polarization by increasing the negative charge inside the cell relative to outside the cell). Through hyperpolarization, these signals decrease the likelihood that the neuron will fire.

Excitatory and inhibitory signals effect

Excitatory and inhibitory signals received by the dendrites are combined within the neuron. Any one signal received by the neuron has little influence on whether the neuron fires. Normally, a neuron is barraged by thousands of excitatory and inhibitory signals, and its firing is determined by the number and frequency of those signals. If the sum of excitatory and inhibitory signals leads to a positive change in voltage that surpasses the neuron’s firing threshold (–55 millivolts), an action potential is generated.

Action potential

The electrical charge inside the neuron relative to outside the neuron starts out negative (resting membrane potential, –70 millivolts). As the neuron fires, it allows more positive ions inside the cell (depolarization), resulting in a reversal of polarity such that the charge inside the neuron is more positive than outside. It then returns to its slightly negative resting state. This happens at each portion of the exposed axon as the action potential travels down the axon.

Presynaptic neuron

The neuron that sends the signal.  

Postsynaptic neuron

The one that receives the signal.

Psychological functions of neurotransmitter: Acetylcholine

Motor control over muscles and learning, memory, sleeping, and dreaming

Psychological functions of neurotransmitter: Norepinephrine

Arousal, vigilance, and attention

Psychological functions of neurotransmitter: Serotonin

Emotional states and impulsiveness and Dreaming

Psychological functions of neurotransmitter: Dopamine

Reward and motivation

Binding of an neurotransmitter

After an action potential travels to the terminal button, it causes the vesicles to attach to the presynaptic membrane and release their neurotransmitters into the synapse. These neurotransmitters then travel across the synapse and attach themselves, or bind, to receptors on the dendrites of the postsynaptic neuron. The binding of a neurotransmitter with a receptor can cause ion channels to open or to close more tightly, producing an excitatory or an inhibitory signal in the postsynaptic neuron.

Enzyme deactivation 

Enzyme deactivation **occurs when an enzyme destroys the neurotransmitter in the synapse. Different enzymes break down different neurotransmitters.

Autoreception

Neurotransmitters can also bind with receptors on the presynaptic neuron. This process is called autoreception. Autoreceptors monitor how much neurotransmitter has been released into the synapse. When an excess is detected, the autoreceptors signal the presynaptic neuron to stop releasing the neurotransmitter.

Agonists

Drugs and toxins that enhance the actions of neurotransmitters are known as agonists. An agonist helps the postsynaptic neuron respond again and again by increasing the action of the neurotransmitter.

Antagonists

Drugs and toxins that inhibit these actions are known as antagonists. An antagonist is anti, or against the neurotransmitter working, and reduces the action of the neurotransmitter.

Event-related potential (ERP)

A powerful method to measure how brain activity changes in response to a specific stimulus involves conducting many trials with a single individual and averaging across the trials. Because this method enables researchers to observe patterns associated with specific events, it is called event-related potential (ERP). ERPs provide information about the speed at which the brain processes events and their timing, but because they measure electrical activity at the scalp that is the sum of all activity of the neural tissue underneath, it is difficult to pinpoint where in the brain those processes take place.

Forebrain

The largest part of the human brain is the forebrain. The forebrain is made up of the cerebral cortex and underlying subcortical areas and consists of two hemispheres.

Gray matter

The outer layer of the cerebral cortex (the bark) consists of gray matter, which is dominated by neurons’ cell bodies, dendrites, and nonmyelinated axons that communicate only with nearby neurons. 

White matter

Underneath the gray matter, you would see the white matter, which consists mostly of axons and the fatty myelin sheaths that surround them. These myelinated axons travel between brain regions.

Primary somatosensory cortex

A strip in the front part of the parietal lobe that runs along the central fissure from the top of the brain down the sides. The primary somatosensory cortex groups nearby sensations. For example, sensations from the fingers are near sensations from the palm. The result, covering the primary somatosensory area, is the somatosensory homunculus.

Somatosensory homunculus

A distorted representation of the entire body called (the term is Greek for “little man”). The homunculus is distorted because more cortical area is devoted to the body’s more sensitive areas, such as the face and the fingers.

Primary auditory cortex

The temporal lobes hold the primary auditory cortex, the brain region responsible for hearing.

Primary motor cortex

In the back part of the frontal lobes, is the primary motor cortex. The primary motor cortex includes neurons that project directly to the spinal cord to move the body’s muscles. Its responsibilities are divided down the middle of the body. For example, the left hemisphere controls the right arm, whereas the right hemisphere controls the left arm

Nucleus accumbens

Within the basal ganglia, the nucleus accumbens is important for experiencing reward and motivating behavior. Nearly every pleasurable experience (from eating food you like to looking at a person you find attractive) involves dopamine activity in the nucleus accumbens that makes you want the thing or person you are experiencing. The more desirable objects are, the more they activate basic reward circuitry in our brains."""
week_2_1_extra = """Shadowing

Cherry developed selective-listening studies to examine what the mind does with unattended information when a person pays attention to one task. He used a technique called *shadowing*. In this procedure, the participant wears headphones that deliver one message to one ear and a different message to the other. The participant is asked to attend to one of the two messages and “shadow” it by repeating it aloud. As a result, the participant usually notices the unattended sound (the message given to the other ear) but will have little knowledge about the content of the unattended sound

Freudian slip

The influence of unconscious thoughts was also at the center of Freud’s theories of human behavior. For example, the classic mistake called a Freudian slip occurs when an unconscious thought is suddenly expressed at an inappropriate time or in an inappropriate social context. Freud compared consciousness to the tip of the iceberg that can be seen above water, whereas the unconscious, below the water, was the driving force influencing behavior. Many of Freud’s ideas about how the unconscious works are difficult to test using scientific methods, and few psychologists today believe his interpretation of the unconscious is correct. However, psychologists today agree that unconscious processes influence people’s thoughts and actions as they go through their daily lives.

Automatic processing 

Automatic processing occurs when a task is so well learned that we can do it without much attention. For example: Have you ever tried to help a new reader make their way through a children’s book? It is a slow process of sounding out and identifying each word and requires a lot of concentration and conscious effort. However, as you read this textbook, the words jump out automatically, and you can devote your conscious efforts to fully understanding

Controlled processing

Difficult or unfamiliar tasks require people to pay attention. Such controlled processing is slower than automatic processing, but it helps people perform in complex or novel situations. For example if a rainstorm starts while you are driving, you will need to pay more attention to your driving and be very conscious of the road conditions

Concentrative meditation 

You focus attention on one thing, such as your breathing pattern, a mental image, or a specific phrase (sometimes called a mantra). 

Mindfulness meditation

In mindfulness meditation, you let your thoughts flow freely, paying attention to them but trying not to react to them. You hear the contents of your inner voice, but you allow them to flow from one topic to the next without examining their meaning or reacting to them in any way.

Runner’s high

One minute a person might feel pain and fatigue, and the next minute euphoria and a glorious release of energy. Commonly known as runner’s high, this state, which is partially mediated by physiological processes, results in a shift in consciousness.

Religious ecstasy

Shifts in consciousness that are similar to runner’s high occur at other moments in our lives. Religious ceremonies often decrease awareness of the external world and create feelings of euphoria, or religious ecstasy. Like meditation, religious ecstasy directs attention away from the self by means of chanting, dancing, and/or other behaviors. In this way, it allows a person to focus on the religious experience.

Flow

Flow is “a particular kind of experience that is so engrossing and enjoyable [that it is] worth doing for its own sake even though it may have no consequence outside itself”. That is, a person might perform a particular task out of fascination with it rather than out of a desire for an external reward. Flow is an optimal experience in that the activity is completely absorbing and satisfying and seems to happen automatically. People experiencing flow lose track of time, forget about their problems, and fail to notice other things going on When athletes talk about being “in the zone,” they are referring to a state of flow. Flow experiences have been reported during many activities, including playing music, playing a moderately challenging version of the computer game Tetris, and simply doing satisfying jobs, In the view of the psychologist Mihaly Csikszentmihalyi (1999), flow experiences bring personal fulfillment.

Escapist Entertainment

Simple entertainment, such as playing video games, may have benefits. When such activity veers toward obsession, it may have negative effects.

Suprachiasmatic nucleus

Information about light detected by the eyes is sent to a small region of the hypothalamus called the suprachiasmatic nucleus. This region then sends signals to a tiny structure called the pineal gland.

Pineal gland

The pineal gland secretes melatonin after the signals from the suprachiasmatic nucleus are send. 

Melatonin

A hormone that travels through the bloodstream and affects various receptors in the body, including the brain. Bright light suppresses the production of melatonin, whereas darkness triggers its release. Melatonin is necessary for circadian cycles that regulate sleep- Researchers have noted that taking melatonin can help people cope with jet lag and shift work, both of which interfere with circadian rhythms. Taking melatonin also appears to help people fall asleep, although it is unclear why this happens.

Theta waves

Short bursts of irregular waves.

Sleep spindles

Occasional bursts of activity 

K-complexes

Large waves. Some researchers believe that sleep spindles and K-complexes are signals from brain mechanisms involved with shutting out the external world and keeping people asleep. Two findings indicate that the brain must work to maintain sleep: Abrupt noises can trigger K-complexes. And as people age and sleep more lightly, EEGs show fewer sleep spindles. 

Delta waves/Slow-wave sleep

Large, regular brain patterns.

Beta waves

Short bursts of irregular waves. This is normally represented by an awake, alert mind. 

Stage 1 of sleep

Consists of Theta waves. You are in a light sleep, which means you are easily aroused (if awakened, probably deny sleeping). The symptoms are might see fantastical images or geometric shapes and might have the sensation of falling or that your limbs are jerking. 

Stage 2 of sleep

Consists of Theta waves, sleep spindles and K-complexes. 

Stage 3 and 4 of sleep

Consists of Delta waves. You are in deep sleep. It is hard to wake up and often disoriented when you do wake up. You still process some information. This is because the mind contibuetes to evaluate the surroundings for potential danger. For example you can be aroused by children cries, but can ignore sounds as sirens or traffic noise, it is not relevant to you.

REM Sleep 

Consists of Beta waves, rapid eye movements and paradoxical sleep. 

Rapid eye movements

The eyes dart back and forth rapidly beneath closed eyelids.

Paradoxical sleep

Because of the paradox of a sleeping body with an active brain. Some neurons (especially occipital cortex and brain stem regions) are more active during REM sleep than during waking hours.  Most of the body muscles are paralyzed. And there is Genital arousal Most males of all ages develop erections, and most females of all ages experience clitoral engorgement. 

The Interpretation of Dreams

Freud speculated that dreams contain hidden content that represents unconscious conflicts within the mind of the dreamer. Consists of manifest content and latent content. Virtually no support exists for Freud’s ideas that dreams represent hidden conflicts and that objects in dreams have special symbolic meanings. However, there is evidence that daily life experiences influence the content of dreams. 

Manifest content

Part of Freud interpretation of dreams. The manifest content is the dream the way the dreamer remembers it. 

Latent content

Part of Freud interpretation of dreams. The latent content is what the dream symbolizes; it is the material that has been disguised to protect the dreamer from confronting a conflict directly. 

Theories about sleep

Restorative theory, Circadian rhythm theory and facilitation of learning theory. 

Restorative theory

Sleep allows body to rest and repair itself. Showing that the amount of sleep is higher after exercising. Deprivation of sleep makes your ability’s less. Immune response becomes worse, can be more vulnerable to infections. Sleep deprivation might serve one very useful purpose: When people are suffering from depression, depriving them of sleep sometimes alleviates their depression. This effect appears to occur because sleep deprivation leads to increased activation of serotonin receptors, as do drugs used to treat depression.  For people who are not suffering from depression, however, sleep deprivation is more likely to produce negative moods than positive ones.

Circadian rhythm theory

Evolved because animals won’t be awake at night. Than the world becomes a dangerous place. Better to sleep than. Thus, an animal’s typical amount of sleep depends on how much time that animal needs to obtain food, how easily it can hidden, and how vulnerable it is to attack. Small animals tend to sleep a lot. Large animals vulnerable to attack, such as cows and deer, sleep little.

Facilitation of learning theory

Sleep is needed to strengthen neural communications and connections. Needed for leaning. For example during exam week students more in REM sleep.

REM Behavior disorder

REM behavior disorder **is roughly the opposite of narcolepsy. In this condition, the normal paralysis that accompanies REM sleep is disabled. People with this disorder act out their dreams while sleeping, often striking their sleeping partners. No treatment exists for this rare condition, which is caused by a neurological deficit and is most often seen in elderly males.

Concussion

A concussion is formally known as mild TBI. Despite the term mild, concussion is far from trivial, as the brain swelling and resulting brain damage can have long-lasting effects. Signs of concussion
include mental confusion, dizziness, a dazed look, memory problems, and sometimes the temporary loss of consciousness. Most people will recover from concussion within one to two weeks . However, concussions may have a cumulative effect with each new injury. That is, each concussion can lead to more serious, longer-lasting symptoms.

Coma

Medical advances are enabling a greater number of people to survivetraumatic brain injuries. Doctors now save the lives of many people who previously would have died from injuries sustained in car accidents or on battlefields. Surviving is just the first step toward recovery, however, and many of those who sustain serious brain injuries fall into comas or, like Giffords, are induced into coma as part of medical treatment. The coma allows the brain to rest. 

Unresponsive wakefulness syndrome

When people appear to have emerged from coma (their eyes are open, and they have sleep/wake cycles) yet do not respond to external stimuli for more than a month, they are in a condition called unresponsive wakefulness syndrome. This unresponsive state is not associated with consciousness. Normal brain activity does not occur when a person is in this state, in part because much of the person’s brain may be damaged beyond recovery. The longer the unresponsive wakefulness state lasts, the less likely it is that the person will ever recover consciousness or show normal brain activity.

Minimally conscious state

Some people who emerge from a coma are able to make deliberate movements, such as following an object with their eyes. They may even try to communicate. This situation is referred to as a minimally conscious state. The prognosis for those in an unresponsive wakefulness state is much worse than for those in a minimally conscious state. Differentiating between states of consciousness by behavior alone is difficult, but brain imaging may prove useful for identifying the extent of a patient’s injury and likelihood of recovery. Researchers have found that measuring brain metabolism via positron emission tomography imaging can identify which patients in unresponsive states are likely to regain consciousness.

Brain dead

The imaging of brain activity can also be used to tell whether a
person is brain dead. Brain death is the irreversible loss of brain function. Unlike patients suffering from unresponsive wakefulness syndrome, who still show activity in regions of the brain stem, with brain death no activity is found in any region of the brain. The brain is essential for integrating brain activity that keeps the bodily organs, such as the heart and lungs, alive. When the brain no longer functions, the rest of the body quickly stops functioning unless it is supported by mechanical interventions.

Kinds of psychoactive drugs

Stimulants, depressants, opioids, hallucinogens/psychedelics, combination. 

Stimulants

Psychological effect(s): Increase behavioral and mental activity. Examples: Amphetamines, Methamphetamine, Cocaine, Nicotine, Caffeine. Neurotransmitter system(s): Dopamine, Norepinephrine, Acetylcholine (nicotine). 

Depressants

Psychological effect(s): Decrease behavioral and mental activity. Examples: Anti-anxiety drugs (barbiturates, benzodiazepines), Alcohol. Neurotransmitter system(s): GABA.

Opioids (narcotics)

Psychological effect(s): Reduce the experience of pain. Examples: Heroin, Morphine, Codeine. Neurotransmitter system(s): Endorphins.

Hallucinogens (psychedelics):

Psychological effect(s): Alter thoughts or perceptions. Examples: LSD, PCP, Peyote, Psilocybin, Mushrooms. Neurotransmitter system(s): Serotonine (LSD, peyote, psilocybin), Glutamate (PCP)

Combination

Psychological effect(s): Mixed effects. Examples: Marijuana, MDMA. Neurotransmitter system(s): Cannabinoid (marijuana): Serotonin, dopamine, norepinephrine (MDMA).

Addiction

Drug use that remains compulsive despite its negative consequences. Physical and psychological dependence.

Tolerance

Increasing amounts of a drug needed to achieve the intended effect.

Withdrawal

Physiological and psychological state characterized by feelings of anxiety, tension, and cravings for the addictive substance.  

Binge drinking

Drinking five or more drinks in one sitting."""
week_2_2_extra = """Sensory receptors

The sensory receptors receive stimulation, physical stimulation in the case of vision, hearing, and touch and chemical stimulation in the case of taste and smell. The sensory receptors then pass the resulting impulses to the brain in the form of neural impulses. With the exception of smell, most sensory information first goes to the thalamus, a structure in the middle of the brain (see Figure 3.26). This information is projected from the thalamus to a specific region of the cerebral cortex for each sense. With smell, sensory information bypasses the thalamus and goes directly to the cortex. In these primary sensory areas, the perceptual process begins in earnest. 

Qualitative information 

Qualitative information consists of the most basic qualities of a stimulus. For example, it is the difference between a tuba’s honk and a flute’s toot. It is the difference between a salty taste and a sweet one.

Quantiative information 

Quantitative information consists of the degree, or magnitude, of those qualities: the loudness of the honk, the softness of the toot, the relative saltiness or sweetness. If you were approaching a traffic light, qualitative information might include whether the light was red or green. Regardless of the color, quantitative information would include the brightness of the light.

Weber’s law

This law states that the just noticeable difference between two stimuli is based on a proportion of the original stimulus rather than on a fixed amount of difference. That is, the more intense the stimulus, the bigger the change needed for you to notice. The difference threshold increases as the stimulus becomes more intense. Pick up a 1-ounce letter and a 2-ounce letter, and you will easily detect the difference. But pick up a 5-pound package and a package that weighs 1 ounce more, and the difference will be harder, maybe impossible, to tell.

Hit

If the signal is presented and the participant detects it, the outcome is a hit. 

Miss

If the participant fails to detect the signal, the outcome is a miss. 

False alarm

If the participant reports there was a signal that was not presented, the outcome is a false alarm. 

Correction rejection

If the signal is not presented and the participant does not detect it, the outcome is a correct rejection

Outcome experiment Signal Detection Theory

Those who are biased toward reporting a signal tend to be ‘yea-sayers’. They have many false alarms. Those who are biased toward denying that a signal occurred tend to be ‘nay-sayers’. They have many misses. 

Cornea 

Light first passes through the cornea, the eye’s thick, transparent outer layer. The cornea focuses the incoming light.

Lens

After the cornea focuses the incoming ligt it enters the lens. There, the light is bent further inward and focused to form an image on the retina. More light is focused at the cornea than at the lens. But the lens is adjustable, whereas the cornea is not.

Pupil

Pupil, the dark circle at the center of the eye, is a small opening in the front of the lens. By contracting (closing) or dilating (opening), the pupil determines how much light enters the eye.

Iris

The iris, a circular muscle, determines the eye’s color and controls the pupil’s size. The pupil dilates not only in dim light but also when we see something we like, such as a beautiful painting or a cute baby

Accommodation

Behind the iris, muscles change the shape of the lens. They flatten it to focus on distant objects and thicken it to focus on closer objects. This process is called accommodation. The lens and cornea work together to collect and focus light rays reflected from an object.

Presbyopia

As people get older, the lens hardens and it becomes more difficult to focus on close images, a condition known as presbyopia. After age 40, many people require reading glasses when trying to focus on nearby objects.

Photopigments 

Protein molecules that become unstable and split apart when exposed to light.

Ganglion cells 

Ganglion cells are the first neurons in the visual pathway with axons. During the process of seeing, they are the first neurons to generate action potentials

Transmission from the eye to the brain

The visual process begins with the generation of electrical signals by the sensory receptors (rods and cones) in the retina. These receptors contain photopigments. Rods and cones do not fire action potentials like other neurons. Instead, decomposition of the photopigments alters the membrane potential of the photoreceptors and triggers action potentials in downstream neurons. Immediately after light is transduced by the rods and cones, other cells in the middle layer of the retina perform a series of sophisticated computations. The outputs from these cells converge on the retinal ganglion cells. Ganglion cells are the first neurons to generate action potentials. The ganglion cells send their signals along their axons from inside the eye to the thalamus. The information then travels to the primary visual cortex, cortical areas in the occipital lobes at the back of the head. The pathway from the retina to this region carries all the information that we consciously experience as seeing.

Optic nerve

These axons of the ganglion cells are gathered into a bundle, the optic nerve, which exits the eye at the back of the retina. 

Blind spot

The point at which the optic nerve exits the retina has no rods or cones, producing a blind spot in each eye. If you stretch out one of your arms, make a fist, and look at your fist, the size that your fist appears to you is about the size of your blind spot. Because your two eyes are separated by a few inches, the blind spot for each eye covers a slightly different region of the visual space in front of you. The brain normally fills in this gap automatically, so you are not aware of it. 

The optic chiasm 

the optic chiasm, half of the axons in the optic nerves cross. (The axons that cross are the ones that start from the portion of the retina nearest the nose.) This arrangement causes all information from the left side of visual space (i.e., everything visible to the left of the point of gaze) to be projected to the right hemisphere of the brain, and vice versa. 

The ventral stream

The ventral stream projects from the occipital lobe to the temporal lobe and appears to be specialized for the perception and recognition of objects, such as determining their colors and shapes. This steam is also known as the “what” stream.

The dorsal stream

The dorsal stream projects from the occipital lobe to the parietal lobe and seems to be specialized for spatial perception, determining where an object is and relating it to other objects in a scene. This steam is also known as the “where” stream.

Object agnostic 

The inability to recognize objects. No longer able to recognize the faces of friends and family members, common objects, or even drawings of squares or circles. It is possible to recognize people by their voices, and recognize objects when they are placed in hands. For example, if a person with object agnostic was asked to draw an apple, she could do so from memory, but when shown a drawing of an apple, she could not identify or reproduce it. She could use visual information about the size, shape, and orientation of the apple to control visually guided movements. She could reach around other objects and grab the apple. In performing this action, she would put exactly the right distance between her fingers, even though she could not tell you what she was going to pick up or how large it was. Because her “where” pathway appeared to be intact, these regions of her visual cortex allowed her to use information about the size and location of objects despite her lack of awareness about those objects. 

Trichromatic theory

According to the trichromatic theory, color vision results from activity in three types of cones that are sensitive to different wavelengths. One type of cone is most sensitive to short wavelengths (blue–violet light), another type is most sensitive to medium wavelengths (yellow–green light), and the third type is most sensitive to long wavelengths red–orange light.  The three types of cones in the retina are therefore called “S,” “M,” and “L” cones because they respond maximally to short, medium, and long
wavelengths, respectively. For example, yellow light looks yellow because it stimulates the L and M cones about equally and hardly stimulates the S cones. In fact, we can create yellow light by combining red light and green light because each type of light stimulates the corresponding cone population. As far as the
brain can tell, there is no difference between yellow light and a combination of red light and green light!

Color blindness

There are two main types of color blindness, determined by the relative activity among the three types of cone receptors. The term blindness is somewhat misleading, because people with this condition do see color. They just have partial blindness for certain colors. People may be missing the photopigment sensitive to either medium or long wavelengths, resulting in red–green color blindness. Alternatively, they may be missing the short-wavelength photopigment, resulting in blue–yellow color blindness. These genetic disorders occur in about 8 percent of males but less than 1 percent of females.

Opponent-process theory

According to this theory, red and green are opponent colors, as are blue and yellow. When we stare at a red image for some time, we see a green afterimage when we look away; when we stare at a green image, we see a red afterimage. In the former case, the receptors for red become fatigued when you stare at red. The green receptors are not fatigued and therefore the afterimage appears green.

Three dimensions of color

Color is categorized along three dimensions: hue, saturation, and lightness.

Hue

Consists of the distinctive characteristics that place a particular color in the spectrum, the color’s greenness or orangeness, for example. These characteristics depend primarily on the light’s dominant wavelength when it reaches the eye.

Saturation

Saturation **is the purity of the color. Saturation varies according to the mixture of wavelengths in a stimulus. Basic colors of the spectrum (e.g., blue, green, red) have only one wavelength, whereas pastels (e.g., baby blue, emerald green, and pink) have a mixture of many wavelengths, so they are less pure.

Lightness 

Lightness is the color’s perceived intensity. This characteristic is determined chiefly by the total amount of light reaching the eye. How light something seems also depends on the background, however, since the same color may be perceived differently depending on whether you are looking at it against a bright or dark background. 

Gestalt principles of perceptual organization

Theorized that perception is more than the result of a collection of sensory data; the whole of perceptual experience is more than the sum of its parts. The brain uses innate principles to group sensory information into organized wholes. Because otherwise to much input, it is efficient. 

Six laws of gestalt grouping 

Proximity, Similarity, Good Continuation, Closure, illusory Contours, Common Fate

Proximity

The closer two figures are to each other, the more likely we are to group them and see them as part of the same object.

Similarity

We tend to group figures according to how closely they resemble each other, whether in shape, color, or orientation. 

Good continuation

We tend to group together edges or contours that are smooth and continuous as opposed to those having abrupt or sharp edges.

Closure 

We tend to complete figures that have gaps. The principles of good continuation and closure sometimes can result in seeing contours, shapes, and cues to depth when they do not exist, as is the case with illusory contours. 

Common fate

We tend to see things that move together as belonging to the same group. For example, you would have no difficulty seeing the Dalmatian in the scene presented in the Figure if the subsets of. black. dots that represent the Dalmatian all began moving in the same direction. 

Illusory Contours

The two triangles are illusions, and implied depth cues make one triangle appear brighter than the surrounding area. 

Size constancy

For size constancy, we need to know how far away the object is from us.

Shape constancy

For shape constancy, we need to know what angle or angles we are seeing the object from.

Color constancy

For color constancy, we need to compare the wavelengths of light reflected from the object with those reflected from its background. 

Lightness constancy 

For lightness constancy, we need to know how much light is being reflected from the object and from its background.

Prosopagnosia

Some people have particular deficits in the ability to recognize faces but not in the ability to recognize other objects. People with prosopagnosia cannot tell one face from another, but they are able to judge whether something is a face or not and whether that face is upside down or not. This specific impairment in recognizing faces implies that facial recognition differs from nonfacial object recognition.Prosopagnosia can be present from birth. Developmental prosopagnosia is thought to affect up to 2.5 percent of the population and to be related to genetic factors. Individuals with developmental prosopagnosia report difficulties identifying unique individuals and learn to rely on other cues, such as voice, but they often do not realize they have a specific deficit recognizing faces, relative to most others, until adulthood. Prosopagnosia can also be acquired following a brain injury. Certain brain regions appear to be dedicated solely to perceiving faces), and damage to these regions results in prosopagnosia. As part of the “what” stream discussed earlier, a region of the fusiform gyrus in the temporal lobe is critical for perceiving faces.

Depth perception (diepte perceptie)

We are able to perceive depth in the two-dimensional patterns of photographs, movies, videos, and television images. But we are still able to distinguish these two-dimensional images from our three-dimensional world because some depth cues are apparent in two-dimensional images while others are not. There are Binocular Depth cues and Monocular depth cues. 

Occlusion

A near object occludes (blocks) an object that is farther away.

Texture gradients: 

As a uniformly textured surface recedes, its texture continuously becomes denser.

Shadow 

Shadows are a depth cue that arises when objects cast shadows onto other surfaces. When an object is illuminated, it can cast a shadow on a surface behind it or nearby objects. The size, shape, and position of the shadow provide important visual information about the depth and location of the object in relation to the light source and the surface. By analyzing the direction and length of shadows, our brains can infer the relative position and distance of objects in a scene. For example, a long shadow may suggest that an object is closer to the light source, while a shorter shadow might indicate a greater distance.

Relative size:

Far-off objects project a smaller retinal image than close objects do, if the far-off and close objects are the same physical size.

Familiar size

Because we know how large familiar objects are, we can tell how far away they are by the size of their retinal images.

Position relative to horizon

All else being equal, objects below the horizon that appear higher in the visual field are perceived as being farther away. Objects above the horizon that appear lower in the visual field are perceived as being farther away.

Stereoscopic vision

The ability to determine an object’s depth based on that object’s projection to each eye. 

Motion parallax

Arises from the relative speed with which objects move across the retina as a person moves. Because our view of objects closer to us changes more quickly than does our view of objects that are farther away, motion provides information about how far away something is. 

Stroboscopic movement

A perceptual illusion that occurs when two or more slightly different images are presented in rapid succession. This apparent motion illusion demonstrates that the brain, much as it fills in gaps to perceive objects, also fills in gaps in the perception of motion.

Motion aftereffects

Motion aftereffects **provide evidence that motion-sensitive neurons exist in the brain. Motion aftereffects occur when you gaze at a moving image for a long time and then look at a stationary scene. You experience a momentary impression that the new scene is moving in the opposite direction from the moving image. This illusion is also called the waterfall effect, because if you stare at a waterfall and then turn away, the scenery you are now looking at will seem to move upward for a moment.

Amplitude of sound waves

A sound wave’s amplitude determines its loudness. Increasing the intensity of an object’s vibratory movement increases the displacement of air molecules and the amplitude of the resulting sound wave. The greater the amplitude, the louder the sound.

Frequency of sound waves

The wave’s frequency determines its pitch: We hear a higher frequency as a sound that is higher in pitch. The frequency of a sound is measured in vibrations per second, called *hertz* (abbreviated *Hz*). Most humans can detect sound waves with frequencies from about 20 Hz to about 20,000 Hz.

Ossicles

Three tiny bones commonly called the hammer, anvil, and stirrup.

Oval window

A membrane, stretched tightly across the canal, which marks the beginning of the middle ear. 

Cochlea

The cochlea is a fluid-filled tube that curls into a snail-like shape.

Basilar membrane

Running through the center of the cochlea is the thin basilar membrane. The oval window’s vibrations create pressure waves in the cochlear fluid, which prompt the basilar membrane to oscillate.

Primary auditory receptors

The hair cells on the basilar membrane, which bend with auditory vibrations and transduce the mechanical signal into neural impulses.

Interaction regions of the ear

When changes in air pressure produce sound waves within a person’s hearing distance, those sound waves arrive at the person’s outer ear and travel down the auditory canal to the eardrum. The sound waves make the eardrum vibrate. These vibrations are transferred to ossicles. The ossicles transfer the eardrum’s vibrations to the oval window. The oval window’s vibrations create pressure waves in the cochlear fluid, which prompt the basilar membrane to oscillate. Movement of the basilar membrane stimulates hair cells to bend and to send information to the auditory nerve. This conversion of sound waves to brain activity produces the sensation of sound. Auditory neurons in the thalamus extend their axons to the primary auditory cortex. **

Cochlear implants 

A cochlear implant is a small electronic device that can help provide the sense of sound to a person who has a severe hearing impairment.

Auditory Localization 

Depending on the location a sound is coming from, there will be slight differences in the timing and intensity of the auditory stimulation for the two ears. This will lead to locate where the sounds are coming from."""
week_3_1_extra = """Dishabituation

An increase in a response because of a change in something familiar. 

Extinguished

The conditioned response is extinguished when the conditioned stimulus no longer predicts the unconditioned stimulus.

Prediction error

Learning theorists refer to the difference between the expected and actual outcomes as prediction error.

Positive prediction error 

Suppose that after a stimulus appears, something surprising happens. It could be either the presence of an unexpected event or a stronger version of the expected stimulus than anticipated. This prediction error is considered a positive prediction error and strengthens the association between the CS (conditioned stimuli) and the US (unconditioned stimuli). Positive means the presence of something unexpected. 

Negative prediction error

Now suppose an expected event does not happen. The absence of the event leads to a negative prediction error, which weakens the CS-US association. Negative refers to the absence of something expected.

Second-order conditioning: 

When a CS (conditioned stimulus) is paired with a new S (stimulus). The new S (stimulus) → produces CR (conditioned response). 

Succesive approximations 

Important in shaping. Reinforcing successive approximations eventually produces the desired behavior. In other words, the animal learns to discriminate which behavior is being reinforced. The notion of successive approximations is familiar to many of us through the children’s game of “hot-cold.” In this game, an object is hidden and the player is given cues to try to find it, such as “Getting warmer” or “Hot” as the player moves closer and closer to the object, and “Chilly” or “Freezing” when the player moves farther away.

Primary reinforces

The most obvious stimuli that act as reinforcers are those necessary for survival, such as food or water. Because they satisfy biological needs, these stimuli are called *primary reinforcers*. From an evolutionary standpoint, the learning value of primary reinforcers makes a great deal of sense: Animals that repeatedly perform behaviors reinforced by food or water are more likely to survive and pass along their genes. 

Secondary reinforces

Stimuli that serve as reinforcers but do not satisfy biological needs are called *secondary reinforcers.* These reinforcers are established through classical conditioning, as described earlier in this chapter: We learn to associate a neutral stimulus, such as money (CS), with rewards such as food, security, and power (US). Money is really only pieces of metal or paper, or electronically represented as numbers in our bank account, but these and other neutral objects become meaningful through their associations with unconditioned stimuli.

Most common reinforcement schedules

Combining the basis for reinforcement with the regularity of reinforcement yields the four most common reinforcement schedules: fixed interval, variable interval, fixed ratio, and variable ratio.

Fixed-Ratio (FR)

Occurs when reinforcement is provided after a certain amount of time has passed. Imagine that you feed your cat twice a day. After some number of days, the cat will start to meow and rub against you at about the feeding times, especially if you are in the location where you typically put out the food. An increase in the behavior just before the opportunity for reinforcement and then a dropping off after reinforcement. Many students follow this kind of pattern when taking courses with regularly scheduled exams. They work extremely hard on the days before the exam and then slack off a bit immediately after the exam.

Variable-Ratio (VR)

Occurs when reinforcement is provided after the passage of time, but the time is not regular. Although you know you will eventually be reinforced, you cannot predict when it will happen. For example, getting texts from friends occurs on a variable interval schedule. You might check for messages throughout the day if you find receiving such messages reinforcing. Unlike the cat learning on an FI schedule, you never know when you will receive reinforcement, so you have to check back frequently. Professors give pop quizzes because they encourage more regular studying by students. If you cannot predict when you will be quizzed, you have to keep up with your classwork and always be prepared.

Fixed-Interval (FI)

Occurs when reinforcement is provided after a certain number of responses have been made. Factory workers who are paid based on the number of objects they make are a good example of the FR schedule. Teachers sometimes use this kind of schedule to reward children for cooperative classroom behavior. Students can earn a star for behaving well. After they collect a certain number of stars, they receive some kind of reinforcer, such as getting to select the next book the teacher will read. Likewise, your local pizzeria might give you a punch card that gives you a free pizza after you buy 10. In each case, the more you do, the more you get. Therefore, FR schedules typically produce high rates of responding.

Variable-Interval (VI)

Occurs when reinforcement is provided after an unpredictable number of responses. Games of chance provide an excellent example of a VR schedule. At a casino, you might drop a lot of money into a slot machine that rarely rewards you with a win. Such behavior is not simply the result of an addiction to gambling. Rather, people put money in slot machines because the machines sometimes provide monetary rewards. VR schedules lead to high rates of responding that last over time because you know that eventually there will be a payoff for responding. You just do not know when it will happen—or even if you will still be the player on that machine at that time."""
week_3_2_extra = """Sorts of implicit memory

Priming, procedural, classical conditioning, nonassociative learning

Priming

A facilitation in the response to a stimulus due to recent experience with that stimulus or a related stimulus. As mentioned earlier, priming is reflected in a facilitation in a response to a stimulus due to recent experience with that stimulus (called repetition priming) or a related stimulus. Priming can be perceptual and conceptual 

Perceptual priming

Priming can be perceptual, in which a response to the same stimulus is facilitated For perceptual priming, brain regions that underlie perceptual processing come into play.

Conceptual priming

Or it can be conceptual, where a response to a conceptually related stimulus is facilitated. For instance, the word table might facilitate a response to the word chair. Whereas for conceptual priming, brain regions involved in conceptual processing are important

Procedural memory

A type of implicit memory that involves skills and habits. Suppose that while driving home you realize you have been daydreaming and have no memory of the past few minutes. During that time, you used implicit memories of how to drive and how to get where you were going, so you did not crash the car or go in the wrong direction. This type of implicit memory is called procedural memory. Procedural memories include skilled and goal-oriented behaviors that become automatic, such as motor skills, cognitive skills, and habitual behaviors. Procedural memories are reflected in knowing how to do something. Motor skills include memory of how to coordinate muscle movements to ride a bicycle, ski, roller-skate, row a boat, or drive. You automatically stop when you see a red light because you have learned to do so, and you might drive home on a specific route without even thinking about Your ability to understand the words on this page is an example of the cognitive skill of reading, which is another example of procedural memory. Procedural memories are very resistant to decay. Once you learn to ride a bike, skate, or read, it is likely that you will always be able to do so. The brain systems that underlie procedural memories vary somewhat depending on the specific memory but generally include the basal ganglia and, for motor skills, the cerebellum.

Classical conditioning

Association between stimuli

Nonassociative learning

Habituation and sensitization are important for this. 

Kinds of explicit memory

Episodic memory and semantic memory

Stages of memory

Encoding to Storage to Retrieval

Levels of processing model: 

Another factor proposed to influence the likelihood of memory encoding is the depth of mental processing. In their levels of processing model. The more deeply an item is encoded and the more meaning it has, the better it is remembered. Although rehearsing an item might improve memory for that item, the way the item is rehearsed matters. Craik and Lockhart proposed that different types of rehearsal lead to different levels of encoding. 

Maintenance rehearsal

Repeating the item over and over. This leads to shallow processing (surface form).

Elaborative rehearsal

Encodes the information in more meaningful ways, such as thinking about the item conceptually or deciding whether it refers to oneself. In other words, in this type of rehearsal, we elaborate on basic information by linking it in meaningful ways to existing knowledge. This leads to deep processing (meaning).

Method of loci or memory place

This mnemonic strategy of associating items you want to remember with physical locations is referred to as the *method of loci*, or memory palace. Suppose you want to remember the names of classmates you just met. First, you might visualize items from various places on your typical route across campus, or you might visualize parts of the physical layout of some familiar location, such as your bedroom. Then you would associate your classmates’ names with the items and places you have visualized. You might picture Justin climbing on your dresser, Malia sitting on a chair, and Anthony hiding under the bed. When you later need to remember the names, you would visualize your room, mentally walk yourself through it, and retrieve the name of the person associated with each piece of furniture.

Iconic memory

When you look at something and quickly glance away, you can briefly picture the image and recall some of its details. This type of visual sensory memory is called iconic memory.

Echoic memory

When someone protests, “You’re not paying attention to me,” you might be able to repeat back the last few words the person spoke, even if you were thinking about something else. This type of auditory sensory memory is called echoic memory.

Memory span

New items in working memory interfere with the recall of older items because working memory can hold a limited amount of information. The cognitive psychologist George Miller (1956) noted that the limit is generally seven items (plus or minus two). This figure is referred to as memory span. More-recent research suggests that Miller’s estimate may be too high and that working memory may be limited to as few as four items 

Primacy effect

The primacy effect refers to the better memory that people have for items presented at the beginning of the list. 

Recency effect

The recency effect refers to the better memory that people have for the most recent items, the ones at the end of the list

Replay 

If the consolidation of memories involves enhancing connections between neurons that represent the memory, it follows that the more these neurons fire together, the more likely they are to wire together. One way this occurs is by memory replay in the brain. Replay occurs when the neural circuit representing the memory fires again. Reminders of the memory when you are awake can replay the memory in your brain. It has also been demonstrated in rodents that neural circuits representing memories replay during sleep. Events that are recently learned or on your mind during the day may be more likely to be replayed during sleep. It has even been shown that reminders of events during sleep, such as a sound or smell associated with an event, can lead to better memory.

Retrieval practice

Retrieval practice **is a strategy of bringing information to mind by deliberately trying to recall it. Recent research in classrooms has shown that repeated testing that includes retrieval practice strengthens memory better than spending the same amount of time reviewing information you have already read does. 

Context-dependent memory

A unique study showed that we encode the physical context of a memory along with the information, and the context can help retrieve the memory. People learned lists of words either on land or underwater. When they had to recall the words later on, they remembered more words if they were tested in the same environment where they had learned the words.

State-dependent memory

Like physical context, internal cues can affect the recovery of information from long- term memory. Think about mood. When you are in a good mood, do you tend to recall good times? At the end of a bad day, do negative memories tend to surface? Memory can be enhanced when a person’s internal states match during encoding and recall. State-dependent memory also applies to internal states brought on by drugs or alcohol. You most likely will not remember much of anything you learn while intoxicated. Whatever you do learn, however, may be easier to recall when you are intoxicated than when you are sober, though do not count on it. 

Good retrieval cues

Context reinstatement, Re-create the state of mind in which the original learning occurred and encoding specificity principle. 

Context reinstatement

Re-create the context in which the original learning occurred. For example, when encoding an item into memory, you are storing not just that item but also aspects of the encoding context or situation, such as the room you are in, any smells or sounds, and even your mood at the time. 

Encoding specificity principle

The idea that any stimulus that is encoded along with an experience can later trigger a memory of the experience. A richter encoding context results in better recall.

Savings
Even if you cannot remember something, traces of the memory might exist. For instance, you may remember very little of the Spanish or calculus you took in high school, but relearning these subjects would take you less time and effort than it took to learn them the first time. The difference between the original learning and relearning is called savings.

Tip-of-the-tongue phenomenon

A type of blocking in which people experience great frustration as
they try to recall specific, somewhat obscure words. For instance, when asked to provide a word that means “patronage bestowed on a relative, in business or politics” or “an astronomical instrument for finding position,” people often struggle. Sometimes they know which letter the word begins with, how many syllables it has, and possibly what it sounds like. Even with these partial retrieval cues, they cannot pull the precise word into working memory.

Infantile amnesia

Most people cannot remember specific episodic memories from before age 3 or 4 because of what is called infantile amnesia. The ability to form lasting episodic memories is thought to depend on the early development of the prefrontal cortex and language abilities. If you have a specific memory from around this age or earlier, the memory is likely to have come from another source, such as your parents, siblings, or a picture from your childhood.

False memory
Researchers have devised tests for investigating whether people can be misled into recalling or recognizing events that did not happen. When people imagine an event happening, they form a mental image of the event, and they might later confuse that mental image with a real memory. Essentially, this is a problem in monitoring the source of the image.

Repressed memories

Over the past few decades, one of the most heated debates in psychological science has centered on repressed memories. On the one side, some psychotherapists and patients claim that long-repressed memories for traumatic events can resurface during therapy. Recovered memories of sexual abuse are the most commonly reported repressed memories. On the other side, memory researchers such as Elizabeth Loftus point out that little credible evidence indicates that recovered memories are genuine or at least sufficiently accurate to be believable. Part of the problem is best summarized by the memory researcher Daniel Schacter: “I am convinced that child abuse is a major problem in our society. I have no reason to question the memories of people who have always remembered their abuse, or who have spontaneously recalled previously forgotten abuse on their own. Yet I am deeply concerned by some of the suggestive techniques that have been recommended to recover repressed memories”"""
week_4_1_extra = """Conformation bias

Focusing only on information that supported their views.

Hindsight bias

When events turned out contrary to their predictions, many people created after-the-fact explanations. This error in reasoning is known as hindsight bias. For instance, people who later claimed to
have known that Donald Trump would defeat Clinton pointed to Clinton’s defeat by Barack Obama in the 2008 Democratic primary and the narrowness of her victory over Bernie Sanders in the 2016 primary.

Loss aversion

Research on framing indicates that when people make choices, they may weigh losses and gains differently. They are generally much more concerned with costs than with benefits, an emphasis known as loss aversion.

Endownment effect

The endowment effect is the tendency to value things we own more than we would pay to buy them, as if the fact that we own something endows it with some additional value in our minds. That is, the price participants required to sell an object they owned was more than the price participants were willing to pay to buy the same object.

Appraisal tendency framework

Why would an unrelated mood change the price required to buy or sell? According to the appraisal tendency framework, moods elicit tendencies, such as wanting to move toward something or away from it. These mood-related tendencies influence how we appraise unrelated information and choices encountered while in that affective state. Incidental affective states can influence the appraisal or evaluation of unrelated decisions, such that positive moods make people more optimistic about their chances of winning the lottery.

Overcoming obstacles to solutions

Understanding by formulating subgoals, Restructuring, Use an algorithm, Working backward, Use an analogy or Wait for a sudden insight.

Use an algorithm 

One such strategy is using an *algorithm*. An algorithm is a guideline that, if followed correctly, will always yield the correct answer. If you wanted to know the area of a rectangle, for example, you could get the right answer by multiplying its length times its width. This formula is an algorithm because it will always work. Similarly, if you follow a recipe exactly, it should always yield pretty much the same outcome. Suppose, however, you substitute one ingredient for another: You use oil instead of the butter that the recipe calls for. Here, you are using a heuristic that one type of fat is equal to another. Your result will likely be fine, but there is no guarantee.

Working backward

Another good conscious strategy for overcoming obstacles is *working backward*. When the appropriate steps for solving a problem are not clear, proceeding from the goal state to the initial state can help yield a solution. Consider the water lily problem: Water lilies double in area every 24 hours. On the first day of summer there is only one water lily on the lake. It takes 60 days for the lake to be completely covered in water lilies. How many days does it take for half of the lake to be covered in water lilies?

Use an analogy 

Transferring a problem-solving strategy means using a strategy that works in one context to solve a problem that is structurally similar. To accomplish this kind of transfer, we must pay attention to the structure of each problem. For this reason, analogous problems may enhance our ability to solve each one. Some researchers have found that participants who solve two or more analogous problems develop a schema that helps them solve similar problems. Analogous solutions work, however, only if we recognize the similarities between the problem we face and those we have solved and if the analogy is correct.

Two approaches to decision making

Maximizing and satisficing.

Maximizing

Maximizers seek to identify the perfect choice among a set of options.

Satisficers

Seek to find a “good enough” choice that meets their minimum requirements.

Vocal chords

The vocal cords are folds of mucous membranes that are part of the larynx, an organ in the neck, often called the voice box.

Oral cavity

The part of the mouth behind the teeth and above the tongue.

Producing sounds

People speak by forcing air through the vocal cords The air passes from the vocal cords to the oral cavity There, jaw, lip, and tongue movements change the shape of the mouth and the flow of the air, altering the sounds produced by the vocal cords. 

Expressive aphasia/Broca’s aphasia

Caused by a lesion in the left frontal lobe. Broca’s aphasia interrupts their ability to speak. These individuals generally understand what is said to them, and they can move their lips and tongues, but they cannot form words or put one word together with another to form a phrase.

Receptive aphasia/Wernicke’s aphasia

When Wernicke’s area is damaged, patients develop receptive aphasia in which they have trouble understanding the meaning of words. Those with receptive aphasia are often highly verbal, but what they say does not follow the rules of grammar or make sense.

Joint Attention

Early interactions with caregivers lay the groundwork for children’s
acquisition of language. If the caregiver is looking at the toy when saying a new name, “dax,” the child will assign the name “dax” to the toy. ****If the caregiver is looking at something else when saying the new name, the child will not assign the name “dax” to the toy.

Overgeneralization 

As children develop more-sophisticated ways of
using language, one relatively rare but telling error they make is to overapply new grammar rules they learn. Children may start to make mistakes at ages 3 to 5 with words they used correctly at age 2 or 3. For example, when they learn that adding -*ed* makes a verb past tense, they then add -*ed* to every verb, including irregular verbs that do not follow that rule. Thus they may say “runned” or “holded” even though they may have said “ran” or “held” at a younger age.

Universal grammar

The linguist Noam Chomsky (1959) transformed the field of linguistics when he hypothesized that language must be governed by universal grammar. In other words, according to Chomsky, all languages are based on humans’ innate knowledge of a set of universal and specifically linguistic elements and relationships. Chomsky argued that how people combine these elements to form sentences and convey meaning is only a language’s surface structure and introduced the term deep structure."""
week_4_2_extra = """Psychometric approach to measuring intelligence

An attempt to understand the nature of intelligence by studying the pattern of results obtained on intelligence tests. Focuses on how people perform on standardized tests that assess mental abilities. These tests examine what people know and how they solve problems. For much of the past century, the psychometric approach to intelligence has been dominant and influential. This approach has especially affected how we view intelligence in everyday life, at least within industrialized nations. There are two main types of standardized tests: Achievement tests and Aptitude tests.

Achievement tests

Achievement tests assess people’s current levels of skill and of knowledge. 

Aptitude tests

Aptitude tests seek to predict what tasks, and perhaps even what jobs, people will be good at in the future. For both kinds of tests, the stakes can be high. People’s performance on them can hugely affect
their lives.

Triarchic theory of intelligence 

Suggests that there are three types of intelligence: analytical, creative, and practical. Although this differentiation makes intuitive sense, some intelligence researchers have been critical, suggesting that the available evidence does not support Sternberg’s mode. 

Analytical intelligence

Analytical intelligence is similar to that measured by psychometric tests, being good at problem solving, completing analogies, figuring out puzzles, and other academic challenges. 

Creative intelligence

Creative intelligence involves the ability to gain insight and solve novel problems—to think in new and interesting ways.

Practical intelligence

Practical intelligence refers to dealing with everyday tasks, such as knowing whether a parking space is large enough for your vehicle, being a good judge of people, being an effective leader, and so on.

Correlation between reaction time and general intelligence

Negative weak correlation. So reaction time is faster when high intelligence score. Correlation is weak. 

Correlation between discrimination task performance and general intelligence

Negative weak correlation (.5). The more time someone needs, lower the intelligence score. Correlation is weak. 

Correlation between working memory Capacity an general intelligence

Presenting long sentences or a lot of items. The more items that can be repeated, the higher intelligence score. 

Correlation between executive control and general intelligence

Presented with a display were they have to read letters were they are at the left side, and a tone tells them that they have to look at the right side or both. People fail to switch, lower on Intelligence score. 

Flynn effect

World wide increase in IQ scores over the last decade about 3 points per decade. This supports the idea that an enriched environment will enhance cognitive performance. Since genes cannot have changed much in modern humans, the increase in cognitive performance in IQ during this period must be due to environmental factors."""
week_5_1_extra = """"Zygote

The process of development begins at the moment of conception, when a sperm unites with an egg to create a *zygote*, the first cell of a new life. At about 2 weeks after conception, the zygote is firmly implanted in the uterine wall, and the next stage of development begins. 

Embryo

From about 2 weeks to 2 months, the developing human is known as an embryo. During this stage, the organs (such as the heart, lungs, liver, kidneys, and sex organs) and internal systems (such as the nervous system) begin to form. During this period, the embryo is especially vulnerable. Exposure to harm, such as toxins, drugs, extreme stress, or poor nutrition, can have lasting effects on developing organ systems.

Fetus

After 2 months of prenatal development, all the organs are formed, the heart begins to beat, and the growing human is called a *fetus*. The body continues to grow into its infant form. The fetus grows larger and stronger as the body organs mature to a point where survival is possible outside the womb.

Fetal alcohol spectrum disorders (FASDs) 

Drinking alcohol during pregnancy can lead to fetal alcohol spectrum disorders (FASDs). Among the symptoms of this
family of disorders are low birth weight, face and head abnormalities, deficient brain growth, and evidence of impairment such as behavioral or cognitive problems or low IQ.

Infant reflexes

Infants are born with innate abilities that help them survive, including the grasping reflex, rooting reflex, and sucking reflex.

Grasping reflex

This reflex is a survival mechanism that has persisted from our primate ancestors. Young apes grasp their mothers, and this reflex is adaptive because the offspring need to be carried from place to place.

Rooting reflex

The turning and sucking that infants automatically engage in when a nipple or similar object touches an area near their mouths.

Sucking reflex 

If they find an object, they will show the sucking reflex. 

Visual acuity in newborns

The ability to distinguish differences among shapes, patterns, and colors is known as visual acuity. Newborns’ visual acuity for distant objects is poor, but it increases rapidly over the first 6 months and reaches adult levels when the infant is about a year old. The increase in visual acuity is probably due to a combination of practice looking at things in the world, the development of the visual cortex, and the development of the cones in the retina

Preferential-looking technique

In using this technique, the researchers show an infant two things. If the infant looks longer at one of the things, the researchers know the infant can distinguish between the two and finds one more interesting. In these studies, the mother or another caregiver was asked to hold the infant in front of a display of two images. The experimenter, not knowing which image was on which side, would observe through a peephole to see where the infant preferred to look. This research revealed that infants look at stripes with high contrast more readily than at gray images. The smaller the stripes are, that is, the less contrast between the images, the more difficult it becomes for infants to distinguish them from the gray patches.

The Memory-Retention Test

In this test, infants learn that kicking their feet moves a mobile because one foot is attached to the mobile by a ribbon around the ankle. After a delay, the infants are placed back under the mobile. If the infants soon kick their feet vigorously to get the mobile to move, they have shown that they remember moving the mobile during the learning phase.

Imprinting

Some bird species seem to have a sensitive period in which fledgling chicks become strongly attached to a nearby adult, even one from another species. This pattern occurs for birds such as chickens, geese, and ducks. Because these birds can walk immediately after hatching, they are at risk of straying from their mothers. Therefore, within about 18 hours after hatching, the birds will attach themselves to an adult (usually to their mothers) and then follow the object of their attachment. The ethologist Konrad Lorenz (1935) called such behavior imprinting. He noted that goslings that became imprinted on him did not go back to their biological mothers when later given access to them. Such birds preferentially imprint on a female of their species if one is available, however.

Harlow findings 

In a now-famous series of experiments, Harlow placed infant rhesus monkeys in a cage with two different “mothers”. One surrogate mother was made of bare wire and could give milk through an attached bottle. The second surrogate mother was made of soft terry cloth and could not give milk. Which of these two substitute mothers do you think the infant monkeys preferred Harlow’s findings established the importance of contact comfort—the importance of physical touch and reassurance —in aiding social development.

Strange-situation test

In a laboratory set up like a playroom, the child, the caregiver, and a friendly but unfamiliar adult engage in a series of eight semi-structured episodes. The crux of the procedure is a standard sequence of separations and reunions between the child and each adult. Over the course of the eight episodes, the child experiences increasing distress and a greater need for caregiver proximity. The researchers observe the test through a one-way mirror in the laboratory. The extent to which the child copes with distress and the strategies for doing so indicate the quality of the child’s attachment to the caregiver. The researchers record the child’s activity level and actions such as crying, playing, and paying attention to the caregiver and the stranger. Using the strange-situation test, Ainsworth classified infant/caregiver pairs as having one of three attachment styles: secure, insecure, or anxious. Later, other researchers added a fourth attachment style: disoriented-disorganized.

Critiques Piaget theory

Children know more than we think and children go smoother through the stages. Also Piaget thought that all adults were formal operational thinkers but formal operational thinking does not just develop, it needs to be taught. Object permanence also develops in the few months of life. Development of conservation occurs earlier and Preoperational children are less egocentric than supposed by Piaget. 

Relationship between theory of mind and prosocial behavior

Those who exhibit greater capacity for theory of mind are more likely to perform prosocial behavior."""
week_5_2_extra = """Moods

Moods **are diffuse, long-lasting emotional states that do not have an identifiable trigger or a specific behavioral and physiological response. Rather than changing what is happening, they more subtly color thought and behavior. Often people who are in good or bad moods have no idea why they feel the way they do. Thus, moods refer to people’s vague senses that they feel certain ways.

Circumplex model

Emotions have also been classified along different dimensions. One such system is the circumplex model. In this model, emotions are plotted along two continuums: valence, or how negative or positive they are, and arousal, or how activating they are. To understand the difference between valence and arousal, imagine you discover that you have lost the one-dollar bill that was in your pants pocket. This experience will most likely make you unhappy, so you will judge it to negative valence. It also might make you slightly aroused (increase your autonomic responses somewhat). Now imagine that you find a lottery ticket that turns out to be worth a million dollars. This experience will most likely make you very, very happy, so you will judge it as on the positive side of the valence scale. Your arousal will probably be topping the chart.

Arousal

Is a generic term used to describe physiological activation (such as increased brain activity) or increased autonomic responses (such as quickened heart rate, increased sweating, or muscle tension).

Systems involved in emotion

We now know that many brain structures outside the limbic system are involved in emotion and that many limbic structures are not central to emotion per se. For instance, the hippocampus is important for memory, and the hypothalamus is important for motivation. Thus, the term *limbic system* is used mainly in a rough, descriptive way rather than as a means of directly linking brain areas to specific emotional functions. For understanding emotion, the most important limbic system structures are the insula and the amygdala other areas contribute to emotional processing. In addition, various regions of the prefrontal cortex are important for generating emotions.

Insula

The insula receives and integrates somatosensory signals from the entire body. It is also involved in the subjective awareness of bodily states, such as sensing your heartbeat, feeling hungry, or needing to urinate. Given that emotions produce bodily responses, it is not surprising that the insula plays an important role in the experience of emotion. Imaging studies have found that the insula is particularly active when people experience disgust, such as when exposed to bad smells. Damage to the insula interferes with the experience of disgust and also with recognizing disgust expressions in others. The insula is also activated in a variety of other emotions, including anger, guilt, and anxiety.

Amygdala

The amygdala processes the emotional significance of stimuli, and it generates immediate emotional and behavioral reactions. According to the emotion theorist Joseph LeDoux, the processing of emotion in the amygdala involves a circuit that has developed over the course of evolution to protect animals from danger. LeDoux has established the amygdala as the brain structure most important for emotional learning, as in the development of classically conditioned fear responses. People with damage to the amygdala do not develop conditioned fear responses to objects associated with danger

Fast pathway to the amygdala

The fast path is a “quick and dirty” system that processes sensory information nearly instantaneously. With the exception of smell, all sensory information travels to the thalamus before going on to other brain structures and the related portions of the cortex. Along this fast path, sensory information travels quickly through the thalamus directly to the amygdala for priority processing

Slow pathway to the amygdala

The slow path leads to more deliberate and more thorough evaluations. Along this slow path, sensory material travels from the thalamus to the cortex (the visual cortex or the auditory cortex), where the information is scrutinized in greater depth before it is passed along to the amygdala. Theorists believe that the fast system prepares animals to respond to a threat in case the slower pathway confirms the threat. You have experienced the two pathways if, for example, you have shied away from a blurry movement in the grass only to realize it was the wind and not a snake.

Amygdala and memory

Emotional events are especially likely to be stored in memory. The amygdala plays a role in this process. Brain imaging studies have shown that emotional events are likely to increase activity in the amygdala and that increased activity is likely to improve long-term memory for the event. Researchers believe that the amygdala modifies how the hippocampus consolidates memory, especially memory for fearful events. This adaptive mechanism enables us to remember harmful situations and thus potentially avoid them.

Polygraph 

Potential suspects in criminal investigations and applicants for certain types of jobs, such as those that involve classified documents, are often asked to take a polygraph test, known informally as a lie detector test. A polygraph is an electronic instrument that assesses the body’s physiological response to questions. It records numerous aspects of arousal, such as breathing rate and heart rate. A polygraph cannot differentiate the increased physiological arousal. 

Facial expression hypothesis 

When your facial expression is different it can lead to other emotions. It is creating some sort of emotional response. Example of reading the comic and pen above lip (making a frown) or between teeth (making a smile) in relationship to how funny you thought the comic was. 

Misattribution of arousal

When people misidentify the source of their arousal, it is called misattribution of arousal. In one exploration of this phenomenon, researchers tried to determine whether people could feel romantic attraction through misattribution. Men who walked across this narrow and scary bridge over the Capilano River displayed more attraction to the female experimenter on the bridge than did men who walked across a safer bridge.

Disruptive emotions

Our actions can be disrupted by negative feelings, such as nervousness, or  positive feelings, such as being distracted by looking forward to an exciting upcoming event.

Negative-feedback model of homeostasis

Similarly, the human body regulates a set-point of around 37°C (98.6°F). When people are too warm or too cold, brain mechanisms (particularly the hypothalamus) initiate responses such as sweating (to cool the body) or shivering (to warm the body). At the same time, people become motivated to perform behaviors such as taking off orThe behaviors continue until the set-point temperature is reached, causing the mechanism to discontinue. This entire process is called a *negative-feedback* loop because feedback decreases the activity of the system.

Habits

Over time, if a behavior consistently reduces a drive, it becomes a *habit* and therefore the dominant response produced by arousal. The likelihood that a behavior will occur is due to drive and habit.

Delaying gratification 

One of the defining features of self-regulation is postponing immediate gratification in the pursuit of long- term goals. For example, students who want to be accepted to graduate school often must stay home and study while their friends are out having fun. Delaying gratification in the service of goals is difficult because of temporal discounting.

Turning hot cognitions into cold cognitions

This strategy involves mentally transforming the desired object into something undesired. In one study, children reported imagining a tempting pretzel as a brown log or imagining marshmallows as clouds. Hot cognitions focus on the rewarding, pleasurable aspects of objects. Cold cognitions focus on conceptual or symbolic meanings. 

Rationalizing

Another way to reduce dissonance is by rationalizing away the conflict. Rationalizations are not truths but rather myths that we tell ourselves to reduce dissonance. For example, smokers might believe that smoking is dangerous but rationalize the conflict between the belief and smoking by convincing themselves that
the stress of quitting would be worse for their health than smoking is."""
week_6_1_extra = """Social brain hypothesis

According the social brain hypothesis primates have large prefrontal cortexes because they live in dynamic and complex social groups that change over time. 

Reciprocity

Implies that if one person helps another person he/she will be inclined to help you as well. Same as if you harm another person.

Transitivity

People generally share the same opinions as your friends. Same with liking the same person as disliking the same person as others.

Risky-shift effect

Groups often make riskier decisions than individuals do. It accounts for why corporate boards, for example, might make relatively risky investments that none of the members would have tried alone.

Individuated

Meaning we walk around with a sense of ourselves as individuals who are responsible for our own actions.

Four sorts of group influence

Group dynamics, Conformity, Compliance, Obedience

Kind of group dynamics

Mere presence effect, social loafing, deindividuation."""
week_6_2_extra = """Psychodynamic approach 

Personality arises from unconscious conflicts and desires. Outdated theory! Human behavior is the expression of unconscious motives and wishes that have their origin in early childhood experiences. For most part unknown to a person. To know a person you need to know the underlying dynamics. 

Catharsis

Release of repressed memories (make patiens aware of the memories). It is the goal of psychodynamic treatment. It is hard because there is resistance. These memories evoke anxiety, that is why they are suppressed in the first place. 

Personality theory of Freud

3 subsystems of human personality. ID, which consists of the biological urges. The ego, which derived from id when confronted with reality. And the Superego, derived from ego. It is an internalized code of conduct. 

Inhibited children

Person-centered approach

The most prominent humanistic psychologist was Carl Rogers, who introduced a person-centered approach to understanding personality and human relationships. That is, he emphasized people’s subjective understandings of their lives. In the therapeutic technique Rogers advocated, the therapist would create a supportive and accepting environment. The therapist and the client would deal with the client’s problems and concerns as the client understood them.

Unconditional positive regard

Rogers encouraged parents to raise their children with
unconditional positive regard. That is, parents should accept and prize their children no matter how the children behave. Parents might express disapproval of children’s bad behavior, but at the same time they should express their love for the children. According to Rogers, a child raised with unconditional positive regard would develop a healthy sense of self-esteem and would become a fully
functioning person. 

Internal locus of control

People with an internal locus of control believe they bring about their own rewards.

External locus of control

People with an external locus of control **believe rewards, and therefore their personal fates, result from forces beyond their control. These generalized beliefs affect individuals’ behaviors and level of psychological adjustment.

Personal constructs

The cognitive theorist George Kelly (1955) emphasized how individuals view and understand their circumstances. He referred to such views and understandings as personal constructs: personal theories of how the world works. Kelly believed that people view the world as if they are scientists, constantly testing their theories by observing ongoing events, then revising those theories based on what they observe. According to Kelly, personal constructs develop through experiences and represent individuals’ interpretations and explanations for events in their social worlds.

Person-situation interaction 

The core idea of this theory is that people react in predictable ways to specific conditions: If A, then B. If there is a reward, then I am excited to pursue it. If there is an uncertain outcome, then I worry about it.

Stong situations

Strong situations (e.g., airplanes, religious services, job interviews) tend to mask differences in personality because of the power of the social environment.

Weak situations

For example, parks, bars, one’s house, tend to reveal differences in personality.

Rank-order stability

Stability in personality refers to a lack of change in where a person stands on the trait relative to other people. This is referred to as *rank-order* stability. For instance, over many years the relative rankings of individuals on each of the Big Five personality traits remain stable. A meta-analysis of 150 studies, through which a total of nearly 50,000 participants had been followed for at least one year, found strong evidence for stability in personality. The rank orderings of individuals on any personality trait were quite stable over long periods across all age ranges. 

Mean-level changes

Focusing only on rank-order stability can hidden changes in personality that many people experience at the same stages of life, referred to as mean-level changes. For example, people tend to get less neurotic, less open to new experiences; more agreeable and more conscientious, even though their rank ordering remains stable. 

Evaluative

Vazire argues that people have blind spots about aspects of their personalities because they want to feel good about themselves. This tendency is particularly true for traits that are highly valued in society, such as creativity. In personality research, these traits are referred to as evaluative.

Working self-concept

When considering themselves or their personalities, people are especially likely to mention characteristics that distinguish them from other people. For example, when working with a group of women, a Black man might be most aware of his maleness. When working with a group of White people, he might be most aware of being Black."""
week_7_1_extra = """Maladaptive behavior

That is, does the behavior interfere with the person’s ability to respond appropriately in some situations? For example, a person who is afraid to leave the house may avoid feeling anxious by staying inside, and that behavior might prevent the person from working, having a social life, or both.

Criteria psychopathology behavior

(1) Does the person act in a way that deviates from cultural norms for acceptable behavior? (2) Is the behavior maladaptive? (3) Is the behavior self-destructive, does it cause the individual personal distress, or does it threaten other people in the community? (4) Does the behavior cause discomfort and concern to others, thus impairing a person’s social relationships?

Diagnostic and Statistical Manual of Mental Disorders (DSM)

The main purpose of the DSM is description. It groups disorders based on similarity in symptoms, thereby providing a shared language and classification scheme for scientists and practitioners to communicate what they have learned about psychopathology. Another purpose of the DSM is to allow care providers to bill health insurance companies for treatment. Most insurance companies require a DSM diagnosis before they pay providers for care.

DSM-5

The current edition, DSM-5 (released in 2013), consists of three sections: (1) an introduction with instructions for using the manual; (2) diagnostic criteria for all of the disorders, which are grouped so that similar categories of disorders are located near each other and (3) a guide for future psychopathology research, which also includes conditions not yet officially recognized as disorders, such as excessive internet gaming and misuse of caffeine. In the second section of the DSM-5, disorders are described in terms of measurable symptoms. A client must meet specific criteria to receive a particular diagnosis. In the coming years, updated versions of the DSM will be released, with further changes to the description and classification of many disorders.

Categorical approach

One problem with the DSM is that it takes a categorical approach, which implies that a person either has a psychological disorder or does not. This approach fails to capture differences in the severity of a disorder. Moreover, it misleadingly implies that there is a distinct cutoff between the absence and presence of psychopathology. What “counts” as psychopathology is not an objective fact that can be determined with a diagnostic test, like a test for a bacterial infection. Instead, psychopathology reflects a social consensus about what to call a cluster of symptoms or behaviors.

Dimensional approach

The dimensional approach considers psychological disorders along a continuum on which people vary in degree rather than in kind. A dimensional approach recognizes that many psychological disorders are extreme versions of normal feelings. We are all a little sad at times, and sometimes we feel more sad than usual. But no specific amount of sadness passes a threshold for depressive disorders. In a dimensional approach, diagnosis is relatively easy at the extremes but more ambiguous in between. As an analogy, consider how we label someone as a social media influencer. Someone with 40 followers is not an influencer and someone with 40 million is. But there is no objective threshold between being an influencer and not, and the classification depends on human judgment and societal standards that shift over time.

Comorbidity

Psychological disorders commonly overlap. For instance, substance abuse is common across psychological disorders, and people with major depression (or a milder form known as persistent depressive disorder) often also have anxiety disorders (such as panic disorder or generalized anxiety disorder).

Types of psychopathology 

Psychologists have identified two major types of psychopathology: Internalizing and externalizing disorders. 

Internalizing disorders

Internalizing disorders are characterized by negative emotions, and they can be divided into broad categories that reflect the emotions of distress and fear. Examples of internalizing disorders include major depressive disorder, generalized anxiety disorder, and panic disorder. 

Externalizing disorders

Externalizing disorders are characterized by impulsive or out-of-control behavior. These disorders include alcoholism, conduct disorders, and antisocial personality disorder.

Specific phobia

In DSM-5, people are diagnosed with specific phobia based on the object of the fear. Specific phobias, which affect about 1 in 8 people around the globe, involve particular objects and situations. Common specific phobias include fear of snakes (ophidiophobia), fear of enclosed spaces (claustrophobia), and fear of heights (acrophobia).

Panic attacks

These are sudden, overwhelming attacks of terror and worry and often involve fears of having additional panic attacks. The attacks seemingly come out of nowhere, or they are cued by external stimuli or internal thought processes. Panic attacks typically last for several minutes, during which the person may begin to sweat and tremble; has a racing heart; feels short of breath; feels chest pain; and may feel dizzy and light-headed, with numbness and tingling in the hands and feet.

Depressive disorders

The DSM-5 categorizes several disorders as depressive disorders. The common feature of all depressive disorders is the presence of sad, empty, or irritable mood along with bodily symptoms and cognitive problems that interfere with daily life.

Cognitive triad

According to Aaron Beck, people suffering from depression perceive themselves, their situations, and the future negatively. These perceptions influence one another and contribute to the disorder. For example: Negative thoughts and beliefs about oneself (“I am worthless”; “I am a failure”; “I am ugly”), the world around one (“Everybody hates me”; “The world is unfair”), and the future (“Things are hopeless”; “I can’t change”).

Mania

Mania refers to an elevated mood that feels like being “on the top of the world.” This positive mood can vary in degree and is  accompanied by major increases in energy level and physical activity. For some people, mania involves a sense of agitation and restlessness rather than positivity.

Manic episodes 

Plays a rol in bipolar disorder 1. True manic episodes last at least one week and are characterized by abnormally and persistently elevated mood, increased activity, diminished need for sleep, grandiose ideas, racing thoughts, and extreme distractibility. During episodes of mania, heightened levels of activity and extreme happiness often lead to excessive involvement in activities that feel good at the time but can be harmful in the long run. People may engage in sexual indiscretions, buying sprees, risky business ventures, and similar “out of character” behaviors that they regret once the mania has subsided. They might also have severe thought disturbances and hallucinations.

Hypomania

Plays a role in bipolar disorder 2. These episodes are often characterized by heightened creativity and productivity, and they can be pleasurable and rewarding. Although these less extreme positive moods may be somewhat disruptive to a person’s life, they do not necessarily cause significant impairment in daily living or require hospitalization. The bipolar II diagnosis requires at least one major depressive episode.

Risk of suicide

According to Thomas Joiner, the individuals who are most at risk of dying by suicide both want to do so and are able to do so.

Fundamental needs for wanting to attempt suicide

The first of these fundamental needs is the need to belong, to feel connected with others. The second of these fundamental needs is the need for competence. 

Need to belong

That need is thwarted if we do not believe we have enough positive interactions with others who care about us. 

Need for competence

This need is thwarted if we do not feel like capable agents in the world. Joiner’s hypothesis is that we desire death when both the need to belong and the need for competence are frustrated.

Able to attempt suicide

Some form of repeated self- preparation is typically needed for people to overcome the pain or fear of death. Joiner writes that people at high risk for suicide reach that point “through a process of exposure to self-injury and other provocative experiences” and “when people get used to dangerous behavior . . . the groundwork for catastrophe is laid”. For example, a person who drives recklessly, engages in self-cutting, and/or experiments with drugs is more practiced at self-harm than someone who does not engage in any of these behaviors and is thus more likely to be able to carry out lethal self-injury.

Positive symptoms Schizophrenia 

Positive symptoms are features that are present in schizophrenia but not in typical behavior. 

Negative symptoms Schizophrenia

Negative symptoms are characteristics missing in schizophrenia that are typically part of daily functioning. Negative symptoms can include apathy, lack of emotion, and slowed speech and movement.

Catatonic behavior 

Sometimes those with schizophrenia display catatonic behavior, where they show a decrease in responsiveness to the environment. For example, they might remain immobilized in one position for hours. Catatonic features can also include a rigid, masklike facial expression with eyes staring into the distance.

Echolalia

Sometimes those with schizophrenia display echolalia behavior, where they repeat words they hear. 

Effects of Biology and Environment on Schizophrenia

****A child who has a genetic risk for schizophrenia and is raised in a dysfunctional family environment will have a high risk of developing schizophrenia. By contrast, a child who has no genetic risk for schizophrenia will have a low risk of developing the disorder whether raised in a dysfunctional family environment or a healthy family environment.

Obsessions

Obsessions are recurrent, intrusive, and unwanted thoughts, ideas, or mental images that increase anxiety. They often include fear of contamination, of accidents, or of one’s own aggression. The individual typically attempts to ignore or suppress such thoughts but sometimes engages in behaviors to neutralize the obsessions and reduce the emotional distress they cause.

Compulsions

Compulsions are particular acts that people with OCD feel driven to perform over and over to reduce anxiety. The most common compulsive behaviors are cleaning, checking, and counting. For instance, a person might continually check to make sure a door is locked because of an obsession that their home might be invaded, or a person might engage in superstitious counting to protect against accidents, such as counting the number of telephone poles while driving. The compulsive behavior or mental act, such as counting, is aimed at preventing or reducing anxiety or preventing something dreadful from happening."""
week_7_2_extra = """Reflective listening

Is a part of humanistic approaches to treatment, in which the therapist listens and then repeats the client’s concerns to help the person clarify their feelings.

System approach

According to a systems approach, an individual is part of a larger context. Any change in individual behavior will affect the whole system. This effect is often most apparent within the family. Each person in a family plays a particular role and interacts with the other members in specific ways. Over the course of therapy, how the individual thinks, behaves, and interacts with others may change. Such changes can profoundly affect the family dynamics. For instance, an alcoholic who gives up drinking may start to criticize other members of the family when they drink. In turn, the family members might provide less support for the person’s continuing abstinence. After all, if the family members do not have drinking problems, they might resent the comments. If they do have drinking problems, they might resist the comments because they do not want to give up drinking.

Brain surgery as treatment to disorders

Some brain surgery is used for disorders, but it involves small regions of the brain and is typically performed only as a last resort.

Alternative biological treatments for psychological disorders

Electroconvulsive therapy (ECT), transcranial magnetic simulation (TMS), and deep brain stimulation (DBS) all attempt to alter brain activity related to psychological symptoms.

Transcranial magnetic stimulation (TMS)

During TMS, a powerful electrical current runs through a wire coil, producing a magnetic field that is about 40,000 times the strength of Earth’s magnetic field. When rapidly switched on and off, this magnetic field induces an electrical current in the brain region directly below the coil, thereby interrupting neural function in that region

Deep brain stimulation (DBS)

This technique involves surgically implanting electrodes deep within the brain. The location of the electrodes depends on which disorder is being treated. Mild electricity is then used to stimulate the brain at an optimal frequency and intensity, much the way a pacemaker stimulates the heart. TMS is used mainly to treat severe depression.

Most typical medications for bipolar disorder

Mood stabilizers, especially lithium, and atypical antipsychotics are the most effective treatments for bipolar disorder. They control manic symptoms better than depression.

General prognosis for antisocial personality disorder

Few therapies work for them, but most people with antisocial personality disorder show a reduction in antisocial behavior after about age 40."""

week_glossaries = [week_7_1_extra]

# Size of dictionaries that go in flashcard generator
batch_size = 8

for i, week in enumerate(week_glossaries):
    cleaned_glossary = strip_empty_lines(week)
    glossary_dict = glossary_to_dict(cleaned_glossary)
    print(glossary_dict)

    # Generate flashcards
    flashcards = flashcard_generator_2(glossary_dict, batch_size)

    # Split flashcards in questions and answers lists
    questions, answers = format_flashcards(flashcards)
    print(f"EINDPRODUCT QUESTIONS ONDERWERP: {i + 1} | {questions}")
    print(f"EINDPRODUCT ANSWERS ONDERWERP: {i + 1} | {answers}")