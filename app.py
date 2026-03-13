from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="System Loop Analyzer")


class AnalyzeRequest(BaseModel):
    text: str


@app.post("/analyze")
def analyze_loop(request: AnalyzeRequest) -> dict:
    words = [word.strip(".,!?;:").lower() for word in request.text.split() if word.strip()]
    unique_words = sorted(set(words))

    key_variables = unique_words[:5] if unique_words else ["input"]

    if "delay" in words or "slow" in words:
        leverage_point = "Reduce delays in feedback and response timing"
    elif "cost" in words or "price" in words:
        leverage_point = "Adjust incentives around pricing and cost signals"
    else:
        leverage_point = "Improve feedback quality between cause and effect"

    system_loop = (
        "Inputs influence behavior, behavior changes outcomes, and outcomes "
        "feed back to influence future inputs."
    )

    return {
        "system_loop": system_loop,
        "key_variables": key_variables,
        "leverage_point": leverage_point,
    }
