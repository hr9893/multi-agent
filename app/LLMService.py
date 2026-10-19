import logging

import streamlit as st

from app.GroqService import GroqService
from app.OpenAIService import OpenAIService

logger = logging.getLogger(__name__)

DEFAULT_PROVIDER_ORDER = ("groq", "openai")


class LLMService:
    """Generates fitness plans with automatic provider fallback.

    The primary provider is tried first. If it raises (rate limit, exhausted
    quota/budget, network error, ...) the next configured provider is tried.
    If every provider fails, a RuntimeError is raised.
    """

    def __init__(self, providers: dict | None = None, provider_order=None):
        self.providers = providers if providers is not None else {
            "groq": GroqService(),
            "openai": OpenAIService(),
        }
        self.provider_order = self._resolve_provider_order(provider_order)

    def _resolve_provider_order(self, provider_order):
        if provider_order is None:
            provider_order = self._configured_provider_order()

        if isinstance(provider_order, str):
            provider_order = [
                name.strip().lower()
                for name in provider_order.split(",")
                if name.strip()
            ]

        order = [
            name for name in provider_order
            if name in self.providers
        ]

        return order or list(DEFAULT_PROVIDER_ORDER)

    @staticmethod
    def _configured_provider_order():
        """Reads the optional LLM_PROVIDER_ORDER secret, never raising."""
        try:
            configured = st.secrets.get("LLM_PROVIDER_ORDER")
        except Exception:
            return list(DEFAULT_PROVIDER_ORDER)

        if not configured:
            return list(DEFAULT_PROVIDER_ORDER)

        return configured

    def generate_response(self, fitness_data: str) -> str:
        errors = []

        for provider_name in self.provider_order:
            provider = self.providers[provider_name]

            try:
                return provider.generate_response(fitness_data)
            except Exception as e:
                errors.append(f"{provider_name}: {e}")
                logger.warning(
                    "LLM provider '%s' failed, trying next provider: %s",
                    provider_name,
                    e,
                )

        raise RuntimeError(
            "All LLM providers failed: " + "; ".join(errors)
        )
