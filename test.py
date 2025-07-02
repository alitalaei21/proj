from main import run_agent

def test_profit_case():
    data = {
        "today": {"revenue": 1500, "cost": 900, "customers": 50},
        "yesterday": {"revenue": 1200, "cost": 800, "customers": 40}
    }
    output = run_agent(data)
    assert output["status"] == "profit"
    assert output["profit"] > 0
    assert len(output["alerts"]) == 0
    assert len(output["recommendations"]) > 0

def test_loss_alert_case():
    data = {
        "today": {"revenue": 400, "cost": 700, "customers": 20},
        "yesterday": {"revenue": 600, "cost": 600, "customers": 40}
    }
    output = run_agent(data)
    assert output["status"] == "loss"
    assert output["profit"] < 0
    assert len(output["alerts"]) >= 1
    assert len(output["recommendations"]) > 0

if __name__ == "__main__":
    test_profit_case()
    test_loss_alert_case()
    print("All tests passed!")