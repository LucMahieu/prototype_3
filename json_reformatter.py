import json

# Function to merge questions and answers with titles in the specified format
def merge_content_with_titles(data):
    merged_modules = []
    for module in data["content"]:
        segments = []
        for i, question in enumerate(module["questions"]):
            segment = {
                "question": question.replace("Infobit: ", ""),
                "answer": module["answers"][i],
                "infobit": 1 if "Infobit:" in question else 0
            }
            segments.append(segment)
        merged_modules.append({"title": module["title"], "segments": segments})
    return merged_modules

# Assuming the JSON data is read from a file named 'data.json'
with open('pages/spaced_repetition_questions.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Merging the content
merged_content = merge_content_with_titles(data)

# Write
with open('pages/spaced_repetition_questions.json', 'w', encoding='utf-8') as file:
    json.dump(merged_content, file, ensure_ascii=False, indent=4)