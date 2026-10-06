# ✦ Polaris — Gemma 4 AI Computer Agent

> **A multimodal AI computer agent that understands visual context, reasons about problems, plans safe actions, asks for human approval, executes controlled actions, and verifies the result.**

**Hackathon:** October Fest  
**Problem Statement:** Best Use of Gemma 4  
**Repository:** `brosploit/polaris-gemma-agent`

---

## 🚀 What is Polaris?

Most AI chatbots give you an answer.

**Polaris is designed to help you move from understanding a problem to safely taking action.**

Polaris uses **Gemma 4** as its multimodal reasoning engine and surrounds it with a controlled agent workflow:

```text
Perceive
   ↓
Understand
   ↓
Reason
   ↓
Plan
   ↓
Approve
   ↓
Act
   ↓
Verify
```

The current MVP focuses on **visual Python debugging**.

A user can provide a screenshot of an error together with a task description. Polaris sends that context to Gemma 4, receives a structured diagnosis and action plan, waits for human approval, executes only an explicitly allowlisted action, and then verifies the result.

---

# 🎯 The Problem

When developers encounter an error, a typical chatbot can tell them:

> "This is the problem. Run this command."

But there is a gap between:

**AI explaining a solution**

and

**AI assisting with a controlled solution workflow.**

Polaris explores that gap.

Instead of allowing an AI model to directly control the computer, Polaris introduces:

- Structured reasoning
- Explicit action planning
- Human approval
- Safe tool boundaries
- Result verification

---

# 🧠 The Core Idea

Polaris treats Gemma 4 as the **reasoning layer**, not as an unrestricted computer controller.

```text
              User
                │
                ▼
       Screenshot + Task
                │
                ▼
           ┌─────────┐
           │ Gemma 4 │
           └────┬────┘
                │
                ▼
      Diagnosis + Action Plan
                │
                ▼
        Human Approval Gate
                │
                ▼
        Safety Allowlist
           │          │
       Allowed      Blocked
           │          │
           ▼          ▼
      Tool Action   No Action
           │
           ▼
       Verification
```

---

# ✨ Features

- 🖼️ **Multimodal screenshot understanding**
- 🧠 **Gemma 4 reasoning**
- 📋 **Structured diagnosis**
- 📝 **Action planning**
- 🛡️ **Human approval gate**
- ⚙️ **Allowlisted tool execution**
- 🔎 **Result verification**
- 🎨 **Interactive Gradio interface**
- ⚡ **Prepared demonstration mode**
- 🔐 **Safety-first agent architecture**

---

# 🏗️ Architecture

```text
┌──────────────────────────────┐
│             User             │
│   Screenshot + Task Input    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Polaris / Gradio       │
│          Interface           │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│           Gemma 4            │
│  Multimodal Understanding    │
│         + Reasoning          │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│    Diagnosis + Action Plan   │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Human Approval         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Safety Allowlist       │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Tool Execution         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         Verification         │
└──────────────────────────────┘
```

---

# 🔐 Safety by Design

Polaris deliberately **does not give Gemma unrestricted shell access**.

The model can propose an action, but its output is **not directly executed as an arbitrary command**.

The current architecture uses:

### 🛡️ Human Approval

An action must be reviewed and approved by the user before execution.

### ✅ Explicit Allowlist

Only actions explicitly implemented in the agent layer are eligible for execution.

### 🚫 No Arbitrary Commands

Model-generated text cannot simply become an arbitrary shell command.

### 🚫 No Destructive Actions

The current MVP does not provide destructive computer-control capabilities.

### 🔑 No Secrets

Polaris does not ask the model to retrieve or expose passwords, API keys, tokens, or other secrets.

### 🔎 Verification

The result of an approved action is examined after execution.

---

# 🧪 Current Demonstration

The MVP contains a deliberately simple Python debugging scenario.

The demo project imports:

```python
import requests

print("Polaris test")
```

If the `requests` package is unavailable, Python produces a:

```text
ModuleNotFoundError
```

Polaris can analyze the screenshot of this error and identify the missing dependency.

The current demonstration allowlists the following action:

```text
python -m pip install requests
```

The important part is that **Gemma does not freely generate and execute arbitrary terminal commands**.

---

# 🎬 Demo Workflow

The repository contains a prepared demonstration asset:

