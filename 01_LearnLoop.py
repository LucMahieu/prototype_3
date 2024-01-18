import openai
import streamlit as st
from dotenv import load_dotenv
import os
import database
import utils
import json
from login import login_module
from openai import OpenAI
client = OpenAI()

load_dotenv()
utils.init_session_state()
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="LearnLoop", layout="wide")

client = database.init_connection(**st.secrets["mongo"])
db = client.LearnLoop

def get_progress(name, module, segments):
    # Get progress object from database
    user_doc = db.users.find_one({"username": name})


    if user_doc is not None and "progress" in user_doc and module in user_doc["progress"]:
        # User found and has a progress field
        progress = user_doc["progress"][module]

        # Parse int in keys of easy_count
        progress["easy_count"] = {int(k): v for k, v in progress["easy_count"].items()}

        return progress
    else:
        # User not found or does not have a progress field -> Initialize
        return {'indices': list(range(len(segments))), 'easy_count': {}}

def upload_progress(name, indices, easy_count, module):
    # Check if user exists and update
    if db.users.find_one({"username": name}):
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


def space_repetition_page(title, segments):
    def change_card_index(index):
        card_idx = st.session_state.indices.pop(0)

        if index > -1:
            # Insert at given index
            st.session_state.indices.insert(index, card_idx)

    # def evaluate_graduation(current_card):
    #     if current_card in st.session_state.easy_count:
    #         st.session_state.easy_count[current_card] += 1
    #     else:
    #         st.session_state.easy_count[current_card] = 1

    #     # Delete card if graduated
    #     if st.session_state.easy_count[current_card] >= 2:
    #         st.session_state.indices.pop(0) # Remove the index of the graduated card
    #     else:
    #         # Move card to back of deck
    #         change_card_index(20)  # Adjust this value as needed

    def reset_easy_count(current_card):
        st.session_state.easy_count[current_card] = 0

    def initialise_new_page():
        st.session_state.segments = segments.copy()

    ## Answer input field
    def process_answer():
        # Input in the text area is saved in session state with key "student_answer"
        input_text = st.session_state.student_answer

        with eval_spinner_cont:
            with st.spinner('Evaluating your answer...'):
                current_question = st.session_state.segments[st.session_state.indices[0]]['question']
                current_answer = st.session_state.segments[st.session_state.indices[0]]['answer']
                score, feedback = evaluate_answer(input_text, current_question, current_answer)
        
        # Store the score and feedback in the session state to access them after the input disappears
        st.session_state.submitted = True
        st.session_state.score = score
        st.session_state.feedback = feedback
        st.session_state.answer = input_text

    def evaluate_answer(answer, question, gold_answer):
        # Toggle to turn openai request on/off for easier and cheaper testing
        currently_testing = True

        if currently_testing != True:
            prompt = f"Input:\nVraag: {question}\nAntwoord student: {answer}\nBeoordelingsrubriek: {gold_answer}\nOutput:\n"

            # Read the role prompt from a file
            with open("./system_role_prompt.txt", "r") as f:
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
        
        else:
            return "2/2", "F"

    def next_question(difficulty):
        st.session_state.submitted = False
        st.session_state.score = ""
        st.session_state.feedback = ""
        st.session_state.answer = ""
        st.session_state.show_answer = False

        # Check which difficulty level was pressed and sort card deck accordingly
        if difficulty == 'easy':
            # Count executive times the user found current card easy
            # evaluate_graduation(st.session_state.indices[0])

            # Remove card from deck so it won't repeat
            st.session_state.indices.pop(0)
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
            if total == '0':
                score_percentage = 0
            else:
                # If there is a comma, change it to a dot
                if ',' in part:
                    part = part.replace(',', '.')
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
        if len(segments) > 0:
            progress = 100 - int((len(st.session_state.indices) / len(segments)) * 100)
        else:
            progress = 0
        st.progress(progress)
        st.session_state.progress = progress

    def render_question():
        current_question = st.session_state.segments[st.session_state.indices[0]]['question']

        # Condition used to indicate if current question is infobit
        infobit = bool(st.session_state.segments[st.session_state.indices[0]]['infobit'])

        # Text input field and submit button
        if not st.session_state.submitted and infobit is not True:
            st.text_area(label='Your answer', label_visibility='hidden', 
                              placeholder="Type your answer",
                              key='student_answer')
            col_prev_question, col_check, col_next_question = st.columns([1, 5, 1])
            with col_prev_question:
                st.button('Previous', use_container_width=True, on_click=change_card_index(1))
            with col_check:
                st.button('Check', on_click=process_answer, use_container_width=True, key='Submit')
            with col_next_question:
                st.button('Next', use_container_width=True, on_click=change_card_index(-1))
            with question_cont:
                st.subheader(current_question)

        # Display infobit
        elif not st.session_state.submitted and infobit:
            with question_cont:
                info, title, text = current_question.split("//")
                st.subheader(title)
                st.write(text)
            col_prev, col_next = st.columns(2)
            with col_prev:
                st.button('Previous', use_container_width=True, on_click=change_card_index(1))
            with col_next:
                st.button('Next', use_container_width=True, on_click=change_card_index(-1))
        else:
            # Display the submitted text as solid text
            with question_cont:
                st.subheader(current_question)
                st.markdown("<span style='color: grey;'>Your answer:</span>", unsafe_allow_html=True)
                st.write(st.session_state.answer)

    def render_SR_buttons():
        col_prev, col1, col2, col3, col_next = st.columns([1.8, 3, 3, 3, 1.8])
        with col_prev:
            st.button('Previous', use_container_width=True)
        with col1:
            st.button('Ask again ↩️', use_container_width=True, on_click=lambda: next_question('hard'))
        with col2:
            st.button('Repeat later 🕒', use_container_width=True, on_click=lambda: next_question('medium'))
        with col3:
            st.button('Got it ✅', use_container_width=True, on_click=lambda: next_question('easy'))
        with col_next:
            st.button('Next', use_container_width=True)


    def render_add_to_practice_buttons():
        col_add, col_yes, col_no = st.columns(3)
        with col_add:
            # st.subheader('Add to **Practice Phase** 📝?')
            st.markdown("""
                <style>
                .centered {
                    text-align: center;
                }
                </style>
                <div class="centered">
                    <p style="font-size: 18px;">Add to <strong>Practice Phase</strong> 📝?</p>
                </div>
            """, unsafe_allow_html=True)
        with col_yes:
            st.button('Yes', use_container_width=True)
        with col_no:
            st.button('No', use_container_width=True)

 
    def render_explanation():
        with st.expander("Explanation"):
            st.markdown(st.session_state.segments[st.session_state.indices[0]]['answer'])


    # -- Construct page

    # Check if title is the same, else reset
    if 'title' not in st.session_state or st.session_state.title != title:
        st.session_state.title = title
        st.session_state.segments = segments

        progress = get_progress(st.session_state.name, st.session_state.selected_module, segments)
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

    # Read and store current file name
    st.session_state.current_page_name = __file__

    # Check if a new page is opened
    if st.session_state.current_page_name != st.session_state.previous_page_name:
        # Change lists in session state with current week lists
        initialise_new_page()
        st.session_state.previous_page_name = st.session_state.current_page_name

    if len(st.session_state.indices) == 0:
        st.title('Done')
        st.write("You've completed the **learning phase** 📖, well done!")
        st.write("To internalise the concepts, you can use the **practice phase** 📝.")
        st.balloons()
        # Restart button
        if st.button('Reset deck'):
            st.session_state.segments = segments.copy()
            st.session_state.easy_count = {}
            st.session_state.indices = list(range(len(segments)))
            # Trigger full rerender
            st.rerun()

    if len(st.session_state.indices) > 0:
        # Renders components on page.
        # Side columns function as margins for the middle column
        side_col1, mid_col, side_col2 = st.columns([1, 6, 1])
        with mid_col:
            render_progress_bar()

            # Container ensures right placement of question
            question_cont = st.container()
            render_question()

            # Container for a spinner that displays during evaluating answer
            eval_spinner_cont = st.container()

            # After submission, display the result
            if st.session_state.submitted:
                # Display the feedback
                display_result()
                render_SR_buttons()
                render_explanation()

            # REMOVE WHEN CONFIGURING THE PAGES AND BUTTONS CORRECTLY
            render_add_to_practice_buttons()


