from ai_engine import UAgentResponse, UAgentResponseType
from uagents import Context, Protocol, Agent
import requests
import json

agent = Agent(name="fit_generator", seed="YOUR NEW PHRASE", port=8000, endpoint=["http://localhost:8000/submit"])


class GetUserDetails:
    uid: int
    age: int
    weight: float
    height: float
    unit: str
    activity: str
    years: int
    
    
generate_fitness_plan = Protocol("Get User Details")

@generate_fitness_plan.on_message(model = GetUserDetails, replies=UAgentResponse)
async def get_user_details(ctx: Context, sender: str, msg: GetUserDetails) -> UAgentResponse:
    ctx.logger.info("User details: \n name: %s \n age: %s \n weight: %s \n height: %s \n unit: %s \n activity: %s \n years: %s", msg.uid, msg.age, msg.weight, msg.height, msg.unit, msg.activity, msg.years)
    ctx.logger.info("Sender: %s", sender)

    message = f"<a href='{msg.uid}'>YOUR FITNESS INFO: \n age:{msg.age}, \n age:{msg.age}, \n weight:{msg.weight}, \n height:{msg.height}</a>"
    await ctx.send(sender, UAgentResponse(message=message, type=UAgentResponseType.FINAL))


if __name__ == "__main__":
    agent.include(generate_fitness_plan)
    agent.run()
 