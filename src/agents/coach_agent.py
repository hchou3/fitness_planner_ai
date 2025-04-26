from uagents import Agent, Context
from tools.models import UserStats, Confirmation, ProgramSuggestion, WorkoutPlan
from tools.protocols import fitness_protocol
import httpx
from tools.db import init_db, save_user_stats, get_user_stats
init_db()

coach_agent = Agent(
    name="coach_agent",
    seed="coach phrase",
    port=8002,
    endpoint=["http://localhost:8002/submit"]
)

@fitness_protocol.on_message(model=UserStats)
async def handle_user_stats(ctx: Context, sender: str, stats: UserStats):
    save_user_stats(sender, stats)
    ctx.logger.info(f"[coach_agent] Received and saved user stats from {sender}")


@fitness_protocol.on_message(model=Confirmation)
async def handle_confirmation(ctx: Context, sender: str, confirmation: Confirmation):
    ctx.logger.info(f"[coach_agent] Received confirmation from {sender}: {confirmation.accepted}")
    
    user = get_user_stats(sender)
    if not user:
        ctx.logger.warning("User stats not found. Cannot proceed.")
        return

    if confirmation.accepted:
        plan = await generate_workout_plan(user)
        await ctx.send(sender, plan)
        ctx.logger.info(f"[coach_agent] Sent workout plan to {sender}")
    else:
        response = "Could you please specify what you'd like to adjust or provide more detail?"
        await ctx.send(sender, Confirmation(accepted=False, additional_info=response))
        ctx.logger.info(f"[coach_agent] Requested more info from {sender}")

async def generate_workout_plan(user: UserStats) -> WorkoutPlan:
    payload = {
        "age": user.age,
        "height": user.height,
        "weight": user.weight,
        "activity": user.activity,
        "goal": user.goal
    }

    try:
        async with httpx.AsyncClient() as client:
            res = await client.post("http://localhost:8001/generate-plan", json=payload)
            res.raise_for_status()
            plan_text = res.json()["plan"]
    except Exception as e:
        plan_text = f"Error generating plan: {str(e)}"

    return WorkoutPlan(
        title="Your AI-Generated Plan",
        details=plan_text
    )

if __name__ == "__main__":
    coach_agent.run()
