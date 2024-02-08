import openai
import streamlit as st
from dotenv import load_dotenv
import os
import database
import json
from login import login_module
from openai import OpenAI
client = OpenAI()

load_dotenv()

st.set_page_config(page_title="LearnLoop", layout="wide")

db_client = database.init_connection(**st.secrets["mongo"])
db = db_client.LearnLoop


def fetch_phase_data(phase):
    """
    Fetch the progress data etc. of the user in the current phase from the database,
    which indicates the relative progress of the user in the current phase.
    """
    # Store user doc in variable for clarity
    user_doc = st.session_state.user_doc

    # Find users document in the database
    if user_doc is not None:
        if user_doc["progress"] is not None:
            if st.session_state.selected_module in user_doc["progress"]:
                if phase in user_doc["progress"][st.session_state.selected_module]:
                    return user_doc["progress"][st.session_state.selected_module][phase]
    else:
        return None


def upload_segment_index():
    """
    Uploads the progress of the user in the current phase to the database.
    """
    st.write(f"Uploading segment index: {st.session_state.segment_index}")
    db.users.update_one(
        {"username": st.session_state.username},
        {"$set": {
            f"progress.{st.session_state.selected_module}.{st.session_state.selected_phase}": {
                "segment_index": st.session_state.segment_index
            }
        }}
    )

    # Write the current database fields
    st.write(fetch_phase_data(st.session_state.selected_phase))


# def change_card_index(index: int):
#     """Function to change the index of the current card in the deck."""
#     card_idx = st.session_state.indices.pop(0)

#     if index > -1:
#         # Insert at given index
#         st.session_state.indices.insert(index, card_idx)


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


def evaluate_answer():
    """Evaluates the answer of the student and returns a score and feedback."""
    if st.session_state.currently_testing != True:
        
        # Create user prompt with the question, correct answer and student answer
        prompt = f"""Input:\n
        Vraag: {st.session_state.current_segment['question']}\n
        Antwoord student: {st.session_state.student_answer}\n
        Beoordelingsrubriek: {st.session_state.current_segment['answer']}\n
        Output:\n"""

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

        st.session_state.feedback = split_response[0].split(">>")
        st.session_state.score = split_response[1]
    else:
        st.session_state.feedback = "O"
        st.session_state.score = "0/2"


# def next_question(difficulty): #TODO: Might be removed because currently not used properly
#     st.session_state.submitted = False
#     st.session_state.score = ""
#     st.session_state.feedback = ""
#     st.session_state.answer = ""
#     st.session_state.show_answer = False

#     # Check which difficulty level was pressed and sort card deck accordingly
#     if difficulty == 'easy':
#         # Count executive times the user found current card easy
#         # evaluate_graduation(st.session_state.indices[0])

#         # Remove card from deck so it won't repeat
#         st.session_state.indices.pop(0)
#     else:
#         reset_easy_count(st.session_state.indices[0])
#         if difficulty == 'medium':
#             change_card_index(5)
#         elif difficulty == 'hard':
#             change_card_index(2)

#     # Save progress to db after next is pressed
#     upload_progress(st.selected_phase)


def score_to_percentage():
    """Converts a score in the form of a string to a percentage."""
    try:
        # Calculate the score percentage
        part, total = st.session_state.score.split('/')
        if total == '0':
            score_percentage = 0
        else:
            # If there is a comma (e.g. 1,5), change it to a dot
            if ',' in part:
                part = part.replace(',', '.')
            score_percentage = int(float(part) / float(total) * 100)
    except Exception as e:
        st.error(f"Error calculating score: {e}")
        return  # Early exit on error
    
    return score_percentage


def render_feedback():
    """Renders the feedback box with the score and feedback."""
    # Calculate the score percentage
    score_percentage = score_to_percentage()

    # Determine color of box based on score percentage
    if score_percentage > 75:
        color = 'rgba(0, 128, 0, 0.2)'  # Green
    elif score_percentage > 49:
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


