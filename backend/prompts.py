"""Level + detail prompt templates."""
LEVEL_GUIDE = {
    "primary": "Explain for a 10-year-old. Use simple words, no equations, one everyday analogy.",
    "secondary": "Explain for a high-school student. Introductory terms allowed, simple equations OK, one worked example.",
    "university": "Explain for an undergraduate. Full technical terms, include equations if present, one applied example.",
    "public": "Explain for an educated general audience. No jargon, no equations, use a real-world analogy.",
}

DETAIL_GUIDE = {
    "brief": "Keep to 2-3 bullet points. No examples.",
    "standard": "Use 4-6 bullet points. Include one example or analogy.",
    "deep": "Use 6-8 bullet points. Include definition, mechanism, and one worked example. If an equation appears, include it in LaTeX.",
}

SYSTEM_PROMPT = """You generate presentation overlay slides in Markdown.
Output ONLY the slide content, no preamble. Format:

# <Short headline, max 8 words>

<Body per instructions>

Keep total content readable on one slide. Do not include meta-commentary."""


def build_user_prompt(text: str, level: str, detail: str) -> str:
    return f"""Source text from the presentation document:

---
{text}
---

Audience: {LEVEL_GUIDE[level]}
Depth: {DETAIL_GUIDE[detail]}

Generate one overlay slide for this text."""
