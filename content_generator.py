from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

load_dotenv()

def openai_call(system_message, user_message="", model='gpt-4', temp=0.0):
    message = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]
    response = client.chat.completions.create(model=model,
    temperature=temp,
    messages=message, response_format="json")

    return response.choices[0].message.content


def strip_empty_lines(text):
    return "\n".join(line.strip() for line in text.splitlines() if line.strip())


def batch_generator(data, batch_size):
    """
    Chunk the study materials into batches so they fit in the context window of the LLM.
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


def question_generator(dict, batch_size):
    questions = ""
    i = 1
    for batch in batch_generator(dict, batch_size):
        print(f"GENERATING BATCH {i}")
        i += 1

        # Load instructions for question generator
        with open("./prompts/question_generator.txt", "r") as f:
            system_message = f.read()
        
        # Input study materials
        user_message = f""" 
            Input: 
            {batch}
            
            Output:
        """

        response = openai_call(system_message, user_message, model='gpt-3.5-turbo-1106', temp=0.7)

        cleaned_response = strip_empty_lines(response)

        # Ensure the new response is added on a new line
        if not cleaned_response.endswith("\n"):
            cleaned_response += "\n"
        questions += cleaned_response

    return questions


def format_questions(raw_text):
    # Initialiseren van de lists.
    questions = []
    answers = []

    # Opsplitsen van de raw_text string in afzonderlijke questions.
    questions = raw_text.strip().split("\n")

    # Itereren over elke question.
    for card in questions:
        if ";;" not in card:
            print(f"WARNING: {card} is not a valid question. It will be skipped.")
            continue
        else:
            # Splitsen van de question in vraag en antwoord met behulp van ";;".
            question, answer = card.split(";;")

        # Toevoegen van vraag en antwoord aan hun respectieve lijsten.
        questions.append(question.strip())
        answers.append(answer.strip())

    return questions, answers

def run_generator(glossary):
    # cleaned_glossary = strip_empty_lines(glossary)
    glossary_dict = glossary_to_dict(glossary)

    # Generate questions
    questions = question_generator(glossary_dict, batch_size)

    # Split questions in questions and answers lists
    questions, answers = format_questions(questions)
    print(f"EINDPRODUCT QUESTIONS: {questions}")
    print(f"EINDPRODUCT ANSWERS: {answers}")


if __name__ == "__main__":
    # Size of the batches that go in question generator
    batch_size = 8

    # Load glossary from txt file
    with open("./study_materials/ml_overview.txt", "r") as f:
        glossary = f.read()
    
    # Generate questions
    run_generator(glossary)

    