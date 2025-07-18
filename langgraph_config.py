from langgraph.graph import StateGraph, END

# Import your Gemini-powered agent functions
from agents.carbon_calc import carbon_calc_agent
from agents.health_analyzer import health_analyzer_agent
from agents.eco_advizer import eco_advisor_agent
from agents.mental_wellness import mental_wellness_agent
from agents.goalplanner import goal_planner_agent

def get_greenpath_graph():
    # Define the graph and its state (dict = our data format)
    graph = StateGraph(dict)

    # Add nodes (each AI Agent is a node)
    graph.add_node("CarbonCalc", carbon_calc_agent)
    graph.add_node("HealthAnalyzer", health_analyzer_agent)
    graph.add_node("EcoAdvisor", eco_advisor_agent)
    graph.add_node("MentalWellness", mental_wellness_agent)
    graph.add_node("GoalPlanner", goal_planner_agent)

    # Define the flow (edges between agents)
    graph.set_entry_point("CarbonCalc")  # Start here
    graph.add_edge("CarbonCalc", "HealthAnalyzer")
    graph.add_edge("HealthAnalyzer", "EcoAdvisor")
    graph.add_edge("EcoAdvisor", "MentalWellness")
    graph.add_edge("MentalWellness", "GoalPlanner")
    graph.add_edge("GoalPlanner", END)

    # Return compiled graph (usable in app.py and main.py)
    return graph.compile()
