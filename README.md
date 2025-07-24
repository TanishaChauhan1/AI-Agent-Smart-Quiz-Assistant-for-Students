<h1> 🧠 AI Agent: Smart Quiz Assistant for Students </h1>
<h3>🚀 Overview</h3>
This AI Agent helps students revise for exams by generating personalized quiz questions based on their syllabus and topics. Designed with a modular prompt architecture, the agent understands input, remembers context, plans its tasks, and generates helpful output — all with the goal of assisting exam preparation.
<h3>👩‍💻 Created by</h3>
Tanisha Chauhan
Role Applied: Data Champion
Assignment Track: AI Agent Development
<h3> 📌 Use Case</h3>
"Students often struggle to revise effectively before exams, not knowing what to focus on or how to test themselves. This agent provides context-based quiz questions to aid self-evaluation and learning."
- 🎯 Target User: Students preparing for exams in school, college, or competitive settings
- 🔑 Core Value: Personalized, topic-specific quiz generation that adapts to student needs
- ❌ Not in Scope: No progress tracking or long-term memory storage for now
<h3> 🧱 Prompt Architecture</h3>
<h4> 🔍 Input Understanding</h4>
Prompt Role: Parses student input to understand subject, topic, and difficulty
"Understand the student request and extract: subject, topic, difficulty, and question type. Clarify if vague."
<h4> 🧠 State Tracker</h4>
Prompt Role: Stores session context like subject and topic using simulated memory via system messages
"Store the subject and topic once provided and use them in future queries unless changed."
<h4> 📋 Task Planner</h4>
Prompt Role: Breaks the request into logical steps to plan quiz generation
"Decide the number and types of questions, fetch key concepts from the topic, and prepare output format."
<h4> 🗣️ Output Generator</h4>
Prompt Role: Generates quiz questions in a readable format
"Generate 5 quiz questions with proper numbering. Mix types (MCQ, True/False, Short Answer)."
<h3> 🔍 ChatGPT Iteration Log</h3>
Attempt Log:
Attempt	Prompt Variant	What Happened	What Changed	Why
1	“Make quiz questions”	Too generic	Added subject/topic extraction	To tailor content
2	“Generate quiz for history”	Good start	Added memory for topic	To retain context
3	“Make it 5 mixed question types”	Output improved	Controlled format	To enhance readability
<h3>✅ Output Examples</h3>
Test 1: Normal Input
Input: "Give me a quiz on World War II for history revision."
Output:
1. Who were the Axis Powers in WWII? (Short Answer)
2. True or False: WWII started in 1939.
3. What event triggered the US to enter WWII? (MCQ)
...
Test 2: Vague Input
Input: "I need help with a quiz"
Output: "Please specify the subject and topic you'd like the quiz to cover."
Test 3: Invalid Input
Input: (empty)
Output: "I didn’t catch that — could you please provide a topic or subject for the quiz?"
<h3>🧠 Reflection</h3>
- Hardest Part: Designing prompts that were modular and did not overlap.
- Most Enjoyed: Watching the AI adapt with better responses after tweaking prompts.
- Improvement Ideas: Add follow-up logic for multi-turn conversations and scoring.
- What I Learned: Prompt structure makes a huge difference — small changes impact outputs greatly.
- When Stuck: I used ChatGPT itself to debug and improve prompts step-by-step.
<h3>💡 Bonus (Hack Value)</h3>
- Simulated short-term memory by passing context between prompts
- Structured output formatting for better readability
- Included mixed-type question generation in a single prompt
<h3>🧾 Setup (Local Test)</h3>
1. Clone the Repo:

git clone https://github.com/your-username/ai-quiz-agent.git
cd ai-quiz-agent

2. Install Dependencies:

pip install -r requirements.txt

3. Add `.env` file:

OPENAI_API_KEY=your_openai_key_here

4. Run the App:

python app.py

<h3>📂 Folder Structure</h3>

├── app.py <br>
├── prompts.py <br>
├── .env <br>
├── README.md <br> 
└── requirements.txt <br>

<h3>🧠 Final Thoughts</h3>
This agent is a foundation — with memory, chaining, or UI, it could evolve into a complete quiz coach. The process helped me understand how AI agents can simulate thought and become powerful tools.