def render_progress_bar(segments):
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
        background-color: green;
        height: 20px;
        border-radius: 30px;
    }
    </style>
    """
    st.markdown(progress_bar_style, unsafe_allow_html=True)

    # Initialise progress bar or update progress that indicates the relative segment index
    if len(segments) > 0:
        progress = int((st.session_state.segment_index + 1) / len(segments) * 100)
    else:
        progress = 0

    # Update the progress bar
    st.progress(progress)
    st.session_state.progress = progress

def next_question(difficulty): #TODO: remove, only here for testing SR nav buttons
    pass

def render_SR_nav_buttons():
    col_prev, col1, col2, col3, col_next = st.columns([1.8, 3, 3, 3, 1.8])
    with col_prev:
        st.button('Previous', use_container_width=True, on_click=lambda: change_segment_index(-1))
    with col1:
        st.button('Ask again ↩️', use_container_width=True, on_click=lambda: next_question('hard'))
    with col2:
        st.button('Repeat later 🕒', use_container_width=True, on_click=lambda: next_question('medium'))
    with col3:
        st.button('Got it ✅', use_container_width=True, on_click=lambda: next_question('easy'))
    with col_next:
        st.button('Next', use_container_width=True, on_click=lambda: change_segment_index(1))


# def render_add_to_practice_buttons():
#     col_add, col_yes, col_no = st.columns(3)
#     with col_add:
#         # st.subheader('Add to **Practice Phase** 📝?')
#         st.markdown("""
#             <style>
#             .centered {
#                 text-align: center;
#             }
#             </style>
#             <div class="centered">
#                 <p style="font-size: 18px;">Add to <strong>Practice Phase</strong> 📝?</p>
#             </div>
#         """, unsafe_allow_html=True)
#     with col_yes:
#         st.button('Yes', use_container_width=True, on_click=add_to_practice_phase)
#     with col_no:
#         st.button('No', use_container_width=True, on_click=change_segment_index, args=(1,))


def render_explanation():
    with st.expander("Explanation"):
        st.markdown(st.session_state.current_segment['answer'])


def change_segment_index(step_direction):
    """Change the segment index based on the direction of step (previous or next)."""
    # Store segments and current segment index in variable for clarity     
    segments = st.session_state.page_content['segments']

    if st.session_state.segment_index + step_direction in range(len(segments)):
        st.session_state.segment_index += step_direction
    elif st.session_state.segment_index == len(segments) - 1:
        st.session_state.segment_index = 0
    else:
        st.session_state.segment_index = len(segments) - 1

    # Prevent evaluating aswer when navigating to the next or previous segment 
    st.session_state.submitted = False
    
    # Update database with new index
    upload_segment_index()


def render_navigation_buttons():
    """Render the navigation buttons that allows users to move between segments."""
    prev_col, next_col = st.columns(2)
    with prev_col:
        st.button("Previous", on_click=change_segment_index, args=(-1,), use_container_width=True)
    with next_col:
        st.button("Next", on_click=change_segment_index, args=(1,), use_container_width=True)


def render_check_and_nav_buttons():
    """Renders the previous, check and next buttons when a question is displayed."""
    
    # Whithout this helper function the user will have to press "check" twice before submitting
    def set_submitted_true():
        st.session_state.submitted = True

    col_prev_question, col_check, col_next_question = st.columns([1, 4, 1])
    with col_prev_question:
        st.button('Previous', use_container_width=True, on_click=change_segment_index, args=(-1,))
    with col_check:
        st.button('Check', use_container_width=True, on_click=set_submitted_true())
    with col_next_question:
        st.button('Next', use_container_width=True, on_click=change_segment_index, args=(1,))


def render_info():
    """Renders the info segment with title and text."""
    st.subheader(st.session_state.current_segment['title'])
    st.write(st.session_state.current_segment['text'])


def render_answerbox():
    """Render a textbox in which the student can type their answer."""
    st.text_area(label='Your answer', label_visibility='hidden', 
                placeholder="Type your answer",
                key='student_answer'
    )
    

def render_question():
    """Function to render the question and textbox for the students answer."""
    st.subheader(st.session_state.current_segment['question'])


def fetch_practice_segments():
    """Fetches the practice segments from the database."""
    practice_segments = st.session_state.user_doc["progress"][st.session_state.selected_module]["practice"].get("practice_segments", [])
    return practice_segments


def update_practice_segments():
    """Updates the practice segments in the database."""
    db.users.update_one(
        {"username": st.session_state.username},
        {"$set": {f"progress.{st.session_state.selected_module}.practice.practice_segments": st.session_state.practice_segments}}
    )


