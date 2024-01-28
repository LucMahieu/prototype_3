import openai
import streamlit as st
from dotenv import load_dotenv
import os
import database
import json
from login import login_module
from openai import OpenAI
client = OpenAI()
from content_generator import Module

from st_clickable_images import clickable_images
import base64

load_dotenv()

st.set_page_config(page_title="LearnLoop", layout="wide")

db_client = database.init_connection(**st.secrets["mongo"])
db = db_client.LearnLoop


def get_progress():
    """
    Gets the progress of the user from the database in the form of a dictionary
    that consists of an index and other info relevant to the progress.
    """
    # For convenience, store the selected module name in a variable
    module = st.session_state.selected_module

    # Get progress object from database
    user_doc = db.users.find_one({"username": st.session_state.username})

    if user_doc is not None and "progress" in user_doc and module in user_doc["progress"]:
        # User found and has a progress field
        progress = user_doc["progress"][module]

        return progress
    else:
        # User not found or does not have a progress field -> Initialize
        return {"segment_index": 0, "easy_count": {}}


def upload_progress():
    """
    Uploads the progress of the user to the database in the form of indexes for each module
    """

    # Check if user exists and update
    if db.users.find_one({"username": st.session_state.username}):
        # # Easy count dict to string keys only
        # easy_count = {str(k): v for k, v in easy_count.items()}

        # Add to progress object
        db.users.update_one(
            {"username": st.session_state.username},
            {"$set": {
                f"progress.{st.session_state.selected_module}": {
                    "segment_index": st.session_state.segment_index,
                    "easy_count": st.session_state.easy_count
                }
            }}
        )
    else:
        print("User does not exist, not updating progress")


def change_card_index(index: int):
    """Function to change the index of the current card in the deck."""
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
        st.session_state.score = "2/2"


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

    # Save progress to db after next is pressed
    upload_progress()


def score_to_percentage(score):
    """Converts a score in the form of a string to a percentage."""
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
    
    return score_percentage


def render_feedback():
    """Renders the feedback box with the score and feedback."""
    # Calculate the score percentage
    score_percentage = score_to_percentage(st.session_state.score)

    # Determine color of box based on score percentage
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


# def add_to_practice_phase():
#     """Adds the current segment to the practice phase and changes the current card index."""
#     # Save current segment index to JSON file
#     with open("./progress.json", "w") as f:
#         json.dump({"module_name": st.session_state.selected_module, "segment_index": st.session_state.segment_index}, f)
    
#     # Change current segment index to the next segment
#     change_segment_index(1)


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
        st.button('Yes', use_container_width=True, on_click=add_to_practice_phase)
    with col_no:
        st.button('No', use_container_width=True, on_click=change_segment_index, args=(1,))


def render_explanation():
    with st.expander("Explanation"):
        st.markdown(st.session_state.current_segment['answer'])


def change_segment_index(step):
    """Change the segment index based on the direction of step (previous or next)."""
    # Store segments and current segment index in variable for clarity     
    segments = st.session_state.page_content['segments']

    if st.session_state.segment_index + step in range(len(segments)):
        st.session_state.segment_index += step
    elif st.session_state.segment_index == len(segments) - 1:
        st.session_state.segment_index = 0
    else:
        st.session_state.segment_index = len(segments) - 1

    # Prevent evaluating aswer when navigating to the next or previous segment 
    st.session_state.submitted = False
    
    # Update database with new index
    upload_progress()


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


def check_add_to_practice_phase(): #TODO: checken of het werkt en dan connecten met practice phase.
    """Checks if the current segment should be added to the practice phase."""
    # Determine if the score is below 100% 
    if score_to_percentage(st.session_state.score) == 100:
        # Add segment index of questions that student found difficult to dict coupled to module name
        st.session_state.practice_questions[st.session_state.selected_module].append(st.session_state.segment_index)


def learning_phase_page():
    """
    Renders the page that takes the student through the concepts of the lecture
    with info segments and questions. The student can navigate between segments
    and will get personalized feedback on their answers. Incorrectly answered
    questions are added to the practice phase.
    """
    # Check if the progress of the page has been saved to the database previously
    # if 
    #     # Save progress to db
    #     upload_progress()

    # Fetch user progress in the segments (by index) from the database
    db_segment_index = get_progress()["segment_index"]

    # Save most recent segment index in session state if it's not already set
    if db_segment_index != st.session_state.segment_index:
        st.session_state.segment_index = db_segment_index

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
                render_feedback()
                check_add_to_practice_phase()
                render_explanation()
                render_navigation_buttons()
                # render_add_to_practice_buttons()
            else:
                render_answerbox()
                render_check_and_nav_buttons()


    # # Check if the end of the phase is reached and display the message and reset button
    # if st.session_state.segment_index + 1 == len(st.session_state.page_content['segments']):
    #     st.title('Done')
    #     st.write("You've completed the **learning phase** 📖, well done!")
    #     st.write("To internalise the concepts, you can use the **practice phase** 📝.")
    #     st.balloons()
    #     # Restart button
    #     if st.button('Reset deck'):
    #         # Trigger full rerender of page
    #         st.rerun()

