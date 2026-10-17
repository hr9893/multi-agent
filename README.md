# 🏋️ Fitness Plan Generator

A Streamlit app that generates a personalized, AI-written workout plan from a few details about your fitness goal, experience level, schedule, available equipment, and any injuries.

**Project Owner:** Ashutosh Swami

---

## 📌 Overview

Instead of relying on a generic template, the app collects your training context and asks a large language model (via the Groq API) to produce a plan tailored to it. The generated plan is shown in the app and can be downloaded as a plain-text file.

### Key Features
* **Goal-aware plans:** Choose from *Build muscle*, *Lose fat*, *General fitness*, or *Improve endurance*.
* **Experience scaling:** Plans adapt to *Beginner*, *Intermediate*, or *Advanced* levels.
* **Flexible scheduling:** Pick anywhere from 1 to 7 training days per week.
* **Equipment-aware exercises:** *No equipment*, *Home dumbbells*, or *Full gym*.
* **Injury input:** A free-text field for injuries, which is passed to the model so the plan can work around them.
* **Downloadable output:** Save the generated plan as `fitness_plan.txt`.

---

## 🩺 How the Project Tracks Health

The app tracks health by building a **fitness profile** from the inputs you provide and using it to generate a plan that matches your current condition and goals. It does not connect to wearables, sensors, or medical records, and it does not store a history of your data.

The health profile is assembled in `app/FitnessApp.py` from five inputs:

| Input | UI control | Values |
| --- | --- | --- |
| Fitness goal | Select box | Build muscle, Lose fat, General fitness, Improve endurance |
| Experience level | Select box | Beginner, Intermediate, Advanced |
| Available days | Slider | 1–7 |
| Available equipment | Select box | No equipment, Home dumbbells, Full gym |
| Injuries | Text input | Free text (may be left empty) |

These values are collected into a `fitness_data` dictionary and passed to `GroqService.generate_response()` in `app/GroqService.py`. That method embeds each field into a prompt for a professional fitness planning assistant and requests a plan that includes:

* A workout for each day
* Exercises
* Sets
* Repetitions
* Rest periods
* General recommendations

The model's reply is displayed under **Generated Fitness Plan** and offered as a download. Because the injury field is part of the prompt, the plan is generated with your reported limitations in mind — but the output is general fitness guidance, not medical advice.

---

## 🏗️ Architecture

```
main.py                  # Entry point: creates FitnessApp and calls run()
app/FitnessApp.py        # Streamlit UI, collects the fitness profile, renders the plan
app/GroqService.py       # Builds the prompt and calls the Groq chat completions API
```

* **`main.py`** instantiates `FitnessApp` and calls `app.run()`.
* **`FitnessApp.run()`** renders the Streamlit form, validates nothing beyond the widget constraints, and on **Generate Plan** shows a spinner while the request is in flight. Errors from the LLM call are caught and printed to the console.
* **`GroqService.generate_response(fitness_data)`** creates a `Groq` client and calls `client.chat.completions.create()` with the model `openai/gpt-oss-20b`, a system message ("You are a professional fitness assistant."), and the user prompt built from `fitness_data`.

---

## 🚀 Getting Started

### Prerequisites
* Python 3
* A Groq API key

### Install dependencies

```bash
pip install streamlit groq
```

### Configure the API key

The app reads the key from Streamlit secrets under the name `GROQ_API_KEY` (`st.secrets["GROQ_API_KEY"]`). Create `.streamlit/secrets.toml` in the project root:

```toml
GROQ_API_KEY = "<YOUR_API_KEY>"
```

Do not commit this file.

### Run the app

```bash
streamlit run main.py
```

Then open the URL Streamlit prints (typically `http://localhost:8501`), fill in the form, and click **Generate Plan**.

---

## 📁 Project Structure

```
.
├── main.py
├── app/
│   ├── FitnessApp.py
│   └── GroqService.py
└── README.md
```

---

## ⚠️ Disclaimer

Generated plans are produced by a language model and are for general informational purposes only. They are not a substitute for advice from a qualified medical or fitness professional. Consult a professional before starting a new training program, especially if you have an injury or health condition.
