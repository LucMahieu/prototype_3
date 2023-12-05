import json

import streamlit as st
from PIL import Image

import utils
import database
client = database.init_connection(**st.secrets["mongo"])
db = client.LearnLoop

# Send to openai for validation
from openai import OpenAI
client = OpenAI()

# st.title("Spaced Repetition Versions")
# st.write("The pages below this page contain the same flashcards per week, but the quizzes use a spaced repetition algorithm that makes studying more effective. This way you can choose to use the learning style you prefer.")
# st.markdown("Here's how it works: You rate the difficulty of a flashcard, and the algorithm organizes the deck so that **harder flashcards appear more frequently**. If you find a flashcard **easy two times in a row**, it's removed from the list and you will progress.")
# st.markdown("IMPORTANT: Your **progress is not saved** and is therefore lost when you refresh the page or switch pages. It is the current limitation of the prototype and will be fixed in later versions.")

def get_progress(name, module, questions):
    print("Getting progress for " + name)
    # Get progress object from database
    user_doc = db.users.find_one({"username": name})

    if user_doc is not None and "progress" in user_doc:
        # User found and has a progress field
        progress = user_doc["progress"][module]

        # Parse int in keys of easy_count
        progress["easy_count"] = {int(k): v for k, v in progress["easy_count"].items()}

        return progress
    else:
        # User not found or does not have a progress field -> Initialize
        print("User not found or does not have a progress field")
        return {'indices': list(range(len(questions))), 'easy_count': {}}

def upload_progress(name, indices, easy_count, module):
    print("Uploading progress for " + name + " in " + module)
    # Update global progress state, check if it exists
    # st.session_state.indices = indices
    # st.session_state.easy_count = easy_count

    # Check if user exists and update
    if db.users.find_one({"username": name}):
        print("User exists, updating progress for " + name + " in " + module + " to " + str(indices) + " and " + str(
            easy_count))

        # Easy count dict to string keys only
        easy_count = {str(k): v for k, v in easy_count.items()}

        # Add to progress object
        db.users.update_one(
            {"username": name},
            {"$set": {
                f"progress.{module}": {
                    "indices": indices,
                    "easy_count": easy_count
                }
            }}
        )
    else:
        print("User does not exist, not updating progress")


