from dotenv import load_dotenv

load_dotenv(override=True)

from src.Infraestructura.LLM.openrouter_llm import  CohereLLMService

def probar_cerebro():
    print("Inicializando servicio LLM con Cohere...")
    try:
        llm_service = CohereLLMService()

        prompt_entrenador = (
            "Eres Coach IA, un entrenador personal experto en fuerza y biomecánica. "
            "Tu personalidad es disciplinada, directa y motivadora. "
            "REGLAS OBLIGATORIAS: "
            "1. Responde en un máximo de 2 a 3 oraciones cortas (máximo 40 palabras) ya que serás leído por texto a voz. "
            "2. Sé directo, sin saludos largos ni rodeos. "
            "4. No uses viñetas, viñetas de lista ni símbolos especiales."
        )

        pregunta_usuario = ("Hola entrenador, como debería ser mi dieta en una etapa de volumen")
        print(f'\nUsuario: "{pregunta_usuario}"')

        historial = [{"role": "user", "content": pregunta_usuario}]

        print("Pensando respuesta...")
        respuesta = llm_service.generar_respuesta(
            historial_mensajes=historial, prompt_sistema=prompt_entrenador
        )

        print("--------------------------------------------------")
        print(f'Entrenador IA: "{respuesta}"')
        print("--------------------------------------------------")

    except Exception as e:
        print(f"\nError durante la prueba del cerebro: {e}")

if __name__ == "__main__":
    probar_cerebro()