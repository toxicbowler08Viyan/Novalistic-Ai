import streamlit as st

# Session state setup
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# Login section
if not st.session_state.logged_in:

    st.title("NOVALISIC")
    st.subheader("The study AI you didn't know you needed. Dive in!!!!")

    name = st.text_input("Enter your name:")
    password = st.text_input("Enter your password", type="password")
    email = st.text_input("Enter your email")

    if st.button("Press me if you want to dive in!"):

        if password == "tung":
            st.session_state.name = name
            st.session_state.logged_in = True
            st.success(f"Welcome back, {name}!")

        else:
            st.session_state.attempts += 1
            st.error(
                f"Incorrect password. Attempts: {st.session_state.attempts}"
            )

# Study section
if st.session_state.logged_in:

    st.write("## Study Section")

subject = st.selectbox(
        "Choose your subject for today!!!",
        ["Maths", "Science", "Coding", "Music"]
    )

mood = st.radio(
        "What's your mood?",
        ["Tired", "Energetic", "Stressed", "Average"]
    )

minute = st.slider(
        "Study time",
        min_value=5,
        max_value=60,
        value=20,
        step=5
    )

number = st.number_input(
    "Enter your phone number",
    step=1
)

if st.button("GET STARTED FELLOW COMRADE"):

    st.write(f"📚 Subject: {subject}")
    st.write(f"😊 Mood: {mood}")
    st.write(f"⏰ Study time: {minute} minutes")

    if subject == "Maths":
        task = "📝 Do a maths test online to warm up! Or use the following link to do your homework. https://www.mathsisfun.com/mathtest.html"

    elif subject == "Science":
        task = "🔬 Review your Science homework and do an experiment related to it! https://www.youtube.com/watch?v=hyctIDPRSqY"

    elif subject == "Coding":
        task = "🐍 Learn something new using Python! https://share.google/GJhHs61hBUX903xZ0"

    elif subject == "Music":
        task = "🎵 Practice your favorite piece 20 times! https://www.youtube.com/watch?v=uRZAQRhPHuE&list=RDuRZAQRhPHuE&start_radio=1"

    if mood == "Tired":
        tip = ""
    elif mood == "Energetic":
        tip = "Challenge yourself today!"
    elif mood == "Stressed":
        tip = "Play it easy. Make sure you take a few breaks and a few deep breaths before you start"

    elif mood == "Average":
        tip = "good"

    quotes = (
        "a lion does not concern himself with the opinions of the sheep"
    )
    st.write(quotes)
