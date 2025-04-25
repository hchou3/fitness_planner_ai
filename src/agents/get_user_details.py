# get_user_details.py

from uagents import Agent, Context, Protocol, Model
from pydantic import BaseModel
from tools.models import UserStats, ProgramSuggestion
from tools.protocols import fitness_protocol

user_input = UserStats(
    age=28,
    height=175.0,
    weight=70.0,
    unit="metric",
    activity="gym",
    goal="lose 10 pounds over a period of 12 weeks, gain visible abdominal muscles"
)

user_agent = Agent(
    name="user_agent",
    seed="user phrase",
    port=8000,
    endpoint=["http://localhost:8000/submit"]
)

@user_agent.on_event("startup")
async def send_user_data(ctx: Context):
    planner_address = "planner_agent_address_here"  
    await ctx.send(planner_address, user_input)

@fitness_protocol.on_message(model=ProgramSuggestion)
async def receive_program(ctx: Context, sender: str, suggestion: ProgramSuggestion):
    ctx.logger.info(f"Received suggestion: {suggestion.summary}")
    from tools.models import Confirmation
    confirmation = Confirmation(accepted=True)
    await ctx.send("coach_agent_address_here", confirmation)

user_agent.include(fitness_protocol)

if __name__ == "__main__":
    user_agent.run()

 