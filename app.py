from fastapi import FastAPI, Request
import openai
from dotenv import load_dotenv
import os
from prompts import *

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Quiz Agent is running!"}

@app.post("/generate-quiz/")
async def generate_quiz(request: Request):
    data = await request.json()
    user_input = data.get("topic", "")

    # Step 1: Input Understanding
    prompt1 = input_understanding_prompt(user_input)
    response1 = call_openai(prompt1)
    topic_summary = response1.strip()

    # Step 2: State Tracker
    context_prompt = state_tracker_prompt(topic_summary)
    call_openai(context_prompt)  # Optional: for future memory logic

    # Step 3: Task Planner
    planner_prompt = task_planner_prompt(topic_summary)
    quiz_questions = call_openai(planner_prompt)

    # Step 4: Output Generator
    final_prompt = output_generator_prompt(quiz_questions)
    final_output = call_openai(final_prompt)

    return {"topic_summary": topic_summary, "quiz": final_output}


def call_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
