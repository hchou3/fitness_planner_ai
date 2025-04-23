from uagents import Context, Protocol, Agent, Model
import json
import requests

class Message(Model):
    message : str

