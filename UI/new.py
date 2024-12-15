import streamlit as st
import tempfile
import subprocess  # Import subprocess module
import os
import requests
from file_processor import extract_text_from_pdf, clean_text
from generate_qa import gen_qa  # Import the QA generation function
import time

# Function to run the Dash app in the background
def run_dash_app():
    cmd = ["python", "dash_app.py"]
    subprocess.Popen(cmd)

# Check if Dash app is already running
def is_dash_app_running():
    try:
        response = requests.get("http://127.0.0.1:8050")
        return response.status_code == 200
    except requests.ConnectionError:
        return False

# Start Dash app if not running
if not is_dash_app_running():
    st.write("Starting Dash app...")
    run_dash_app()
    time.sleep(5)  # Wait for a few seconds to allow the Dash app to start

# Heading
st.write("# Flash Card Generator")

# Description
st.write("""
    Enter your academic notes, PowerPoint presentations, or reading material to generate Flash Cards on the material to help you prepare better.
""")

# File uploader
file = st.file_uploader("Upload New File", type="pdf")

if file is not None:
    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(file.read())
        tmp_file_path = tmp_file.name

    # Extract and clean text from the temporary file
    extracted_text = extract_text_from_pdf(tmp_file_path)
    cleaned_text = clean_text(extracted_text)

    # Generate multiple question-answer pairs
    num_questions = st.slider("Number of Questions", 4, 10, 5)
    questions_answers = gen_qa(cleaned_text, num_questions)

        # Provide link to open the Dash app
    if is_dash_app_running():
        st.write("[Open Flashcard App](http://127.0.0.1:8050)")
    else:
        st.write("Dash app is not running. Please try again.")
    
    # Display the question-answer pairs
    st.write("## Generated Question-Answer pairs")
    for question, answer in questions_answers:
        st.write(f"**Question:** {question}")
        st.write(f"**Answer:** {answer}")
        st.write("---")

    # Save the question-answer pairs to a file
    with open("q_a_pairs.txt", "w") as f:
        for question, answer in questions_answers:
            f.write(f"{question}\t{answer}\n")

    st.write("Flashcards have been generated and saved.")


