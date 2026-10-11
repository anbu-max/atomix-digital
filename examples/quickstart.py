"""Atomix Agent Core - Quickstart Example."""

import os
from dotenv import load_dotenv
from atomix_core import AtomixAgent, AgentRouter, AgentConfig

load_dotenv()

def main():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("[!] Note: Set ANTHROPIC_API_KEY in your environment to make live API calls.")
        print("[+] Initializing Atomix Multi-Agent Router demonstration mode...")

    # Create specialized agents
    analyst = AtomixAgent(
        config=AgentConfig(
            name="code_analyst",
            model="claude-3-5-sonnet-20241022",
            system_prompt="You are an expert software architect analyzing code bases."
        ),
        api_key=api_key or "demo-key"
    )

    router = AgentRouter()
    router.register_agent(analyst)

    print(f"Registered agents: {router.list_agents()}")
    print("Ready to route autonomous tasks with Claude 3.5 Sonnet.")

if __name__ == "__main__":
    main()
