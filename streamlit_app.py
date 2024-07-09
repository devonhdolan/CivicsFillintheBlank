import streamlit as st
import random

# Load questions from the PDF
questions = [
    {"text": "What is the supreme law of the land? _____", "answer": "the Constitution"},
    {"text": "What does the Constitution do? It _____ the government.", "answer": "sets up"},
    {"text": "The idea of self-government is in the first three words of the Constitution. What are these words? _____", "answer": "We the People"},
    {"text": "What is an amendment? It is a _____ (to the Constitution).", "answer": "change"},
    {"text": "What do we call the first ten amendments to the Constitution? _____", "answer": "the Bill of Rights"},
    {"text": "What is one right or freedom from the First Amendment? _____", "answer": "speech"},
    {"text": "How many amendments does the Constitution have? _____", "answer": "twenty-seven"},
    {"text": "What did the Declaration of Independence do? It _____ our independence (from Great Britain).", "answer": "announced"},
    {"text": "What are two rights in the Declaration of Independence? _____ and _____", "answer": "life", "answer2": "liberty"},
    {"text": "What is freedom of religion? You can _____ any religion, or not practice a religion.", "answer": "practice"},
    {"text": "What is the economic system in the United States? _____ economy.", "answer": "capitalist"},
    {"text": "What is the rule of law? Everyone must _____ the law.", "answer": "follow"},
    {"text": "Name one branch or part of the government. _____", "answer": "Congress"},
    {"text": "What stops one branch of government from becoming too powerful? _____ and balances.", "answer": "checks"},
    {"text": "Who is in charge of the executive branch? The _____", "answer": "President"},
    {"text": "Who makes federal laws? _____", "answer": "Congress"},
    {"text": "What are the two parts of the U.S. Congress? The _____ and House of Representatives.", "answer": "Senate"},
    {"text": "How many U.S. Senators are there? _____", "answer": "one hundred"},
    {"text": "We elect a U.S. Senator for how many years? _____", "answer": "six"},
    {"text": "The House of Representatives has how many voting members? _____", "answer": "four hundred thirty-five"},
]

# Set up session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = random.choice(questions)
    st.session_state.score = 0
    st.session_state.total_questions = 0

def check_answer():
    user_answer = st.session_state.user_answer.strip().lower()
    correct_answer = st.session_state.current_question['answer'].strip().lower()
    if user_answer == correct_answer:
        st.success("Correct!")
        st.session_state.score += 1
    else:
        st.error(f"Incorrect! The correct answer is '{st.session_state.current_question['answer']}'.")

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

# Input for the user's answer
user_answer = st.text_input("Your answer:", key="user_answer")

# Buttons for checking answer and skipping question
st.button("Check Answer", on_click=check_answer)
st.button("Skip Question", on_click=skip_question)

# Display score and progress
st.write(f"Score: {st.session_state.score}/{st.session_state.total_questions}")

# Progress bar
progress = st.session_state.total_questions / len(questions)
st.progress(progress)
