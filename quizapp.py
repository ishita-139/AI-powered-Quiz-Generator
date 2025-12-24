import streamlit as st
import json
import os
from openai import OpenAI

# ❌ Hard-coded API key (NOT recommended)
client = OpenAI(api_key="sk-XXXXXXXXXXXXXXXXXXXXXXXX")

@st.cache_data
def fetch_questions(text_content, quiz_level):

    RESPONSE_JSON = {
      "mcqs" : [
        {
            "mcq": "multiple choice question1",
            "options": {
                "a": "choice here1",
                "b": "choice here2",
                "c": "choice here3",
                "d": "choice here4"
            },
            "correct": "a"
        }
      ]
    }

    PROMPT_TEMPLATE = f"""
    Text: {text_content}
    You are an expert in generating MCQ type quiz.
    Create 3 MCQs with difficulty {quiz_level}.
    Format strictly as JSON like below:
    {RESPONSE_JSON}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": PROMPT_TEMPLATE}],
        temperature=0.3,
        max_tokens=1000
    )

    return json.loads(response.choices[0].message.content)["mcqs"]
