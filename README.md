# 🧠 MindMesh AI

MindMesh AI is an educational assistant that helps students learn more effectively by generating concept explanations, practice quizzes, and a short study plan from a single topic input — all in one Streamlit app.

## 🎯 Problem

Students often spend significant time searching for explanations, creating study plans, and preparing practice questions. Learning resources are scattered across multiple platforms, making studying less efficient.

## 💡 Solution

MindMesh AI brings learning assistance into one place. Enter a topic, and the app uses the Gemini API to generate:

* A beginner-friendly explanation
* 3 quiz questions with answers
* A 3-day study plan

All three are generated together from a single prompt to `gemini-2.5-flash` and displayed on one page.

## 🤖 Architecture (Current State)

The current implementation is a **single-prompt MVP**, not yet a true multi-agent system. One Gemini call handles explanation, quiz, and study-plan generation together; there is no agent orchestration, message passing, or routing logic yet.

The planned architecture consists of four specialized roles:

| Role               | Current Status                                                                 |
| ------------------ | ------------------------------------------------------------------------------ |
| **Coordinator**    | Not implemented. No routing logic exists yet — there is one fixed prompt path. |
| **Explainer**      | Implemented as part of the combined prompt (not a separate agent).             |
| **Quiz Generator** | Implemented as part of the combined prompt (not a separate agent).             |
| **Study Planner**  | Implemented as part of the combined prompt (not a separate agent).             |

Splitting these into independent agents with a coordinator that routes between them is the core next step in development.

## 🛠️ Technologies

### Currently Used

* Python
* Streamlit
* Google Gemini API (`gemini-2.5-flash`)
* python-dotenv

### Planned

* Google ADK (Agent Development Kit)
* MCP (Model Context Protocol)

## 🔒 Security Notes

Current input handling is minimal: the app checks that the topic field is not empty before sending a request. Dedicated input validation, prompt-injection protection, and agent-level safeguards are planned as the system evolves into a true multi-agent architecture.

## 🚀 Roadmap

* [ ] Refactor into separate Explainer, Quiz, and Study Planner agents
* [ ] Implement a Coordinator Agent for task routing
* [ ] Integrate Google ADK for agent orchestration
* [ ] Add MCP integration for tool and context sharing
* [ ] Add input validation and prompt-injection safeguards
* [ ] Implement conversation memory
* [ ] Add progress tracking
* [ ] Generate flashcards
* [ ] Add subject-specific learning modes
* [ ] Develop a voice-based learning assistant

## 🏃 Running Locally

Clone the repository:

```bash
git clone https://github.com/Deepthii7/mindmesh-ai-agent.git
cd mindmesh-ai-agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

## 🏆 Kaggle Capstone Project

This project is being developed as part of the **5-Day AI Agents: Intensive Vibe Coding Course With Google**, hosted through Kaggle.
