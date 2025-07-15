import os
import gradio as gr

from brain_of_the_doctor import encode_image, analyze_image_and_query
from voice_of_the_patient import record_audio, transcribe
from voice_of_the_doctor import text_to_speech

system_prompt="""
You need to act as a professional doctor.
What's in this image? Do you find anything wrong with it medically?
If you find something, suggest some remedies. Do not add numbers or special characters in your response.
Your response should be one long paragraph. Answer as if you are answering to a patient.
Do not say 'In the image I see...', but say 'With what I see, you seem to have...'
Do not respond as an AI robot in markdown.
Keep your answer concise (max 2 sentences). No preamble, start your answer right away.
"""

def process_inputs(audio_filepath, image_filepath):
    speech_to_text=transcribe(model="whisper-large-v3", file_path=audio_filepath)
    if image_filepath:
        doctor_response=analyze_image_and_query(query=system_prompt+speech_to_text, encoded_image=encode_image(image_filepath))
    else:
        doctor_response="No response provided"
    
    voice_of_doctor=text_to_speech(doctor_response, "final.mp3", "final.wav")

    return speech_to_text, doctor_response, voice_of_doctor

interface=gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=['microphone'], type='filepath'),
        gr.Image(type='filepath')
    ],
    outputs=[
        gr.Textbox(label="Speec to text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio("Temp.mp3")
    ],
    title="AI Doctor with Vision and Voice",
)
interface.launch(debug=True)