# ====================

# Function to load content from JSON file
def load_content():
    with open("./spaced_repetition_questions.json", "r") as f:
        content = json.load(f)
    return content

# Create a list of possible pages based on the titles in the json file
def get_pages(content):
    titles = [page['title'] for page in content]

    return titles


# Function to handle page display
def display_page(page_title, content):
    page_title = page_title.split(" (")[0]

    # Set selected module as session state
    st.session_state.selected_module = page_title

    page_idx = next((index for (index, d) in enumerate(content) if d["title"] == page_title), None)
    if page_idx is not None:
        page_content = content[page_idx]
        space_repetition_page(page_content['title'], page_content['segments'])


## RENDERING

utils.init_session_state()

if 'answer' not in st.session_state:
    st.session_state.answer = ""

# Init selected module
if 'selected_module' not in st.session_state:
    st.session_state.selected_module = None

if 'pages' not in st.session_state:
    st.session_state.pages = []

if 'segments' not in st.session_state:
    st.session_state.segments = None

if 'current_question' not in st.session_state:
    st.session_state.current_question = ''

if 'current_answer' not in st.session_state:
    st.session_state.current_answer = ''

if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False

if 'previous_page_name' not in st.session_state:
    st.session_state.previous_page_name = None

if 'current_page_name' not in st.session_state:
    st.session_state.current_page_name = __file__



