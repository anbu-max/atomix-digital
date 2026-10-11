# Atomix Agent Core ⚡

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Powered by](https://img.shields.io/badge/Anthropic%20Claude-3.5%20Sonnet-FF6B35.svg)](https://anthropic.com)
[![Maintained by](https://img.shields.io/badge/Maintained%20by-Atomix%20Digital-black.svg)](https://atomixdigital.com)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://python.org)

**Atomix Agent Core** is an enterprise-grade multi-agent execution and workflow orchestration framework powered by Anthropic's **Claude 3.5 Sonnet** and **Claude 3.5 Haiku**. 

Engineered for autonomous task routing, high-accuracy structured JSON extraction, and scalable business process automation.

Maintained with ❤️ by the engineering team at [Atomix Digital](https://atomixdigital.com).

---

## 🚀 Key Highlights

- **Claude 3.5 Native Integration**: First-class support for prompt caching, tool use (function calling), and structured outputs.
- **Dynamic Multi-Agent Routing**: Coordinate specialized worker agents (e.g., Code Reviewer, Data Extractor, Workflow Planner) using a centralized router.
- **Type-Safe Validation**: Native Pydantic V2 schema enforcement to guarantee zero-hallucination structured responses.
- **Production Resilience**: Built-in exponential backoff, rate-limit adapters, and fallback strategies.

---

## 📋 Architecture

```text
               Incoming User / API Request
                            │
                            ▼
               ┌────────────────────────┐
               │   Atomix Agent Router  │
               └───────────┬────────────┘
                           │
       ┌───────────────────┼───────────────────┐
       ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Data Extract │   │ Code Analysis│   │ Webhook Exec │
│ (Haiku 3.5)  │   │ (Sonnet 3.5) │   │ (Tool Runner)│
└──────┬───────┘   └──────┬───────┘   └──────┬───────┘
       └───────────────────┼───────────────────┘
                           ▼
               ┌────────────────────────┐
               │ Type-Safe Pydantic V2  │
               │   Output Validation    │
               └───────────┬────────────┘
                           ▼
                    Final Response
```

---

## 🛠️ Installation

```bash
git clone https://github.com/anbu-max/atomix-digital.git
cd atomix-agent-core
pip install -e .
```

Or install requirements directly:
```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Configuration

Set your Anthropic API key in a `.env` file:

```env
ANTHROPIC_API_KEY=sk-ant-api03-...
ATOMIX_LOG_LEVEL=INFO
```

---

## 💡 Quickstart Example

Run a structured agent in under 10 lines of code:

```python
import os
from atomix_core import AtomixAgent, AgentConfig

# Initialize agent powered by Claude 3.5 Sonnet
agent = AtomixAgent(
    config=AgentConfig(
        model="claude-3-5-sonnet-20241022",
        system_prompt="You are an autonomous research and extraction agent."
    )
)

response = agent.run("Summarize the architectural advantages of Claude 3.5 Sonnet.")
print(response.content)
```

---

## 📂 Project Structure

```
atomix-agent-core/
├── src/
│   └── atomix_core/
│       ├── __init__.py      # Package entrypoint
│       ├── client.py        # Anthropic Claude API wrapper
│       ├── router.py        # Multi-agent dispatch & coordination
│       └── types.py         # Pydantic schemas & state models
├── examples/
│   └── quickstart.py        # Complete runnable demo
├── requirements.txt         # Production dependencies
├── pyproject.toml           # PEP 621 package metadata
└── README.md                # Documentation
```

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a PR.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Developed by [Atomix Digital](https://atomixdigital.com).
