"""Use this module to translate between English and French text using deep_translator."""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Translate input from English to French."""
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    """Translate input from French to English."""
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text