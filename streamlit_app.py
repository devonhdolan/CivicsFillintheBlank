import streamlit as st
import random

# Load questions from the PDF
questions = [
    {"text": "What is the supreme law of the land?", "answer": "the Constitution", "choices": ["the Constitution", "the President", "the Congress", "the Supreme Court"]},
    {"text": "What does the Constitution do?", "answer": "sets up the government", "choices": ["sets up the government", "defines the President", "declares war", "establishes taxes"]},
    {"text": "The idea of self-government is in the first three words of the Constitution. What are these words?", "answer": "We the People", "choices": ["We the People", "We the Congress", "We the States", "We the Citizens"]},
    {"text": "What is an amendment?", "answer": "a change (to the Constitution)", "choices": ["a change (to the Constitution)", "a new law", "an executive order", "a bill"]},
    {"text": "What do we call the first ten amendments to the Constitution?", "answer": "the Bill of Rights", "choices": ["the Bill of Rights", "the Preamble", "the Articles", "the Declarations"]},
    {"text": "What is one right or freedom from the First Amendment?", "answer": "speech", "choices": ["speech", "voting", "arms", "education"]},
    {"text": "How many amendments does the Constitution have?", "answer": "twenty-seven", "choices": ["twenty-seven", "ten", "fifteen", "twenty"]},
    {"text": "What did the Declaration of Independence do?", "answer": "announced our independence (from Great Britain)", "choices": ["announced our independence (from Great Britain)", "declared war on Britain", "established the Constitution", "created the Supreme Court"]},
    {"text": "What are two rights in the Declaration of Independence?", "answer": "life and liberty", "choices": ["life and liberty", "speech and arms", "voting and education", "privacy and property"]},
    {"text": "What is freedom of religion?", "answer": "You can practice any religion, or not practice a religion.", "choices": ["You can practice any religion, or not practice a religion.", "You must practice a religion", "You can only practice certain religions", "Religion is not allowed"]},
]

# Set up session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = random.choice(questions)
    st.session_state.score = 0
    st.session_state.total_questions = 0

def check_answer():
    user_answer = st.session_state.user_answer
    correct_answer = st.session_state.current_question['answer']
    if user_answer == correct_answer:
        st.success("Correct!")
        st.session_state.score += 1
    else:
        st.error(f"Incorrect! The correct answer is '{correct_answer}'.")

    st.session_state.total_questions += 1
    st.session_state.current_question = random.choice(questions)
    st.session_state.user_answer = ""

def skip_question():
    st.session_state.current_question = random.choice(questions)
    st.session_state.user_answer = ""

# Title and instruction
st.title("American Civics Fill-in-the-Blank Test")
st.write("Fill in the blank with the correct answer based on your knowledge of American civics.")

# Display the current question
st.write(st.session_state.current_question['text'])

# Multiple choice options for the user's answer
user_answer = st.radio("Choose your answer:", options=st.session_state.current_question['choices'], key="user_answer")

# Buttons for checking answer and skipping question
st.button("Check Answer", on_click=check_answer)
st.button("Skip Question", on_click=skip_question)

# Display score and progress
st.write(f"Score: {st.session_state.score}/{st.session_state.total_questions}")

# Progress bar
progress = st.session_state.total_questions / len(questions)
st.progress(progress)

# Feedback image for correct or incorrect answer
if 'user_answer' in st.session_state and st.session_state.user_answer:
    if st.session_state.user_answer == st.session_state.current_question['answer']:
        st.image("https://media.giphy.com/media/111ebonMs90YLu/giphy.gif", width=200)
    else:
        st.image("https://media.giphy.com/media/l4FGuhL4U2WyjdkaY/giphy.gif", width=200)
