import streamlit as st

import utils
import database


def main():
    st.title("Experience Rating and Review")

    st.write("We are very curious how this tool helps you study better. Please leave your review below. Feel free to write as much as you want!")
    st.write("**Note:** Your review will be fully anonymous.")

    # Initialize the session state variable
    if 'submitted' not in st.session_state:
        st.session_state['submitted'] = False

    # Rating
    rating = st.slider("Rate your experience (1-5):", 1, 5, 1)

    # Review
    review = st.text_area("Leave your review here:")

    # Submit button
    if st.session_state['submitted']:
        st.success("Thank you for your review!")
    if not st.session_state['submitted']:
        if st.button('Submit Review'):
            # Here you can add code to store the review in a database or a file
            # For now, it just displays a thank you message
            client = database.init_connection(**st.secrets["mongo"])
            db = client.LearnLoop
            db.reviews.insert_one({"rating": rating, "review": review})

            st.session_state['submitted'] = True
            st.experimental_rerun()

def clear_form():
    st.session_state['slider'] = 1
    st.session_state['text_area'] = ""

if __name__ == "__main__":
    utils.init_session_state()

    if st.session_state["authentication_status"] is False or st.session_state["authentication_status"] is None:
        st.warning('Please enter your credentials on the homepage')
    else:
        main()