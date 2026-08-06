from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

# Mensaje individual en la interacción
@dataclass
class Mensaje:
    rol: str
    contenido_texto: str
    timestap: datetime = field(default_factory = datetime.now)
    ruta_audio: Optional[str] = None

    def mensaje_usuario(self) -> bool:
        return self.rol == "user"

    def mensaje_entrenador(self) -> bool:
        return self.rol == "assistant"