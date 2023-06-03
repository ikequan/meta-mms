import gradio as gr
import speech_recognition as sr
from ttsmms import TTS
from deep_translator import GoogleTranslator

# Initialize the TTS model for Ewe and Twi languages
ewe = TTS("data/{put your language iso code here}")
twi = TTS("data/{put your language iso code here}")

# Create a list of supported languages and their corresponding TTS models
langs = [{"lang": 'ewe', "tts": ewe}, {"lang": 'twi', "tts": twi}]


# Function to convert speech to text using Google's speech recognition API
def speech_to_text(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        print("Speech recognition service unavailable.")
        return None


# Function to convert text to speech
def text_to_speech(text, lang):
    # Find the selected language in the list of supported languages
    selected_lang = next((lang_item for lang_item in langs if lang_item["lang"] == lang), None)
    if selected_lang is None:
        raise ValueError(f"Language '{lang}' is not supported.")
    selected_tts = selected_lang["tts"]
    # Translate the text to the selected language using Google Translator
    translated = GoogleTranslator(source='auto', target=lang).translate(text)
    wav_path = "output.wav"
    # Generate speech synthesis and save it as a WAV file
    selected_tts.synthesis(translated, wav_path=wav_path)
    return wav_path


# Function to handle the speech to text app
def speech_to_text_app(audio_file):
    text = speech_to_text(audio_file)
    return text if text else "Unable to transcribe audio."


# Function to handle the text to speech output
def text_to_speech_output(text, lang):
    wav_path = text_to_speech(text, lang)
    return wav_path


# Function to handle the speech to text and text to speech app
def speech_to_text_and_tts_app(lang_input, audio_file, text_input):
    if audio_file:
        print("Converting audio to text:", audio_file)
        text = speech_to_text(audio_file)
        wav_path = text_to_speech_output(text, lang_input)
        return text, wav_path
    else:
        wav_path = text_to_speech_output(text_input, lang_input)
        return text_input, wav_path


# Define the Gradio interface inputs and outputs
audio_input = gr.inputs.Audio(source="microphone", type="filepath", label="Record Audio")
text_input = gr.inputs.Textbox(label="Enter your text here")
lang_input = gr.inputs.Dropdown(choices=[lang["lang"] for lang in langs], label="Language")
output_text = gr.outputs.Textbox(label="Transcription")
output_audio = gr.outputs.Audio(label="Text-to-Speech Audio", type='filepath')

# Create the Gradio interface
interface = gr.Interface(
    fn=speech_to_text_and_tts_app,
    inputs=[lang_input, audio_input, text_input],
    outputs=[output_text, output_audio],
    title="META Text-to-Speech",
    description="Record audio to convert to text or enter text to generate audio."
)

# Launch the interface
interface.launch()
