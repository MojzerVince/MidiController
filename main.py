import mido
from pynput.keyboard import Key, Controller

print("Starting MIDI to Keyboard Mapper...\n")
print("Please select a MIDI input device:")
midi_input = mido.get_input_names()
for i, device in enumerate(midi_input):
    print(f"{i}: {device}")