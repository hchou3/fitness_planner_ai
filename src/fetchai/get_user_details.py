from uagents import Context, Protocol, Agent, Model

class Message(Model):
    message : str

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



initial_agent = Agent(name="fit_generator", seed="YOUR NEW PHRASE", port=8000, endpoint=["http://localhost:8000/submit"])   
generate_fitness_plan = Protocol("Get User Details")

@initial_agent.on_message(model = Message)
def generate_fitness_plan(message: Message):
    print(f"Received message: {message.message}")

    response = f"The user's body statistics and history of atheltic activity: {message.message}"
    return response

context = Context(agent="fit_generator", protocol="Get User Details")



 
if __name__ == "__main__":
    initial_agent.include(generate_fitness_plan)
    initial_agent.run()
 