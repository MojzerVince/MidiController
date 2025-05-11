import mido
from pynput.keyboard import Key, Controller

print("Starting MIDI to Keyboard Mapper...\n")
print("Please select a MIDI input device")

# List available MIDI input devices
midi_input = mido.get_input_names()
for i, device in enumerate(midi_input):
    print(f"{i}: {device}")

# Get user input for MIDI device selection
while True:
    try:
        device_index = int(input("\nEnter the number of the MIDI device you want to use: "))
        if 0 <= device_index < len(midi_input): # Check if the input is within the valid range
            midi_device = midi_input[device_index]
            break
        else:
            print("Invalid selection. Please try again.")
    except ValueError: # If the input is not a number
        print("Invalid input. Please enter a number.")

# Open the selected MIDI input port
midi_port = mido.open_input(midi_device)
keyboard = Controller()

print(f"\nListening for MIDI messages on {midi_device}...\n")
print("Please press the MIDI button you want to use as the UP ARROW!")
with midi_port:
    for msg in midi_port:
        if 'note_on' in msg:
            up = msg
            print(f"UP ARROW MIDI message: {up}")
            break
print("\nPlease press the MIDI button you want to use as the DOWN ARROW!")
with midi_port:
    for msg in midi_port:
        if 'note_on' in msg:
            down = msg
            print(f"DOWN ARROW MIDI message: {down}")
            break

print("Successfully mapped MIDI buttons to keyboard arrows!")