# Function to handle authentication check
def check_authentication():
    if st.session_state["authentication_status"] is False or st.session_state["authentication_status"] is None:

        # courses_header, learnloop_logo = st.columns(2)
        # with courses_header:
        #     st.markdown('<p style="font-size: 60px;">Courses</p>', unsafe_allow_html=True)
        # with learnloop_logo:
        #     st.image('logo.png', width=100)

        # Display 'Courses' header
        st.markdown('<p style="font-size: 60px;"><strong>Courses</strong></p>', unsafe_allow_html=True)

        # Display courses
        course_1, course_2 = st.columns(2)
        with course_1:
            st.image('neuropsycho.png')
        with course_2:
            st.image('neuropsycho.png')

        # Load login module at top of sidebar, but remove from top when logged in
        with st.sidebar:

            # Place logo in horizontal centre of sidebar
            render_logo()

            # Login in sidebar
            login_module()

        return False
    return True

def render_logo():
    # Place logo in horizontal centre of sidebar with spacer column
    spacer, image_col = st.columns([0.4, 1])
    with image_col:
        st.image('logo.png', width=100)


# Main logic
if check_authentication():
    content = load_content()
    st.session_state.pages = get_pages(content)
    
    with st.sidebar:
        st.sidebar.title("Ontwikkeling")
        for option in st.session_state.pages:
            with st.expander(option):
                # Display buttons for the two fases in learning with LearnLoop
                if st.button('Learning Phase 📖', key=option):
                    st.session_state.selected_module = option
                if st.button('Practice Phase 📝', key=option + ' practice'):
                    st.session_state.selected_module = option

        # Display login module at bottom of sidebar after logged in
        login_module()

    # Display correct module
    if st.session_state.selected_module is None:
        st.write("Welcome! Please select a module to get started.")
    else:
        display_page(st.session_state.selected_module, content)
