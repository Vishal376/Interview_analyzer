import whisper
import os

def transcribe_audio(file_path, model_size="base"):
    """
    Transcribe an audio file to text using OpenAI Whisper.
    """
    model = whisper.load_model(model_size)
    result = model.transcribe(file_path)
    return result["text"]

# Example usage
if __name__ == "__main__":
    text = transcribe_audio("data/sample_interview.mp3")
    print(text)
