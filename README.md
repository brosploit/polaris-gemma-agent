# ✦ Polaris — Gemma 4 AI Computer Agent

> A multimodal AI computer agent powered by Gemma 4 that understands visual context, reasons about problems, plans safe actions, waits for human approval, executes controlled tools, and verifies the result.

**Hackathon:** October Fest  
**Problem Statement:** Best Use of Gemma 4

---

## 🎯 Problem

Traditional chatbots can explain a problem, but they usually stop at providing an answer.

When a developer encounters an error on their computer, they may need to:

1. Understand what the error means.
2. Identify the actual cause.
3. Decide what action should be taken.
4. Execute the fix.
5. Check whether the fix actually worked.

This creates a gap between **getting an answer** and **solving the problem**.

Polaris aims to bridge that gap by combining Gemma 4's multimodal reasoning with a controlled computer-agent workflow.

---

## 💡 My Approach

Polaris follows an agentic pipeline:

**Perceive → Understand → Reason → Plan → Approve → Act → Verify**

### 1. Perceive
Polaris receives a screenshot and/or a description of the user's problem.

### 2. Understand
Gemma 4 analyzes the visual and textual context.

### 3. Reason
The model identifies the likely cause of the problem.

### 4. Plan
Polaris generates a structured and safe action plan.

### 5. Approve
The user reviews the proposed action and explicitly approves it.

### 6. Act
Polaris executes only an allowlisted action through its controlled tool layer.

### 7. Verify
The result is checked to determine whether the action appears to have solved the problem.

This makes Polaris more than a chatbot: it is an **AI-assisted problem-solving workflow**.

---

## 🚀 Current Use Case: Visual Python Debugging

The demonstration focuses on a common developer problem.

A Python project produces:

```text
ModuleNotFoundError: No module named 'requests'
```

Instead of simply explaining the error, Polaris:

**Screenshot → Diagnosis → Action Plan → Human Approval → Tool Execution → Verification**

For the prepared demonstration, Polaris identifies the missing `requests` package and proposes installing it.

The installation action is explicitly allowlisted and requires human approval before execution.

---

## ✨ Key Features

- 🖼️ Multimodal screenshot understanding
- 🧠 Gemma 4 reasoning
- 📋 Structured action planning
- 🛡️ Human approval before execution
- ⚙️ Controlled allowlisted tool execution
- 🔎 Result verification
- 🎨 Interactive Gradio interface
- ⚡ Reproducible demonstration mode

---

## 🏗️ Architecture

```text
                    ┌───────────────┐
                    │     User      │
                    └───────┬───────┘
                            │
                    Screenshot + Task
                            │
                            ▼
                    ┌───────────────┐
                    │    Polaris    │
                    │    /Gradio    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    Gemma 4    │
                    │   Multimodal  │
                    │    Reasoning  │
                    └───────┬───────┘
                            │
                  Diagnosis + Action Plan
                            │
                            ▼
                    ┌───────────────┐
                    │    Human      │
                    │    Approval   │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    Safety     │
                    │   Allowlist   │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Tool Execution│
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Verification  │
                    └───────────────┘
```

---

## 🔐 Safety by Design

Polaris is designed so that Gemma does **not** receive unrestricted computer control.

- Human approval is required before an action.
- Only explicitly allowlisted actions can execute.
- Arbitrary model-generated shell commands are not executed.
- Destructive commands are not allowed.
- Passwords, API keys, tokens, and secrets are not requested.
- System-critical files are not modified.

This creates a **human-in-the-loop agent architecture**.

---

## 📁 Project Structure

