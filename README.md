# 🤖 Malti-Agent AI Sistem

A production-grad, multi-agent AI system designed to handle complex, distributed tasks through specialized, collaborating autonomous agents. 

**Owner / Maintainer:** Ashutosh Swami

---

## 📌 Overview

This project implements a multi-agent framework where individual AI agents cooperate, pass context, and execute workflows to solve complex workloads. Instead of relying on a single large language model (LLM) prompt, this system breaks down tasks into specialized sub-problems handled by dedicated agents.

### Key Features
* **Specialaized Agent Architectures:** Every agent is equiped with distinct system prompts, tools, and constraints.
* **Flexible Workflows:** Supports sequential execution, concurrent processing, and dynamic agent-to-agent handoffs.
* **Human-in-the-Loop (HITL):** Built-in checkpoints requiring human validation for critical actions (e.g., executing transactions or database migrations).
* **Observbility & Logging:** Full tracking of agent thoughts, tool execution, and communication pathways.

---

## 🩺 How the Project Tracks Health

This project is a **Fitness Plan Generator** that tracks a user's health and fitness profile in order to produce personalized workout plans. Health tracking is driven by the inputs collected in the Streamlit UI (`app/FitnessApp.py`) and used to build the LLM prompt in `app/GroqService.py`:

* **Fitness goal** — e.g. build muscle, lose fat, general fitness, or improve endurance.
* **Experience level** — beginner, intermediate, or advanced.
* **Available training days** — 1 to 7 days per week.
* **Available equipment** — no equipment, home dumbbells, or full gym.
* **Injuries** — any injuries the user reports, so the generated plan can account for them.

These health-related inputs are passed to the Groq LLM service (`app/GroqService.py`), which generates a personalized plan including daily workouts, exercises, sets, repetitions, rest periods, and general recommendations. The generated plan can then be downloaded as a text file for the user to keep and follow.

> Note: The project does not currently expose a health-check endpoint or automated monitoring/uptime checks. "Health" here refers to the user's fitness/health profile that the app collects and uses to generate plans.

---

## 🏗️ Multi-Agent Architechture
