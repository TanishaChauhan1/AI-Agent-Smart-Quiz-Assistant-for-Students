def input_understanding_prompt(user_input):
    return f"""You are a helpful study assistant. The user said: "{user_input}".
Identify the subject and format it into a short summary."""

def state_tracker_prompt(previous_topic):
    return f"""Remember that the user was studying "{previous_topic}". 
Use this to keep context for upcoming questions."""

def task_planner_prompt(topic):
    return f"""You need to create 3 quiz questions based on the topic: "{topic}". 
Make sure they vary in difficulty."""

def output_generator_prompt(questions):
    return f"""Present these questions in a clean numbered list:
{questions}"""
