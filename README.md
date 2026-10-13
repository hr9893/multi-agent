# 🏋️ Workout Plan Generator

A small **Streamlit** web app that generates a personalized, AI-written workout plan
based on a user's fitness goal, experience level, available training days, available
equipment, and any injuries.

The app collects a few inputs from the user, builds a structured prompt, sends it to a
large language model through the **Groq API**, and displays the generated plan in the
browser. The plan can then be downloaded as a plain-text file.

---

## 📌 What It Does

Instead of manually designing a training program, the user answers five quick questions
and the app produces a complete workout plan that includes:

- A workout for each training day
- Exercises
- Sets
- Repetitions
- Rest periods
- General recommendations

The generated plan is tailored to the user's goal (e.g. build muscle, lose fat), their
experience level, how many days per week they can train, what equipment they have
access to, and any injuries they want the plan to account for.

---

## ✨ Key Features

- **Guided input form** — Streamlit widgets for fitness goal, experience level,
  available days (1–7), available equipment, and injuries.
- **LLM-generated plans** — Uses the Groq API with the `openai/gpt-oss-20b` model to
  generate the workout plan.
- **Structured prompt** — The user's answers are injected into a professional
  fitness-assistant prompt that requests day-by-day workouts, sets, reps, rest periods,
  and recommendations.
- **Downloadable output** — The generated plan can be downloaded as `fitness_plan.txt`.
- **Loading feedback** — A spinner is shown while the plan is being generated.

---

## 🏗️ How It Works

The application is intentionally small and has three main pieces:

```
main.py                 →  app/FitnessApp.py  →  app/GroqService.py  →  Groq API
(entry point)              (Streamlit UI)         (LLM client)
```

1. **`main.py` (entry point)**
   Creates an instance of `FitnessApp` and calls `app.run()`.

2. **`app/FitnessApp.py` (UI / controller)**
   - Renders the Streamlit interface: title, selectboxes for fitness goal, experience
     level and equipment, a slider for available days, and a text input for injuries.
   - When the **Generate Plan** button is pressed, it collects the inputs into a
     `fitness_data` dictionary.
   - Calls `GroqService.generate_response(fitness_data)` inside a spinner.
   - Displays the returned plan and offers a download button for `fitness_plan.txt`.

3. **`app/GroqService.py` (LLM service)**
   - Reads the API key from Streamlit secrets (`st.secrets["GROQ_API_KEY"]`).
   - Builds a prompt from the `fitness_data` dictionary.
   - Sends a system message ("You are a professional fitness assistant.") and the user
     prompt to the Groq chat completions endpoint using the `openai/gpt-oss-20b` model.
   - Returns the model's response text.

### Data Flow

```
User input (Streamlit widgets)
        │
        ▼
fitness_data = { fitness_goal, experience_level,
                 available_days, available_equipment, injuries }
        │
        ▼
GroqService.generate_response(fitness_data)
        │  builds prompt
        ▼
Groq API  (model: openai/gpt-oss-20b)
        │
        ▼
response.choices[0].message.content
        │
        ▼
Displayed in Streamlit  +  Download as fitness_plan.txt
```

---

## 🧰 Technical Details

| Item | Value |
| --- | --- |
| Language | Python |
| Python version | `>=3.11` (from `pyproject.toml`) |
| Project name | `workoutplangenerator` |
| Version | `0.1.0` |
| UI framework | [Streamlit](https://streamlit.io/) |
| LLM provider | [Groq](https://groq.com/) via the `groq` Python SDK |
| Model | `openai/gpt-oss-20b` |
| Declared dependencies | None in `pyproject.toml` (see note below) |

### Dependencies

`pyproject.toml` declares the project metadata but lists **no dependencies**
(`dependencies = []`). The code, however, imports the following third-party packages,
which must be installed to run the app:

- `streamlit` — used in `app/FitnessApp.py` and `app/GroqService.py`
- `groq` — used in `app/GroqService.py`

### Configuration / Secrets

The Groq API key is **not** hard-coded. It is read at runtime from Streamlit secrets:

```python
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
```

This means the key must be provided through Streamlit's secrets mechanism, i.e. a
`.streamlit/secrets.toml` file containing:

```toml
GROQ_API_KEY = "your-groq-api-key-here"
```

> ⚠️ Never commit your real `secrets.toml` or API key to version control.

### Notable Design Decisions

- **Separation of concerns:** the UI (`FitnessApp`) is kept separate from the LLM
  integration (`GroqService`), so the model/provider could be swapped without touching
  the interface.
- **Prompt-driven generation:** all personalization is achieved through the prompt
  template rather than hard-coded workout logic, so the plan format is controlled by the
  instructions given to the model.
- **Secrets over environment variables:** the API key is sourced from Streamlit secrets
  rather than `os.environ`.

---

## 🚀 Installation & Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create and activate a virtual environment** (Python 3.11+)

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # On Windows: .venv\Scripts\activate
   ```

3. **Install the required packages**

   ```bash
   pip install streamlit groq
   ```

4. **Configure your Groq API key**

   Create `.streamlit/secrets.toml` in the project root:

   ```toml
   GROQ_API_KEY = "your-groq-api-key-here"
   ```

   You can obtain an API key from the Groq console.

---

## ▶️ Usage

Run the Streamlit app from the project root:

```bash
streamlit run main.py
```

Then, in the browser window that opens:

1. Select a **Fitness Goal** (Build muscle, Lose fat, General fitness, Improve endurance).
2. Select an **Experience Level** (Beginner, Intermediate, Advanced).
3. Choose the number of **days** you can train (1–7).
4. Select your **Available Equipment** (No equipment, Home dumbbells, Full gym).
5. Enter any **injuries** (optional).
6. Click **Generate Plan**.
7. Review the generated plan and click **📥 Download Plan** to save it as
   `fitness_plan.txt`.

---

## 📁 Project Structure

```
.
├── main.py                 # Entry point: creates FitnessApp and runs it
├── pyproject.toml          # Project metadata (name, version, Python requirement)
├── README.md               # This file
└── app/
    ├── FitnessApp.py       # Streamlit UI and input handling
    └── GroqService.py      # Groq API client and prompt construction
```

---

## 🧪 Testing

There is currently **no test suite** in the repository. To verify the app manually:

1. Start the app with `streamlit run main.py`.
2. Fill in the form and click **Generate Plan**.
3. Confirm that a plan is displayed and that the download button produces
   `fitness_plan.txt`.

If the API key is missing or invalid, the app will raise an exception while calling the
LLM; check that `.streamlit/secrets.toml` contains a valid `GROQ_API_KEY`.

---

## 🤝 Contributing

Contributions are welcome. Since there is no `CONTRIBUTING.md` in the repository, the
general workflow is:

1. Fork the repository and create a feature branch.
2. Make your changes.
3. Open a pull request describing what you changed and why.

---

## 📄 License

No license file is present in this repository. Please contact the repository owner
regarding licensing and usage terms.
