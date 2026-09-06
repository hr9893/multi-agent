# Fitness Plan Generator

A Streamlit application that generates personalized fitness plans using the Groq LLM.

## Overview

This project provides a simple web interface where users can input their fitness goals, experience level, available workout days, equipment, and any injuries. The app then leverages the Groq AI model to generate a detailed workout plan tailored to the user's specifications.

## Features

- Interactive UI built with **Streamlit**
- Integration with **Groq** LLM for intelligent plan generation
- Downloadable workout plan as a text file
- Supports multiple fitness goals and equipment options

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirments.txt
   ```

4. **Configure Groq API Key**
   - Create a file `/.streamlit/secrets.toml` (or set the environment variable `GROQ_API_KEY`).
   - Add the following content:
   ```toml
   GROQ_API_KEY = "your-groq-api-key"
   ```

5. **Run the application**
   ```bash
   streamlit run main.py
   ```

   The app will be available at `http://localhost:8501`.

## Usage

- Select your **Fitness Goal**, **Experience Level**, number of **Available Days**, and **Equipment**.
- Optionally provide any **Injuries**.
- Click **Generate Plan** to receive a personalized workout plan.
- Use the **Download Plan** button to save the plan locally.

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License.