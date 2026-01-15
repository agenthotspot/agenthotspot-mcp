from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_cerebras import ChatCerebras
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    # Setup MCP client config
    client = MultiServerMCPClient({
        "agenthotspot": {
            "transport": "stdio",
            "command": "python3",
            "args": ["-m", "agenthotspot_mcp"],
            "env": {}
        }
    })

    # Initialize LLM and agent
    tools = await client.get_tools()
    
    # Replace with llm client of choice 
    # Make sure to set CEREBRAS_API_KEY=... in .env environment file.
    llm = ChatCerebras(model="gpt-oss-120b", temperature=0.6) 
    agent = create_react_agent(llm, tools)

    # Invoke agent and output response with insights
    response = await agent.ainvoke({
        "messages": [{"role": "user", "content": "Find memory related MCPs."}],
    })

    print(response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())