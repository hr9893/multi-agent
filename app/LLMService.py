import streamlit as st

from app.GroqService import GroqService
from app.OpenAIService import OpenAIService


class LLMService:
    """Tries each configured LLM provider in order until one succeeds."""

    def __init__(self, providers=None):
        if providers is None:
            providers = [
                ("Groq", GroqService()),
                ("OpenAI", OpenAIService()),
            ]
        self.providers = providers

    def _is_configured(self, provider) -> bool:
        # Providers may optionally expose is_configured(); if they do not,
        # assume they are usable and let the call itself fail.
        check = getattr(provider, "is_configured", None)
        if check is None:
            return True
        try:
            return bool(check())
        except Exception:
            return False

    def generate_response(self, fitness_data: str):

        errors = []

        for name, provider in self.providers:

            if not self._is_configured(provider):
                print(f"Skipping LLM provider {name}: API key is not configured.")
                errors.append(f"{name}: API key is not configured")
                continue

            try:
                return provider.generate_response(fitness_data)

            except Exception as e:
                print(f"LLM provider {name} failed: {e}")
                errors.append(f"{name}: {e}")

        raise RuntimeError(
            "All LLM providers failed. " + "; ".join(errors)
        )