def space_repetition_page(title, questions, answers):
    def change_card_index(index):
        card_idx = st.session_state.indices.pop(0)

        if index > -1:
            # Insert at given index
            st.session_state.indices.insert(index, st.session_state.indices.pop(0))

    def evaluate_graduation(current_card):
        if current_card in st.session_state.easy_count:
            st.session_state.easy_count[current_card] += 1
        else:
            st.session_state.easy_count[current_card] = 1

        # Delete card if graduated
        if st.session_state.easy_count[current_card] >= 2:
            st.session_state.indices.pop(0) # Remove the index of the graduated card
        else:
            change_card_index(20)  # Adjust this value as needed

    def reset_easy_count(current_card):
        st.session_state.easy_count[current_card] = 0

    def initialise_new_page():
        st.session_state.questions = questions.copy()
        st.session_state.answers = answers.copy()

    ## Answer input field
    def process_answer(input_text):
        with st.spinner('Evaluating your answer...'):
            current_question = st.session_state.questions[st.session_state.indices[0]]
            current_answer = st.session_state.answers[st.session_state.indices[0]]
            score, feedback = evaluate_answer(input_text, current_question, current_answer)
        # Store the score and feedback in the session state to access them after the input disappears
        st.session_state.submitted = True
        st.session_state.score = score
        st.session_state.feedback = feedback
        st.session_state.answer = input_text

    def evaluate_answer(answer, question, gold_answer):
        prompt = f"Input:\nVraag: {question}\nAntwoord student: {answer}\nBeoordelingsrubriek: {gold_answer}\nOutput:\n"

        # Read the role prompt from a file
        with open("./pages/system_role_prompt.txt", "r") as f:
            role_prompt = f.read()

        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": role_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )

        split_response = response.choices[0].message.content.split(";;")

        if len(split_response) != 2:
            raise ValueError("Server response is not in the correct format. Please retry.")

        feedback = split_response[0].split(">>")
        score = split_response[1]

        return score, feedback

    def next_question(difficulty):
        st.session_state.submitted = False
        st.session_state.score = ""
        st.session_state.feedback = ""
        st.session_state.answer = ""
        st.session_state.show_answer = False

        # Check which difficulty level was pressed and sort card deck accordingly
        if difficulty == 'easy':
            # Count executive times the user found current card easy
            evaluate_graduation(st.session_state.indices[0])
        else:
            reset_easy_count(st.session_state.indices[0])
            if difficulty == 'medium':
                change_card_index(5)
            elif difficulty == 'hard':
                change_card_index(2)

        # Save process on submit
        upload_progress(st.session_state.name, st.session_state.indices, st.session_state.easy_count, title)


    # Define a function to display the score and feedback with color coding
    def display_result():
        try:
            # Calculate the score percentage
            part, total = st.session_state.score.split('/')
            score_percentage = float(part) / float(total)
        except Exception as e:
            st.error(f"Error calculating score: {e}")
            return  # Early exit on error

        # Determine color based on score percentage
        if score_percentage > 0.75:
            color = 'rgba(0, 128, 0, 0.2)'  # Green
        elif score_percentage > 0.49:
            color = 'rgba(255, 165, 0, 0.2)'  # Orange
        else:
            color = 'rgba(255, 0, 0, 0.2)'  # Red

        # Generate feedback paragraphs
        feedback_html = ''.join(
            f"<p style='font-size: 20px; margin: 10px 0;'>{line}</p>" for line in st.session_state.feedback if
            line.strip())

        result_html = f"""
        <div style='background-color: {color}; padding: 25px; margin-bottom: 20px; border-radius: 8px;'>
            <h1 style='font-size: 30px; margin-bottom: 15px;'>{st.session_state.score}</h1>
            {feedback_html}
        </div>
        """

        st.markdown(result_html, unsafe_allow_html=True)

    def render_progress_bar():
        # Change style of progressbar
        progress_bar_style = """
        <style>
        /* Change main container */
        .stProgress > div > div > div {
            height: 20px;
            border-radius: 30px;
        }
        /* Change moving part of progress bar */
        .stProgress .st-bo {
            background-color: #00A000;
            height: 20px;
            border-radius: 30px;
        }
        </style>
        """
        st.markdown(progress_bar_style, unsafe_allow_html=True)

        # Initialise progress bar
        progress = int(sum(st.session_state.easy_count.values()) / (2 * len(questions)) * 100)
        st.progress(progress)
        st.session_state.progress = progress

    def render_question():
        current_index = st.session_state.indices[0]
        current_question = st.session_state.questions[st.session_state.indices[0]]
        current_answer = st.session_state.answers[st.session_state.indices[0]]

        # Condition used to indicate if current question is infobit
        infobit = current_question[0:8] == "Infobit:"

        # Text input field and submit button
        if not st.session_state.submitted and infobit is not True:
            answer = st.text_area(label='Your answer', label_visibility='hidden', placeholder="Type your answer",
                                  key='answer')
            st.button('Submit', on_click=process_answer, use_container_width=True, args=(answer,))
            with question_cont:
                st.subheader(current_question)

        # Display infobit
        elif not st.session_state.submitted and infobit:
            with question_cont:
                info, title, text = current_question.split("//")
                st.subheader(title)
                st.write(text)
            st.button('Next', use_container_width=True, on_click=change_card_index(-1))
            if current_index in st.session_state.easy_count:
                st.session_state.easy_count[current_index] += 1
            else:
                st.session_state.easy_count[current_index] = 1
        else:
            # Display the submitted text as solid text
            st.write("Your answer:")
            st.write(st.session_state.answer)

    def render_next_buttons():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button('Got it', use_container_width=True, on_click=lambda: next_question('easy'))
        with col2:
            st.button('Getting closer', use_container_width=True, on_click=lambda: next_question('medium'))
        with col3:
            st.button('Some extra practice', use_container_width=True, on_click=lambda: next_question('hard'))

    def render_explanation():
        def toggle_answer():
            st.session_state.show_answer = not st.session_state.show_answer
        st.button('Explanation', use_container_width=True, on_click=toggle_answer)

        if st.session_state.show_answer:
            st.markdown(st.session_state.answers[st.session_state.indices[0]], unsafe_allow_html=True)


    # -- Construct page

    # Check if title is the same, else reset
    if 'title' not in st.session_state or st.session_state.title != title:
        st.session_state.title = title
        st.session_state.questions = questions
        st.session_state.answers = answers

        progress = get_progress(st.session_state.name, st.session_state.selected_module, questions)
        st.session_state.indices = progress['indices']
        st.session_state.easy_count = progress['easy_count']

        # Initialize session state variables if they don't exist
        if 'submitted' not in st.session_state:
            st.session_state.submitted = False
        if 'answer' not in st.session_state:
            st.session_state.answer = ""
        if 'score' not in st.session_state:
            st.session_state.score = ""
        if 'feedback' not in st.session_state:
            st.session_state.feedback = ""
        if 'difficulty' not in st.session_state:
            st.session_state.difficulty = ""

    # print("Rendering with session state: ", st.session_state.indices, st.session_state.easy_count)

    # Read and store current file name
    st.session_state.current_page_name = __file__

    # Check if a new page is opened
    if st.session_state.current_page_name != st.session_state.previous_page_name:
        # Change lists in session state with current week lists
        initialise_new_page()
        st.session_state.previous_page_name = st.session_state.current_page_name


    # RENDER COMPONENTS
    question_cont = st.container()
    render_progress_bar()
    render_question()

    # Set as percentage
    # if st.session_state['authentication_status'] == True and st.session_state['selected_module'] is not None:
    #     upload_score(st.session_state['name'], progress, st.session_state['selected_module'])

    # After submission, display the result
    if st.session_state.submitted:

        with question_cont:
            st.subheader(st.session_state.current_question)

        # Display the feedback
        display_result()
        render_next_buttons()
        render_explanation()

        # Restart card carousel when deck is emptied (reset deck)
        if len(st.session_state.indices) == 0:
            st.session_state.questions = questions.copy()
            st.session_state.answers = answers.copy()
            st.session_state.easy_count = {}
            st.session_state.indices = list(range(len(questions)))

