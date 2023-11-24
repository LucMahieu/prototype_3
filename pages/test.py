import streamlit as st

def reset(difficulty):
    st.write(difficulty)

col1, col2, col3 = st.columns(3)
with col1:
    st.button('Easy', use_container_width=True, on_click=lambda: reset('easy'))
with col2:
    st.button('Medium', use_container_width=True, on_click=lambda: reset('medium'))
with col3:
    st.button('Hard', use_container_width=True, on_click=lambda: reset('hard'))

# Je progress bar
progress = st.progress(0)
progress.progress(1)

st.markdown("""
<style>
.stProgress .st-bo {
    background-color: #28a745;
}
</style>
""", unsafe_allow_html=True)

