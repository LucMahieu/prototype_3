from dotenv import load_dotenv
import os
import openai

# Load OpenAI API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


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


# OpenAI models
llm16k = 'gpt-3.5-turbo-16k'
gpt4 = 'gpt-4'

# Input which is processed by openai call
with open('IP02A.txt', 'r', encoding='utf-8', errors='replace') as f:
    IP02A_lecture = f.read()
with open('BM41040_Lecture_10_SensoryIntegration_2022-20231.txt',
          'r', encoding='utf-8', errors='replace') as f:
    Sensory_Integration_lecture = f.read()

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

# Make call with input and instructions
core_material = openai_call(
    cleaning_message,
    Sensory_Integration_lecture,
    model=gpt4,
    temp=0
)
print(core_material)
