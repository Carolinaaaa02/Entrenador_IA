from dataclasses import  dataclass, field
from _datetime import datetime
from typing import List, Dict
from .mensaje import Mensaje

#Sesion completa de interacción entre el alumno y el entrenador
@dataclass
class SesionEntrenamiento:
    id_sesion: str
    mensajes: List[Mensaje] = field(default_factory=list)
    fecha_inicio: datetime = field(default_factory=datetime.now)

    #Agrega nuevo mensaje a la conversación
    def agregar_mensaje(self, mensaje: Mensaje) -> None:
        self.mensajes.append(mensaje)

    #Exporta el historial en formato de diccionario
    def obtener_historial(self) -> List[Dict[str, str]]:
        return [
            {"role": msg.rol, "content": msg.contenido_texto}
            for msg in self.mensajes
        ]
