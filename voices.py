#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Check all available voices
"""

import os
import time
import argparse
from pathlib import Path

# Note: Write your API key here or provide it via the GOOGLE_API_KEY environment variable
API_KEY = 'AIzaSyCL1hEMA3f0JeSIZnVqN_0YfbKMmBY77Ps'

# Default output directory name
DEFAULT_OUTPUT_DIR = "voice_example"

# List of voices for testing (Languages/Descriptions are approximate!)
# Note: Some voices may not be supported!
VOICES_INFO = {
    "Puck":    "Male",
    "Charon":  "Male (deep)",
    "Kore":    "Female",
    "Fenrir":  "Male",
    "Aoede":   "Female" 
}

VOICES = list(VOICES_INFO.keys()) # List for checking

def test_all_voices(api_key=None, text=None, output_dir=None):
    """
    Test all known voices and display their descriptions
    """
    try:
        from gemini_tts import GeminiTTS
        
        if not api_key:
            if API_KEY:
                api_key = API_KEY
            elif os.environ.get('GOOGLE_API_KEY'):
                api_key = os.environ.get('GOOGLE_API_KEY')
            else:
                raise ValueError(
                    "API key not provided. Edit the API_KEY variable in test_voices.py, "
                    "or use the --api_key parameter, "
                    "or set the GOOGLE_API_KEY environment variable."
                )
        
        # Use default text if not provided
        if not text:
            text = "Hello! My name is {voice}, I am one of the voices of the Gemini TTS library."
        
        # Determine and create output directory
        if not output_dir:
            output_dir = DEFAULT_OUTPUT_DIR
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        print(f"Audio files will be saved to the '{output_dir}' directory.")
        
        print("*** Note: Language information is not retrieved from the API, only an estimate!")
        print("*** For full details, see the Google Gemini/Vertex AI documentation.")
        
        # Create TTS client
        client = GeminiTTS(api_key=api_key)
        
        # Test each voice
        for voice in VOICES:
            # Get voice description
            voice_desc = VOICES_INFO.get(voice, "Unknown description")
            
            # Create file name (inside directory)
            file_name = f"voice_{voice.lower()}.wav"
            file_path = f"voice_example/{file_name}"
            
            # Prepare text
            voice_text = text.format(voice=voice)
            
            print(f"\nTesting voice: {voice} ({voice_desc})")
            print(f"Text: {voice_text}")
            print(f"File: {file_path}")
            
            # Convert text to speech
            try:
                result = client.say(voice_text, output_file=file_path, voice=voice, play_audio=False) # Do not play during test
                print(f"Result: {result}")
            except Exception as e:
                 # If the voice is unavailable, print the error and continue
                 print(f"!!! Error ({voice}): {str(e)}")
                 if "is not available for model" in str(e):
                      print(f"--- Voice '{voice}' skipped.")
                      continue # Go to next voice
                 else:
                      # For other errors, show full info
                      import traceback
                      traceback.print_exc()
                      # Maybe better to stop here, but for now continue
            
            print(f"Please wait...")
            time.sleep(1) # Small wait
            
        print("\nAll available voices have been tested!")
        return True
        
    except ImportError:
         print("Error: 'gemini_tts' library not found. Install with: pip install -e .")
         return False
    except ValueError as ve:
         print(f"API key error: {ve}")
         return False
    except Exception as e:
        print(f"Unexpected general error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test Gemini TTS voices")
    parser.add_argument("--api_key", help="Google Gemini API key (if not specified in file or ENV)")
    parser.add_argument("--text", help="Text template to convert to speech (optional)")
    parser.add_argument("--output_dir", help=f"Directory to save audio files (default: {DEFAULT_OUTPUT_DIR})")
    
    args = parser.parse_args()
    
    test_all_voices(
        api_key=args.api_key,
        text=args.text,
        output_dir=args.output_dir
    ) 