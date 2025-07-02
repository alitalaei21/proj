from langgraph.graph import StateGraph, END
from node.input_node import input_node
from node.processing_node import processing_node
from node.recommendation_node import recommendation_node

class BusinessState(dict):
    pass

def build_graph():
    graph = StateGraph(dict)
    graph.add_node("input", input_node)
    graph.add_node("process", processing_node)
    graph.add_node("recommend", recommendation_node)

    graph.set_entry_point("input")
    graph.add_edge("input", "process")
    graph.add_edge("process", "recommend")
    graph.add_edge("recommend", END)

    return graph.compile()
