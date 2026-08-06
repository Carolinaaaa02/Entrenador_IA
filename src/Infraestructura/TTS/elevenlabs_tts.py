import os
import io
from elevenlabs.client import ElevenLabs

class ElevenLabsTTSService:
    #Servicio para convertir texto a audio utilizando ElevenLabs
    def __init__(
            self,
            api_key: str = None,
            voice_id: str = "JBFqnCBsd6RMkjVDRZzb",
            model_id: str = "eleven_multilingual_v2",
    ):
        self.api_key = api_key or os.getenv("ELEVENLABS_API_KEY")
        if not  self.api_key:
            raise ValueError(
                "No se encontró la ELEVENLABS_API_KEY"
            )

        self.client = ElevenLabs(api_key = self.api_key)
        self.voice_id = voice_id
        self.model_id = model_id

    def texto_a_audio(self, texto: str) -> io.BytesIO:
        try:
            #Generar el audio desde elevenlabs
            audio_steam = self.client.text_to_speech.convert(
                text = texto,
                voice_id = self.voice_id,
                model_id = self.model_id,
            )

            #Acumular los chuncks de audio en un buffer de memoria
            buffer_audio = io.BytesIO()
            for chunk in audio_steam:
                buffer_audio.write(chunk)

            buffer_audio.seek(0)
            return buffer_audio

        except Exception as e:
            raise RuntimeError(f"Error al generar audio: {str(e)}")