def add_to_practice_phase():
    """Adds the current segment to the practice phase in the database if the score is lower than 100."""
    # Store session states in variables for clarity
    segment_index = st.session_state.segment_index
    
    if score_to_percentage() < 100:
        # Fetch the practice segments from the database
        practice_segments = fetch_practice_segments()

        if segment_index not in practice_segments:
            st.session_state.practice_segments = practice_segments.append(segment_index)
        
        # Update the practice segments in the database
        update_practice_segments()

        # # Check if the selected module exists in the user's progress
        # if st.session_state.selected_module in user_progress:

        #     # Check if the practice object exists for the selected module
        #     if "practice" in user_progress[st.session_state.selected_module] and "practice_segments" in user_progress[st.session_state.selected_module]["practice"]:
                
        #         # Fetch the existing practice segments
        #         practice_segments = fetch_practice_segments()
        #     else:
        #         # If the practice object does not exist, create it
        #         st.session_state.practice_segments = []
        #         update_practice_segments()
        #         st.write(f"Practice phase data{fetch_phase_data('practice')}")
        #         # practice_segments = fetch_practice_segments()

            # # Check if the practice segments exists and if not, create it
            # if practice_segments is None or segment_index not in practice_segments:
            #     st.session_state.practice_segments.append(segment_index)
            #     update_practice_segments()


def render_student_answer():
    """Renders the student's answer."""
    st.write('Your answer:')
    st.write(st.session_state.student_answer)


def fetch_segment_index():
    """Fetches the segment index from the database."""
    st.session_state.segment_index = st.session_state.user_doc["progress"][st.session_state.selected_module][st.session_state.selected_phase]["segment_index"]


def learning_phase_page():
    """
    Renders the page that takes the student through the concepts of the lecture
    with info segments and questions. The student can navigate between segments
    and will get personalized feedback on their answers. Incorrectly answered
    questions are added to the practice phase.
    """
    # fetch_segment_index()
    # st.write(f"Fetched segment index: {st.session_state.segment_index}")
    # determine_current_segment()

    phase = 'learning'
    # Fetch user progress in the segments (by index) from the database
    if fetch_phase_data(phase) is None:
        st.session_state.segment_index = 0
    else:
        st.session_state.segment_index = fetch_phase_data(phase)["segment_index"]
        

    # Select the segment that corresponds to the saved index where the user left off
    st.session_state.current_segment = st.session_state.page_content['segments'][st.session_state.segment_index]

    # Display the info or question in the middle column
    with mid_col:
        render_progress_bar(st.session_state.page_content['segments'])

        # Determine what type of segment to display and render interface accordingly
        if st.session_state.current_segment['type'] == 'info':
            render_info()
            render_navigation_buttons()

        if st.session_state.current_segment['type'] == 'question':
            render_question()
            if st.session_state.submitted:
                # Spinner that displays during evaluating answer
                with st.spinner('Evaluating your answer 🔄'):
                    evaluate_answer()
                render_student_answer()
                render_feedback()
                add_to_practice_phase()
                render_explanation()
                render_navigation_buttons()
            else:
                render_answerbox()
                render_check_and_nav_buttons()
                

def upload_practice_segment_index():
    """
    Uploads the practice segment index to the database.
    """
    db.users.update_one(
        {"username": st.session_state.username},
        {"$set": {
            f"progress.{st.session_state.selected_module}.practice.practice_segment_index": st.session_state.practice_segment_index
        }}
    )


def fetch_practice_segment_index():
    """
    Fetches the practice segment index from the database.
    """
    practice_segment_index = st.session_state.user_doc["progress"][st.session_state.selected_module]["practice"]["practice_segment_index"]
    return practice_segment_index


def determine_segment_index():
    """
    Determines the segment index based on the practice segments and the practice segment index.
    """
    # Fetch the practice segments from the database
    practice_segments = fetch_practice_segments()

    # Fetch the practice segment index from the database
    practice_segment_index = fetch_practice_segment_index()

    # If the practice segments are not empty, set the segment index to the first segment in the practice segments
    if practice_segments is not None:
        if len(practice_segments) > 0:
            st.session_state.segment_index = practice_segments[practice_segment_index]
        else:
            st.session_state.segment_index = 0
    else:
        st.session_state.segment_index = 0


def determine_current_segment():
    """Determine the current segment based on the segment index and put in session state."""
    st.session_state.current_segment = st.session_state.page_content['segments'][st.session_state.segment_index]


