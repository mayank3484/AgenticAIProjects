from config import BASE_URL, MAX_ITERATIONS
from agent_definitions import Reviewer_Agent, Critic_Agent,Evaluation_Feedback
from openai import AsyncOpenAI
import os
from agents import Runner, set_default_openai_client, set_tracing_disabled
import logging
from rich.console import Console
from rich.markdown import Markdown
from prompts import Critic_User

logger=logging.getLogger(__name__)

ollama_client=AsyncOpenAI(
    base_url=BASE_URL,
    api_key="ollama"
)
set_default_openai_client(ollama_client)
set_tracing_disabled(True)

def validate_env_variables():
    if os.getenv("REVIEWER_MODEL") is None: raise Exception("Reviewer Model is missing in .env file")
    if os.getenv("CRITIC_MODEL") is None: raise Exception("Critic Model is missing in .env file")
    if os.getenv("BASE_URL") is None: raise Exception("Base url is missing in .env file")

validate_env_variables()
console=Console()
while True:
    user_input=input("enter pr url> ")
    if user_input in ["exit" or "quit"]:
        break
    iteration=1
    while iteration<MAX_ITERATIONS:
        input_items=[
            {'role':'user','content':f"Fetch and review the pull request at {user_input}"}
        ]
        logger.info(f"[Reviewer] generating the code review")
        review_result=Runner.run_sync(Reviewer_Agent,input_items)
        console.print(Markdown(review_result.final_output))
        console.print("-" * 80)
        input_items=review_result.to_input_list()
        critic_input=Critic_User.format(
            diff="(see the conversation to find the diff)",
            review=review_result.final_output
        )
        input_items.append({
            'role':'user','content':critic_input
        })
        logger.info(f"[Critic] generating the code review")
        critic_result=Runner.run_sync(
            Critic_Agent,input_items
        )
        result:Evaluation_Feedback=critic_result.final_output
        console.print(f"score={result.score}")
        if result.score =='pass':
            break

        if iteration==MAX_ITERATIONS:
            break
        iteration+=1

    console.print("-- final response --")
    console.print(Markdown(result.feedback))

