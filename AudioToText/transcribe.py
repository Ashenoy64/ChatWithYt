import whisper
import os

def transcribe_audio( file_path, model="base" ):
    model = whisper.load_model( model ) 
    result = model.transcribe( file_path )
    return result[ "text" ]

def transcribe( filePath, outPath="transcription.txt", model="base" ):
    try:    
        fileNameBase = os.path.splitext( os.path.basename( filePath ) )[ 0 ] 
        fileName = f"{fileNameBase}.txt"
        if os.path.exists(os.path.join(outPath, fileName)):
            os.remove( filePath )
            print(f"File {fileName} already exists. Skipping Transcription.")
            return fileName
        print(f"Transcribing {fileNameBase}...")
        transcription = transcribe_audio( filePath, model )
        with open( os.path.join( outPath, fileName ) , "w" ) as f:
            f.write( transcription )
        os.remove( filePath )
        return fileName
    except Exception as e:
        print( f"An error occurred: {e}" )
        return None


if __name__ == "__main__":
    transcribe( "playback.mp3", "transcription.txt" )