#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Барлық қолжетімді дауыстарды тексеру
"""

import os
import time
import argparse
from pathlib import Path

# Оқыңыз: API кілтіңізді осыда жазыңыз немесе GOOGLE_API_KEY айнымалысы арқылы беріңіз
API_KEY = 'AIzaSyCL1hEMA3f0JeSIZnVqN_0YfbKMmBY77Ps'

# Әдепкі шығыс бумасының атауы
DEFAULT_OUTPUT_DIR = "voice_example"

# Тестілеуге арналған дауыстар тізімі (Тілдер/Сипаттамалар болжамды!)
# Қолдау көрсетілмеуі мүмкін екенін ескеріңіз!
VOICES_INFO = {
    "Puck":    "Ер",
    "Charon":  "Ер(жуан)",
    "Kore":    "Әйел",
    "Fenrir":  "Ер",
    "Aoede":   "Әйел" 
}

VOICES = list(VOICES_INFO.keys()) # Тексеру үшін тізім

def test_all_voices(api_key=None, text=None, output_dir=None):
    """
    Барлық белгілі дауыстарды тексеру және сипаттамаларын көрсету
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
                    "API кілті берілмеді. test_voices.py файлында API_KEY айнымалысын өзгертіңіз, "
                    "немесе --api_key параметрін қолданыңыз, "
                    "немесе GOOGLE_API_KEY айнымалысын қоршаған ортада орнатыңыз."
                )
        
        # Егер мәтін берілмесе, әдепкі мәтінді қолдану
        if not text:
            text = "Сәлем! Менің атым {voice}, мен Gemini TTS кітапханасының бір дауысымын."
        
        # Шығыс директориясын анықтау және құру
        if not output_dir:
            output_dir = DEFAULT_OUTPUT_DIR
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        print(f"Аудио файлдар '{output_dir}' бумасына сақталады.")
        
        print("*** Ескерту: Тілдер туралы ақпарат API арқылы алынбаған, тек болжам!")
        print("*** Толық ақпаратты Google Gemini/Vertex AI құжаттамасынан қараңыз.")
        
        # TTS клиентін жасау
        client = GeminiTTS(api_key=api_key)
        
        # Әр дауысты тексеру
        for voice in VOICES:
            # Дауыс сипаттамасын алу
            voice_desc = VOICES_INFO.get(voice, "Белгісіз сипаттама")
            
            # Файл атауын жасау (бума ішінде)
            file_name = f"voice_{voice.lower()}.wav"
            file_path = f"voice_example/{file_name}"
            
            # Мәтінді дайындау
            voice_text = text.format(voice=voice)
            
            print(f"\nДауыс тексеру: {voice} ({voice_desc})")
            print(f"Мәтін: {voice_text}")
            print(f"Файл: {file_path}")
            
            # Мәтінді дауысқа айналдыру
            try:
                result = client.say(voice_text, output_file=file_path, voice=voice, play_audio=False) # Тест кезінде ойнатпау
                print(f"Нәтиже: {result}")
            except Exception as e:
                 # Егер дауыс қолжетімсіз болса, қатені басып шығарып, жалғастыру
                 print(f"!!! Қате ({voice}): {str(e)}")
                 if "is not available for model" in str(e):
                      print(f"--- '{voice}' дауысы өткізіліп жіберілді.")
                      continue # Келесі дауысқа өту
                 else:
                      # Басқа қате болса, толық ақпаратты көрсету
                      import traceback
                      traceback.print_exc()
                      # Мүмкін, мұнда тоқтаған дұрыс шығар, бірақ қазір жалғастырамыз
            
            print(f"Күте тұрыңыз...")
            time.sleep(1) # Кішкене күту
            
        print("\nБарлық қолжетімді дауыстар тексерілді!")
        return True
        
    except ImportError:
         print("Қате: 'gemini_tts' кітапханасы табылмады. Орнату: pip install -e .")
         return False
    except ValueError as ve:
         print(f"API кілті қатесі: {ve}")
         return False
    except Exception as e:
        print(f"Күтпеген жалпы қате: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gemini TTS дауыстарын тексеру")
    parser.add_argument("--api_key", help="Google Gemini API кілті (егер файлда немесе ENV-да көрсетілмесе)")
    parser.add_argument("--text", help="Сөйлеуге айналдыру үшін мәтін шаблоны (міндетті емес)")
    parser.add_argument("--output_dir", help=f"Аудио файлдарды сақтау үшін директория (әдепкі: {DEFAULT_OUTPUT_DIR})")
    
    args = parser.parse_args()
    
    test_all_voices(
        api_key=args.api_key,
        text=args.text,
        output_dir=args.output_dir
    ) 