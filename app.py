import argparse
from enum import Enum
from morse import text_to_morse, morse_to_text

class FileExtension(Enum):
    MORSE = "morse"
    TEXT = "txt"
    AUDIO = "wav"

def write(text, morse, audio, file_name):

    if text is not None:
        write_text(text, file_name)
        # escreve audio
    
    if morse is not None:
        write_morse(morse, file_name)
        # escreve audio
            
    if audio is not None:
        # escreve morse
        # escreve texto
        pass

def write_text(text, file_name):
    with open('text.txt', 'w') as f:
        f.write(text)

def write_morse(morse, file_name):
    with open('code.morse', 'w') as m:
        m.write(morse)

def write_audio(audio, file_name):
    pass

def main():
    parser = argparse.ArgumentParser(description = 'Text, morse and audio files parser')
    parser.add_argument("file_path", type=str, help="arquivo com a extensão a ser traduzida")
    args = parser.parse_args()

    file_name = args.file_path.split('.')[0]
    extension = args.file_path.split('.')[-1]

    with open(args.file_path, 'r') as f:
        content = f.read()

    if extension == FileExtension.TEXT.value:
        morse = text_to_morse(content)
        write(None, morse, None, file_name)

    elif extension == FileExtension.MORSE.value:
        text = morse_to_text(content)
        write(text, None, None, file_name)
    
    elif extension == FileExtension.AUDIO.value:
        pass

if __name__ == "__main__":
    main()