from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
import requests

client = ElevenLabs(
    api_key="YOUR API KEY",
)

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/cjVigY5qzO86Huf0OWal"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "sk_349947407fae2488a4371bf6ba61b82bf349af56121d7317"
}

# load text from file
text_file = open('output.txt', 'r')
text_file = text_file.read()
print("Text content loaded from file 'output.txt'")

data = {
  "text": text_file,
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}


print("Sending request to ElevenLabs API...")
response = requests.post(url, json=data, headers=headers)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)

print("Audio content written to file 'output.mp3'")