from dataclasses import dataclass, field
from typing import List, Optional

#Contiene el contexto del usuario para personalizar las respuestas del entrenador
@dataclass
class PerfilUsuario:
    id_usuario: str
    nombre: str
    objetivo_principal: str
    nivel_experiencia: str
    limitaciones_lesiones: List[str] = field(default_factory=list)

    #Genera una cadena con el perfil para agregarla en el prompt del LLM
    def obtener_contexto(self) -> str:
        lesiones = ", ".join(self.limitaciones_lesiones) if self.limitaciones_lesiones else "Ninguna"
        return (
            f"Usuario: {self.nombre} | Objetivo: {self.objetivo_principal} | "
            f"Nivel: {self.nivel_experiencia} | Lesiones/Limitaciones: {lesiones}"
        )
