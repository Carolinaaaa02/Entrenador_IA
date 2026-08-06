from abc import ABC, abstractclassmethod, abstractmethod
from typing import Union


# Interfaz para el servicio de convertir voz a texto
class ISTTService(ABC):
    #Recibe audio y devuelve transcripción a texto
    @abstractmethod
    def transcribir_audio(self, ruta_audio_bytes: Union[str, bytes]) -> str:
        pass