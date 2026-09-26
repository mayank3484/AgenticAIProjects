from agents import Agent,Runner, set_default_openai_client, set_tracing_disabled, function_tool
from openai import AsyncOpenAI
from config import LLM_MODEL
from vectorstore import vector_store

client=AsyncOpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)
set_default_openai_client(client)
set_tracing_disabled(True)

@function_tool
def load_knowledge(user_query:str):
    """
    description: use to retrieve knowledge from knowledge base
    argument: user query
    return: knowledge requires to return the query"""
    vs=vector_store()
    docs=vs.similarity_search(
        query=user_query,k=5
    )
    result=[]
    for doc in docs:
        result.append(doc.page_content)
    return result

def main():
    agent=Agent(
        name="Rag  Agent",
        model=LLM_MODEL,
        instructions="""
        You are a helpful assistant and have a tool access of load_knowledge.
        Use this tool to answer user's query.

        Do Not Use your own knowledge to answer user's query.
        If knowledge is not sufficient then say: i don't know.
        Never hallucinate the information.
        """,
        tools=[load_knowledge]
    )
    while True:
        user_query=input("> ")
        if user_query in ["exit" or "quit"]:
            break
        response=Runner.run_sync(
            starting_agent=agent,
            input=user_query
        )
        print(f"[agent]> {response.final_output}")
        print("")
if __name__ =='__main__':
    main()




