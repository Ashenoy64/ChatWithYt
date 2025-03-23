# ChatWithYT

ChatWithYT is a tool that allows users to chat with YouTube videos. Users provide a list of YouTube URLs, and the system processes the videos by downloading their audio, converting it into transcripts using Whisper, storing the data in a vector database, and enabling a conversational interface to interact with the extracted content.

## Prerequisites
Ensure the following dependencies are installed before proceeding:
- Install [Ollama](https://ollama.com/download)
- Download the required Ollama models:
  ```sh
  ollama pull gemma3:4b
  ollama pull nomic-embed-text
  ```
- Install FFmpeg (for processing audio):
  - **Windows:** [Install FFmpeg](https://windowsloop.com/install-ffmpeg-windows-10/)
  - **macOS:** `brew install ffmpeg`
  - **Linux:** `sudo apt install ffmpeg` (or use your package manager)

## Installation
### Clone and Setup
```sh
# Clone the repository
git clone https://github.com/Ashenoy64/ChatWithYt.git
cd ChatWithYt

# Set up virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration
Check `Settings.py` to configure the system:
- `WHISPER_MODEL`: Defines the Whisper model used for audio transcription. Options include 'tiny', 'base', 'small', 'medium', and 'large'.
- `VECTOR_DB_NAME`: Specifies the name of the vector database where transcript embeddings are stored.
- `DOCUMENT_SPLIT_OPTIONS`: Configures how text is split into smaller chunks, including chunk size, overlap, and separator priorities.
- `SHARE_CHAT_INTERFACE`: If set to `True`, allows the chat interface to be accessible over the internet.
- `EMBEDDING_MODEL`, `LLM_MODEL`, `CHAT_MEMORY`: Define the embedding model, language model, and chat memory storage for conversations.

## Usage
Run the script with one or more YouTube URLs:
```sh
python main.py https://www.youtube.com/watch?v=<VideoId>
```

For example:
```sh
python main.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Command-line Options
- **`URLS`** *(positional argument)*: One or more YouTube video URLs that you want to process.
- **`-h, --help`** *(optional argument)*: Displays help information about usage and available options.

## Contributing
Feel free to fork the repository and submit pull requests!

## License
This project is licensed under the MIT License.

