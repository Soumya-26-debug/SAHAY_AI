import subprocess
import os
import winsound

MODEL_PATH = "models/en_US-lessac-medium.onnx"
OUTPUT_FILE = "output/sahay_response.wav"


def generate_speech(text):
    """
    Convert text into speech using Piper TTS.
    """

    os.makedirs("output", exist_ok=True)

    command = [
        "piper",
        "--model",
        MODEL_PATH,
        "--output_file",
        OUTPUT_FILE
    ]

    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        text=True
    )

    process.communicate(text)

    return OUTPUT_FILE


def play_audio(audio_file):
    """
    Play the generated WAV file.
    """

    winsound.PlaySound(
        audio_file,
        winsound.SND_FILENAME
    )


if __name__ == "__main__":

    print("SahayAI Text-to-Speech")
    print("Type 'exit' to stop.")

    while True:

        text = input("\nEnter text: ")

        if text.lower() == "exit":
            break

        audio_file = generate_speech(text)

        print("Speech generated.")

        play_audio(audio_file)
