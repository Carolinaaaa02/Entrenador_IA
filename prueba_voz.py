from dotenv import load_dotenv
import sounddevice as sd
import soundfile as sf

load_dotenv(override=True)

from src.Infraestructura.TTS.elevenlabs_tts import ElevenLabsTTSService

def probar_voz():
    print("Inicializando servicio TTS con ElevenLabs...")
    try:
        tts_service = ElevenLabsTTSService()

        texto_entrenador = "Aumenta la ingesta de proteínas y carbohidratos complejos. Come alimentos ricos en nutrientes y evita los procesados. Mantén un equilibrio para apoyar el crecimiento muscular."
        print(f'\nGenerando audio para: "{texto_entrenador}"')

        # Convertir texto a bytes de audio en memoria
        buffer_audio = tts_service.texto_a_audio(texto_entrenador)

        print("Reproduciendo respuesta...")
        data, samplerate = sf.read(buffer_audio)
        sd.play(data, samplerate)
        sd.wait()
        print("Reproducción finalizada con éxito.")

    except Exception as e:
        print(f"\nError durante la prueba de voz: {e}")

if __name__ == "__main__":
    probar_voz()