# 🤖 Malti-Agent AI Sistem

A production-grad, multi-agent AI system designed to handle complex, distributed tasks through specialized, collaborating autonomous agents. 

---

## 📌 Overview

This project implements a multi-agent framework where individual AI agents cooperate, pass context, and execute workflows to solve complex workloads. Instead of relying on a single large language model (LLM) prompt, this system breaks down tasks into specialized sub-problems handled by dedicated agents.

### Key Features
* **Specialaized Agent Architectures:** Every agent is equiped with distinct system prompts, tools, and constraints.
* **Flexible Workflows:** Supports sequential execution, concurrent processing, and dynamic agent-to-agent handoffs.
* **Human-in-the-Loop (HITL):** Built-in checkpoints requiring human validation for critical actions (e.g., executing transactions or database migrations).
* **Observbility & Logging:** Full tracking of agent thoughts, tool execution, and communication pathways.

---

## 🏗️ Multi-Agent Architechture

---

## 🔁 LLM Providers and Automatic Fallback

The fitness plan generator can use more than one LLM provider. Requests are sent to
the providers in order, and if one fails (rate limit, exhausted quota/budget, network
error, or any other exception) the next provider is tried automatically.

Order of providers:

1. **Groq** (`app/GroqService.py`) — primary provider.
2. **OpenAI** (`app/OpenAIService.py`) — fallback provider.

The orchestration lives in `app/LLMService.py`. It exposes the same
`generate_response(fitness_data) -> str` method as the individual providers, so it is a
drop-in replacement. A provider whose API key is not configured is skipped instead of
crashing the app. If every provider fails, a `RuntimeError` describing each failure is
raised.

### Required secrets

Create `.streamlit/secrets.toml` (or set the equivalent secrets in Streamlit Cloud):

```toml
GROQ_API_KEY = "your-groq-api-key"
OPENAI_API_KEY = "your-openai-api-key"

# Optional: override the default OpenAI model ("gpt-4o-mini")
# OPENAI_MODEL = "gpt-4o-mini"
```

Only `GROQ_API_KEY` is required to keep the previous single-provider behavior working;
adding `OPENAI_API_KEY` enables the automatic fallback.
