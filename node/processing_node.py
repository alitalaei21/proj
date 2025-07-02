

def processing_node(state):
    today = state['today']
    yesterday = state['yesterday']

    revenue_today = today['revenue']
    cost_today = today['cost']
    customers_today = today["customers"]

    revenue_yesterday = yesterday['revenue']
    cost_yesterday = yesterday['cost']
    customers_yesterday = yesterday["customers"]

    profit = revenue_today - cost_today

    cac_today = cost_today / max(customers_today, 1)
    cac_yesterday = cost_yesterday / max(customers_yesterday, 1)

    rcp = ((revenue_today - revenue_yesterday) / revenue_yesterday) * 100 if revenue_yesterday > 0 else 0

    ccp = ((cost_today - cost_yesterday) / cost_yesterday) * 100 if cost_yesterday > 0 else 0
    cac_increase_pct = ((cac_today - cac_yesterday) / max(cac_yesterday, 1)) * 100
    alerts = []
    if profit < 0:
        alerts.append("Profit is negative.")
    if cac_increase_pct > 20:
        alerts.append("CAC increased more than 20%.")

    state["metrics"] = {
        "profit": profit,
        "today_revenue": revenue_today,
        "today_cost": cost_today,
        "cac_today": cac_today,
        "cac_yesterday": cac_yesterday,
        "revenue_change_pct": rcp,
        "cost_change_pct": ccp,
    }
    state["status"] = "profit" if profit >= 0 else "loss"
    state["alerts"] = alerts
    return state
    
