import json

# Dit is een lijst die je bijhoudt (practice segments)
ordered_segment_sequence = [1, 3, 5, 1, 6, 8, 13, 5]

# Dit is een variabele die je bijhoudt
segment_index = 3

# Hiermee bepaal je de json waarde die je moet gebruiken om de current_segment te krijgen.
def determine_json_index():
    return ordered_segment_sequence[segment_index]

json_index = determine_json_index()

print(json_index)

with open(f"modules/test_slide_chemie.json", "r") as f:
    page_content = json.load(f)

print(page_content["segments"][json_index])

feedback = -1
current_index = 2

if feedback != 1:
    ordered_segment_sequence.append(current_index)

print(ordered_segment_sequence)


# Walk through the line
button = 1
if button == 1:
    segment_index += 1

json_index = determine_json_index()

print(json_index)




