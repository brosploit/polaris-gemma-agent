import gradio as gr
from dotenv import load_dotenv

load_dotenv()

from app.gemma import analyze_task
from app.agent import execute_plan, verify_result


# ============================================================
# POLARIS PIPELINE
# ============================================================

def make_pipeline(active=0, completed=0):
    labels = [
        "Perceive",
        "Understand",
        "Reason",
        "Plan",
        "Verify",
    ]

    output = []

    for i, label in enumerate(labels):
        if i < completed:
            icon = "✓"
            cls = "done"
        elif i == active:
            icon = "●"
            cls = "active"
        else:
            icon = "○"
            cls = "pending"

        output.append(
            f"""
            <div class="stage {cls}">
                <span class="stage-icon">{icon}</span>
                <span>{label}</span>
            </div>
            """
        )

    return "\n".join(output)


# ============================================================
# GEMMA ANALYSIS
# ============================================================

def analyze(image, task):

    if not image and not task.strip():
        return (
            "⚠️ Please upload a screenshot or describe the problem.",
            "",
            "",
            make_pipeline(0, 0),
            0,
            "Waiting for input...",
        )

    try:

        result = analyze_task(
            image_path=image,
            task=task,
        )

        return (
            result["diagnosis"],
            result["plan"],
            result["risk"],
            make_pipeline(3, 3),
            60,
            "✓ Gemma 4 analysis complete — waiting for human approval.",
        )

    except Exception as e:

        return (
            f"### ❌ Analysis Error\n\n`{e}`",
            "",
            "",
            make_pipeline(0, 0),
            0,
            f"❌ Analysis failed: {e}",
        )


# ============================================================
# SAFE ACTION EXECUTION
# ============================================================

def run_action(plan):

    if not plan:

        return (
            "⚠️ No approved action available.",
            "",
            make_pipeline(3, 3),
            60,
            "⚠️ Nothing to execute.",
        )

    try:

        result = execute_plan(plan)

        return (
            result["message"],
            result["output"],
            make_pipeline(4, 4),
            80,
            "⚙️ Approved action executed — ready for verification.",
        )

    except Exception as e:

        return (
            f"❌ Action execution failed: `{e}`",
            str(e),
            make_pipeline(3, 3),
            60,
            f"❌ Action failed: {e}",
        )


# ============================================================
# VERIFICATION
# ============================================================

def verify(output, diagnosis):

    if not output:

        return (
            "⚠️ No tool output available for verification.",
            make_pipeline(4, 4),
            80,
            "Waiting for an action result...",
        )

    try:

        result = verify_result(
            output,
            diagnosis,
        )

        return (
            result,
            make_pipeline(4, 5),
            100,
            "✓ Verification complete — task pipeline finished.",
        )

    except Exception as e:

        return (
            f"⚠️ Verification error: `{e}`",
            make_pipeline(4, 4),
            80,
            f"Verification failed: {e}",
        )


# ============================================================
# DEMO LOADER
# ============================================================

def load_demo():

    return (
        "assets/test_error.png",
        "Why is this Python project failing? Identify the cause and give me one safe fix.",
        "⚡ Demo loaded. Click **Analyze with Gemma 4**.",
    )


# ============================================================
# CUSTOM CSS
# ============================================================

CSS = """

/* ---------- GLOBAL ---------- */

body {
    background: #070b14 !important;
}

.gradio-container {
    max-width: 1450px !important;
    margin: auto !important;

    background:
        radial-gradient(
            circle at 10% 0%,
            rgba(70, 90, 255, .10),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(0, 220, 255, .08),
            transparent 30%
        ),
        #070b14 !important;

    color: #e8eefc !important;
}


/* ---------- HEADER ---------- */

#header {
    padding: 28px 10px 18px 10px;
}

.brand {
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -1px;
}

.subtitle {
    color: #8793aa;
    font-size: 15px;
    margin-top: 4px;
}

.badge {
    display: inline-block;

    padding: 7px 13px;

    border-radius: 999px;

    background: rgba(40, 220, 140, .10);

    border: 1px solid rgba(40, 220, 140, .30);

    color: #61e6a4;

    font-size: 13px;

    font-weight: 700;

    margin-top: 12px;
}


/* ---------- CARDS ---------- */

.card {
    background: rgba(15, 22, 38, .86);

    border: 1px solid #202b42;

    border-radius: 16px;

    padding: 20px;

    box-shadow:
        0 10px 35px rgba(0, 0, 0, .22);
}

.card-title {
    font-size: 14px;

    font-weight: 800;

    letter-spacing: .8px;

    text-transform: uppercase;

    color: #8fa1bd;

    margin-bottom: 12px;
}


/* ---------- PIPELINE ---------- */

.pipeline {
    display: flex;

    justify-content: space-between;

    gap: 8px;

    margin: 8px 0 18px 0;
}

.stage {
    flex: 1;

    text-align: center;

    padding: 13px 6px;

    border-radius: 10px;

    background: #0c1220;

    border: 1px solid #1d2940;

    font-size: 12px;

    font-weight: 700;
}

.stage-icon {
    display: block;

    font-size: 18px;

    margin-bottom: 5px;
}

.stage.done {
    border-color: rgba(75, 225, 160, .35);

    color: #61e6a4;
}

.stage.active {
    border-color: rgba(100, 150, 255, .55);

    color: #8bb1ff;

    box-shadow:
        0 0 18px rgba(80, 120, 255, .12);
}

.stage.pending {
    color: #5e6b82;
}


/* ---------- BUTTONS ---------- */

.approve-btn {
    min-height: 58px !important;

    font-size: 17px !important;

    font-weight: 800 !important;

    border-radius: 13px !important;
}

.demo-btn {
    border-radius: 10px !important;
}


/* ---------- INPUTS ---------- */

textarea,
input {
    background: #0b1120 !important;

    border-color: #202d46 !important;
}


/* ---------- CODE OUTPUT ---------- */

pre {
    border-radius: 12px !important;
}


/* ---------- HIDE FOOTER ---------- */

footer {
    display: none !important;
}

"""


