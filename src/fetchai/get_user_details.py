from uagents import Context, Protocol, Agent

class GetUserDetails:
    def get_user_stats(uid: int, age: int, unit: str, weight: float, height: float, activity: str, years: int):
        stats = {
            "uid": uid,
            "age": age,
            "unit": unit,
            "weight": weight,
            "height": height,
            "activity": activity,
            "years": years
        }


agent = Agent(name="fit_generator", seed="YOUR NEW PHRASE", port=8000, endpoint=["http://localhost:8000/submit"])   
generate_fitness_plan = Protocol("Get User Details")



 
 
if __name__ == "__main__":
    agent.include(generate_fitness_plan)
    agent.run()
 