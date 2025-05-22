#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The simplest test - check TTS with a single line
"""

# Note: Write your API key here
API_KEY = "AIzaSyCL1hEMA3f0JeSIZnVqN_0YfbKMmBY77Ps"

# Default text - you can change this
TEXT = "Hello, how are you?"

# Voice type - Puck (female), Kore (male)
VOICE = "Kore"  # Male voice

try:
    # Import Gemini TTS library
    from gemini_tts import say, GeminiTTS
    
    # Use GeminiTTS object directly
    client = GeminiTTS(api_key=API_KEY or None, default_voice=VOICE)
    
    # Convert text to speech
    result = client.say(TEXT, output_file="test_output.wav")
    print(f"Audio saved to: {result}")
    
except Exception as e:
    print(f"An error occurred: {str(e)}")
    import traceback
    traceback.print_exc() 