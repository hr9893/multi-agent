from app.LLMService import GroqProvider, LLMService, _read_secret


class GroqService(LLMService):
    """Backward-compatible Groq-only service.

    Kept so existing imports keep working. New code should use
    :class:`app.LLMService.LLMService`, which falls back to other providers
    when Groq is unavailable.
    """

    def __init__(self):
        super().__init__(
            providers=[GroqProvider(api_key=_read_secret("GROQ_API_KEY"))])
