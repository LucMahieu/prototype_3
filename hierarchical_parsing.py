from dotenv import load_dotenv
import os
import openai
import streamlit as st
from PyPDF2 import PdfReader

# Connect .env file where the API key for OPENAI is stored.
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit interface to upload lecture slides easily
uploaded_slide = st.file_uploader("Upload lecture slides in PDF format", type='pdf')


# Extracts the text from the uploaded PDF
def extract_pdf_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    return text


# Converts every line a text file into a key in a dictionary
def convert_to_dictionary(text):
    text = [line.lstrip() for line in text.splitlines() if line.strip()]
    dictionary = {}
    for line in text:
        key, value = line.split(' ', 1)
        dictionary[key] = value

    return dictionary


# Make call to OpenAI LLM
def openai_call(system_message, user_message, model, temp):
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


# Make dictionary with parent-children pairs from indexed topics
def parent_children_parsing(indexed_text):
    parent_children = {}

    # Split the text into clean lines.
    lines = [line.lstrip() for line in indexed_text.splitlines() if line.strip()]

    for line in lines:
        # Delete whitespaces before the index number.
        line = line.lstrip()
        # print(f"This is a line: {line}")

        # Save the index and corresponding content.
        index, content = line.split(' ', 1)

        # Determine indentation level.
        parent = index[:-1]

        if len(index) == 1:
            parent_children[index] = []
        elif parent in parent_children:
            parent_children[parent].append(index)
        else:
            parent_children[parent] = [index]

    return parent_children


def flashcard_generator(parent_children_pairs, content_dictionary):
    children = ""
    raw_flashcards = []
    for parent_key, children_keys in parent_children_pairs.items():
        parent = content_dictionary[parent_key]
        print(parent)
        for child_key in children_keys:
            if children == "":
                children += " '" + content_dictionary[child_key] + "'"
            else:
                children += "," + " '" + content_dictionary[child_key] + "'"
        print(children)
        flashcard_system_message = f"""
        Create 1 question explicitly about "{parent}" and
        an answer that includes the key concepts mentioned in "{children}"
        using a flashcard format where you first write the question on
        the front of the flashcard, followed by a semicolon (;) and then
        the answer to the question on the back of the flashcard.

        % BEGIN EXAMPLE
        Parent topic 1: Niko Tinbergen's four questions.

        Children topics 1: Used by researchers, Analyze, Understand, Behaviour.

        Flashcard 1: What are Niko Tinbergen's four questions used for?; 
        These questions help researchers analyze and understand behavior.
        
        Parent topic 2: Niko Tinbergen's asked four questions.

        Children topics 2: What is the causal basis of
        behavior? What is its function or evolutionary advantage?
        How does behavior develop within the individual? How does
        behavior influence interactions between individuals and the
        population as a whole?

        Flashcard 2: What do Niko Tinbergen's four questions ask about?
        1. Causal basis of behaviour
        2. Function of behaviour
        3. How behavior develops
        4. Influence on interactions
        % END EXAMPLE
        """
        flashcard_user_message = f"""
        Parent topic: {parent}
        Children topics: {children}
        Flashcard:
        """
        response = openai_call(
            flashcard_system_message,
            flashcard_user_message,
            model=gpt4,
            temp=0
        )

        raw_flashcards.append(response)
        children = ""

    return raw_flashcards


# OpenAI models
llm3_5 = 'gpt-3.5-turbo'
llm16k = 'gpt-3.5-turbo-16k'
gpt4 = 'gpt-4'

# Input which is processed by openai call
with open('IP02A.txt', 'r', encoding='utf-8', errors='replace') as f:
    IP02A_lecture = f.read()
with open('Inleiding_psy_hc_1.txt', 'r', encoding='utf-8', errors='replace') as f:
    Inleiding_psy_hc_1 = f.read()

# Instructions on how to process the input
cleaning_message = """
The following text is extracted from a lecture slide from a 
university. What elements of the following text are irrelevant 
for a student that wants to study the core learning material
for an exam? Remove those elements from the text whilst keeping 
the hierarchical structure. Make sure to also remove the 
following or similar words: introduction, topic, overview, 
conclusion, end, lecture, assignments, readings.
"""

indexing_message = """
The text below was extracted from presentation slides. Then 
determine what was likely the hierarchical structure of the 
text in order to restore the hierarchical structure by 
restructuring the current layout to fit the original structure. 
Make sure each line is indexed at the right level.

Rules:
- Only include words provided in de text below.
- Include all words directly related to the core learning material.
- Exclude all words related to the introduction, conclusion 
and structure of the presentation.
- Don't use indentations, only indexes.
- Write the indexes without separating period.

% OUTPUT EXAMPLE BEGIN
1 Dierenrijk (Animalia)
11 Gewervelden (Chordata)
111 Zoogdieren (Mammalia)
1111 Roofdieren (Carnivora)
11111 Hondachtigen (Canidae)
11112 Katachtigen (Felidae)
111121 Huiskat (Felis catus)
112 Vogels (Aves)
1121 Zangvogels (Passeriformes)
11211 Mussen (Passeridae)
113 Reptielen (Reptilia)
1131 Schubreptielen (Squamata)
11311 Slangen (Serpentes)
113111 Adder (Vipera berus)
114 Amfibieën (Amphibia)
1141 Kikkers (Anura)
% OUTPUT EXAMPLE END
"""

