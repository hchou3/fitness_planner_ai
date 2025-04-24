from uagents import Context, Protocol, Agent, Model
import ai_engine

class Message(Model):
    message : str

class UserDetails(Model):
    uid: str
    age: str
    unit: str
    weight: str
    height: str
    activity: str
    years: str
    goal: str

initial_agent = Agent(name="fit_generator", seed="YOUR NEW PHRASE", port=8000, endpoint=["http://localhost:8000/submit"])   
generate_fitness_plan = Protocol("Get User Details")

@initial_agent.on_message(model = UserDetails, protocol = generate_fitness_plan)
def generate_fitness_plan(message: UserDetails):
    print(f"Received message: {message.message}")

    response = f"The user's body statistics and history of atheltic activity: {message.message}"
    return response

context = Context(agent="fit_generator", protocol="Get User Details")



 
if __name__ == "__main__":
    initial_agent.include(generate_fitness_plan)
    initial_agent.run()
 