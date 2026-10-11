"""Atomix Claude API client wrapper."""

import os
from typing import Any, Dict, List, Optional
import anthropic
from .types import AgentConfig, AgentResponse


class AtomixAgent:
    """Production client wrapping Claude 3.5 Sonnet / Haiku."""

    def __init__(self, config: Optional[AgentConfig] = None, api_key: Optional[str] = None):
        self.config = config or AgentConfig()
        resolved_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not resolved_key:
            raise ValueError(
                "Anthropic API key required. Set ANTHROPIC_API_KEY environment variable "
                "or pass api_key parameter."
            )
        self.client = anthropic.Anthropic(api_key=resolved_key)

    def run(
        self,
        prompt: str,
        chat_history: Optional[List[Dict[str, str]]] = None,
        system_override: Optional[str] = None,
    ) -> AgentResponse:
        """Execute a synchronous prompt through the Claude API."""
        messages: List[Dict[str, Any]] = []

        if chat_history:
            messages.extend(chat_history)

        messages.append({"role": "user", "content": prompt})

        system = system_override or self.config.system_prompt

        response = self.client.messages.create(
            model=self.config.model,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            system=system,
            messages=messages,
        )

        content_text = ""
        for block in response.content:
            if getattr(block, "type", None) == "text":
                content_text += block.text

        return AgentResponse(
            agent_name=self.config.name,
            model=response.model,
            content=content_text,
            stop_reason=response.stop_reason,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
        )
