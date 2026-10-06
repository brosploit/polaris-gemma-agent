# ✦ Polaris — Gemma 4 AI Computer Agent

> A multimodal AI computer agent powered by Gemma 4 that understands visual context, reasons about a problem, proposes a safe action, waits for human approval, executes an allowlisted action, and verifies the result.

**Hackathon:** October Fest  
**Problem Statement:** Best use of Gemma 4

## 🚀 What is Polaris?

Generic chatbots can give you an answer. **Polaris is designed to help you solve the problem.**

Pipeline:

**Perceive → Understand → Reason → Plan → Approve → Act → Verify**

The current MVP focuses on visual Python debugging.

## ✨ Features

- 🖼️ Multimodal screenshot understanding
- 🧠 Gemma 4 reasoning
- 📋 Structured action planning
- 🛡️ Human approval gate
- ⚙️ Safe allowlisted tool execution
- 🔎 Result verification
- 🎨 Interactive Gradio interface
- ⚡ Reproducible demo mode

## 🏗️ Architecture

```text
User
  ↓
Screenshot + Task
  ↓
Polaris / Gradio
  ↓
Gemma 4
  ↓
Diagnosis + Action Plan
  ↓
Human Approval
  ↓
Safety Allowlist
  ↓
Tool Execution
  ↓
Verification
```

## 🔐 Safety

Polaris does **not** give Gemma unrestricted shell access.

- Human approval is required.
- Actions are checked against an explicit allowlist.
- Arbitrary model-generated shell commands are not executed.
- Destructive commands are not allowed.
- Secrets, passwords, API keys, and tokens are not requested.
- System-critical files are not modified.

The current demonstration allowlists installation of the Python `requests` package.

## 📁 Project Structure

```text
polaris-gemma-agent/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── gemma.py
│   └── agent.py
├── assets/
│   └── test_error.png
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

Do **not** commit `.env`, `.venv/`, or `__pycache__/`.

## 🛠️ Installation

### 1. Clone

```bash
git clone https://github.com/YOUR-USERNAME/polaris-gemma-agent.git
cd polaris-gemma-agent
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Copy `.env.example` to `.env` and put your own Google Gemini API key inside:

```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMMA_MODEL=gemma-4-26b-a4b-it
```

**Never commit `.env` or expose your API key publicly.**

### 5. Run Polaris

```bash
python -m app.main
```

## 🎬 Demo

1. Launch Polaris.
2. Click **⚡ DEMO**.
3. Click **✦ ANALYZE WITH GEMMA 4**.
4. Review the diagnosis and action plan.
5. Click **🛡️ APPROVE & EXECUTE**.
6. Review the tool output.
7. Click **✓ VERIFY RESULT**.

The prepared demo uses `assets/test_error.png`, which shows a Python `ModuleNotFoundError` caused by the missing `requests` package.

## 🧠 Why Gemma 4?

Polaris is built around a multimodal agent workflow rather than a simple text chatbot.

Gemma 4 receives visual context and the user's task, reasons about the problem, and produces a structured diagnosis and action plan. Polaris adds the agent layer:

**Understand → Plan → Approve → Act → Verify**

## 🆚 Polaris vs Generic Chatbot

| Capability | Generic Chatbot | Polaris |
|---|---:|---:|
| Understand text | ✅ | ✅ |
| Understand screenshot | Depends | ✅ |
| Diagnose visual problem | Limited | ✅ |
| Create action plan | ✅ | ✅ |
| Human approval gate | Usually manual | ✅ |
| Execute safe tool action | Usually no | ✅ |
| Verify result | Usually manual | ✅ |
| Application-level safety allowlist | Usually not | ✅ |

## 🔮 Roadmap

- [ ] More allowlisted developer tools
- [ ] Automatic test verification
- [ ] Richer computer context
- [ ] Code editor integration
- [ ] More multimodal workflows
- [ ] Plugin architecture
- [ ] Local/offline model options
- [ ] Voice interface
- [ ] Cross-platform support

## 💡 Hackathon Pitch

> “Generic chatbots can explain an error. Polaris is designed to understand the computer context around that error, plan a solution, ask for human approval, perform a safe action, and verify the result.”

**The chatbot gave you an answer. Polaris helped you solve the problem.**
