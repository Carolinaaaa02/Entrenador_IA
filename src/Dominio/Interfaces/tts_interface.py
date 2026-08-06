from abc import ABC, abstractmethod

# Interfaz para el servicio de conversión de texto a voz
class ITTSService(ABC):

    #Recibe un texto y genera un archivo de audio
    @abstractmethod
    def sintetizar_voz(self, texto: str) -> bytes:
        pass