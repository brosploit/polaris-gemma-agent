import os
import json

from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load environment variables from .env
load_dotenv()

# Gemma model
MODEL = os.getenv("GEMMA_MODEL", "gemma-4-26b-a4b-it")


SYSTEM_PROMPT = """You are Polaris, a safe multimodal computer assistant.

Analyze the user's screenshot and/or text.

Return ONLY valid JSON using exactly these fields:
{
  "diagnosis": "concise diagnosis",
  "plan": "numbered safe action plan",
  "risk": "explain whether human approval is needed",
  "suggested_action": "one narrow safe action, or none"
}

Safety rules:
- Never request secrets, passwords, API keys, or tokens.
- Never suggest destructive commands.
- Never delete files.
- Never modify system-critical files.
- Never claim that an action was executed.
- Human approval is required before any action is executed.
- If uncertain, say so.
"""


def _create_client():
    """Create a fresh Google GenAI client."""
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. "
            "Add your API key to the .env file."
        )

    return genai.Client(api_key=api_key)


def analyze_task(image_path=None, task=""):
    """
    Analyze a screenshot and/or user-described problem with Gemma.
    """

    parts = [
        SYSTEM_PROMPT,
        f"User task: {task.strip() if task else '(not provided)'}",
    ]

    # Add screenshot if provided
    if image_path:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()

        extension = os.path.splitext(image_path)[1].lower()

        if extension == ".png":
            mime_type = "image/png"
        elif extension in [".jpg", ".jpeg"]:
            mime_type = "image/jpeg"
        elif extension == ".webp":
            mime_type = "image/webp"
        else:
            mime_type = "image/png"

        parts.insert(
            0,
            types.Part.from_bytes(
                data=image_data,
                mime_type=mime_type,
            ),
        )

    client = _create_client()

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=parts,
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            ),
        )

        raw_response = response.text or ""

    finally:
        # Explicitly close this client after the request.
        client.close()

    # Parse Gemma's JSON response
    try:
        data = json.loads(raw_response)

    except json.JSONDecodeError:
        data = {
            "diagnosis": raw_response or "Gemma returned an empty response.",
            "plan": "Review the model response manually.",
            "risk": "Human review required.",
            "suggested_action": "none",
        }

    return {
        "diagnosis": (
            "### Diagnosis\n"
            + str(data.get("diagnosis", "Unknown"))
        ),
        "plan": (
            "### Plan\n"
            + str(data.get("plan", "No plan returned."))
        ),
        "risk": (
            "### Approval\n"
            + str(data.get("risk", "Human approval required."))
        ),
        "suggested_action": data.get(
            "suggested_action",
            "none",
        ),
    }


def verify_with_gemma(output, diagnosis):
    """
    Ask Gemma to verify whether the tool output
    appears to resolve the diagnosed issue.
    """

    prompt = f"""You are verifying a computer-agent action.

Diagnosis:
{diagnosis}

Tool output:
{output}

Return a concise verification result.

Rules:
- Do not invent facts.
- Only use information present in the diagnosis and tool output.
- Clearly state whether the result appears successful, unsuccessful, or uncertain.
"""

    client = _create_client()

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
        )

        return response.text or "Verification returned no response."

    finally:
        client.close()