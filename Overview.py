import streamlit as st

st.set_page_config(
    page_title="Learnloop",
    page_icon="♾️"
)

st.title("LearnLoop")
st.subheader("**Excited for you to be one of the first users of LearnLoop!** ")
st.write(""" 
We crafted LearnLoop to help you swiftly and efficiently comprehend subjects from your study materials. It will do this by **automatically transforming your study materials into a more fun and effective learning pathway**. This is the first prototype, so it only contains pre-generated quizzes from one subject and these were manually checked for accuracy by fellow students. With your feedback and that of others, we will determine how to improve the algoritms that drive LearnLoop and what features to build next.
""")

# Create two columns
col1, col2 = st.columns(2)

# Write into column 1
col1.subheader("**Why use LearnLoop?**")
col1.write(""" 
📚 All concepts clearly organized in one place. \n
⏱️ Study effectively by testing yourself. \n
""")

# Write into column 2
col2.subheader("**Upcoming features:**")
col2.write(""" 
📖 Transform personal notes into a customized learning pathway. \n
🎮 A gamified learning experience. \n
📈 Learning pathway tailored to your learning curve. \n
""")

st.write("""
**See the potential?** Your donation signals to us that there's a demand for LearnLoop to continue evolving and improving. Every contribution will be directly channeled into the development of new features and the enhancement of our algorithms.
""")

st.subheader("**Voluntary donation options:**")
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
