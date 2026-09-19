from agents import Agent
from config import REVIEWER_MODEL,CRITIC_MODEL
from prompts import Reviewer_prompt,Critic_prompt
from tools import fetch_pull_request_diff
from dataclasses import dataclass
from typing import Literal

@dataclass
class Evaluation_Feedback:
    """ Structured output from the critic agent"""
    feedback: str
    score:Literal['pass', 'needs_improvement']

Reviewer_Agent=Agent(
    name="Review Agent",
    instructions=Reviewer_prompt,
    tools=[fetch_pull_request_diff],
    model=REVIEWER_MODEL,
    
)

Critic_Agent=Agent(
    name="Critic Agent",
    instructions=Critic_prompt,
    model=CRITIC_MODEL,
    output_type=Evaluation_Feedback
)