# ============================================================
# GRADIO APPLICATION
# ============================================================

with gr.Blocks(
    title="Polaris — Gemma 4 Agent",
) as demo:

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    gr.HTML(
        """
        <div id="header">

            <div class="brand">
                ✦ POLARIS
            </div>

            <div class="subtitle">
                Multimodal AI Computer Agent
                · Perceive · Reason · Act · Verify
            </div>

            <div class="badge">
                ● GEMMA 4 ONLINE
            </div>

        </div>
        """
    )


    # --------------------------------------------------------
    # AGENT PIPELINE
    # --------------------------------------------------------

    pipeline = gr.HTML(
        value=f"""
        <div class="pipeline">
            {make_pipeline(0, 0)}
        </div>
        """,
        elem_classes=["card"],
    )


    progress = gr.Slider(
        minimum=0,
        maximum=100,
        value=0,
        step=1,
        label="Agent progress",
        interactive=False,
    )


    status = gr.Markdown(
        "### 🟢 Ready\nUpload a screenshot or describe a problem."
    )


    # --------------------------------------------------------
    # MAIN WORKSPACE
    # --------------------------------------------------------

    with gr.Row():

        # ====================================================
        # LEFT — COMPUTER CONTEXT
        # ====================================================

        with gr.Column(scale=1):

            gr.HTML(
                """
                <div class="card-title">
                    📸 COMPUTER CONTEXT
                </div>
                """
            )

            image = gr.Image(
                type="filepath",
                label="Screenshot",
                height=330,
            )

            task = gr.Textbox(
                label="What are you trying to do?",

                placeholder=(
                    "Example: Why is this Python project failing?"
                ),

                lines=4,
            )


            with gr.Row():

                analyze_btn = gr.Button(
                    "✦ ANALYZE WITH GEMMA 4",

                    variant="primary",

                    size="lg",
                )

                demo_btn = gr.Button(
                    "⚡ DEMO",

                    variant="secondary",

                    elem_classes=["demo-btn"],
                )


        # ====================================================
        # RIGHT — GEMMA REASONING
        # ====================================================

        with gr.Column(scale=1):

            gr.HTML(
                """
                <div class="card-title">
                    🧠 GEMMA 4 REASONING
                </div>
                """
            )

            diagnosis = gr.Markdown(
                "Waiting for analysis..."
            )

            plan = gr.Markdown(
                "Your action plan will appear here."
            )

            risk = gr.Markdown(
                "Safety assessment will appear here."
            )


    # --------------------------------------------------------
    # HUMAN APPROVAL
    # --------------------------------------------------------

    gr.Markdown("---")


    gr.HTML(
        """
        <div class="card-title">
            🛡️ HUMAN APPROVAL GATE
        </div>

        <div style="
            color:#8793aa;
            margin-bottom:12px;
        ">
            Polaris will only execute actions that pass its
            safe-action allowlist after explicit human approval.
        </div>
        """
    )


    approve = gr.Button(
        "🛡️ APPROVE & EXECUTE",

        variant="primary",

        size="lg",

        elem_classes=["approve-btn"],
    )


    action_msg = gr.Markdown(
        "No action has been executed."
    )


    action_output = gr.Code(
        label="Tool output",

        language="shell",
    )


    # --------------------------------------------------------
    # VERIFICATION
    # --------------------------------------------------------

    gr.Markdown("---")


    gr.HTML(
        """
        <div class="card-title">
            🔎 VERIFICATION
        </div>
        """
    )


    verify_btn = gr.Button(
        "✓ VERIFY RESULT",

        variant="secondary",

        size="lg",
    )


    verification = gr.Markdown(
        "Verification will appear here."
    )


    # ========================================================
    # BUTTON EVENTS
    # ========================================================

    demo_btn.click(
        load_demo,

        outputs=[
            image,
            task,
            status,
        ],
    )


    analyze_btn.click(
        analyze,

        inputs=[
            image,
            task,
        ],

        outputs=[
            diagnosis,
            plan,
            risk,
            pipeline,
            progress,
            status,
        ],
    )


    approve.click(
        run_action,

        inputs=[
            plan,
        ],

        outputs=[
            action_msg,
            action_output,
            pipeline,
            progress,
            status,
        ],
    )


    verify_btn.click(
        verify,

        inputs=[
            action_output,
            diagnosis,
        ],

        outputs=[
            verification,
            pipeline,
            progress,
            status,
        ],
    )


# ============================================================
# LAUNCH
# ============================================================

if __name__ == "__main__":

    demo.launch(
        css=CSS,
        theme=gr.themes.Base(
            primary_hue="blue",
            neutral_hue="slate",
        ),
    )
