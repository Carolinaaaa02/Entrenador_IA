from abc import ABC, abstractmethod
from typing import List, Dict, Optional

#Interfaz para el servicio de modelo de lenguaje
class ILLMService(ABC):
    @abstractmethod
        #Recibe mensaje de usuario y opcionalmente el historial de la conversacion
        #y devuelve la respuesta del entrenador
    def generar_respuesta(self, mensaje_usuario: str, historial: Optional[List[Dict[str, str]]] = None) -> str:
        pass