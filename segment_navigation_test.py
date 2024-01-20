import streamlit as st

def initialise_session_states():
    """Initialise the session states."""
    if "segment_index" not in st.session_state:
        st.session_state.segment_index = 0

segments = ["Segment 1", "Segment 2", "Segment 3"]

def render_segment(segments):
    """Render the current segment."""
    st.write(segments[st.session_state.segment_index])


def render_nav_buttons():
    """Render the navigation buttons that allows users to move between segments."""
    prev_col, next_col = st.columns(2)
    with prev_col:
        st.button("Previous", on_click=change_segment_index, args=(-1,))
    with next_col:
        st.button("Next", on_click=change_segment_index, args=(1,))


def change_segment_index(direction):
    """Change the segment index based on the direction of navigation."""
    if st.session_state.segment_index + direction in range(len(segments)):
        st.session_state.segment_index += direction
    elif st.session_state.segment_index == len(segments) - 1:
        st.session_state.segment_index = 0
    else:
        st.session_state.segment_index = len(segments) - 1


if __name__ == "__main__":
    st.title("Segment Navigation Test")
    initialise_session_states()
    render_segment(segments)
    render_nav_buttons()