# Lectures to turn into flashcards.
lecture = [IP02A_lecture, Inleiding_psy_hc_1]

# On/Off button to rerun everything or to use the previous cache
rerun_everything = True

if rerun_everything:
    # Clean lecture text to only include core learning material
    core_material = openai_call(cleaning_message, lecture[1], model=gpt4, temp=0)

    # Index the core learning material by hierarchy
    indexed_text = openai_call(indexing_message, core_material, model=gpt4, temp=0)

    # Determine parent-children pairs
    parent_children = parent_children_parsing(indexed_text)

else:
    core_material = """"
    Topic 2
    The Brain and the Nervous System

    • Building blocks of the nervous system
    • Communication among neurons
    • Communication of the brain with the body
    • Studying the brain
    • The brain
    • Genes x environment phenotype

    • The nervous system is made up of two basic kinds of cells
    • Glia
    • Neurons

    Building blocks of the nervous system
    Neuron

    • Different types of neurons
    • Sensory receptors
    • Sensory (afferent) neurons
    • Motor (efferent) neurons
    • Interneurons

    Communication among neurons

    • Neurons either fire or do not fire
    • All‐or‐none law
    • Intensity variations by
    • variations in the number of neurons firing.
    • variations in firing rate.
    • Neurons interact
    • via synapses.
    • through chemical substances.

    • Synapse
    • the place where a signal passes from one nerve cell to another

    • Neurotransmitters
    • Chemical substances that transmit signals from one neuron to another
    • Lock‐and‐key Model
    • Effect is terminated by
    • autoreceptors
    • synaptic reuptake
    • enzymes

    • The binding of a neurotransmitter with a receptor produces an excitatory or inhibitory signal.

    • Drugs
    • Agonists
    • Increase of precursor
    • counteracting the cleanup enzymes
    • blocking the re‐uptake
    • mimicking the transmitter’s action
    • Antagonists
    • decrease precursor (or neurotransmitter)
    • increase effectiveness cleanup enzymes
    • enhance the re‐uptake
    • blocking of receptors

    Communication of the brain with the body

    • Somatic NS

    • Autonomic NS
    • Endocrine system

    Studying the brain

    • 19th century ‐> Phrenology
    • Bumps on the skull were interpreted in terms of personality traits.

    • Methods for studying the brain
    • Clinical observation of patients with brain damage
    • Experimental techniques
    • Invasive: animal studies (e.g., lesions, single‐cell recordings)
    • TMS (Transcranial Magnetic Stimulation)
    • Other techniques
    • Electrophysiology
    • EEG (ERP)
    • Brain imaging
    • (f)MRI scan
    • PET scan
    """
    indexed_text = """
    1 Psychology
    11 Psychology is the scientific study of mind, brain, and behavior
    12 Why do we need a science for that?
    13 Because common sense fails

    2 Genes and Evolution
    21 The genetic basis
    211 Genes
    212 Meaningful sections of the DNA molecule
    213 Govern the cell’s functioning by providing instructions for making proteins
    22 Gene Protein
    221 Gene expression
    222 Genotype
    223 Phenotype
    224 Monozygotic (identical) twins have the same genotype but different environments
    225 Each gene is paired with another gene
    226 Allele is one specific variant of a gene
    227 Homozygote: alleles on locus are the same
    228 Heterozygote: alleles on locus are different
    229 A specific trait or behavior is determined by the interaction between the environment (past and present) and one gene pair
    23 Where do our parent’s sets of genes come from?
    231 The genome is shaped by evolution over the years ‐> Darwin’s evolution theory
    24 Evolution by natural selection
    241 Charles Darwin hypothesized that all modern organisms are descended from a small set of shared ancestors
    242 The key mechanism of evolution is natural selection
    243 Organisms differ in genotype and variations in genotype are passed from generation to generation
    244 The evidence for modern evolutionary theory comes from many sources
    245 Despite overwhelming evidence, many people remain skeptical about the theory of evolution
    25 Genes and behavior
    251 Nature (genes) versus Nurture (environment)
    252 The nature nurture debate has become increasingly irrelevant
    253 Who we are is determined by how our genes are expressed in distinct environments
    254 Is it correct to claim that “a violent person has violent genes”?
    255 MAOA allele for low MAO activity
    256 Severe maltreatment
    257 Higher probability of being convicted of violent crimes
    """
    parent_children = {'1': ['11', '12', '13'], '2': ['21', '22', '23', '24', '25'], '21': ['211', '212', '213'],
                       '22': ['221', '222', '223', '224', '225', '226', '227', '228', '229'], '23': ['231'],
                       '24': ['241', '242', '243', '244', '245'],
                       '25': ['251', '252', '253', '254', '255', '256', '257']}

content_dict = convert_to_dictionary(indexed_text)
flashcards = flashcard_generator(parent_children, content_dict)
st.title("CORE MATERIAL")
st.write(f"CORE MATERIAL: {core_material}")
st.title("INDEXED TEXT")
st.write(f"INDEXED TEXT: {indexed_text}")
st.title("PARENT AND CHILDREN")
st.write(f"PARENT AND CHILDREN: {parent_children}")
st.title("CONTENT DICTIONARY")
st.write(f"CONTENT DICTIONARY: {content_dict}")
st.title("FLASHCARDS")
st.write(f"FLASHCARDS: {flashcards}")
