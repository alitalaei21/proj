from graph import build_graph

sample_data = {
    "today": {"revenue": 1200, "cost": 800, "customers": 50},
    "yesterday": {"revenue": 1000, "cost": 700, "customers": 40}
}

def run_agent(data):
    graph = build_graph()
    result = graph.invoke(data)
    return result

if __name__ == "__main__":
    output = run_agent(sample_data)
    print("--- Agent Output ---")
    print(output)
