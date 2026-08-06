import os
from typing import Union
from deepgram import DeepgramClient

from src.Dominio.Interfaces.stt_interface import ISTTService

# Implementación del servicio STT usando Deepgram
class DeepgramSTTService(ISTTService):
    # Inicializa el cliente Deepgram
    def __init__(self, api_key: str = None, model: str = "nova-2", language: str = "es"):
        #Asegurar la API Key desde el parámetro o desde os.getenv
        self.api_key = api_key or os.getenv("DEEPGRAM_API_KEY")

        if not self.api_key:
            raise ValueError(
                "No se encontró la DEEPGRAM_API_KEY. Verifica que el archivo .env tenga la clave definida."
            )

        # Instanciar pasándole explícitamente el parámetro nombrado 'api_key'
        self.client = DeepgramClient(api_key=self.api_key)
        self.model = model
        self.language = language

    #Recibe la ruta de un archivo de audio o bytes de audio y devuelve el texto
    def transcribir_audio(self, ruta_audio_bytes: Union[str, bytes]) -> str:
        try:
            # Configuración de las opciones de transcripcion
            if isinstance(ruta_audio_bytes, str):
                with open(ruta_audio_bytes, "rb") as audio_file:
                    datos_wav_bytes = audio_file.read()
            else:
                datos_wav_bytes = ruta_audio_bytes

            #Llamada a la api
            respuesta = self.client.listen.v1.media.transcribe_file(
                request=datos_wav_bytes,
                request_options={
                    "additional_query_parameters": {
                        "model": self.model,
                        "language": self.language,
                        "smart_format": "true",
                    }
                },
            )
            texto = respuesta.results.channels[0].alternatives[0].transcript
            return texto if texto else ""

        except Exception as e:
            raise RuntimeError(f"Error al transcribir audio con deepgram {str(e)}")


