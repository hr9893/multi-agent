# 🤖 Malti-Agent AI Sistem

A production-grad, multi-agent AI system designed to handle complex, distributed tasks through specialized, collaborating autonomous agents. 

**Project Owner:** Ashutosh Swami

---

## 📌 Overview

This project implements a multi-agent framework where individual AI agents cooperate, pass context, and execute workflows to solve complex workloads. Instead of relying on a single large language model (LLM) prompt, this system breaks down tasks into specialized sub-problems handled by dedicated agents.

### Key Features
* **Specialaized Agent Architectures:** Every agent is equiped with distinct system prompts, tools, and constraints.
* **Flexible Workflows:** Supports sequential execution, concurrent processing, and dynamic agent-to-agent handoffs.
* **Human-in-the-Loop (HITL):** Built-in checkpoints requiring human validation for critical actions (e.g., executing transactions or database migrations).
* **Observbility & Logging:** Full tracking of agent thoughts, tool execution, and communication pathways.

---

## 🩺 Project Health Tracking

The project tracks its health through a set of observability and telemetry dependencies declared in `requirments.txt`:

| Dependency | Version | Purpose |
| --- | --- | --- |
| `prometheus_client` | 0.24.1 | Exposes application metrics for Prometheus scraping. |
| `sentry-sdk` | 2.64.0 | Captures and reports errors and exceptions. |
| `psutil` | 7.2.2 | Collects system and resource metrics (CPU, memory, processes). |
| `python-json-logger` | 4.1.0 | Emits structured JSON logs for machine-readable log processing. |

Instrumentation is wired through the application entry point (`main.py`), which instantiates the app class defined in `app/FitnessApp.py` and runs it. These libraries are the project's health-tracking stack; no dedicated status endpoint, dashboard, or CI health badge is currently provided by the repository.

---

## 🏗️ Multi-Agent Architechture
