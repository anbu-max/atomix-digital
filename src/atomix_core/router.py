"""Multi-agent orchestrator and dispatcher."""

from typing import Dict, List
from .client import AtomixAgent
from .types import AgentConfig, AgentResponse


class AgentRouter:
    """Dispatches tasks across specialized Claude agents."""

    def __init__(self):
        self.agents: Dict[str, AtomixAgent] = {}

    def register_agent(self, agent: AtomixAgent) -> None:
        """Register a specialized worker agent."""
        self.agents[agent.config.name] = agent

    def dispatch(self, agent_name: str, task: str) -> AgentResponse:
        """Route task to designated agent."""
        if agent_name not in self.agents:
            raise KeyError(f"Agent '{agent_name}' not found. Available: {list(self.agents.keys())}")
        return self.agents[agent_name].run(prompt=task)

    def list_agents(self) -> List[str]:
        return list(self.agents.keys())
