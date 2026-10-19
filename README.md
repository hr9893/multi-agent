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

## 🔁 LLM providers and fallback

The fitness plan generator can use more than one LLM provider. Requests are sent
through an ordered provider chain:

1. **Groq** (`app/GroqService.py`)
2. **OpenAI** (`app/OpenAIService.py`)

`app/LLMFallbackService.py` orchestrates the chain. If a provider fails — for
example because its budget, quota or rate limit is exhausted, or because of any
other provider error — a warning is logged and the same request is automatically
retried on the next provider in the chain. If every provider fails, a
`RuntimeError` listing the attempted providers and their errors is raised.

### Configuration

Both API keys must be set in `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "your-groq-api-key"
OPENAI_API_KEY = "your-openai-api-key"
```

The provider order can be changed by passing a custom list of
`(name, provider)` pairs to `LLMFallbackService(providers=[...])`.
