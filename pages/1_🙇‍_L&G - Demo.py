import json

import streamlit as st
from PIL import Image

import utils
import database
client = database.init_connection(**st.secrets["mongo"])
db = client.LearnLoop


# st.title("Spaced Repetition Versions")
# st.write("The pages below this page contain the same flashcards per week, but the quizzes use a spaced repetition algorithm that makes studying more effective. This way you can choose to use the learning style you prefer.")
# st.markdown("Here's how it works: You rate the difficulty of a flashcard, and the algorithm organizes the deck so that **harder flashcards appear more frequently**. If you find a flashcard **easy two times in a row**, it's removed from the list and you will progress.")
# st.markdown("IMPORTANT: Your **progress is not saved** and is therefore lost when you refresh the page or switch pages. It is the current limitation of the prototype and will be fixed in later versions.")

def get_scores(name):
    # Get progress object from database
    progress = db.users.find_one({"username": name})["progress"]
    st.session_state.progress = progress


def upload_score(name, score, module):
    # Update global progress state, check if it exists
    st.session_state.progress[module] = score


    # Check if user exists and update
    if db.users.find_one({"username": name}):
        print("User exists, updating score for " + name + " in " + module + " to " + str(score))
        # Add scores to progress object, make object if does not exist
        db.users.update_one({"username": name}, {
            "$set": {
                "progress." + module: score
            }
        })
    else:
        print("User does not exist, not updating score")