```text
assets/test_error.png
```

### Step 1 — Launch

```bash
python -m app.main
```

### Step 2 — Load Demo

Click:

```text
⚡ DEMO
```

### Step 3 — Analyze

Click:

```text
✦ ANALYZE WITH GEMMA 4
```

Gemma analyzes the screenshot and task.

### Step 4 — Review

Polaris displays:

- Diagnosis
- Action plan
- Approval requirement
- Suggested action

### Step 5 — Approve

Click:

```text
🛡️ APPROVE & EXECUTE
```

### Step 6 — Execute

Polaris checks the action against the safe-action allowlist.

### Step 7 — Verify

Click:

```text
✓ VERIFY RESULT
```

Polaris examines the output and reports whether the action appears successful.

---

# 🆚 Polaris vs. Generic Chatbot

| Capability | Generic Chatbot | Polaris |
|---|:---:|:---:|
| Text understanding | ✅ | ✅ |
| Screenshot understanding | Depends | ✅ |
| Visual debugging | Limited | ✅ |
| Diagnosis | ✅ | ✅ |
| Action planning | ✅ | ✅ |
| Human approval workflow | Usually manual | ✅ |
| Controlled tool execution | Usually unavailable | ✅ |
| Explicit action allowlist | Usually unavailable | ✅ |
| Result verification | Usually manual | ✅ |

The goal is not simply:

> **"Make AI execute commands."**

The goal is:

> **"Give AI controlled capabilities with a human in the loop."**

---

# 🛠️ Technology Stack

## Runtime Technologies

| Technology | Role |
|---|---|
| **Gemma 4** | Multimodal AI reasoning |
| **Google GenAI SDK** | Gemma API integration |
| **Python** | Core application and agent logic |
| **Gradio** | Interactive user interface |
| **Pillow** | Image processing |
| **python-dotenv** | Environment configuration |
| **Git** | Version control |
| **GitHub** | Source-code hosting |

---

# 🤖 AI Tools Used During Development

Polaris was developed with the help of AI-assisted development workflows.

### ChatGPT

Used for:

- Project ideation
- Architecture planning
- Agent workflow design
- Debugging assistance
- Code generation and refinement
- Safety architecture discussion
- README/documentation creation
- Git/GitHub workflow guidance

### Google Gemini

Used as part of the development workflow and for experimentation with Google's Gemini/Gemma ecosystem.

The project itself uses **Gemma 4 as the runtime AI model**.

### Gemma 4

Gemma 4 is the **core AI model used by Polaris itself**.

It handles:

- Visual understanding
- Problem analysis
- Reasoning
- Diagnosis
- Action planning
- Verification-related reasoning

---

# 💻 Development Tools & Editors

| Tool | Usage |
|---|---|
| **Visual Studio Code** | Main code editor and debugging environment |
| **Git** | Version control |
| **GitHub** | Repository and open-source project hosting |
| **PowerShell / Terminal** | Running, testing, and managing the application |
| **Python virtual environment** | Dependency isolation |
| **Gradio** | Local interactive application interface |

---

# 🧩 AI-Assisted Development Workflow

The development process combined human decisions with AI-assisted programming.

```text
        Project Idea
             ↓
      Architecture Design
             ↓
      AI-Assisted Coding
             ↓
        Local Testing
             ↓
       Error Debugging
             ↓
       Safety Review
             ↓
       Feature Refinement
             ↓
       Git + GitHub
             ↓
       Hackathon Demo
```

AI tools were used as **development assistants**, while the project's architecture, implementation decisions, testing, and final integration were reviewed and controlled during development.

---

# 📁 Project Structure

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

### Components

| File | Purpose |
|---|---|
| `app/main.py` | Gradio interface and agent workflow |
| `app/gemma.py` | Gemma 4 API integration and reasoning |
| `app/agent.py` | Safe allowlisted action execution |
| `assets/test_error.png` | Prepared debugging demonstration |
| `.env.example` | Environment configuration template |
| `.gitignore` | Prevents secrets and generated files from being committed |
| `requirements.txt` | Python dependencies |
| `LICENSE` | MIT license |

---

# ⚙️ Installation

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
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure the environment

Copy:

```text
.env.example
```

to:

```text
.env
```

Then configure:

```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMMA_MODEL=gemma-4-26b-a4b-it
```

