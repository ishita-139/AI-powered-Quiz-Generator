# AI-powered-Quiz-Generator
A Streamlit-based AI Quiz Generator that takes user-provided text as input and uses Large Language Models (LLMs) via the OpenAI API to generate quiz questions based on the selected difficulty level (Easy/Medium/Hard).

![ai-quiz-generator](https://github.com/user-attachments/assets/9f0d866e-3e4c-45f4-ada3-414c8dd9a3b1)

# About the Project
The AI-powered-Quiz-Generator is an interactive web application built with Streamlit that leverages the power of Large Language Models (LLMs) via the OpenAI API to create customized quizzes. Users can provide any text content, select a desired difficulty level (Easy, Medium, or Hard), and the application will intelligently generate relevant quiz questions based on the input.

This tool is ideal for educators, students, content creators, or anyone looking to quickly generate assessment questions from textual material without manual effort. It streamlines the process of creating engaging and challenging quizzes, adapting to various learning needs.

# Features
Text-to-Quiz Generation: Input any custom text to serve as the basis for quiz questions.
AI-Powered Questioning: Utilizes state-of-the-art LLMs (via OpenAI API) to understand text and formulate questions.
Difficulty Levels: Generate quizzes tailored to specific learning needs with Easy, Medium, and Hard difficulty options.
Streamlit User Interface: A clean, intuitive, and easy-to-use web interface for seamless interaction.
Instant Quiz Creation: Get questions generated in real-time, enhancing productivity.

# Getting Started
Follow these instructions to set up and run the AI Quiz Generator on your local machine.

# Prerequisites
Before you begin, ensure you have the following installed:

Python 3.8+: Download from python.org.
OpenAI API Key: You'll need an API key from OpenAI to access their LLM services. If you don't have one, you can get it from the OpenAI Platform.
Installation
Clone the repository:

bash

git clone https://github.com/ishita-139/AI-powered-Quiz-Generator.git
cd AI-powered-Quiz-Generator
Create a virtual environment (recommended):

bash

python -m venv venv
Activate the virtual environment:

On Windows:
bash

.\venv\Scripts\activate
On macOS/Linux:
bash

source venv/bin/activate
Install the required dependencies:

bash

pip install -r requirements.txt

# Usage
Once you have installed the dependencies and set up your API key, you can run the Streamlit application:

bash

streamlit run quizapp.py
This command will open the application in your default web browser (usually at http://localhost:8501).

# How to use the app:

Input Text: Paste or type the content you want to generate questions from into the large text area.
Select Difficulty: Choose "Easy", "Medium", or "Hard" from the dropdown menu.
Generate Quiz: Click the "Generate Quiz" button.
View Questions: The AI-generated quiz questions will appear below the input section.

# Project Structure
AI-powered-Quiz-Generator/
├── quizapp.py             # Main Streamlit application script
├── requirements.txt       # List of Python dependencies
└── README.md              # Project README file
└── .env                   # Environment variables (e.g., OPENAI_API_KEY - recommended, not committed)
quizapp.py: Contains all the Streamlit UI code and the logic for calling the OpenAI API to generate quiz questions.
requirements.txt: Specifies all the Python packages required to run the application.

# Contact
Owner: ishita-139
GitHub: https://github.com/ishita-139
Feel free to reach out for any questions or feedback!
