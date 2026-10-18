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

## 🔁 Multi-LLM Fallback

The fitness plan generator does not depend on a single LLM. `app/LLMService.py`
defines a provider-agnostic `LLMService` that tries a list of providers in order:

1. **Groq** (`openai/gpt-oss-20b`) — primary provider
2. **OpenAI** (`gpt-4o-mini`) — fallback provider

If the primary provider fails — for example because its rate limit, quota or
budget is exhausted (HTTP 429 / insufficient quota) — the request is
automatically retried on the next provider. The provider that produced the
response is logged, and providers without an API key are skipped, so the app
keeps working with only one provider configured.

### Required secrets

Create `.streamlit/secrets.toml` (never commit it) with the keys you have:

```toml
GROQ_API_KEY = "your-groq-api-key"
OPENAI_API_KEY = "your-openai-api-key"
```

At least one of the two keys must be present. If every configured provider
fails, `LLMService.generate_response()` raises a `RuntimeError` listing the
per-provider errors.

`app/GroqService.py` is kept as a thin, backward-compatible Groq-only wrapper
around `LLMService`; new code should use `LLMService` directly.
