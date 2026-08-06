import os
from typing import List, Dict
import cohere
from src.Dominio.Interfaces.llm_interface import ILLMService


class CohereLLMService(ILLMService):
    """
    Implementación del servicio LLM usando la API de Cohere (Command R+ / Command R).
    """

    def __init__(
        self,
        api_key: str = None,
        model: str = "command-r-08-2024",
        temperature: float = 0.7,
        max_tokens: int = 250,
    ):
        self.api_key = api_key or os.getenv("COHERE_API_KEY")
        if not self.api_key:
            raise ValueError(
                "No se encontró la COHERE_API_KEY. Verifica tu archivo .env"
            )

        self.client = cohere.ClientV2(api_key=self.api_key)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generar_respuesta(
        self, historial_mensajes: List[Dict[str, str]], prompt_sistema: str = None
    ) -> str:
        try:
            mensajes = []

            # System prompt
            if prompt_sistema:
                mensajes.append({"role": "system", "content": prompt_sistema})

            # Mapear historial al formato V2 de Cohere
            for msg in historial_mensajes:
                role = "user" if msg["role"] == "user" else "assistant"
                mensajes.append({"role": role, "content": msg["content"]})

            response = self.client.chat(
                model=self.model,
                messages=mensajes,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )

            # Extraer respuesta
            return response.message.content[0].text

        except Exception as e:
            raise RuntimeError(f"Error al generar respuesta con Cohere: {str(e)}")