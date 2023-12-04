import streamlit as st

import utils
import database


def main():
    st.title("Share Your Feedback & Thoughts")

    st.write("We are very curious how this tool helps you study better and how we can improve it. Please leave your feedback below. Feel free to write as much as you want!")
    st.write("**Note:** Your feedback will be **fully anonymous**.")

    # Feedback
    review = st.text_area("Share **any feedback** you have on your mind:")

    # Submit button
    if st.session_state['submitted']:
        st.success("Thank you for your feedback!")
    if not st.session_state['submitted']:
        if st.button('Submit Feedback'):
            # Here you can add code to store the review in a database or a file
            # For now, it just displays a thank you message
            client = database.init_connection(**st.secrets["mongo"])
            db = client.LearnLoop
            db.reviews.insert_one({"review": review})

            st.session_state['submitted'] = True
            st.experimental_rerun()

    st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)  # Pas de hoogte aan naar wens

    # Rating
    rating = st.slider("Rate your experience (1-5):", 1, 5, 1)

    if st.session_state['submitted']:
        st.success("Thank you for your feedback!")
    if not st.session_state['rating']:
        if st.button('Submit Rating'):
            # Here you can add code to store the review in a database or a file
            # For now, it just displays a thank you message
            client = database.init_connection(**st.secrets["mongo"])
            db = client.LearnLoop
            db.reviews.insert_one({"rating": rating})

            st.session_state['rating'] = True
            st.experimental_rerun()

def clear_form():
    st.session_state['slider'] = 1
    st.session_state['text_area'] = ""

if __name__ == "__main__":
    # Initialize the session state variable
    if 'submitted' not in st.session_state:
        st.session_state['submitted'] = False

    if 'rating' not in st.session_state:
        st.session_state['rating'] = False

    utils.init_session_state()

    if st.session_state["authentication_status"] is False or st.session_state["authentication_status"] is None:
        st.warning('Please enter your credentials on the homepage')
    else:
        main()