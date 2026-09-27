from mcp.server.fastmcp import FastMCP
from mcp.server.auth.provider import TokenVerifier,AccessToken
from mcp.server.auth.settings import AuthSettings

from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client, get_default_environment
from config import SECRET,ALGORITHM, PSQL_DB,PSQL_HOST,PSQL_PASSWORD,PSQL_PORT,PSQL_USER
import jwt
from langchain.chat_models import init_chat_model

model=init_chat_model(model="llama3.2:3b",model_provider="ollama")
MCP_URL="http://localhost:8600/mcp"

class JWTTokenVerifier(TokenVerifier):
    async def verify_token(self, token:str):
        try:
            payload=jwt.decode(token,SECRET,algorithms=[ALGORITHM],audience="mcp_demo")
            return AccessToken(
                token=token,
                client_id="mcp-client",
                subject=payload["sub"],
                scopes=payload["permissions"],
                resource=MCP_URL,
                claims=payload
            )
        except Exception as e:
            print(f"Exception occurred: {e}")
            return None

MCP=FastMCP(
    name="MCP Demo",
    token_verifier=JWTTokenVerifier(),
    auth=AuthSettings(
        issuer_url="http://localhost:8001",
        resource_server_url=MCP_URL,
        required_scopes=["products:read"],
        validate_token_resource=True
    ),
    json_response=True,
    port=8600,
    host="0.0.0.0",
)

async def execute_query(query:str):
    env=get_default_environment()
    env.update(
        {
            "PSQL_USER":PSQL_USER,
            "PSQL_PASSWORD":PSQL_PASSWORD,
            "PSQL_DB":PSQL_DB,
            "PSQL_HOST":PSQL_HOST,
            "PSQL_PORT":PSQL_PORT
        }
    )
    parameters=StdioServerParameters(command="postgres-mcp-server",env=env)
    async with stdio_client(parameters) as (read,write):
        async with ClientSession(read_stream=read,write_stream=write) as session:
            await session.initialize()
            result=await session.call_tool("exexute_sql",{"query":query})
    text=result.content[0].text if result.content else ""

    return text

@MCP.tool(title="Get the list of products")
async def get_list_of_products():
    """Get the list of products"""
    query="select * from products"
    result=await execute_query(query)
    return result

if __name__ =='__main__':
    MCP.run(transport="streamable-http")