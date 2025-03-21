import whisper

def transcribe_audio(file_path, model="base"):
    model = whisper.load_model(model)  # Choose from: tiny, base, small, medium, large
    result = model.transcribe(file_path)
    return result["text"]

def transcribe( filePath, outPath="transcription.txt" ,model="base"):
    transcription = transcribe_audio(filePath, model)
    with open( outPath, "w") as f:
        f.write(transcription)
    


if __name__ == "__main__":
    transcribe("playback.mp3", "transcription.txt")