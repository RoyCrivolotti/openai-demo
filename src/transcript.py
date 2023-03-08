import openai

def transcribe(audio_file: str, api_key: str):
    # set up the OpenAI API credentials
    openai.api_key = api_key

    # define the file location
    audio_file = audio_file

    # open audio file
    audio_data = open(audio_file, "rb")

    # send the audio and prompt to OpenAI's Whisper API
    transcript = openai.Audio.transcribe("whisper-1", audio_data)

    # print the response from the server
    return transcript.text