```text
polaris-gemma-agent/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── gemma.py
│   └── agent.py
│
├── assets/
│   └── test_error.png
│
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

# 🛠️ Setup

## 1. Clone the repository

```bash
git clone https://github.com/brosploit/polaris-gemma-agent.git
cd polaris-gemma-agent
```

## 2. Create a virtual environment

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure the API key

Create a `.env` file based on `.env.example`.

```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMMA_MODEL=gemma-4-26b-a4b-it
```

**Never commit your `.env` file or expose your API key publicly.**

## 5. Run Polaris

```bash
python -m app.main
```

The Gradio interface will start locally.

---

# 🎬 Running the Demo

1. Launch Polaris.
2. Click **⚡ DEMO**.
3. Click **✦ ANALYZE WITH GEMMA 4**.
4. Review the diagnosis.
5. Review the proposed action.
6. Click **🛡️ APPROVE & EXECUTE**.
7. Review the tool output.
8. Click **✓ VERIFY RESULT**.

The prepared demonstration uses:

```text
assets/test_error.png
```

The screenshot contains a Python `ModuleNotFoundError` caused by the missing `requests` package.

---

# 🧠 Why Gemma 4?

Polaris is designed around a multimodal agent workflow rather than a simple text conversation.

Gemma 4 receives the visual context and user task and helps Polaris:

- understand the problem,
- reason about its cause,
- generate a structured plan,
- and identify an appropriate safe action.

Polaris then adds the surrounding agent workflow:

**Understand → Plan → Approve → Act → Verify**

---

# 🆚 Polaris vs Generic Chatbot

| Capability | Generic Chatbot | Polaris |
|---|---:|---:|
| Understand text | ✅ | ✅ |
| Understand screenshots | Depends | ✅ |
| Diagnose visual problems | Limited | ✅ |
| Create an action plan | ✅ | ✅ |
| Human approval workflow | Usually manual | ✅ |
| Execute controlled tool actions | Usually no | ✅ |
| Verify result | Usually manual | ✅ |
| Application-level safety allowlist | Usually no | ✅ |

---

# 🚀 What We Should Build Next

Polaris is designed to grow into a broader AI computer-assistance platform.

### Smarter Computer Understanding

- Active application context
- Richer screenshot analysis
- Code and terminal context
- Visual UI understanding
- Combined visual + textual reasoning

### Developer Tools

- Python diagnostics
- Dependency management
- Test execution
- Log analysis
- Safe file inspection
- Development-environment diagnostics

### Advanced Permission System

- Action risk assessment
- Permission levels
- Human approval workflows
- Controlled tool execution
- Action history

### Better Verification

- Automated tests
- Before/after state comparison
- Error-state detection
- Tool-output analysis
- Gemma-powered verification

### Extensible Agent Architecture

- Plugin system
- Additional safe tools
- IDE integrations
- Cross-platform support
- Multimodal workflows
- Local and cloud model options
- Voice interaction

### Long-Term Vision

```text
Visual Debugging
       ↓
Developer Assistant
       ↓
Multimodal Agent
       ↓
Tool-Based Computer Agent
       ↓
Safety-Aware Computer Assistant
       ↓
Open-Source AI Agent Platform
```

---

# 🧰 Technology Stack

- **Python**
- **Gemma 4**
- **Google GenAI SDK**
- **Gradio**
- **Pillow**
- **python-dotenv**
- **Git**
- **GitHub**

---

# 🤖 AI-Assisted Development


Polaris was developed using AI-assisted programming and iterative engineering.

AI tools were used for:

- Architecture brainstorming
- Prompt design
- Code generation and refinement
- Debugging
- Documentation
- UI development
- Testing ideas
- Project planning

The project was developed and tested locally using **VS Code**, **Python**, **PowerShell**, and **Git**.

---

# 🌟 Development Vision

The goal of Polaris is simple:

> **Build an AI assistant that can understand your computer, help you accomplish tasks, and keep you in control.**

Polaris combines multimodal AI, reasoning, controlled tool use, human approval, and verification into one workflow.

---

# 💡 Hackathon Pitch

> **“The chatbot gave you an answer. Polaris understands the context, plans the action, asks for permission, executes it safely, and verifies the result.”**

---

## 📜 License

This project is released under the **MIT License**.

---

## 🔗 Project

**GitHub:**  
https://github.com/brosploit/polaris-gemma-agent
