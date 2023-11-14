import json

import streamlit as st
from dotenv import load_dotenv
load_dotenv()

# st.title("Spaced Repetition Versions")
# st.write("The pages below this page contain the same flashcards per week, but the quizzes use a spaced repetition algorithm that makes studying more effective. This way you can choose to use the learning style you prefer.")
# st.markdown("Here's how it works: You rate the difficulty of a flashcard, and the algorithm organizes the deck so that **harder flashcards appear more frequently**. If you find a flashcard **easy two times in a row**, it's removed from the list and you will progress.")
# st.markdown("IMPORTANT: Your **progress is not saved** and is therefore lost when you refresh the page or switch pages. It is the current limitation of the prototype and will be fixed in later versions.")

# -------------------------SESSION STATES----------------------------- #

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

#----------------------------SR------------------------------#

def space_repetition_page(title, questions, answers):
    # Check if title is the same, else reset
    if 'title' not in st.session_state or st.session_state.title != title:
        st.session_state.title = title
        st.session_state.questions = questions
        st.session_state.answers = answers

    st.title(title)

    def change_card_index(index):
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


    card_progress = st.progress(0)
    main_container = st.container()

    with main_container:
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button('Easy', use_container_width=True):
                # Count executive times the user found current card easy
                evaluate_graduation(st.session_state.questions[0])
                st.session_state.show_answer = False

        with col2:
            if st.button('Medium', use_container_width=True):
                st.session_state.show_answer = False
                reset_easy_count(st.session_state.questions[0])
                change_card_index(5)

        with col3:
            if st.button('Hard', use_container_width=True):
                st.session_state.show_answer = False
                reset_easy_count(st.session_state.questions[0])
                change_card_index(2)


    if st.button('Show Answer', use_container_width=True):
        st.session_state.show_answer = not st.session_state.show_answer

    if len(st.session_state.questions) == 0:
        st.session_state.questions = questions.copy()
        st.session_state.answers = answers.copy()
        st.session_state.easy_count = {}

    st.subheader(st.session_state.questions[0])
    if st.session_state.show_answer:
        st.write(st.session_state.answers[0])

    card_progress.progress(int(sum(st.session_state.easy_count.values()) / (2 * len(questions)) * 100))


    # Initialize session state variables if they don't exist
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    if 'answer' not in st.session_state:
        st.session_state.answer = ""

    if 'score' not in st.session_state:
        st.session_state.score = ""
    if 'feedback' not in st.session_state:
        st.session_state.feedback = ""

    ## Answer input field
    def process_answer():
        with st.spinner('Evaluating your answer...'):
            score, feedback = evaluate_answer(st.session_state.answer, st.session_state.questions[0], st.session_state.answers[0])
        # Store the score and feedback in the session state to access them after the input disappears
        st.session_state.submitted = True
        st.session_state.score = score
        st.session_state.feedback = feedback

    # Send to openai for validation
    from openai import OpenAI
    client = OpenAI()
    def evaluate_answer(answer, question, gold_answer):
        prompt = f"""
            Question: {question}
            Correct Answer: {gold_answer}
            Student Answer: {answer}
            Output:
            """

        # Read the role prompt from a file
        with open("./system_role_prompt.txt", "r") as f:
            role_prompt = f.read()

        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": role_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=120
        )
        print(response.choices[0].message.content)

        score, feedback = response.choices[0].message.content.split(";;")

        return score, feedback

    # Define a function to display the score and feedback with color coding
    def display_result():
        try:
            # Calculate the score percentage
            part, total = st.session_state.score.split('/')
            score_percentage = int(part) / int(total)
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

        # Displaying score and feedback with formatting within the div
        result_html = f"""
        <div style='background-color: {color}; padding: 25px; margin-bottom: 10px; border-radius: 5px;'>
            <h1 style='font-size: 40px; margin: 0;'>{st.session_state.score}</h1>
            <p style='font-size: 20px; font-style: italic; margin: 0;'>{st.session_state.feedback}</p>
        </div>
        """
        st.markdown(result_html, unsafe_allow_html=True)

    # Text input field and submit button
    if not st.session_state.submitted:
        answer = st.text_input("Jouw antwoord:", key='answer')
        st.button('Submit', on_click=process_answer)
    else:
        # Display the submitted text as solid text
        st.text("Jouw antwoord:")
        st.write(st.session_state.answer)

    # After submission, display the result
    if st.session_state.submitted:
        display_result()

        def reset():
            st.session_state.submitted = False
            st.session_state.score = ""
            st.session_state.feedback = ""
            st.session_state.answer = ""
            st.session_state.show_answer = False
            st.session_state.easy_count = {}
            st.session_state.questions.pop(0)
            st.session_state.answers.pop(0)

        # Reset button
        st.empty()
        st.button('Next question >', on_click=reset)


# ====================


# Function to load content from JSON file
def load_content():
    with open("./spaced_repetition_questions.json", "r") as f:
        content = json.load(f)['content']
    return content

# Create a list of possible pages based on the titles in the json file
def get_pages(content):
    return [page['title'] for page in content]

# Function to handle page display
def display_page(page_title, content):
    page_idx = next((index for (index, d) in enumerate(content) if d["title"] == page_title), None)
    if page_idx is not None:
        page_content = content[page_idx]
        space_repetition_page(page_content['title'], page_content['questions'], page_content['answers'])

# Load content from JSON
content = load_content()
pages = get_pages(content)

# Create navbar
selected_page = st.sidebar.selectbox("Choose a page", pages)

# Display the selected page and reset the state if needed
display_page(selected_page, content)