def initialise_practice_db():
    """
    Initialise the practice object in the database.
    """
    db.users.update_one(
        {"username": st.session_state.username},
        {"$set": {
            f"progress.{st.session_state.selected_module}.practice": {
                "segment_index": 0,
                "practice_segment_index": 0,
                "practice_segments": []
            }
        }}
    )


def practice_phase_page():
    """
    Renders the page that contains the practice questions and 
    answers without the info segments and with the spaced repetition buttons.
    This phase allows the student to practice the concepts they've learned
    during the learning phase and which they found difficult.
    """
    db_data = fetch_phase_data(phase="practice")
    if db_data is None:
        initialise_practice_db()
        st.session_state.practice_segments = []
    else:
        st.session_state.practice_segments = db_data["practice_segments"]
    
    determine_segment_index()
    determine_current_segment()
    
    # Display the info or question in the middle column
    with mid_col:
        render_progress_bar(st.session_state.page_content['segments'])

        # Determine what type of segment to display and render interface accordingly
        if st.session_state.current_segment['type'] == 'info':
            render_info()
            render_navigation_buttons()

        if st.session_state.current_segment['type'] == 'question':
            render_question()
            if st.session_state.submitted:
                # Spinner that displays during evaluating answer
                with st.spinner('Evaluating your answer 🔄'):
                    evaluate_answer()
                render_student_answer()
                render_feedback()
                render_explanation()
                render_navigation_buttons()
            else:
                render_answerbox()
                render_check_and_nav_buttons()


def select_page_type():
    """
    Determines what type of page to display based on which module the user selected.
    """
    # For convenience, store the selected module name in a variable
    module = st.session_state.selected_module

    # Make module name lowercase and replace spaces and with underscores and cuts off at the first
    module_json_name = module.lower().replace(" ", "_")

    # Find the json with content that corresponds to the selected module
    with open(f"./modules/{module_json_name}.json", "r") as f:
        st.session_state.page_content = json.load(f)
    
    # Determine what type of page to display
    if st.session_state.selected_phase == 'learning':
        learning_phase_page()
    if st.session_state.selected_phase == 'practice':
        practice_phase_page()



def initialise_session_states():
    """Initialise the session states."""

    if 'selected_phase' not in st.session_state:
        st.session_state.selected_phase = None

    if 'easy_count' not in st.session_state:
        st.session_state.easy_count = {}

    if 'page_content' not in st.session_state:
        st.session_state.page_content = None

    if 'indices' not in st.session_state:
        st.session_state.indices = []

    # Index of current segment (question or info) that user sees
    if 'segment_index' not in st.session_state:
        st.session_state.segment_index = 0

    if 'authentication_status' not in st.session_state:
        st.session_state.authentication_status = None

    if 'selected_module' not in st.session_state:
        st.session_state.selected_module = None

    if 'modules' not in st.session_state:
        st.session_state.modules = []

    if 'segments' not in st.session_state:
        st.session_state.segments = None
    
    if 'current_segment' not in st.session_state:
        st.session_state.current_segment = None

    if 'previous_page_name' not in st.session_state:
        st.session_state.previous_page_name = None

    if 'current_page_name' not in st.session_state:
        st.session_state.current_page_name = __file__

    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    
    if 'student_answer' not in st.session_state:
        st.session_state.student_answer = ""
        
    if 'score' not in st.session_state:
        st.session_state.score = ""

    if 'feedback' not in st.session_state:
        st.session_state.feedback = ""

    if 'difficulty' not in st.session_state:
        st.session_state.difficulty = ""


