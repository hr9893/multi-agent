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

## 🔁 LLM Providers and Fallback

The fitness plan generator can use two LLM providers:

| Provider | Service class | Default model | Secret |
| --- | --- | --- | --- |
| Groq (primary) | `app/GroqService.py` | `openai/gpt-oss-20b` | `GROQ_API_KEY` |
| OpenAI (fallback) | `app/OpenAIService.py` | `gpt-4o-mini` | `OPENAI_API_KEY` |

`app/LLMService.py` orchestrates them. It calls the primary provider first; if that
call raises for any reason (rate limit, exhausted quota/budget, network error, ...)
it logs a warning and retries the same request with the next provider. If every
provider fails, a `RuntimeError` listing each provider error is raised.

### Configuration

Add the keys to `.streamlit/secrets.toml` (or the Streamlit Cloud secrets editor):

```toml
GROQ_API_KEY = "your-groq-key"
OPENAI_API_KEY = "your-openai-key"
```

The provider order is optional and defaults to Groq then OpenAI. Override it with a
comma-separated secret:

```toml
LLM_PROVIDER_ORDER = "groq,openai"
```

If `OPENAI_API_KEY` is missing, the OpenAI fallback simply fails and the error is
reported like any other provider failure; the app does not crash at startup.