# ====================


# Function to load content from JSON file
def load_content():
    with open("./pages/spaced_repetition_questions.json", "r") as f:
        content = json.load(f)['content']
    return content

# Create a list of possible pages based on the titles in the json file
def get_pages(content):
    titles = [page['title'] for page in content]

    # # Add scores to titles
    # for i, title in enumerate(titles):
    #     if title in st.session_state.progress:
    #         titles[i] += " (" + str(st.session_state.progress[title]) + "%)"

    return titles


# Function to handle page display
def display_page(page_title, content):
    page_title = page_title.split(" (")[0]

    # Set selected module as session state
    st.session_state.selected_module = page_title

    page_idx = next((index for (index, d) in enumerate(content) if d["title"] == page_title), None)
    if page_idx is not None:
        page_content = content[page_idx]
        space_repetition_page(page_content['title'], page_content['questions'], page_content['answers'])


## RENDERING

utils.init_session_state()

# if 'progress' not in st.session_state:
#     st.session_state.progress = 0

# Init selected module
if 'selected_module' not in st.session_state:
    st.session_state.selected_module = None

if 'pages' not in st.session_state:
    st.session_state.pages = []

if 'questions' not in st.session_state:
    st.session_state.questions = None

if 'current_question' not in st.session_state:
    st.session_state.current_question = ''

if 'answers' not in st.session_state:
    st.session_state.answers = None

if 'current_answer' not in st.session_state:
    st.session_state.current_answer = ''

if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False

if 'previous_page_name' not in st.session_state:
    st.session_state.previous_page_name = None

if 'current_page_name' not in st.session_state:
    st.session_state.current_page_name = __file__






if st.session_state["authentication_status"] is False or st.session_state["authentication_status"] is None:
    st.warning('Please enter your credentials on the homepage')
else:
    # Load content from JSON
    content = load_content()
    st.session_state.pages = get_pages(content)

    # Loop through each option and create a button for it in the sidebar
    st.sidebar.header("Modules")
    for option in st.session_state.pages:
        if st.sidebar.button(option):
            # Display the selected page and reset the state if needed
            display_page(option, content)
        else:
            if st.session_state.selected_module is None:
                st.warning("Select a module to get started.")
                # st.write("Welcome to our demo. Please select a subject on the left to get started.")
            elif st.session_state.selected_module is not None:
                display_page(st.session_state.selected_module, content)

