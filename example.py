#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ең қарапайым тест - бір жолмен TTS тексеру
"""

# Оқыңыз: API кілтіңізді осында жазыңыз
API_KEY = "AIzaSyCL1hEMA3f0JeSIZnVqN_0YfbKMmBY77Ps"

# Әдепкі мәтін - мұны өзгертуге болады
TEXT = "Сәлем қалайсың?"

# Дауыс түрі - Puck (әйел), Kore (ер)
VOICE = "Kore"  # Ер дауысы

try:
    # Gemini TTS кітапханасын импорттау
    from gemini_tts import say, GeminiTTS
    
    # GeminiTTS объектісін тікелей пайдалану
    client = GeminiTTS(api_key=API_KEY or None, default_voice=VOICE)
    
    # Мәтінді сөйлеуге айналдыру
    result = client.say(TEXT, output_file="test_output.wav")
    print(f"Аудио сақталған жол: {result}")
    
except Exception as e:
    print(f"Қате орын алды: {str(e)}")
    import traceback
    traceback.print_exc() 