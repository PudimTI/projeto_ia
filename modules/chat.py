from __future__ import annotations

from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
_client: Optional[OpenAI] = None

SYSTEM_PROMPT = (
    "Você é uma IA especialista em Minecraft, que responde com dicas, curiosidades "
    "e explicações sobre o jogo de forma amigável e clara."
)


def set_client(client: OpenAI) -> None:
    """Permite configurar o cliente OpenAI externamente."""
    global _client
    _client = client


def _get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI()
    return _client


def generate_response(prompt: str) -> str:
    """Gera uma resposta usando o modelo gpt-4o-mini."""
    client = _get_client()
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )
    return response.output_text or "Não consegui gerar uma resposta agora. Tente novamente."

