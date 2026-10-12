
from pathlib import Path
import torch
import torchaudio as ta
from chatterbox.tts_turbo import ChatterboxTurboTTS


def clone_voice(audio_file, voice_name, text):
    print("Creating voice clone:", voice_name)

    audio_path = Path(audio_file)

    if not audio_path.is_file():
        raise FileNotFoundError(
            f"Reference audio not found: {audio_path}"
        )

    device = "cuda" if torch.cuda.is_available() else "cpu"

    print("Using device:", device)
    print("Loading voice cloning model...")

    model = ChatterboxTurboTTS.from_pretrained(
        device=device
    )

    print("Generating cloned speech...")

    wav = model.generate(
        text,
        audio_prompt_path=str(audio_path)
    )

    output_path = Path("output/cloned_voice.wav")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    ta.save(str(output_path), wav.cpu(), model.sr)

    print("Voice generated successfully!")
    print("Saved to:", output_path)

    return str(output_path)
