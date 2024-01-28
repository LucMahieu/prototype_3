from openai import OpenAI
from dotenv import load_dotenv
import os
import tqdm
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Module:
    def __init__(self, name, lecture_path, batch_size):
        self.name = name
        self.lecture_path = lecture_path
        self.batch_size = batch_size


    def openai_call(self, system_message, user_message, model='gpt-3.5-turbo-1106', temp=0.0):
        message = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]
        response = client.chat.completions.create(model=model,
        temperature=temp,
        messages=message, response_format={"type": "json_object"})

        return response.choices[0].message.content


    def batch_generator(self, glossary):
        lines = ""
        glossary_lines = glossary.split("\n")
        for i, line in enumerate(glossary_lines):
            lines += line
            if i % self.batch_size == 0 and i != 0:
                yield lines
                lines = ""


    def add_response_to_json_file(self, json_response_string, module_name):
        # Turn json string into python object
        json_response = json.loads(json_response_string)


        
        if os.path.exists("./modules/questions.json"):
            print("File exists")
            # Open json file to read existing content
            with open("./modules/questions.json", "r") as f:
                content = json.load(f)
            
            # Check if 'segments' key already exists
            if 'segments' in content:
                # Add the new segments to the existing segments
                content['segments'].extend(json_response['segments'])
            else:
                # Create the 'module name' key and assign the module name
                content['module_name'] = module_name
                # Create 'segments' key and assign the new segments
                content['segments'] = json_response['segments']
        else:
            # Create json file with the module name and response
            content = {}
            content['module_name'] = module_name
            content['segments'] = json_response['segments']

        # Write the new content to the json file
        with open("./modules/questions.json", "w") as f:
            json.dump(content, f, indent=4)


    def generate_content(self):
        # Load glossary from lecture path txt file
        with open(f"{self.lecture_path}", "r") as f:
            glossary = f.read()

        for batch in self.batch_generator(glossary):

            if batch == "":
                print("Batch is empty")
                break
            else:
                print(f"Batch: {batch}")
            # Load instructions for question generator
            with open("./prompts/generate_content.txt", "r") as f:
                system_message = f.read()
            
            # Input study materials
            user_message = f""" 
                Input: 
                {batch}
                
                Output:
            """

            json_response = self.openai_call(system_message, user_message, model='gpt-4-1106-preview', temp=0.7)

            self.add_response_to_json_file(json_response, module_name="ml_overview") #TODO: Change module name to be variable


    if __name__ == "__main__":
        lecture_path = "./modules/ml_overview/lecture.txt"
        generate_content(lecture_path, batch_size=2)

        