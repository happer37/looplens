from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="System Loop Analyzer")


class AnalysisRequest(BaseModel):
    text: str


@app.post("/analyze")
def analyze_system_loop(request: AnalysisRequest) -> dict:
    text = request.text.lower()
    detected_loops: list[str] = []
    leverage_points: list[str] = []

    if "delay" in text or "slow" in text:
        detected_loops.append("Reinforcing loop: delays create slower responses, which increase delays")
        leverage_points.append("Reduce delays in information flow and decision-making")

    if "cost" in text or "price" in text:
        detected_loops.append("Balancing loop: higher costs trigger controls that push costs down")
        leverage_points.append("Improve cost feedback and pricing review cadence")

    if not detected_loops:
        detected_loops.append("General feedback loop: outcomes influence future actions")
        leverage_points.append("Clarify key feedback signals and response rules")

    summary = (
        f"Input highlights {len(detected_loops)} loop pattern(s). "
        "The system behavior can be improved by acting on the listed leverage points."
    )

    return {
        "detected_loops": detected_loops,
        "leverage_points": leverage_points,
        "summary": summary,
    }
