# Gemini TTS (or Gemini Parrot TTS) - Simple Text-to-Speech Library

This library is a **creative solution** for text-to-speech conversion using the Google Gemini API. It attempts to guide the Gemini model into a "parrot mode" (repeating the given text exactly), but due to the model's conversational nature, this might not always be fully successful.

## Installation

### Install via Pip (Future)
```bash
# Basic functionality
pip install gemini-tts

# With audio playback support (recommended)
pip install gemini-tts[audio]
```

### Install from Source
```bash
git clone https://github.com/dauitsuragan002/gemini-tts.git
cd gemini-tts
pip install -e .
# For audio playback
pip install -e .[audio]
```

## Requirements
- Python 3.7+
- websockets
- wave
- pygame (optional, for audio playback)

## Usage

### 1. Using the Class (Recommended Method)
```python
from gemini_tts import GeminiTTS

# Create a client
client = GeminiTTS(api_key="your_api_key_here", default_voice="Puck")

# Convert to speech and save the audio file
client.say("This is an example using the class")

# Change the voice
client.say("This is a different voice", voice="Kore")

# Don't play the audio
client.say("Only save to file", play_audio=False)
```

### 3. Direct Audio Playback
```python
from gemini_tts import GeminiTTS

client = GeminiTTS(api_key="your_api_key_here")

# Convert text to speech and play immediately
client.say("This audio will play automatically", play_audio=True)
```

### 4. Synchronous File Generation (No Playback)
```python
from gemini_tts import GeminiTTS

client = GeminiTTS(api_key="your_api_key_here")

# Convert text to speech, but don't play
file_path = client.text_to_speech("This will only be saved to a file", output_file="sync_output.wav")
print(f"Audio file saved synchronously: {file_path}")
```

**Note:** Voices synthesized via Gemini TTS (sometimes called "Gemini Parrot TTS") might not always be perfectly accurate renditions of the input text. This is because the library attempts to "force" the Gemini model into a "parrot mode" (only repeating), but the model may still sometimes shift into a conversational mode and respond to the input text instead. This is a known limitation of this creative approach.

## Full Examples

- `example.py` - shows basic functions
- `/voice_example` - contains audio files converted with different voices

## Voice Types
Available voices tested (may vary based on model compatibility):
- **Male Voices:**
  - Puck (Male)
  - Charon (Male, Deep)
  - Fenrir (Male)
- **Female Voices:**
  - Kore (Female)
  - Aoede (Female)

**Note:** This list might not be exhaustive, and some voices (e.g., Bassett) might be incompatible with the `gemini-2.0-flash-exp` model. Check the official Gemini API documentation.

## Version History

### v0.1.1
- Added direct audio playback
- Optimized voice parameters (for deep male voices)
- Organized voices by category
- Parrot AI

### v0.1.0
- Initial release

## Authors
- Developer: David Suragan
- AI Assistant: Claude (Anthropic) & Gemini (Google)

## Acknowledgments
This project was inspired by the [agituts/gemini-2-tts](https://github.com/agituts/gemini-2-tts) repository. Many thanks to the author of that project.

## License
MIT  