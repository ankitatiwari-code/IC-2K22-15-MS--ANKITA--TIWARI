
import os
from clone_voice import clone_voice

os.makedirs("output", exist_ok=True)

print("===== FREE AI VOICE CLONING PROJECT =====")

text = input("Enter text to speak in cloned voice: ")

output_file = clone_voice(
    "input/Amitabh_voice.wav",
    "My Cloned Voice",
    text
)

print("\nVoice cloning completed!")
print("Generated audio:", output_file)

# Open the generated WAV file in Windows
os.startfile(os.path.abspath(output_file))
