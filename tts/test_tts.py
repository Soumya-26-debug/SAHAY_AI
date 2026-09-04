from tts import generate_speech
def test_tts_generation():

    text = "Welcome to SahayAI."

    output_file = generate_speech(text)

    assert output_file.endswith(".wav")

    print("TTS generation test passed.")


if __name__ == "__main__":
    test_tts_generation()