### ⚠️ Security

Never commit `.env` or expose your API key publicly.

The repository's `.gitignore` is intended to prevent local secrets and virtual environments from being committed.

---

# ▶️ Run Polaris

```bash
python -m app.main
```

The Gradio interface will start locally.

---

# 🧪 Try Your Own Task

Provide a screenshot and a task such as:

```text
Why is this Python project failing?
Identify the cause and give me one safe fix.
```

Polaris will attempt to:

```text
Screenshot
     ↓
Gemma 4
     ↓
Diagnosis
     ↓
Action Plan
     ↓
Human Approval
     ↓
Allowlist Check
     ↓
Action
     ↓
Verification
```

---

# 🎯 Current MVP Scope

## Included

- [x] Gemma 4 integration
- [x] Multimodal screenshot analysis
- [x] Structured diagnosis
- [x] Action planning
- [x] Human approval
- [x] Safe action allowlist
- [x] Controlled action execution
- [x] Result verification
- [x] Gradio interface
- [x] Reproducible demo

## Can be Included

- [ ] Fully autonomous computer control
- [ ] Unrestricted shell execution
- [ ] Voice assistant
- [ ] Wake-word system
- [ ] IoT control
- [ ] Mobile application
- [ ] User accounts
- [ ] Cloud dashboard
- [ ] Large plugin marketplace

The MVP intentionally focuses on demonstrating one strong agent workflow rather than trying to solve every computer-control problem at once.

---

# 🔮 Roadmap

### MVP

- [x] Gemma 4 integration
- [x] Multimodal input
- [x] Reasoning
- [x] Action planning
- [x] Human approval
- [x] Allowlisted execution
- [x] Verification

---

# 🏆 Hackathon Pitch

### The Problem

Generic chatbots can explain errors.

### The Idea

Polaris uses Gemma 4 to understand visual computer context and reason about what should happen next.

### The Difference

Polaris adds:

```text
Plan
 ↓
Approve
 ↓
Act
 ↓
Verify
```

### 30-Second Pitch

> **"Generic chatbots can explain an error. Polaris understands the computer context around that error, plans a solution, asks for human approval, performs a safe action, and verifies the result."**

### In One Sentence

> **Polaris turns Gemma 4 from a chatbot into a safety-aware computer-assistance workflow.**

---

# 🌟 Why Polaris?

The project explores a progression in AI assistants:

```text
Chatbot
   ↓
Reasoning Assistant
   ↓
Agent
   ↓
Safe Computer Assistant
```

The goal is not to give AI unlimited control.

The goal is to give AI **useful capabilities with controlled permissions**.

Humans remain in the loop for important actions, while Gemma 4 handles tasks it is well suited for:

- Understanding
- Reasoning
- Planning
- Visual interpretation

---

# 🔒 Security Considerations

Polaris is currently a hackathon MVP.

The execution layer intentionally uses a narrow allowlist.

For production use, the architecture would need stronger:

- Permission management
- Sandboxing
- Command validation
- Process isolation
- Resource limits
- Audit logging
- Failure recovery
- Tool-specific security policies

The current implementation should **not** be treated as a complete production-grade computer-control security boundary.

---

# 🤝 Contributing

Contributions are welcome.

```bash
git checkout -b feature/my-feature
```

Make your changes, test them locally, then:

```bash
git add .
git commit -m "feat: add my feature"
git push origin feature/my-feature
```

Open a pull request on GitHub.

When adding new tools, preserve the project's safety principles:

- Explicit permissions
- Human approval where appropriate
- Input validation
- Restricted execution
- Verification

---

# 📜 License

This project is licensed under the **MIT License**.

See [`LICENSE`](LICENSE) for details.

---

# 👨‍💻 Project

## Polaris — Gemma 4 AI Computer Agent

Built for:

**October Fest — Best Use of Gemma 4**

Repository:

**https://github.com/brosploit/polaris-gemma-agent**

---

## ⭐ Support the Project

If you find Polaris interesting:

- ⭐ Star the repository
- 🍴 Fork the project
- 💡 Open an issue
- 🐛 Report bugs
- 🔧 Submit improvements
- 🤝 Contribute new safe tools

---

> **The chatbot gave you an answer. Polaris helps you move from understanding to action — safely.**
