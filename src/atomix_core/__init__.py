"""Atomix Agent Core - Multi-agent orchestration powered by Claude 3.5 Sonnet."""

from .types import AgentConfig, AgentResponse, MessageRole
from .client import AtomixAgent
from .router import AgentRouter

__version__ = "0.1.0"
__all__ = ["AtomixAgent", "AgentRouter", "AgentConfig", "AgentResponse", "MessageRole"]
