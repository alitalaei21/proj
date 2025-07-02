from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def recommendation_node(state):
    metrics = state["metrics"]

    prompt = f"""
You are a business analyst. Given the following metrics:
- Revenue today: {metrics['today_revenue']}
- Cost today: {metrics['today_cost']}
- Profit: {metrics['profit']}
- CAC today: {metrics['cac_today']:.2f}
- CAC yesterday: {metrics['cac_yesterday']:.2f}
- Revenue change: {metrics['revenue_change_pct']:.2f}%
- Cost change: {metrics['cost_change_pct']:.2f}%
Give 2-3 specific, useful business recommendations.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        raw = response.choices[0].message.content.split("\n")
        recommendations = [r.strip("-• ") for r in raw if r.strip()]
        state["recommendations"] = recommendations
    except Exception as e:
        state["recommendations"] = [f"Error generating recommendations: {str(e)}"]

    return state