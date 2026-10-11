"""Data types and schemas for Atomix Agent Core."""

from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class AgentConfig(BaseModel):
    """Configuration for an autonomous Claude agent instance."""
    name: str = "default_agent"
    model: str = "claude-3-5-sonnet-20241022"
    system_prompt: str = "You are an autonomous AI agent built by Atomix Digital."
    temperature: float = Field(default=0.2, ge=0.0, le=1.0)
    max_tokens: int = Field(default=2048, ge=1)
    tools: Optional[List[Dict[str, Any]]] = None


class AgentResponse(BaseModel):
    """Normalized response schema returned by the agent."""
    agent_name: str
    model: str
    content: str
    stop_reason: Optional[str] = None
    input_tokens: int = 0
    output_tokens: int = 0
    raw_response: Optional[Dict[str, Any]] = None
