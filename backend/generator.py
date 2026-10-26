"""Generate overlay slides via LLM."""
from openai import OpenAI
from backend.config import OPENAI_API_KEY, OPENAI_BASE_URL, MODEL
from backend.prompts import SYSTEM_PROMPT, build_user_prompt

client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)


def generate_overlay(text: str, level: str, detail: str) -> str:
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(text, level, detail)},
        ],
        temperature=0.4,
        max_tokens=600,
    )
    return resp.choices[0].message.content.strip()