def space_repetition_page(title, questions, answers):
    # Check if title is the same, else reset
    if 'title' not in st.session_state or st.session_state.title != title:
        st.session_state.title = title
        st.session_state.questions = questions
        st.session_state.answers = answers

    def change_card_index(index):
        if index > -1:
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
    progress_bar = st.progress(0)
    progress = int(sum(st.session_state.easy_count.values()) / (2 * len(questions)) * 100)
    progress_bar.progress(progress)
    # Set session state to percentage
    # st.session_state.progress = progress

    # Set as percentage
    # if st.session_state['authentication_status'] == True and st.session_state['selected_module'] is not None:
    #     upload_score(st.session_state['name'], progress, st.session_state['selected_module'])




    question_cont = st.container()

    ## Answer input field
    def process_answer(input_text):
        with st.spinner('Evaluating your answer...'):
            score, feedback = evaluate_answer(st.session_state.answer, st.session_state.questions[0], st.session_state.answers[0])
        # Store the score and feedback in the session state to access them after the input disappears
        st.session_state.submitted = True
        st.session_state.score = score
        st.session_state.feedback = feedback
        st.session_state.answer = input_text

    # Send to openai for validation
    from openai import OpenAI
    client = OpenAI()
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

    # Define a function to display the score and feedback with color coding
    def display_result():
        try:
            # Calculate the score percentage
            part, total = st.session_state.score.split('/')
            score_percentage = float(part) / float(total)
        except ValueError:
            score_percentage = 0

        # Give rgba with 0.2 opacity
        if score_percentage > 0.75:
            # Green
            color = 'rgba(0, 128, 0, 0.2)'
        elif score_percentage > 0.49:
            # Orange
            color = 'rgba(255, 165, 0, 0.2)'
        else:
            # Red
            color = 'rgba(255, 0, 0, 0.2)'

        # Each element corresponds to a new line
        feedback_lines = ["", "", "", "", "", "", "", ""]
        for i in range(len(st.session_state.feedback)):
            feedback_lines[i] = st.session_state.feedback[i]

        result_html = f"""
        <div style='background-color: {color}; padding: 25px; margin-bottom: 20px; border-radius: 8px;'>
            <h1 style='font-size: 30px; margin: 0;'>{st.session_state.score}</h1>
            <p style='font-size: 20px; margin: 0;'>{feedback_lines[0]}</p>
            <p style='font-size: 20px; margin: 0;'>{feedback_lines[1]}</p>
            <p style='font-size: 20px; margin: 0;'>{feedback_lines[2]}</p>
            <p style='font-size: 20px; margin: 0;'>{feedback_lines[3]}</p>
            <p style='font-size: 20px; margin: 0;'>{feedback_lines[4]}</p>     
            <p style='font-size: 20px; margin: 0;'>{feedback_lines[5]}</p>     
            <p style='font-size: 20px; margin: 0;'>{feedback_lines[6]}</p>
            <p style='font-size: 20px; margin: 0;'>{feedback_lines[7]}</p>
        </div>
        """

        # Displaying score and feedback with formatting within the div
        # formatted_feedback = [f"<p style='font-size: 20px; font-style: italic; margin: 0;'>{f}</p>" for f in st.session_state.feedback]

        # result_html = f"""
        # <div style='background-color: {color}; padding: 25px; margin-bottom: 10px; border-radius: 5px;'>
        #     <h1 style='font-size: 30px; margin: 0;'>{st.session_state.score}</h1>
        #     {''.join(formatted_feedback)}
        # </div>
        # """

        st.markdown(result_html, unsafe_allow_html=True)

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

    # Condition used to indicate if current question is infobit
    infobit = st.session_state.questions[0][0:8] == "Infobit:"

    # Text input field and submit button
    if not st.session_state.submitted and infobit is not True:
        answer = st.text_area(label='Your answer', label_visibility='hidden', placeholder="Type your answer", key='answer')
        st.button('Submit', on_click=process_answer, use_container_width=True, args=(answer,))
        with question_cont:
            st.subheader(st.session_state.questions[0])
    # Display infobit
    elif not st.session_state.submitted and infobit:
        with question_cont:
            info, title, text = st.session_state.questions[0].split("//")
            st.subheader(title)
            st.write(text)
        st.button('Next', use_container_width=True, on_click=change_card_index(-1))
        current_card = st.session_state.questions[0]
        if current_card in st.session_state.easy_count:
            st.session_state.easy_count[current_card] += 1
        else:
            st.session_state.easy_count[current_card] = 1
    else:
        # Display the submitted text as solid text
        st.write("Your answer:")
        st.write("test")
        st.write(st.session_state.answer)

    # After submission, display the result
    if st.session_state.submitted:

        with question_cont:
            st.subheader(st.session_state.questions[0])

        # Display the feedback
        display_result()

        def reset(difficulty):
            st.session_state.submitted = False
            st.session_state.score = ""
            st.session_state.feedback = ""
            st.session_state.answer = ""
            st.session_state.show_answer = False

            # Check which difficulty level was pressed and sort card deck accordingly
            if difficulty == 'easy':
                # Count executive times the user found current card easy
                evaluate_graduation(st.session_state.questions[0])
            else:
                reset_easy_count(st.session_state.questions[0])
                if difficulty == 'medium':
                    change_card_index(5)
                elif difficulty == 'hard':
                    change_card_index(2)

            # st.session_state.easy_count = {}
            # st.session_state.questions.pop(0)
            # st.session_state.answers.pop(0)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.button('Easy', use_container_width=True, on_click=lambda: reset('easy'))
        with col2:
            st.button('Medium', use_container_width=True, on_click=lambda: reset('medium'))
        with col3:
            st.button('Hard', use_container_width=True, on_click=lambda: reset('hard'))

        def toggle_answer():
            st.session_state.show_answer = not st.session_state.show_answer

        st.button('Explanation', use_container_width=True, on_click=toggle_answer)

        if st.session_state.show_answer:
            st.markdown(st.session_state.answers[0])

        # Restart card carousel (reset deck)
        if len(st.session_state.questions) == 0:
            st.session_state.questions = questions.copy()
            st.session_state.answers = answers.copy()
            st.session_state.easy_count = {}

        # st.button('Next question >', on_click=reset)

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

if 'progress' not in st.session_state:
    st.session_state.progress = []

# if len(st.session_state['progress']) == 0  and st.session_state["authentication_status"] is True:
#     get_scores(st.session_state['name'])

# Init selected module
if 'selected_module' not in st.session_state:
    st.session_state.selected_module = None

if 'pages' not in st.session_state:
    st.session_state.pages = []

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

