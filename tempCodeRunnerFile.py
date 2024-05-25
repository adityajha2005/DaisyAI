for voice in voices:
    if "zira" in voice.name.lower():
        engine.setProperty("voice", voice.id)
        break