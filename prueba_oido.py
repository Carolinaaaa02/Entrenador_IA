import io
import wave
import sounddevice as sd
from dotenv import load_dotenv
from src.Infraestructura.STT.deepgram_stt import DeepgramSTTService

# Cargar variables del archivo .env
load_dotenv(override=True)

def probar_oido_en_vivo():
    print("Inicializando servicio STT...")
    try:
        stt_service = DeepgramSTTService()

        # Configuración de grabación
        duracion = 5  # segundos
        frecuencia_muestreo = 16000
        canales = 1

        print("\n--- Iniciando grabación ---")
        print(f"Grabando {duracion} segundos... ¡Habla ahora!")

        captura_audio = sd.rec(
            int(duracion * frecuencia_muestreo),
            samplerate=frecuencia_muestreo,
            channels=canales,
            dtype="int16",
        )
        sd.wait()
        print("Grabación finalizada.")

        # Convertir a buffer WAV en memoria RAM
        buffer_wav = io.BytesIO()
        with wave.open(buffer_wav, "wb") as wf:
            wf.setnchannels(canales)
            wf.setsampwidth(2)
            wf.setframerate(frecuencia_muestreo)
            wf.writeframes(captura_audio.tobytes())

        datos_bytes = buffer_wav.getvalue()

        # Transcribir
        print("Enviando audio a Deepgram...")
        texto = stt_service.transcribir_audio(datos_bytes)

        print("\n¡Resultado de la transcripción!")
        print("--------------------------------------------------")
        if texto:
            print(f'Dijiste: "{texto}"')
        else:
            print("No se detectó ninguna palabra en el audio.")
        print("--------------------------------------------------")

    except Exception as e:
        print(f"\nError durante la prueba: {e}")

if __name__ == "__main__":
    probar_oido_en_vivo()