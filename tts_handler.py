# tts_handler.py

from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings, save

# ✅ Use your API key directly
client = ElevenLabs(api_key="sk_19ddde31417919076e839ab00b0224c10eb341af823db49b")

def text_to_speech(text):
    voice_id = "JBFqnCBsd6RMkjVDRZzb"  # Obi-Wan like voice or similar
    audio = client.text_to_speech.convert(
        text=text,
        voice_id=voice_id,
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
        voice_settings=VoiceSettings(stability=0.4, similarity_boost=0.8)
    )
    save(audio, "static/audio/ai_voice.mp3")
