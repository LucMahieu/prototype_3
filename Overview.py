import streamlit as st

st.set_page_config(
    page_title="Learnloop",
    page_icon="♾️"
)

st.title("LearnLoop")
st.subheader("**Excited for you to be one of the first users of LearnLoop!** ")
st.write(""" 
We crafted LearnLoop to help you swiftly and efficiently comprehend subjects from your study materials. This is the first prototype, so it only has the bare minimum features and there might be some errors. With your feedback and that of others, we will determine what features to build next. 

**Why use LearnLoop?** \n
📚 All concepts clearly organized in one place. \n
⏱️ Study effectively by testing yourself. \n

**Upcoming features:** \n
📖 Transform personal notes into a customized learning pathway. \n
🎮 A gamified learning experience. \n
📈 Learning pathway tailored to your learning curve. \n
\n
**See the potential?** A voluntary donation goes a long way. It not only fuels our progress but also signifies how many students want LearnLoop to keep growing and improving.
"""
         )

st.subheader("**Voluntary Donation options:**")
st.write("""€1,00: http://bit.ly/3PPHysV \n
€2,00: https://bit.ly/3tAq6kt \n
€3,00: https://bit.ly/3LZ83uH \n
€5,00: https://bit.ly/3rOFLMI \n
€10,00: https://bit.ly/3tloZ8f \n

Thank you for your support and help in improving LearnLoop!""")

# st.subheader("Log in")
# user_password = st.text_input("Use your unique code to log in and keep track of your learning progress.", type='password')
# st.button("Enter")

# st.write(user_password)
# Blue circle to indicate that the user logged in: ":large_blue_circle:"