def render_start_page():
    """Renders the start page with the explanation and login module if not logged in yet."""

    if st.session_state["authentication_status"] is False or st.session_state["authentication_status"] is None:

        # Display 'How to use' header
        st.markdown('<p style="font-size: 50px;"><strong>Explanation</strong></p>', unsafe_allow_html=True)

        # Display explanation
        st.write("This app is designed to help you learn concepts easily. It consists of two phases: the **learning phase** and the **practice phase**.")
        # Spacing
        st.write("")
        st.write("")

        # Columns to divide the explanation for practice and learning phase
        learning_col, practice_col = st.columns(2)
        with learning_col:
            st.markdown('<p style="font-size: 30px;"><strong>Learning Phase 📖</strong></p>', unsafe_allow_html=True)
            st.write("The **learning phase** guides you through the concepts of a lecture in an interactive way with personalized feedback. Incorrectly answered questions are added to the practice phase.")
        with practice_col:
            st.markdown('<p style="font-size: 30px;"><strong>Practice Phase 📝</strong></p>', unsafe_allow_html=True)
            st.write("The **practice phase** is where you can practice the concepts you've learned in the **learning phase**. It uses spaced repetition to reinforce your memory and improve long-term retention.")
        
        # # Display 'Courses' header
        # st.markdown('<p style="font-size: 60px;"><strong>Courses</strong></p>', unsafe_allow_html=True)

        # # Display courses
        # course_1, course_2 = st.columns(2)
        # with course_1:
        #     st.image('neuropsycho.png')
        # with course_2:
        #     st.image('neuropsycho.png')

        # Load login module at top of sidebar, but remove from top when logged in
        with st.sidebar:

            # Place logo in horizontal centre of sidebar
            render_logo()

            # Login in sidebar
            login_module()

        return False
    else:
        return True


def render_logo():
    # Place logo in horizontal centre of sidebar with spacer column
    spacer, image_col = st.columns([0.4, 1])
    with image_col:
        st.image('./images/logo.png', width=100)


def determine_modules(): #TODO: change the way the sequence of the modules is determined so it corresponds to the sequence of the course
    """	
    Function to determine which names of modules to display in the sidebar 
    based on the JSON module files.	
    """
    # Determine the modules to display in the sidebar
    if st.session_state.modules == []:
        # Read the modules from the modules directory
        modules = os.listdir("./modules")
        # Remove the json extension and replace the underscores with spaces
        modules = [module.replace(".json", "").replace("_", " ") for module in modules]
        # Capitalize the first letter of each module
        modules = [module.capitalize() for module in modules]
        st.session_state.modules = modules


def render_sidebar():
    """	
    Function to render the sidebar with the modules and login module.	
    """
    with st.sidebar:
        # Toggle to turn openai request on/off for easier and cheaper testing
        # st.checkbox("Currently testing", key="currently_testing")
        st.session_state.currently_testing = True #TODO: remove this line with the checkbox when coding

        st.sidebar.title("Modules")

        # Display the modules in expanders in the sidebar
        for module in st.session_state.modules:
            with st.expander(module):
                # Display buttons for the two types of phases per module
                if st.button('Learning Phase 📖', key=module + ' learning'):
                    st.session_state.selected_module = module
                    st.session_state.selected_phase = 'learning'
                if st.button('Practice Phase 📝', key=module + ' practice'):
                    st.session_state.selected_module = module
                    st.session_state.selected_phase = 'practice'

        # Display login module at bottom of sidebar after logged in
        login_module()


def initialise_database_fields():
    """
    Initialise all database fields next to username and hashed password.
    """
    st.write("Initialising database fields")
    # Add the modules and phases to the progress object in the database
    for module in st.session_state.modules:
        db.users.update_one(
            {"username": st.session_state.username},
            {"$set": {
                f"progress.{module}": {
                    "learning": {"segment_index": 0},
                    "practice": {"segment_index": 0, "practice_segments": [], "practice_segment_index": 0}
                }
            }}
        )
    # st.write(fetch_phase_data(phase='practice'))


# MAIN PROGRAM
if __name__ == "__main__":
    # Create a mid column with margins in which everything one a 
    # page is displayed (referenced to mid_col in functions)
    left_col, mid_col, right_col = st.columns([2, 6, 2])
    
    initialise_session_states()
    
    # Determine the modules of the current course
    if st.session_state.modules == []:
        determine_modules()
    
    # Check authentication
    if render_start_page():
        render_sidebar()

        # Display correct module
        if st.session_state.selected_module is None:         
            # Automatically start the first module if no module is selected        
            st.session_state.selected_module = st.session_state.modules[0] #TODO: this should start at the module where the student left off instead of the first module
            st.session_state.selected_phase = 'learning'
            # Rerun to make sure the page is displayed directly after start button is clicked
            st.rerun()
        else:
            # Initialise user document reference in database
            if 'user_doc' not in st.session_state:
                st.session_state.user_doc = db.users.find_one({"username": st.session_state.username})
            # Check if database has been initialised
            if "progress" not in st.session_state.user_doc:
                initialise_database_fields()
            select_page_type()