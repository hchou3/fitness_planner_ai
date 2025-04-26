# get_user_details.py

from uagents import Agent, Context, Protocol, Model
from tools.models import UserStats, ProgramSuggestion
from tools.protocols import fitness_protocol
from tools.models import Confirmation


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
    planner_address = "agent1q24lj3f0kz3cuy3uksh33erzsh0vs00pvh4y0vfcxxeqxjfaxktw2y9y7qk"  
    await ctx.send(planner_address, user_input)

@fitness_protocol.on_message(model=ProgramSuggestion)
async def receive_program(ctx: Context, sender: str, suggestion: ProgramSuggestion):
    ctx.logger.info(f"Received suggestion: {suggestion.summary}")
    from tools.models import Confirmation
    confirmation = Confirmation(accepted=True)
    await ctx.send("coach_agent_address_here", confirmation)

@fitness_protocol.on_message(model=Confirmation)
async def handle_additional_info_request(ctx: Context, sender: str, confirmation: Confirmation):
    if not confirmation.accepted:
        ctx.logger.info(f"Coach asked for more info: {confirmation.additional_info}")


        updated_input = UserStats(
            age=28,
            height=175.0,
            weight=70.0,
            unit="metric",
            activity="gym + yoga 3x/week",
            goal="lose 10 pounds over 12 weeks with focus on core strength and visible abs"
        )

        await ctx.send(sender, updated_input)

user_agent.include(fitness_protocol)

if __name__ == "__main__":
    user_agent.run()

 