def practice_phase_page():
    """
    Renders the page that contains the practice questions and 
    answers without the info segments and with the spaced repetition buttons.
    This phase allows the student to practice the concepts they've learned
    during the learning phase and which they found difficult.
    """

def select_page_type():
    """
    Determines what type of page to display based on which module the user selected.
    """
    # For convenience, store the selected module name in a variable
    module_name = st.session_state.selected_module

    # Make module name lowercase and replace spaces and with underscores and cuts off at the first |
    module_json_name = module_name.split(" |")[0].lower().replace(" ", "_")

    # Find the json with content that corresponds to the selected module
    with open(f"./modules/{module_json_name}.json", "r") as f:
        st.session_state.page_content = json.load(f)
    
    # Determine what type of page to display
    if module_name.endswith('practice'):
        practice_phase_page()
    elif module_name.endswith('learning'):
        learning_phase_page()



def initialise_session_states():
    """Initialise the session states."""

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


def get_image_data(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def render_clickable_images(image_paths):
    """Function to render clickable images."""
    
    # Convert images to base64 in order for the st-clickable-images package to work
    image_data = [f"data:image/jpeg;base64,{get_image_data(path)}" for path in image_paths]

    # Display clickable images
    clicked = clickable_images(
        image_data,
        titles=[f"Image #{str(i)}" for i in range(5)],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "40px", "height": "100px", "border-radius": "8px"},
    )

    # Write clicked image number if an image was clicked
    st.session_state.clicked = clicked


# Function to handle authentication check
def render_start_page():
    # Check if user is logged in or not
    if st.session_state["authentication_status"] is False or st.session_state["authentication_status"] is None:
        
        # Display 'Create Course' header
        st.markdown('<p style="font-size: 50px;"><strong>Create Course</strong></p>', unsafe_allow_html=True)

        # st.markdown('<p style="font-size: 22px;"><strong>Course Name</strong></p>', unsafe_allow_html=True)
        # Input textbox for course name
        st.text_input("", placeholder="Enter course name", key="course_name")

        # Spacing
        st.write("")
        st.write("")
        
        # Display 'Select Lectures' header
        st.markdown('<p style="font-size: 22px;"><strong>Select Lectures</strong></p>', unsafe_allow_html=True)
        st.write("Select one of the lectures below to create a module for this course.")

        # Render clickable images
        render_clickable_images(image_paths=["./images/hoorcollege_2_tumbnail.jpg", "./images/hoorcollege_7_tumbnail.jpg", "./images/hoorcollege_x_tumbnail.jpg", "./images/hoorcollege_x2_tumbnail.jpg"])

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

        st.markdown(f"Image #{st.session_state.clicked} clicked" if st.session_state.clicked > -1 else "No image clicked")
        if st.session_state.clicked > -1:
            with st.spinner("Generating content for module"):
                # Determine what lecture was selected
                lecture_path = f"./study_materials/ml_overview.txt" #TODO: is now hardcoded, but should be an integration with the lectures of the uva
                new_module = Module(st.session_state.course_name, lecture_path, batch_size=2)
                new_module.generate_content()
                st.success("Module generated successfully!")

        return False
    else:
        return True


def render_logo():
    # Place logo in horizontal centre of sidebar with spacer column
    spacer, image_col = st.columns([0.4, 1])
    with image_col:
        st.image('./images/logo.png', width=100)


def determine_modules():
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
        st.checkbox("Currently testing", key="currently_testing")

        st.sidebar.title("Modules")

        # Determine the modules to display in the sidebar
        if st.session_state.modules == []:
            determine_modules()

        # Display the modules in expanders in the sidebar
        for module in st.session_state.modules:
            with st.expander(module):
                # Display buttons for the two types of phases per module
                if st.button('Learning Phase 📖', key=module + ' learning'):
                    st.session_state.selected_module = module + ' | learning'
                if st.button('Practice Phase 📝', key=module + ' practice'):
                    st.session_state.selected_module = module + ' | practice'

        # Display login module at bottom of sidebar after logged in
        login_module()


# MAIN PROGRAM
if __name__ == "__main__":
    # Create a mid column with margins in which everything one a 
    # page is displayed (referenced to mid_col in functions)
    left_col, mid_col, right_col = st.columns([2, 6, 2])
    
    initialise_session_states()
    
    # Check authentication
    if render_start_page():
        render_sidebar()

        # Display correct module
        if st.session_state.selected_module is None:
            
            # Column to centre the start button in the middle of the page
            start_col = st.columns(3)
            with start_col[0]:
                st.subheader("Start where you left off")
            
                # Create button to start learning phase of first module
                if st.button('Start', key='start', use_container_width=True):
                    st.session_state.selected_module = st.session_state.modules[0] + ' | learning'
                    
                    # Rerun to make sure the page is displayed directly after start button is clicked
                    st.rerun()
        else:
            select_page_type()