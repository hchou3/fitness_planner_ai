import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)
load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"))

@app.route("/generate-plan", methods=["POST"])
def generate_plan():
    data = request.get_json()
    age = data.get("age")
    height = data.get("height")
    weight = data.get("weight")
    activity = data.get("activity")
    goal = data.get("goal")

    prompt = f"""
    Create a personalized fitness program for a user with:
    - Age: {age}
    - Height: {height}
    - Weight: {weight}
    - Activity: {activity}
    - Goal: {goal}

    Provide a weekly plan summary and estimated time to reach the goal.
    Include a breakdown of exercises, nutrition, and any other relevant information.
    Make sure to consider the user's activity, which can be their sport of choice or a specific type of exercise.
    The plan should be realistic and achievable, taking into account the user's current fitness level and any potential limitations.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4.0-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        plan_text = response.choices[0].message.content
        return jsonify({"plan": plan_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
