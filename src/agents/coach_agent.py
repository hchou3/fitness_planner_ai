from uagents import Agent, Context
from tools.models import UserStats, Confirmation, ProgramSuggestion, WorkoutPlan
from tools.protocols import fitness_protocol

# Initialize the coach agent
coach_agent = Agent(
    name="coach_agent",
    seed="coach phrase",  # Change to a unique seed
    port=8002,
    endpoint=["http://localhost:8002/submit"]
)
